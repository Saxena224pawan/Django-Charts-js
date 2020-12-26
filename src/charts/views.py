from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model


User = get_user_model()
class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request,'charts.html',{})

def get_Data(request, *args, **kwargs):
    data ={
        'sales':100,
        'customers':10
    }
    return JsonResponse(data)

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        user_Count =User.objects.all().count()
        labels = ['Users','Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange']
        defaultData =[user_Count, 23,45,51,89,99,1]
        data ={
        'labels':labels,
        'defaultData':defaultData
        }
        return Response(data)
