from django.db import models
from users.models import CustomUser
from django.db.models.signals import post_save

class EmployerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, default=None)
    company_name = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    website = models.URLField(blank=True, null=True)
    about_company = models.TextField(blank=True, null=True)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=20, blank=True, null=True)
    logo = models.ImageField(upload_to='employer_logos/', blank=True, null=True)
    #job_offers = models.ManyToManyField('job_offers.JobOffer')

    def __str__(self):
        return self.user.email

def created_profile(sender, instance, created, **kwargs):
    if created and instance.is_employer:
        user_profile = EmployerProfile(user=instance)
        user_profile.save()

post_save.connect(created_profile, sender=CustomUser)