from django.db import models

class Topic(models.Model):
    """A topic user is learnig about"""
    text = models.charField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
def __str__(self):
    """Return a string representation of model."""
    return self.text