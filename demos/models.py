# Create your models here.
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class ModelComment(models.Model):
    pass


class ModelAuthor(models.Model):
    username = models.CharField(max_length=150, null=False, blank=False)

    def __str__(self):
        return self.username  # This gets called for example when you create an user input, the text shown is the returned string


class ModelPost(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(User)
    body = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return "post from {} created at {}".format(self.author, self.created)


class ModelDummyUser(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=False)
    age = models.IntegerField(validators=[MinValueValidator(3), MaxValueValidator(100)])
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def get_absolute_url(self):
        return reverse('demos-ui-createview')


class ModelDemo(models.Model):
    first_name = models.CharField(max_length=100)

    age = models.IntegerField(validators=[MinValueValidator(3), MaxValueValidator(100)])
    created_at = models.DateTimeField(auto_now_add=True, editable=False)


class ModelBookForRest(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100)


class ModelAuthorForRest(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class ModelBookForRestEx(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(ModelAuthorForRest, on_delete=models.CASCADE, related_name='author')
    isbn = models.CharField(max_length=100)
