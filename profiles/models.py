from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(blank=True, upload_to='photos')
    bio = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"profile of {self.user.username}"
    
class ProgrammingQuestion(models.Model):
    question_text = models.TextField()
    answer_text = models.TextField()
    difficulty_level = models.CharField(max_length=20, default='hard' )
    tags = models.CharField(max_length=255, blank=True)  # To store comma-separated tags

    def __str__(self):
        return f"{self.question_text[:50]}..."  # Truncate long questions for display
