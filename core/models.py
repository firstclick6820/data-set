from django.db import models




# Affiliate Programms Model
class AffiliatePrograms(models.Model):
    service = models.CharField(max_length=200)
    bio = models.CharField(max_length=255)
    earnings = models.CharField(max_length=255)
    link = models.URLField()
    type = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    
    def __str__(self):
        return self.service
    
    


    