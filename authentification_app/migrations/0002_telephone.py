# Generated by Django 5.2.2 on 2025-06-23 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentification_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Telephone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_telephone', models.CharField(max_length=255)),
            ],
        ),
    ]
