from django import forms
from .models import Student, Book, Library

# forms.py
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'student_class', 'photo', 'video']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'author', 'publication', 'year']



class LibraryForm(forms.ModelForm):
    class Meta:
        model = Library
        fields = ['student', 'book', 'start_date', 'end_date']

        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
