# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Status of a blog item, draft or published
STATUS = (
    (0, "Draft"),
    (1, "Published")
)


class Post(models.Model):
    """
    This model is for a post item
    """
    class Meta:
        ordering = ['-create_date']

    title = models.CharField(
        verbose_name=_('Title'),
        max_length=250,
        unique=True
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='blog_posts'
    )
    content = models.TextField(
        max_length=500,
    )
    image = models.ImageField(
        null=True,
        blank=True
    )
    update_date = models.DateTimeField(
        auto_now=True
    )
    create_date = models.DateTimeField(
        auto_now_add=True
    )
    status = models.IntegerField(
        choices=STATUS,
        default=0
    )

    def __str__(self):
        """
        Return new title string
        Args:
            self (object): self
        Returns:
            blog title
        """
        return self.title


class Comment(models.Model):
    """
    This model is for a post item comment
    """
    class Meta:
        ordering = ['create_date']

    user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    comment_text = models.TextField(
        verbose_name=_('Comment Text'),
        max_length=250,
        null=False,
        blank=False
    )
    create_date = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        """
        Return comment text string
        Args:
            self (object): self
        Returns:
            comment text
        """
        return self.comment_text