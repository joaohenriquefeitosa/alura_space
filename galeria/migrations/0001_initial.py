# Generated by Django 4.2.3 on 2023-07-26 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fotografia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('legenda', models.CharField(blank=True, max_length=150, null=True)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('foto', models.CharField(max_length=100)),
            ],
        ),
    ]
