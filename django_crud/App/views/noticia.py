from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from App.services import noticia


@csrf_exempt
def noticiaApi(request, id=0):
    if request.method == "GET":
        return JsonResponse(noticia.getNoticia(id), safe=False)
    elif request.method == "POST":
        return JsonResponse(
            noticia.postNoticia(JSONParser().parse(request)), safe=False
        )
    elif request.method == "PUT":
        return JsonResponse(
            noticia.putNoticia(JSONParser().parse(request), id), safe=False
        )
    elif request.method == "DELETE":
        return JsonResponse(noticia.deleteNoticia(id), safe=False)
