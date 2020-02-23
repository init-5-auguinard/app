# Generated by Django 2.2.9 on 2020-02-21 11:38

from django.db import migrations, models
import galerie.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Galerie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to=galerie.models.image_path)),
            ],
        ),
    ]