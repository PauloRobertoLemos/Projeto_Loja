from django.db import models


class Produto(models.Model):
    produto_id = models.CharField(max_length=20)
    