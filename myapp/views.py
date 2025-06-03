from django.shortcuts import render
from rest_framework.response import Response
from .serializers import questionSerializer, LanguageSerializer, CareerAdviceSerializer
from .models import *
from rest_framework.decorators import api_view
from rest_framework import status
from django.db.models import Q
import logging

# Create your views here.
logger = logging.getLogger(__name__)

@api_view(['GET'])
def get_question(request):
    language_id = request.GET.get('language', '')
    print("language_id----------",language_id)
    difficulty = request.GET.get('difficulty')
    try:
        if language_id != 'none':
            que = Question.objects.filter(language=int(language_id))
            
            if difficulty != 'all':
                que = que.filter(difficulty=difficulty)
            
        serializer = questionSerializer(que, many=True)
        return Response(serializer.data)

    except Exception as e:
        print("ERROR:", str(e))
        return Response({'error': "Something went wrong"}, status=500)


@api_view(['GET'])
def get_languages(request):
    try:
        languages = Language.objects.all()
        serializer = LanguageSerializer(languages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        logger.error(f"Error retrieving languages: {str(e)}")
        return Response(
            {"error": "An error occurred while retrieving languages."},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
        
@api_view(['GET'])
def get_carrierAdvice(request):
    try:
        advice = CareerAdvice.objects.all()
        serializer = CareerAdviceSerializer(advice, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': "Something went wrong"}, status=500)
        