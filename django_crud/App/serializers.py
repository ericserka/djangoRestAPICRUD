from rest_framework import serializers
from App.models import Noticia, Pessoa


class NoticiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noticia
        fields = "__all__"


class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = "__all__"
