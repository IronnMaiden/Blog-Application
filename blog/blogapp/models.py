from django.db import models

# Create your models here.

class BlogAuthor(models.Model):
	bio = models.TextField(max_length= 400, help_text="Enter your bio details here.")
