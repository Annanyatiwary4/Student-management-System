
# Generated by Django 5.1.1 on 2024-10-16 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0001_initial'),
        ('facultyapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AddCourses',
            new_name='AddCourse',
        ),
        migrations.DeleteModel(
            name='AddCourseForm',
        ),
    ]
