# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

# auto_now_add = True faz com que created_at seja o valor do dia/hora atual em que a linha da tabela foi criada
# auto_now = True faz com que updated_at seja alterado para o dia/hora atual sempre que alguma outra coluna da tabela for alterada

class Noticia(models.Model):
    id = models.AutoField(primary_key = True)
    link = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'noticia'


class Pessoa(models.Model):
    id = models.AutoField(primary_key = True)
    nome = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'pessoa'
