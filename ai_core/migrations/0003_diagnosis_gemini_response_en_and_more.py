# Generated by Django 5.0.2 on 2025-06-26 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ai_core', '0002_diagnosis_audio_en_diagnosis_audio_hi_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagnosis',
            name='gemini_response_en',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='diagnosis',
            name='gemini_response_hi',
            field=models.TextField(blank=True),
        ),
    ]
