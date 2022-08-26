from django import forms
from .models import Student


class StudentFrom(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('fullname','number','mobile', 'email', 'gender','path')
        labels = {
            'fullname':'Full Name',
            'number':'Student Number'
        }
    def __init__(self, *args, **kwargs):
        super(StudentFrom,self).__init__(*args, **kwargs)
        self.fields['path'].empty_label = "Select"
        self.fields['number'].required = False
