from django.db import models

# Create your models here.

class Language(models.Model):
    name = models.CharField(max_length=100, unique=True)
    icon = models.ImageField(upload_to='language-icons/', blank=True, null=True)

    def __str__(self):
        return self.name

class DifficultyEnum(models.TextChoices):
    EASY = 'easy', 'Easy'
    MEDIUM = 'medium', 'Medium'
    HARD = 'hard', 'Hard'

class Question(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    difficulty = models.CharField(max_length=10, choices=DifficultyEnum.choices)
    
    def __str__(self):
        return self.question