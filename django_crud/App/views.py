from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from App.models import Noticia, Pessoa
from App.serializers import NoticiaSerializer, PessoaSerializer
from django.core.files.storage import default_storage

# Create your views here.


@csrf_exempt
def noticiaApi(request, id=0):
    if request.method == "GET":
        if id != 0:
            try:
                noticia = Noticia.objects.get(id=id)
                noticia_serializer = NoticiaSerializer(noticia)
                return JsonResponse(noticia_serializer.data, safe=False)
            except:
                return JsonResponse({"message": "Notícia não encontrada!"}, safe=False)
        else:
            noticias = Noticia.objects.all().order_by("-created_at")
            noticias_serializer = NoticiaSerializer(noticias, many=True)
            return JsonResponse(noticias_serializer.data, safe=False)
    elif request.method == "POST":
        noticia_data = JSONParser().parse(request)
        noticia_serializer = NoticiaSerializer(data=noticia_data)
        if noticia_serializer.is_valid():
            noticia_serializer.save()
            return JsonResponse({"message": "Criado com sucesso!"}, safe=False)
        return JsonResponse({"message": "Erro ao criar!"}, safe=False)
    elif request.method == "PUT":
        noticia_data = JSONParser().parse(request)
        try:
            noticia = Noticia.objects.get(id=id)
            noticia_serializer = NoticiaSerializer(noticia, data=noticia_data)
            if noticia_serializer.is_valid():
                noticia_serializer.save()
                return JsonResponse({"message": "Atualizado com sucesso!"}, safe=False)
        except:
            return JsonResponse({"message": "Erro ao atualizar!"}, safe=False)
    elif request.method == "DELETE":
        try:
            noticia = Noticia.objects.get(id=id)
            noticia.delete()
            return JsonResponse({"message": "Deletado com sucesso!"}, safe=False)
        except:
            return JsonResponse({"message": "Erro ao deletar!"}, safe=False)


@csrf_exempt
def pessoaApi(request, id=0):
    if request.method == "GET":
        if id != 0:
            try:
                pessoa = Pessoa.objects.get(id=id)
                pessoa_serializer = PessoaSerializer(pessoa)
                return JsonResponse(pessoa_serializer.data, safe=False)
            except:
                return JsonResponse({"message": "Pessoa não encontrada!"}, safe=False)
        else:
            pessoas = Pessoa.objects.all().order_by("-created_at")
            pessoas_serializer = PessoaSerializer(pessoas, many=True)
            return JsonResponse(pessoas_serializer.data, safe=False)
    elif request.method == "POST":
        pessoa_data = JSONParser().parse(request)
        pessoa_serializer = PessoaSerializer(data=pessoa_data)
        if pessoa_serializer.is_valid():
            pessoa_serializer.save()
            return JsonResponse({"message": "Criado com sucesso!"}, safe=False)
        return JsonResponse({"message": "Erro ao criar!"}, safe=False)
    elif request.method == "PUT":
        pessoa_data = JSONParser().parse(request)
        try:
            pessoa = Pessoa.objects.get(id=id)
            pessoa_serializer = PessoaSerializer(pessoa, data=pessoa_data)
            if pessoa_serializer.is_valid():
                pessoa_serializer.save()
                return JsonResponse({"message": "Atualizado com sucesso!"}, safe=False)
        except:
            return JsonResponse({"message": "Erro ao atualizar!"}, safe=False)
    elif request.method == "DELETE":
        try:
            pessoa = Pessoa.objects.get(id=id)
            pessoa.delete()
            return JsonResponse({"message": "Deletado com sucesso!"}, safe=False)
        except:
            return JsonResponse({"message": "Erro ao deletar!"}, safe=False)


# Para testar usando Insomnia ou Postman, basta colocar o tipo de body Multipart Form, definir o 'name' como 'file' e o tipo do value como File. Feito isso, eh so fazer o upload de um arquivo do computador e enviar a requisicao.
@csrf_exempt
def saveFile(request):
    file = request.FILES["file"]
    file_name = default_storage.save(file.name, file)
    return JsonResponse({"file_name": file_name}, safe=False)
