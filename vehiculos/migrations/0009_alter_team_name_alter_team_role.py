# Generated by Django 4.2.1 on 2023-06-24 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0008_alter_team_name_alter_team_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='role',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
