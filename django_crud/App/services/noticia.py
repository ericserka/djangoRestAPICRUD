from App.models import Noticia
from App.utils.serializers import NoticiaSerializer


def getNoticia(id):
    if id != 0:
        try:
            return NoticiaSerializer(
                Noticia.objects.values("id", "link").get(id=id)
            ).data
        except:
            return {"message": "Notícia não encontrada!"}
    else:
        return NoticiaSerializer(
            Noticia.objects.all().values("id", "link").order_by("-created_at"),
            many=True,
        ).data


def postNoticia(noticia_data):
    noticia_serializer = NoticiaSerializer(data=noticia_data)
    if noticia_serializer.is_valid():
        noticia_serializer.save()
        return {"message": "Criado com sucesso!"}
    return {"message": "Erro ao criar!"}


def putNoticia(noticia_data, id):
    try:
        noticia_serializer = NoticiaSerializer(
            Noticia.objects.get(id=id), data=noticia_data
        )
        if noticia_serializer.is_valid():
            noticia_serializer.save()
            return {"message": "Atualizado com sucesso!"}
        else:
            return {"message": "Erro ao atualizar!"}
    except:
        return {"message": "Erro ao atualizar!"}


def deleteNoticia(id):
    try:
        Noticia.objects.get(id=id).delete()
        return {"message": "Deletado com sucesso!"}
    except:
        return {"message": "Erro ao deletar!"}
