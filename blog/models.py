from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from ckeditor.fields import RichTextField


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = RichTextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to='blog_images',validators=[FileExtensionValidator(['jpg','gif','png'])],blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
# 
# class Aboutme(models.Model):
#     mybio = RichTextField(max_length=700)
#
#     def publish(self):
#         self.save()
#
#     def __str__(self):
#         return self.mybio
