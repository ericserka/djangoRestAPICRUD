from App.views import noticia, pessoa, upload
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

# Apesar de por padrao o Django já adicionar a '/' numa url, isso so eh possível nos metodos GET e DELETE. No POST e PUT, voce eh obrigado a terminar a url em '/'. No GET e DELETE nao eh obrigatorio, se voce fizer com ou sem a '/' no final, vai funcionar do mesmo jeito.
urlpatterns = [
    path("noticia/", noticia.noticiaApi),
    path("noticia/<int:id>/", noticia.noticiaApi),
    path("pessoa/", pessoa.pessoaApi),
    path("pessoa/<int:id>/", pessoa.pessoaApi),
    path("upload/", upload.saveFile),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# O + concatena dois arrays em python. O segundo array eh a url /Files/<file_name>, que serve para mostrar no navegador os arquivos que foram upados.
