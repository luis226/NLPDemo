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
        try:
            if request.data["queryResult"]["intent"]["displayName"] == 'GetProducts':
                products = Product.objects.all()
                text_response = 'We have the products: '
                if len(products):
                    for product in products:
                        text_response += product.name + ','
                    text_response += ' avaiable for buying'
                else:
                    text_response = 'We have no products avaiable now, sorry!'
                df_response = {"fulfillmentMessages": [{"text": {"text" : [text_response]}}]}
                return Response(data=df_response, status=status.HTTP_200_OK,
                                content_type="application/json; charset=UTF-8")
        except KeyError:
            pass
        return Response(status=status.HTTP_200_OK)

    if request.method == 'GET':
        d_requests = DialogFlowRequest.objects.all().order_by('-created_date')
        serializer = DialogFlowRequestSerializer(d_requests, many=True)
        return Response(serializer.data)

    return Response(status=status.HTTP_400_BAD_REQUEST)
