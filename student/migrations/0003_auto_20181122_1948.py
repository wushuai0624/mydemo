# Generated by Django 2.1.3 on 2018-11-22 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_userinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stuinfo',
            name='id',
            field=models.CharField(default='', max_length=100, primary_key=True, serialize=False),
        ),
    ]
