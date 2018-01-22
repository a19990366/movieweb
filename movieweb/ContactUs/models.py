from django.db import models




class ContactMe(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    phonenumber = models.CharField(max_length=128)
    content = models.TextField()

    def __str__(self):
        return self.name+'('+self.email+')'
    
    class Meta:
        verbose_name = "聯絡人資訊"
        verbose_name_plural = verbose_name