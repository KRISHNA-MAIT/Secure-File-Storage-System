# Generated by Django 2.1.7 on 2019-03-15 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20190315_0252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='FirstName',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='LastName',
            field=models.CharField(default='', max_length=20),
        ),
    ]