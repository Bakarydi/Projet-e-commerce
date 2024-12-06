# Generated by Django 4.1.1 on 2024-10-01 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Produits', '0002_alter_mesproduits_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagesCategorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgs', models.ImageField(upload_to='img_categorie')),
            ],
        ),
        migrations.RemoveField(
            model_name='categories',
            name='image_categorie',
        ),
        migrations.AddField(
            model_name='categories',
            name='image_categorie',
            field=models.ManyToManyField(to='Produits.imagescategorie'),
        ),
    ]