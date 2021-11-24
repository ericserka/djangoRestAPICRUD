from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from App.services.upload import uploadFile

# Para testar usando Insomnia ou Postman, basta colocar o tipo de body Multipart Form, definir o 'name' como 'file' e o tipo do value como File. Feito isso, eh so fazer o upload de um arquivo do computador e enviar a requisicao.
@csrf_exempt
def saveFile(request):
    return JsonResponse(uploadFile(request.FILES["file"]), safe=False)
