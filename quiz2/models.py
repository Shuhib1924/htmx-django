from django.db import models


class Question(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text


class Answer(models.Model):
    text = models.CharField(max_length=255)
    question = models.ForeignKey(
        Question, related_name="answers", on_delete=models.CASCADE
    )
    next_question = models.ForeignKey(
        Question, related_name="next_answers", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.text
