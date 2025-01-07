from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import *
from .serializers import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
# Create your views here.
# def fun1(request):
#     if request.method=='GET':
#         data=students.objects.all()
#         s=studSerializer(data,many=True)
#         return JsonResponse(s.data,safe=False)

# @csrf_exempt
# def fun1(request):
#     if request.method=='GET':
#         data=students.objects.all()
#         s=studModelSerializer(data,many=True)
#         return JsonResponse(s.data,safe=False)
#     elif request.method=='POST':
#         d=JSONParser().parse(request)
#         s=studModelSerializer(data=d)
#         print(s)
#         if s.is_valid():
#             s.save()
#             return JsonResponse(s.data,safe=False)
#         else:                                                                                        
#             return JsonResponse(s.errors)

@csrf_exempt
def fun1(request,pk):
    try:
        demo=students.objects.get(pk=pk)
        print('hello')
    except:
        return HttpResponse("Invalid")    
    if request.method=='GET':
        s=studModelSerializer(demo)
        return JsonResponse(s.data)
    elif request.method=='PUT':
        d=JSONParser().parse(request)
        s=studModelSerializer(demo,data=d)
        if s.is_valid():
            s.save()
            return JsonResponse(s.data)
        else:                                                                                        
            return JsonResponse(s.errors)  
    elif request.method=='DELETE': 
        demo.delete()         
        return HttpResponse("Deleted")    