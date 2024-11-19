# Generated by Django 4.2.9 on 2024-11-16 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shopcart',
            options={'verbose_name': 'Корзина', 'verbose_name_plural': 'Корзины'},
        ),
        migrations.AddConstraint(
            model_name='shopcart',
            constraint=models.UniqueConstraint(fields=('user', 'game'), name='unique_user_game_constraint'),
        ),
    ]
