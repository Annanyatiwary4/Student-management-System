# Generated by Django 5.1.1 on 2024-10-29 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_studentlist_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=15)),
                ('address', models.TextField(max_length=160)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
