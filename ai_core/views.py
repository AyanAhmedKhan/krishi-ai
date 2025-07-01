from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import DiagnosisForm
from .models import Diagnosis, DiagnosisHistory
from django.urls import reverse
import requests
from gtts import gTTS
import os
from django.conf import settings
from groq import Groq
import re
# from pydub import AudioSegment
from deep_translator import GoogleTranslator

# Placeholder for AI model prediction
from .model import predict_disease

# Create your views here.

def clean_text_for_tts(text):
    # Remove emojis and non-ASCII characters
    return re.sub(r'[^\u0000-\u007F]+', ' ', text)

def split_text(text, max_length=200):
    # Split text into chunks for gTTS
    sentences = text.split('. ')
    chunks = []
    current = ''
    for sentence in sentences:
        if len(current) + len(sentence) < max_length:
            current += sentence + '. '
        else:
            chunks.append(current.strip())
            current = sentence + '. '
    if current:
        chunks.append(current.strip())
    return chunks

def call_groq_api(disease):
    try:
        client = Groq(api_key="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")
        prompt = f"Suggest cure, suitable fertilizer, and preventive practices for {disease} in a farmer-friendly language. Provide a concise, helpful response under 100 words."
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="llama3-8b-8192",
        )
        response_text = chat_completion.choices[0].message.content
        print("Groq API response:", response_text)
        return response_text
    except Exception as e:
        print(f"Error calling Groq API: {e}")
        return "No response from AI service."

@login_required
def diagnosis_upload(request):
    if request.method == 'POST':
        form = DiagnosisForm(request.POST, request.FILES)
        if form.is_valid():
            diagnosis = form.save(commit=False)
            diagnosis.user = request.user
            diagnosis.save()  # Save first so image file is written
            diagnosis.result = predict_disease(diagnosis.image.path)
            diagnosis.save()
            return redirect('diagnosis_result', pk=diagnosis.pk)
    else:
        form = DiagnosisForm()
    return render(request, 'ai_core/diagnosis_upload.html', {'form': form})

def extract_fertilizer_recommendation(ai_text):
    for line in ai_text.splitlines():
        if line.lower().startswith('fertilizer'):
            return line
    return None

@login_required
def diagnosis_result(request, pk):
    diagnosis = get_object_or_404(Diagnosis, pk=pk, user=request.user)
    if not diagnosis.gemini_response_en:
        full_ai_response = call_groq_api(diagnosis.result)
        # Summarize and Translate
        summary_en = full_ai_response # Groq output is already summarized
        summary_en = summary_en.replace('*', '')
        summary_hi = GoogleTranslator(source='auto', target='hi').translate(summary_en)
        summary_hi = summary_hi.replace('*', '')
        diagnosis.gemini_response_en = summary_en
        diagnosis.gemini_response_hi = summary_hi
        diagnosis.gemini_response = f"English:\n{summary_en}\n\nहिंदी:\n{summary_hi}"
        # Generate audio for Hindi summary
        try:
            audio_dir = os.path.join(settings.MEDIA_ROOT, 'audio')
            os.makedirs(audio_dir, exist_ok=True)
            tts_hi = gTTS(summary_hi, lang='hi')
            audio_hi_path = os.path.join(audio_dir, f'diagnosis_{diagnosis.pk}_hi.mp3')
            tts_hi.save(audio_hi_path)
            diagnosis.audio_hi.name = f'audio/diagnosis_{diagnosis.pk}_hi.mp3'
            diagnosis.audio_en.delete(save=False)
        except Exception as e:
            print(f"Error generating Hindi audio: {e}")
        diagnosis.save()
        # Save chat history
        DiagnosisHistory.objects.create(
            user=diagnosis.user,
            diagnosis=diagnosis,
            chat_content=diagnosis.gemini_response
        )
    fertilizer_reco = extract_fertilizer_recommendation(diagnosis.gemini_response_en)
    return render(request, 'ai_core/diagnosis_result.html', {'diagnosis': diagnosis, 'fertilizer_reco': fertilizer_reco})

@login_required
def chat_history(request):
    history = DiagnosisHistory.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'ai_core/chat_history.html', {'history': history})
