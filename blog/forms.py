from django import forms
from products.widgets import CustomClearableFileInput
from .models import Blog


class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('title', 'content', 'image', 'status')

    image = forms.ImageField(
        label='Image',
        required=False,
        widget=CustomClearableFileInput)
