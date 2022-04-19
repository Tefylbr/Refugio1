# Generated by Django 4.0.3 on 2022-04-18 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_registromascota_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registromascota',
            name='imagen',
        ),
        migrations.AddField(
            model_name='registromascota',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='fotos_mascotas'),
        ),
    ]
