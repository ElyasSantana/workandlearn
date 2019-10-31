from rest_framework import viewsets, status
from rest_framework.response import Response
from appwnl.models import Empresa, Desenvolvedor, Endereco, Tecnologia, Local, Reserva
from appwnl.api.serializers import *
from passlib.hash import pbkdf2_sha256
from django.shortcuts import get_object_or_404


class EmpresaViewSet(viewsets.ModelViewSet):
    serializer_class = EmpresaSerializer

    def get_queryset(self):
        empresa_id = self.request.query_params.get('id', None)
        queryset = Empresa.objects.all()

        if empresa_id:
            queryset = queryset.filter(id=empresa_id)
        return queryset

    def create(self, request):
        request.data['password'] = pbkdf2_sha256.encrypt(
            request.data['password'], salt_size=32)
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            Empresa.objects.create(**serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DesenvolvedorViewSet(viewsets.ModelViewSet):
    serializer_class = DesenvolvedorSerializer

    def get_queryset(self):
        endereco_id = self.request.query_params.get('id', None)
        queryset = Desenvolvedor.objects.all()

        if endereco_id:
            queryset = queryset.filter(id=endereco_id)
            return queryset

        return queryset

    def create(self, request):
        request.data['password'] = pbkdf2_sha256.encrypt(
            request.data['password'], salt_size=32)
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            Desenvolvedor.objects.create(**serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EnderecoViewSet(viewsets.ModelViewSet):
    serializer_class = EnderecoSerializer

    def get_queryset(self):
        endereco_id = self.request.query_params.get('id', None)
        queryset = Endereco.objects.all()

        if endereco_id:
            queryset = queryset.filter(id=endereco_id)
            return queryset

        return queryset


class LocalViewSet(viewsets.ModelViewSet):
    serializer_class = LocalSerializer

    def get_queryset(self):
        local_id = self.request.query_params.get('id', None)
        preco = self.request.query_params.get('preco', None)
        queryset = Local.objects.all()

        if local_id:
            queryset = queryset.filter(id=local_id)

        if preco:
            queryset = queryset.filter(preco=preco)
        return queryset


class TecnologiaEmpresaViewSet(viewsets.ModelViewSet):
    serializer_class = TecnologiaEmpresaSerializer

    def get_queryset(self):
        tech_id = self.request.query_params.get('id', None)
        tech_nome = self.request.query_params.get('tecnologia', None)
        queryset = Tecnologia.objects.all()

        if tech_id:
            queryset = queryset.filter(id=tech_id)

        if tech_nome:
            queryset = queryset.filter(tecnologia=tech_nome)
        return queryset


class TecnologiaDesenvolvedorViewSet(viewsets.ModelViewSet):
    serializer_class = TecnologiaDesenvolvedorSerializer

    def get_queryset(self):
        tech_id = self.request.query_params.get('id', None)
        tech_nome = self.request.query_params.get('tecnologia', None)
        queryset = Tecnologia.objects.all()

        if tech_id:
            queryset = queryset.filter(id=tech_id)

        if tech_nome:
            queryset = queryset.filter(tecnologia=tech_nome)
        return queryset


class ReservaEmpresaViewSet(viewsets.ModelViewSet):
    serializer_class = ReservaEmpresaSerializer

    def get_queryset(self):
        reserva_id = self.request.query_params.get('id', None)
        data = self.request.query_params.get('data', None)
        queryset = Reserva.objects.all()

        if reserva_id:
            queryset = queryset.filter(id=reserva_id)

        if data:
            queryset = queryset.filter(data=data)

        return queryset


class ReservaDesenvolvedorViewSet(viewsets.ModelViewSet):
    serializer_class = ReservaDesenvolvedorSerializer

    def get_queryset(self):
        reserva_id = self.request.query_params.get('id', None)
        data = self.request.query_params.get('data', None)
        queryset = Reserva.objects.all()

        if reserva_id:
            queryset = queryset.filter(id=reserva_id)

        if data:
            queryset = queryset.filter(data=data)

        return queryset

    def create(self, request, *args, **kwargs):
        local = request.data['local']
        empresa = request.data['empresa']
        queryset = Local.objects.all()
        if (local and empresa):
            queryset = queryset.filter(id=local, empresa=empresa)
            if queryset:
                serializer = self.serializer_class(data=request.data)

                if serializer.is_valid():
                    Reserva.objects.create(**serializer.validated_data)
                    return Response(
                        {
                            "message": "Reserva solicitada com sucesso!",
                            "content": serializer.data
                        },
                        status=status.HTTP_201_CREATED)

                return Response(serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)

        return Response({"message": "Reserva não encontrada!"},
                        status=status.HTTP_400_BAD_REQUEST)
