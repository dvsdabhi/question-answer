import math
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from .serializers import questionSerializer, LanguageSerializer, CareerAdviceSerializer
from .models import *
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from django.db.models import Q
import logging

# Create your views here.
logger = logging.getLogger(__name__)

@api_view(['GET'])
def get_question(request):
    language_id = request.GET.get('language', '')
    difficulty = request.GET.get('difficulty')
    page = int(request.GET.get('page'))
    try:
        que = Question.objects.all()
        if language_id and language_id != 'none':
            que = que.filter(language=int(language_id))
            
            if difficulty and difficulty != 'all':
                que = que.filter(difficulty=difficulty)
        
        que_count = que.count()
        paginator = PageNumberPagination()
        paginator.page_size = 5
        
        total_page = math.ceil(que_count / paginator.page_size)
        print(total_page)
        if page <= total_page:
            
            result_page = paginator.paginate_queryset(que, request)
            print("result_page", result_page)
            
            serializer = questionSerializer(result_page, many=True)
            res = paginator.get_paginated_response(serializer.data)
            res.data['total_page'] = total_page
            return res
        else:
            data = {
                "success":False,
                "message":"Page not found",
                "results":[]
            }
            return JsonResponse(data)

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
        