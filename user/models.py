from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.

#-------------
# Comapny Table
#--------------
class Company(models.Model):
    name = models.CharField(max_length=255)
    registration_no = models.CharField(max_length=100,unique=True)
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=20,blank=True)
    email = models.EmailField(blank=True)
    parent_company = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='subcompanies'
    )
    is_subcompany = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
#-------------
# Role Table
#--------------
class Role(models.Model): 
    name = models.CharField(max_length=100,unique=True)
    description = models.TextField(blank=True)
    permissions = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return self.name
#-------------
# User Table
#--------------
class User(AbstractUser):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    phone = models.CharField(max_length=20)
    
    groups = models.ManyToManyField(
        Group,
        related_name="finance_user_set",  
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="finance_user_permissions_set", 
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

    def __str__(self):
        return self.username
    
class Client(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='clients')
    business_name = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20,blank=True)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    lead_source = models.CharField(max_length=100, blank=True, null=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        if self.business_name:
            return f"{self.business_name} ({self.company.name})"
        return f"{self.first_name} {self.last_name} ({self.company.name})"