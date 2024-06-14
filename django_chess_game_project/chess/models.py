from django.db import models
import json

class BoardState(models.Model):
    
    state = models.TextField()