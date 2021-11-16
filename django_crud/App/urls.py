from django.conf.urls import url
from App import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

# Apesar de por padrao o Django já adicionar a '/' numa url, isso so eh possível nos metodos GET e DELETE. No POST e PUT, voce eh obrigado a terminar a url em '/'. No GET e DELETE nao eh obrigatorio, se voce fizer com ou sem a '/' no final, vai funcionar do mesmo jeito.
urlpatterns = [path('noticia/',views.noticiaApi), path('noticia/<int:id>/',views.noticiaApi), path('pessoa/',views.pessoaApi), path('pessoa/<int:id>/',views.pessoaApi), path('upload/',views.saveFile)]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
# O + concatena dois arrays em python. O segundo array eh a url /Files/<file_name>, que serve para mostrar no navegador os arquivos que foram upados.