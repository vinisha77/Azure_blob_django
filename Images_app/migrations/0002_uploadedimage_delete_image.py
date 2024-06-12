# Generated by Django 5.0.6 on 2024-06-07 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Images_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
