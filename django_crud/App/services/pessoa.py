from App.models import Pessoa
from App.utils.serializers import PessoaSerializer


def getPessoa(id):
    if id != 0:
        try:
            return PessoaSerializer(Pessoa.objects.values("id", "nome").get(id=id)).data
        except:
            return {"message": "Pessoa não encontrada!"}
    else:
        return PessoaSerializer(
            Pessoa.objects.all().values("id", "nome").order_by("-created_at"), many=True
        ).data


def postPessoa(noticia_data):
    pessoa_serializer = PessoaSerializer(data=noticia_data)
    if pessoa_serializer.is_valid():
        pessoa_serializer.save()
        return {"message": "Criado com sucesso!"}
    return {"message": "Erro ao criar!"}


def putPessoa(noticia_data, id):
    try:
        pessoa_serializer = PessoaSerializer(
            Pessoa.objects.get(id=id), data=noticia_data
        )
        if pessoa_serializer.is_valid():
            pessoa_serializer.save()
            return {"message": "Atualizado com sucesso!"}
        else:
            return {"message": "Erro ao atualizar!"}
    except:
        return {"message": "Erro ao atualizar!"}


def deletePessoa(id):
    try:
        Pessoa.objects.get(id=id).delete()
        return {"message": "Deletado com sucesso!"}
    except:
        return {"message": "Erro ao deletar!"}
