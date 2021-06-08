import rest_framework.request

from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

from .models import RouteModel
from .serializers import RouteSerializer


@api_view(['GET'])
def routeList(request: rest_framework.request.Request):
    routes = RouteModel.objects.all()
    serializer = RouteSerializer(routes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def routeDetail(request: rest_framework.request.Request, pk: int):
    routes = RouteModel.objects.all()
    route = get_object_or_404(routes, id=pk)
    serializer = RouteSerializer(route)
    return Response(serializer.data)


@api_view(['POST'])
def routeCreate(request: rest_framework.request.Request):
    serializer = RouteSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def routeUpdate(request: rest_framework.request.Request, pk: int):
    routes = RouteModel.objects.all()
    route = get_object_or_404(routes, id=pk)
    serializer = RouteSerializer(instance=route, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def routeDelete(request: rest_framework.request.Request, pk: int):
    routes = RouteModel.objects.all()
    route = get_object_or_404(routes, id=pk)
    route.delete()

    return Response('Deleted')
