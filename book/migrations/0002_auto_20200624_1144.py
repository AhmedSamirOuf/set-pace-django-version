# Generated by Django 3.0.7 on 2020-06-24 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(default='samir', max_length=30),
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.CharField(default='thriller', max_length=15),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.CharField(default='samir', max_length=100),
        ),
        migrations.AddField(
            model_name='book',
            name='types',
            field=models.TextField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='vendors',
            field=models.TextField(max_length=30, null=True),
        ),
    ]