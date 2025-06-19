from django.db import models

class GlobalUser(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20, unique=True) 
    email_address = models.EmailField(blank=True, null=True)
    num_spam = models.IntegerField(default=0)
    total_appearance = models.IntegerField(default=0)
    spam_likelyhood = models.IntegerField(default=0)
    
    class Meta:
        db_table = 'global_users'

class GlobalContacts(models.Model):
    contact_from = models.EmailField(blank=True, null=True)
    contact_to = models.EmailField(blank=True, null=True)
    
    class Meta:
        db_table = 'global_contacts'

