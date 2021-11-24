from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from App.services import pessoa


@csrf_exempt
def pessoaApi(request, id=0):
    if request.method == "GET":
        return JsonResponse(pessoa.getPessoa(id), safe=False)
    elif request.method == "POST":
        return JsonResponse(pessoa.postPessoa(JSONParser().parse(request)), safe=False)
    elif request.method == "PUT":
        return JsonResponse(
            pessoa.putPessoa(JSONParser().parse(request), id), safe=False
        )
    elif request.method == "DELETE":
        return JsonResponse(pessoa.deletePessoa(id), safe=False)
