from django.db import models

# Form model.
class Waitlist(models.Model):
    email = models.EmailField()
    date_sent = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email