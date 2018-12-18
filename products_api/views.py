from django.shortcuts import render
from rest_framework import viewsets
from .serializer import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


@api_view(['POST', 'GET'])
def payload(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'POST':
        data = request.data
        d = DialogFlowRequest(content=data)
        d.save()
        return Response(status=status.HTTP_200_OK)

    if request.method == 'GET':
        d_requests = DialogFlowRequest.objects.all()
        serializer = DialogFlowRequestSerializer(d_requests, many=True)
        return Response(serializer.data)

    return Response(status=status.HTTP_400_BAD_REQUEST)
