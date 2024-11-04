from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published_date']  # Sort posts by publication date in descending order


####ADD COURSE ############

from django.db import models
from adminapp.models import studentList  # Importing the StudentList model

class AddCourse(models.Model):
    COURSE_CHOICES = [
        ('AOOP', 'Advanced Object-Oriented Programming'),
        ('PFSD', 'Python Full Stack Development'),
    ]
    SECTION_CHOICES = [
        ('S11', 'Section S11'),
        ('S12', 'Section S12'),
        ('S13', 'Section S13'),
        ('S14', 'Section S14'),
        ('S15', 'Section S15'),
    ]
    student = models.ForeignKey(studentList, on_delete=models.CASCADE)
    course = models.CharField(max_length=50, choices=COURSE_CHOICES)
    section = models.CharField(max_length=50, choices=SECTION_CHOICES)

    def __str__(self):
        return f'{self.student.Register_Number} - {self.course} ({self.section})'


class Marks(models.Model):
    COURSE_CHOICES = [
        ('AOOP', 'Advanced Object-Oriented Programming'),
        ('PFSD', 'Python Full Stack Development'),
        # Add other courses as necessary
    ]
    student = models.ForeignKey('adminapp.studentList', on_delete=models.CASCADE)
    course = models.CharField(max_length=100, choices=COURSE_CHOICES)
    marks = models.IntegerField()

    def __str__(self):
        return f"{self.student.name} - {self.course}"
