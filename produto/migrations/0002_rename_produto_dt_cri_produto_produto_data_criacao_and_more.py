# Generated by Django 5.1.5 on 2025-01-14 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='produto_dt_cri',
            new_name='produto_data_criacao',
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='produto_price',
            new_name='produto_preco',
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='produto_qnd_est',
            new_name='produto_quantidade_estoque',
        ),
    ]
