# Generated by Django 3.0.5 on 2020-04-17 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20200418_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tuser',
            name='user_email',
            field=models.EmailField(max_length=50),
        ),
    ]