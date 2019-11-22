from django.db import models

class Customer(models.Model):
    customer_fname=models.CharField(max_length=20)
    customer_lname=models.CharField(max_length=20)

    def __str__(self):
        return(f" Customer Full Name: {self.customer_lname}, {self.customer_fname}")