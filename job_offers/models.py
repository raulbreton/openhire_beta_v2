from django.db import models
from employers.models import EmployerProfile

class JobOffer(models.Model):
    JOB_TYPE_CHOICES = (
        ('Tiempo Completo', 'Tiempo Completo'),
        ('Medio Tiempo', 'Medio Tiempo'),
        ('Becario', 'Becario'),
        ('Temporal', 'Temporal'),
        ('Contrato', 'Contrato'),
    )

    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100, default='UnknownCompany')
    description = models.TextField()
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    employer_profile = models.ForeignKey(
        EmployerProfile, on_delete=models.CASCADE, 
        related_name='job_offers', default=None
    )

    def __str__(self):
        return(
            f"{self.job_title}"
            f"{self.company_name}"
            #f"({self.created_at:%d-%m-%Y})"
        )