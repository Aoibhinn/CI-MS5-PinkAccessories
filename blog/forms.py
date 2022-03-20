from django import forms
from products.widgets import CustomClearableFileInput
from .models import Blog, Comment


class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('title', 'content', 'image', 'status')

    image = forms.ImageField(
        label='Image',
        required=False,
        widget=CustomClearableFileInput)


class CommentForm(forms.ModelForm):
    """
    A class for the comment form
    """
    class Meta:
        model = Comment
        fields = ('comment_text',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholder
        Args:
            self (object): Self object
            *args: *args
            **kwargs: **kwargs
        Returns:
            N/A
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'comment_text': 'Add your comment text here',
        }
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-1'
            self.fields[field].label = "Comment"
