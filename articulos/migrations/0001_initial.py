# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=200)),
                ('contenido', models.TextField()),
                ('fecha_pub', models.DateTimeField(auto_now_add=True)),
                ('categoria', models.CharField(max_length=11, choices=[(b'Academico', b'Academico'), (b'Tecnologico', b'Tecnologico'), (b'Noticias', b'Noticias'), (b'Deportes', b'Deportes'), (b'Espiritual', b'Espiritual'), (b'Social', b'Social')])),
                ('imagen', models.ImageField(upload_to=b'articulos', verbose_name=b'Imagen')),
                ('autor', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('texto', models.TextField()),
                ('fecha', models.DateField(auto_now_add=True)),
                ('articulo', models.ForeignKey(to='articulos.Articulo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
