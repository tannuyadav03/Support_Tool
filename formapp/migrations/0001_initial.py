# Generated by Django 2.0.3 on 2022-06-27 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50, verbose_name='Enter first name')),
                ('lastname', models.CharField(max_length=50, verbose_name='Enter last name')),
                ('email', models.EmailField(max_length=254, verbose_name='Enter Email')),
                ('file', models.FileField(upload_to='')),
            ],
            options={
                'db_table': 'files',
            },
        ),
    ]
