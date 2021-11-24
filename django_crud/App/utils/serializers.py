from rest_framework import serializers
from App.models import Noticia, Pessoa

# required False eh util na hora do PUT para nao ser obrigado a sempre passar todos os fields


class NoticiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noticia
        fields = "__all__"
        extra_kwargs = {"link": {"required": False}}


class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = "__all__"
        extra_kwargs = {"nome": {"required": False}}
