from django.db import IntegrityError
from django.http import HttpResponse, JsonResponse
from .models import Book
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView



# Create your views here.
"""@csrf_exempt
def books(request):
    if(request.method == 'GET'):
        books = Book.objects.all().values()
        context = {"books": list(books)}
        return JsonResponse(context)
    elif(request.method == 'POST'):
        title =request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        book = Book(
            title = title,
            author = author,
            price = price
        )
        try:
            book.save()
        except IntegrityError:
            return JsonResponse({'error':'true','message':'required field missing'},status=400)
        return JsonResponse(model_to_dict(books),status=201)
"""
@api_view(['GET','POST'])
def books(request):
    return Response('list of the books',status = status.HTTP_200_OK)

class BookList(APIView):
    def get(self,request):
        return Response({"message":"list of the books"}, status.HTTP_200_OK)