from django.db import models

class Test(models.Model):

    class CorrectChoice(models.TextChoices):
        OPTION1 = 'a', 'option1'
        OPTION2 = 'b', 'option2'
        OPTION3 = 'c', 'option3'
        OPTION4 = 'd', 'option4'

    question = models.CharField(max_length=1000, blank=False)
    option1 = models.CharField(max_length=500, blank=False)
    option2 = models.CharField(max_length=500, blank=False)
    option3 = models.CharField(max_length=500, blank=False)
    option4 = models.CharField(max_length=500, blank=False)
    correct = models.CharField(max_length=1, choices = CorrectChoice, default=CorrectChoice.OPTION1)

    def __str__(self) -> str:
        return self.question
