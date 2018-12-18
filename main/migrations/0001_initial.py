# Generated by Django 2.0.2 on 2018-12-18 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_description', models.CharField(max_length=250)),
                ('file_upload', models.FileField(upload_to='files/')),
            ],
            options={
                'db_table': 'file_upload',
            },
        ),
    ]