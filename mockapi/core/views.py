from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
import string
import random
import csv
import pandas as pd
from .models import Voucher
from .serializers import VoucherSerializer
from rest_framework.parsers import JSONParser
from django.http import JsonResponse


def id_generator(amount=1,size=6, chars=string.ascii_uppercase + string.digits):
    return ['DVPD'+''.join(random.choice(chars) for _ in range(size)) for _ in range(amount)]


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)             # <-- And here
    df = pd.DataFrame(id_generator(50,7))
    df.to_csv('file_name.csv', index = False, header=True)
    def get(self, request):
        list_voucher = []
        list_voucher=id_generator(50,7)
        print(list_voucher)
        for i in range(len(list_voucher)) :
            Voucher.objects.create(
                code = list_voucher[i]
            )
        df = pd.DataFrame(list_voucher)
        # df.to_csv('file_name.csv', index = False, header=True)
        print (df)
        content = {'message': df}
        return Response(content)

@api_view(['POST'])
def CheckVoucher(request):
    if request.method == 'POST':
        voucher = request.data.get('code')
        result = Voucher.objects.filter(code=voucher)
        if result:
            voucher_serializer = VoucherSerializer(result, many=True)
            return Response(voucher_serializer.data)
        else:
            return Response({"error" :"Voucher not Found"})
        # return JsonResponse(voucher_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def ActivateVoucher(request):
    if request.method == 'PUT':
        voucher = request.data.get('code')
        result = list(Voucher.objects.filter(code=voucher).values('used'))
        if result:
            if result[0]['used']:
                return Response({"Message" :"Voucher has been used"})
            else:
                Voucher.objects.filter(code=voucher).update(used=True)
                result = Voucher.objects.filter(code=voucher)
                voucher_serializer = VoucherSerializer(result, many=True)
                return Response({"Message" :"Voucher Activated"})
        else:
            return Response({"error" :"Voucher not Found"})
        # return JsonResponse(voucher_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
   