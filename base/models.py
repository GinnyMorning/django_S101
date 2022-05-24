from operator import mod
from pickle import TRUE
from pyexpat import model
from statistics import mode
import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class QuizzQuestion(models.Model):
    title = models.TextField()
    content = models.TextField()
    createAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title
    
class QuizzAnswer(models.Model):
    answer = models.TextField(max_length=255)
    isRight = models.BooleanField(default=False)
    quizQuestionId = models.ForeignKey(QuizzQuestion,on_delete=models.CASCADE)
    createAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.answer} - {self.isRight}"
    
class Quizz(models.Model):
    class QuizzStatus(models.IntegerChoices):
        NEW = 1, "New"
        READY = 2, "Ready"
        DELETED = 3, "Deleted"
        HIDE = 4, "Hidden"
    
    title = models.TextField(max_length=255)
    description = models.TextField()
    status = models.PositiveSmallIntegerField(
        choices=QuizzStatus.choices,
        default=QuizzStatus.NEW
    )
    question = models.ForeignKey(QuizzQuestion,on_delete=models.SET_NULL,null=True)
    createAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title

class Results(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=TRUE)
    quiz_id = models.ForeignKey(Quizz,on_delete=models.SET_NULL,null=True)
    result = models.JSONField(decoder=None,encoder=None)
    createAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return str(self.id)