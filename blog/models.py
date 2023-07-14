from django.db import models
from froala_editor.fields import FroalaField

# Create your models here.
class BlogModel(models.Model):
    title = models.CharField(max_length=1000)
    content = FroalaField()
    image = models.ImageField(upload_to='static/images')
    created_at = models.DateTimeField(auto_now_add=True)
    upload_to = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.self
    