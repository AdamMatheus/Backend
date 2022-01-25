# Generated by Django 4.0.1 on 2022-01-24 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fscohort', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['number'], 'verbose_name_plural': 'Student_List'},
        ),
        migrations.AddField(
            model_name='student',
            name='about_me',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
        migrations.AlterModelTable(
            name='student',
            table='Student_Table',
        ),
    ]