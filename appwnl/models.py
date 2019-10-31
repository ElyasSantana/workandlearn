from django.db import models
from passlib.hash import pbkdf2_sha256
from django.contrib.auth.models import User


class Usuario(models.Model):
    class Meta:
        abstract = True

    email = models.EmailField(unique=True, max_length=254)
    password = models.CharField(max_length=256)
    telefone = models.CharField(max_length=12)

    def verify_password(self, raw_password):
        return pbkdf2_sha256.verify(raw_password, self.password)


class Empresa(Usuario):
    foto = models.ImageField(upload_to='image_perfil', blank=True)
    razao_social = models.CharField(max_length=100)
    cnpj = models.CharField(unique=True, max_length=14)

    def __str__(self):
        return self.razao_social


class Desenvolvedor(Usuario):
    foto = models.ImageField(upload_to='image_perfil', blank=True)
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    cpf = models.CharField(max_length=11, unique=True)
    rg = models.CharField(max_length=10, unique=True)
    telefone = models.CharField(max_length=12)

    def __str__(self):
        return '%s %s' % (self.nome, self.sobrenome)


class Endereco(models.Model):
    desenvolvedor = models.ForeignKey(Desenvolvedor,
                                      on_delete=models.CASCADE,
                                      null=True,
                                      blank=True)
    logradouro = models.CharField(max_length=80)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=80)
    estado = models.CharField(max_length=80)
    numero = models.CharField(max_length=20)

    def __str__(self):
        return '%s, %s, %s, %s - %s' % (self.logradouro, self.numero,
                                        self.bairro, self.cidade, self.estado)


class Tecnologia(models.Model):
    empresa = models.ForeignKey(Empresa,
                                on_delete=models.CASCADE,
                                null=True,
                                blank=True)
    desenvolvedor = models.ForeignKey(Desenvolvedor,
                                      on_delete=models.CASCADE,
                                      null=True,
                                      blank=True)
    tecnologia = models.CharField(max_length=50)


class Local(models.Model):
    empresa = models.ForeignKey(Empresa,
                                on_delete=models.CASCADE,
                                null=True,
                                blank=True)
    logradouro = models.CharField(max_length=80)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=80)
    estado = models.CharField(max_length=80)
    numero = models.CharField(max_length=20)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return '%s, %s, %s, %s - %s' % (self.logradouro, self.numero,
                                        self.bairro, self.cidade, self.estado)


class Reserva(models.Model):
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    desenvolvedor = models.ForeignKey(Desenvolvedor, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    data = models.DateField()
    aprovado = models.BooleanField(null=True)
