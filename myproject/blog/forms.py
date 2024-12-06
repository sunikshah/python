from django import forms
from .models import Blog, Student, Item

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'author', 'content']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','address', 'phone_no']

    def clean(self):
        return super().clean()

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description']