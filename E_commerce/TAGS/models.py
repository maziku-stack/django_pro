from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Create your models here.
class Tag(models.Model):
    label = models.CharField(max_length=50)



class TaggedItems(models.Model):
     # What tag has applied to what object  
     tag = models.ForeignKey(Tag,on_delete= models.CASCADE)
     # To solve this problems we need two things
     # 1.Type of object like video,Article,product
     # 2.ID
     # Therefore to solve the generic relatioship we use the Contenttype app from django
     #so we import the contenttype from django library to resolve the generic relationship of entities rather than importing the particular module
     content_type = models.ForeignKey(ContentType,on_delete= models.CASCADE)
     object_Id = models.PositiveIntegerField()
     content_object = GenericForeignKey('content_type', 'object_Id')
    
     def __str__(self):
        return f"{self.tag} - {self.content_object}"