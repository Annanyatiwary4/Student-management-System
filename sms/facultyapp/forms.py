from django import forms
from .models import AddCourse, Marks

class AddCourseForm(forms.ModelForm):
    class Meta:
        model = AddCourse
        fields = ['student', 'course', 'section']
        widgets = {
            'course': forms.Select(attrs={'class': 'form-control'}),
            'section': forms.Select(attrs={'class': 'form-control'}),
            'student': forms.Select(attrs={'class': 'form-control'}),
        }

class MarksForm(forms.ModelForm):
    class Meta:
        model = Marks
        fields = ['student', 'course', 'marks']
