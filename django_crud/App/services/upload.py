from django.core.files.storage import default_storage


def uploadFile(file):
    try:
        return {"file_name": default_storage.save(file.name, file)}
    except Exception as e:
        return {"message": "Erro ao fazer upload do arquivo!","exception": str(e)}
