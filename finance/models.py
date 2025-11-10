from django.db import models
from user.models import Company,User,Client

# Create your models here.

#-------------
# FINANCES
#--------------

#-------------------
# Services Table
#-------------------
class Service(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    unit_price = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.name
#-------------------
# Quotation Table
#-------------------
class Quotation(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='quotations')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_quotations')
    date_created = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2,default=0)
    status = models.CharField(max_length=20, default='Pending')
    class Meta:
        ordering = ['date_created']

    def __str__(self):
        return f"Quotation #{self.id} - {self.client.__str__()}"
    
#---------------------------
# Quotation-Line Item Table
#---------------------------   
class QuotationItem(models.Model):
    quotation = models.ForeignKey(Quotation, on_delete=models.CASCADE, related_name='items')
    description = models.CharField(max_length=255)
    quantity = models.DecimalField(max_digits=10, decimal_places=2,default=1)
    unit_price = models.DecimalField(max_digits=12, decimal_places=2)
    total_price = models.DecimalField(max_digits=12, decimal_places=2)
    def __str__(self):
        return f"{self.description} - {self.quantity} x {self.unit_price}"
    def save(self, *args, **kwargs):
        self.total_price = self.quantity * self.unit_price
        super().save(*args, **kwargs)
#-------------------
# Invoice Table
#-------------------
class Invoice(models.Model):
    quotation = models.OneToOneField(Quotation, on_delete=models.CASCADE, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE,related_name='invoices')
    total_amount = models.DecimalField(max_digits=12, decimal_places=2,default=0)
    issued_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()
    paid = models.BooleanField(default=False)
    class Meta:
        ordering = ['issued_date']

    def __str__(self):
        return f"Invoice #{self.id} - {self.client.__str__()}"

    
class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='items')
    quotation_item = models.ForeignKey(QuotationItem, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.CharField(max_length=255)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit_price = models.DecimalField(max_digits=12, decimal_places=2)
    total_price = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.description} - {self.quantity} x {self.unit_price}"
    def save(self, *args, **kwargs):
        self.total_price = self.quantity * self.unit_price
        super().save(*args, **kwargs)

#-------------------
# Expenses Table
#-------------------
class Expense(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    recorded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Expense #{self.id} - {self.amount}"
    
#-------------------
# Payments Table
#-------------------
class Payments(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    invoice = models.ForeignKey(Invoice, on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    method = models.CharField(max_length=50, choices=[
        ("CARD","Card"),
        ("CASH","Cash"),
        ("BANK","Bank Transfer"),
        ("OTHER","Other")
    ])
    date=models.DateTimeField(auto_now_add=True)
    is_paid=models.BooleanField(default=False)
    note=models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Payments #{self.id} - {self.amount}"