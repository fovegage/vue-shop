# Generated by Django 2.1 on 2019-07-21 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0006_auto_20190721_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='name',
            field=models.CharField(max_length=100, verbose_name='商品名称'),
        ),
    ]
