from django.db import models
from django.conf import settings

class Bill(models.Model):
    id = models.AutoField(primary_key=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    payment_status = models.CharField(
        max_length=10, 
        choices=[('unpaid', 'Unpaid'), ('paid', 'Paid')], 
        default='unpaid'
    )
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"Bill {self.id} - {self.payment_status}"
