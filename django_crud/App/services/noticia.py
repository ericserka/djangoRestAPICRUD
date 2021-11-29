from App.models import Noticia
from App.utils.serializers import NoticiaSerializer


def getNoticia(id):
    if id != 0:
        try:
            return NoticiaSerializer(
                Noticia.objects.values("id", "link").get(id=id)
            ).data
        except Exception as e:
            return {"message": "Notícia não encontrada!","exception": str(e)}
    else:
        return NoticiaSerializer(
            Noticia.objects.all().values("id", "link").order_by("-created_at"),
            many=True,
        ).data


def postNoticia(noticia_data):
    noticia_serializer = NoticiaSerializer(data=noticia_data)
    if noticia_serializer.is_valid():
        noticia_serializer.save()
        return {"message": "Notícia riada com sucesso!"}
    return {"message": "Erro ao criar notícia!"}


def putNoticia(noticia_data, id):
    try:
        noticia_serializer = NoticiaSerializer(
            Noticia.objects.get(id=id), data=noticia_data
        )
        if noticia_serializer.is_valid():
            noticia_serializer.save()
            return {"message": "Notícia atualizada com sucesso!"}
        else:
            return {"message": "Erro ao atualizar notícia!"}
    except Exception as e:
        return {"message": "Erro ao atualizar notícia!","exception": str(e)}


def deleteNoticia(id):
    try:
        Noticia.objects.get(id=id).delete()
        return {"message": "Notícia deletada com sucesso!"}
    except Exception as e:
        return {"message": "Erro ao deletar notícia!","exception": str(e)}
