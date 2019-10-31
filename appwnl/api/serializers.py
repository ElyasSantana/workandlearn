from rest_framework import serializers
from appwnl.models import Empresa, Desenvolvedor, Endereco, Tecnologia, Local, Reserva


class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'


class EmpresaLocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ['id', 'email', 'razao_social', 'telefone', 'foto']


class DesenvolvedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Desenvolvedor
        fields = '__all__'


class DesenvolvedorEnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Desenvolvedor
        fields = ['id', 'email', 'nome', 'telefone', 'foto']


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco

        fields = '__all__'


class EnderecoDesenvolvedorSerializer(serializers.ModelSerializer):
    desenvolvedor = DesenvolvedorEnderecoSerializer()

    class Meta:
        model = Endereco
        fields = [
            'id', 'logradouro', 'bairro', 'numero', 'cidade', 'estado',
            'desenvolvedor'
        ]


class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local

        fields = '__all__'


class LocalEmpresaSerializer(serializers.ModelSerializer):
    empresa = EmpresaLocalSerializer()

    class Meta:
        model = Local
        fields = [
            'id', 'logradouro', 'bairro', 'numero', 'cidade', 'estado',
            'empresa'
        ]


class TecnologiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecnologia
        fields = '__all__'


class TecnologiaEmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecnologia
        fields = '__all__'
        read_only_fields = ['desenvolvedor']


class TecnologiaDesenvolvedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecnologia
        fields = '__all__'
        read_only_fields = ['empresa']


class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'


class ReservaEmpresaSerializer(serializers.ModelSerializer):
    empresa = EmpresaSerializer(read_only=True)

    class Meta:
        model = Reserva
        fields = '__all__'
        read_only_fields = ['data']


class ReservaDesenvolvedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'
        read_only_fields = ['aprovado']