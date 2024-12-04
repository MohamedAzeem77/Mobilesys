from django.db import models

class mobile(models.Model):
    id=models.AutoField(primary_key=True)
    brand=models.CharField(max_length=140)
    model=models.CharField(max_length=120)
    price=models.DecimalField(max_digits=10,decimal_places=2)


    def __str__(self):
        return f"{self.brand}"