from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from .models import Crop, SoilType, Region, Fertilizer, FertilizerRecommendation, UserFertilizerRequest
from .forms import FertilizerRecommendationForm
from groq import Groq

# Create your views here.

def fertilizer_home(request):
    return render(request, 'fertilizer/home.html')

@login_required
def fertilizer_recommendation(request):
    if request.method == 'POST':
        form = FertilizerRecommendationForm(request.POST)
        if form.is_valid():
            # Save the user request
            user_request = form.save(commit=False)
            user_request.user = request.user
            
            # Try to find a matching recommendation
            try:
                recommendation = FertilizerRecommendation.objects.get(
                    crop=user_request.crop,
                    soil_type=user_request.soil_type,
                    region=user_request.region
                )
                user_request.recommendation = recommendation
                user_request.save()
                
                # Generate AI-enhanced recommendation
                ai_recommendation = generate_ai_recommendation(user_request, recommendation)
                
                return render(request, 'fertilizer/result.html', {
                    'user_request': user_request,
                    'recommendation': recommendation,
                    'ai_recommendation': ai_recommendation
                })
                
            except FertilizerRecommendation.DoesNotExist:
                # Generate AI recommendation without database match
                ai_recommendation = generate_ai_recommendation(user_request, None)
                user_request.save()
                
                return render(request, 'fertilizer/result.html', {
                    'user_request': user_request,
                    'recommendation': None,
                    'ai_recommendation': ai_recommendation
                })
    else:
        form = FertilizerRecommendationForm()
    
    return render(request, 'fertilizer/recommendation.html', {'form': form})

def generate_ai_recommendation(user_request, db_recommendation):
    """Generate AI-enhanced fertilizer recommendation using Groq"""
    try:
        # Check if API key is configured
        if not hasattr(settings, 'GROQ_API_KEY') or not settings.GROQ_API_KEY:
            return "AI recommendation unavailable. Please configure GROQ_API_KEY in settings."
        
        client = Groq(api_key=settings.GROQ_API_KEY)
        
        # Build the prompt
        prompt = f"""
        As an agricultural expert, provide detailed fertilizer recommendations for:
        
        Crop: {user_request.crop.name}
        Soil Type: {user_request.soil_type.name}
        Region: {user_request.region.name}
        Area: {user_request.area_hectares} hectares
        
        {f'Database Recommendation: {db_recommendation.primary_fertilizer.name} ({db_recommendation.primary_fertilizer.npk_ratio})' if db_recommendation else 'No specific database recommendation available.'}
        
        Please provide:
        1. Recommended fertilizers with NPK ratios
        2. Application rates per hectare
        3. Application timing
        4. Organic alternatives
        5. Special considerations for this region and soil type
        6. Cost estimates
        
        Keep the response under 200 words and provide practical, actionable advice.
        """
        
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": "You are an expert agricultural consultant specializing in fertilizer recommendations for Indian farmers."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.7
        )
        
        return response.choices[0].message.content
        
    except Exception as e:
        return f"AI recommendation unavailable. Error: {str(e)}"

@login_required
def fertilizer_history(request):
    """Show user's fertilizer recommendation history"""
    user_requests = UserFertilizerRequest.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'fertilizer/history.html', {'user_requests': user_requests})
