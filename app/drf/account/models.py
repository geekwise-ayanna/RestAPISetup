from django.db import models

class Account (models.Model):
    account_no=models.CharField(max_length=10)
    account_email=models.EmailField(max_length=30)

    def __str__(self):
        return(f"Account No: {self.account_no}")