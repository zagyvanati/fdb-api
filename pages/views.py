from django.http import JsonResponse
from .models import Page
from .serializers import PageSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def page_list(request, format=None):

    if request.method == 'GET':
        pages = Page.objects.all()
        serializer = PageSerializer(pages, many=True)
        # A JsonReturn helyett mindenhol ez van a tutorialban:
        # return Response(serializer.data) 
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        serializer = PageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def page_detail(request, slug, format=None):

    try:
        page = Page.objects.get(slug=slug)
    except Page.DoesNotExist:
        return JsonResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PageSerializer(page)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        serializer = PageSerializer(page, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        page.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)