# Generated by Django 3.2.15 on 2024-10-16 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0049_alter_orderproduct_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='restaurant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='foodcartapp.restaurant'),
            preserve_default=False,
        ),
    ]
