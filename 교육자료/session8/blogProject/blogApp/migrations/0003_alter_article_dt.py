# Generated by Django 4.1.7 on 2023-04-02 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0002_article_dt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='dt',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
