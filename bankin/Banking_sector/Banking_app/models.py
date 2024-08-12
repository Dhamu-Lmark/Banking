from django.db import models
import random
import string
from django.core.validators import RegexValidator


# Create your models here.
def gen_ac_no():
    return ''.join(random.choices(string.digits, k=12))



class Accounts(models.Model):
    name = models.CharField(max_length=100, null=True)
    account_no = models.CharField(max_length=100, default=gen_ac_no, unique=True, editable=False)
    ac_balance = models.FloatField(default=1000)
    ph_number = models.CharField(max_length=10,validators=[RegexValidator(r'^\d{10}$', 'Phone number must be 10 digits numbers.')])   
    date_of_birth = models.DateField('Date-Of-Birth(YYYY-MM-DD)')
    create_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Transfer(models.Model):
    sender = models.ForeignKey(Accounts, related_name='Senter_transfer', on_delete=models.CASCADE)
    receiver = models.ForeignKey(Accounts, related_name='receiver_transfer', on_delete=models.CASCADE)
    amount = models.FloatField()
    time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.sender.name
    
    @property
    def debit(self):
        return self.sender.name ,self.sender.account_no, -self.amount, self.time
    
    @property
    def credit(self):
        return self.receiver.name, self.receiver.account_no, +self.amount, self.time        
    
    @property
    def AnotherCredit(self):
        return self.receiver.name, self.receiver.account_no, +self.amount, self.time    

class TransactionDetail(models.Model):
    TRANSACTION_TYPES = [
        ('debit', 'Debit'),
        ('credit', 'Credit'),
        ('another_credit', 'Another Credit'),
    ]

    transaction = models.ForeignKey(Transfer, related_name='details', on_delete=models.CASCADE)
    account = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    tran_type = models.CharField(max_length=15, choices=TRANSACTION_TYPES)

    def __str__(self):
        return f'{self.tran_type} of {self.account.name}'

    
    
    
     