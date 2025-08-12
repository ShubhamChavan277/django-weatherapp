from django.db import models

# Create your models here.
class Contact_Form(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    text_message = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Contact_Form'  
        verbose_name_plural = 'Contact_Form'  