from django.db import models


class Produto(models.Model):
    produto_id = models.CharField(max_length=20)
    produto_name = models.CharField(max_length=100)
    produto_price = models.DecimalField(max_digits=10, decimal_places=2)
    produto_qnd_est = models.PositiveIntegerField()
    produto_dt_cri = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.produto_name
