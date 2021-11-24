from django.core.files.storage import default_storage


def uploadFile(file):
    return {"file_name": default_storage.save(file.name, file)}
