from django.db import models

# Create your models here.

class Transaction(models.Model):

    title = models.CharField(max_length=100)

    amount = models.FloatField()

    transaction_type = models.CharField(max_length=100, choices=(("DEBIT","DEBIT"),("CREDIT","CREDIT")))

    

    def save(self, *args, **kwargs):

        if self.transaction_type == "DEBIT":
            self.amount = self.amount * -1
        return super().save(*args, **kwargs)
    


