from django.shortcuts import render,redirect,HttpResponse
from .models import *
from .forms import *

# Create your views here.
def home(request):
    ac = Accounts.objects.all()
    return render(request, 'home.html', {'ac':ac})

def add_account(request):
    if request.method == 'POST':
        form = Account_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_ac')
    else:
        form = Account_form()
    return render(request, 'add_ac.html', {'form':form})


def edit_account(request,id):
    edit = Accounts.objects.get(id=id)
    if request.method == 'POST':
        form = Account_form(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('view_ac')
    else:
        form = Account_form(instance=edit)
    return render(request, 'edit.html', {'form':form})

def delete_account(request,id):
    edit = Accounts.objects.get(id=id)
    edit.delete()
    return redirect('view_ac')

def View_account(request):
    ac = Accounts.objects.all()
    return render(request, 'view_acc.html', {'ac':ac})

def transfer(request):
    if request.method == 'POST':
        form = Transfer_form(request.POST)
        if form.is_valid():
            trans = form.save()
            if trans.amount<=trans.sender.ac_balance:
                trans.sender.ac_balance -= trans.amount
                trans.receiver.ac_balance += trans.amount
                trans.sender.save()
                trans.receiver.save()
                
                # Save transaction details
                TransactionDetail.objects.create(transaction=trans, account=trans.sender, amount=trans.amount, tran_type='debit')
                TransactionDetail.objects.create(transaction=trans, account=trans.receiver, amount=trans.amount, tran_type='credit')
                TransactionDetail.objects.create(transaction=trans, account=trans.receiver, amount=trans.amount, tran_type='another_credit')

                
                return redirect('home')
            else:
                return HttpResponse('insuffient balance')
    else:
        form = Transfer_form()
    return render(request, 'transfer.html', {'form':form})
        
def view_transfer(request):
    transfers = Transfer.objects.all()
    return render(request, 'transfer_status.html', {'tf': transfers})