from django.db import models

# Create your models here.
class UploadForm(models.Model):  
    firstname = models.CharField("Enter first name", max_length=50)  
    lastname  = models.CharField("Enter last name", max_length = 50)  
    email     = models.EmailField("Enter Email")  
    file      = models.FileField() # for creating file input  
  
    class Meta:  
        db_table = "files"

