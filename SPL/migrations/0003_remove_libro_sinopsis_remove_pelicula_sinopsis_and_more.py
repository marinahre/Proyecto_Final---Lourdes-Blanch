# Generated by Django 4.1.5 on 2023-02-07 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SPL', '0002_rename_libros_libro_rename_series_pelicula_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libro',
            name='sinopsis',
        ),
        migrations.RemoveField(
            model_name='pelicula',
            name='sinopsis',
        ),
        migrations.RemoveField(
            model_name='serie',
            name='sinopsis',
        ),
    ]
