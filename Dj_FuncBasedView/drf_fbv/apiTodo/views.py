from django.db.models.query_utils import Q
from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import serializers

from .models import Todo
from .serializers import TodoSerializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from rest_framework import status

# Create your views here.
def home(request):
    return HttpResponse(
        '<center><h1 style="background-color:powderblue;">Welcome to ApiTodo</h1></center>'
    )


# @api_view(["GET"])
# def todolist(request):

#     queryset = Todo.objects.all()
#     serializer = TodoSerializer(queryset, many=True)

#     return Response(serializer.data)


# @api_view(["POST"])
# def todocreate(request):

#     serializer = TodoSerializer(data=request.data)

#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)


@api_view(["GET", "POST"])
def todoListCreate(request):

    if request.method == "GET":

        queryset = Todo.objects.all()
        serializer = TodoSerializer(queryset, many=True)

        return Response(serializer.data)

    elif request.method == "POST":

        serializer = TodoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)


# @api_view(["GET"])
# def todo_detail(request, pk):

#     queryset = Todo.objects.get(id=pk)
#     serializer = TodoSerializer(queryset)

#     return Response(serializer.data)


@api_view(["GET", "PUT", "DELETE"])
def todo_detail(request, pk):

    if request.method == "GET":

        queryset = Todo.objects.get(id=pk)
        serializer = TodoSerializer(queryset)

        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    elif request.method == "PUT":

        queryset = Todo.objects.get(id=pk)
        serializer = TodoSerializer(instance=queryset, data=request.data)

        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    elif request.method == "DELETE":
        queryset = Todo.objects.get(id=pk)
        queryset.delete()
        return Response("Item deleted", status=status.HTTP_204_NO_CONTENT)


# @api_view(["DELETE"])
# def todo_delete(request, pk):
#     queryset = Todo.objects.get(id=pk)
#     queryset.delete()
#     return Response("Item deleted")