from django import forms
from .models import  Task
from .models import studentList

class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=['title']

class StudentForm(forms.ModelForm):
    class Meta:
        model = studentList
        fields=['Register_Number','Name']


class uploadfileform(forms.Form):
    file = forms.FileField()

        ## feedback form #########


from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email','phone_number', 'comment']
        labels = {

            'name': 'Your Name',
            'email': 'Your Email',
            'phone_number': 'phone_number',
            'comment': 'Your Comment (max 160 characters)',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}),
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your comment',
                'maxlength': '160',  # HTML attribute to limit input length
                'rows': 3,
            }),
        }

    def clean_comment(self):
        comment = self.cleaned_data.get('comment')
        if len(comment) > 160:
            raise forms.ValidationError("Comment cannot exceed 160 characters.")
        return comment


from .models import Contact
class Contactform(forms.ModelForm):
    class Meta:
        model = Contact

        fields=['name','phone_number','address']
