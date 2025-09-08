# hello this is demo project

from .models import Registration
from .serializers import RegistrationSerializer
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response

class RegistrationCreateAPIView(CreateAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = RegistrationSerializer(data=request.data)  # ✅ correct serializer object
            if serializer.is_valid():  # ✅ validate
                serializer.save()
                return Response({
                    'status': 'success',
                    'message': f'Registration successfully created',
                    'data': serializer.data
                })
            else:
                return Response({
                    'status': 'error',
                    'message': serializer.errors
                })
        except Exception as e:
            return Response({
                'status': 'error',
                'message': str(e)
            })


class RegistrationListAPIView(ListAPIView):
    serializer_class = RegistrationSerializer

    def get(self, request, *args, **kwargs):
        try:
            registrations = Registration.objects.all()
            serializer = RegistrationSerializer(registrations, many=True)
            return Response({
                'status': 'success',
                'data': serializer.data
            })
        except Exception as e:
            return Response({
                'status': 'error',
                'message': str(e)
            })
