# Generated by Django 5.1 on 2024-08-09 11:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Banking_app', '0006_alter_accounts_ph_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tran_type', models.CharField(choices=[('debit', 'Debit'), ('credit', 'Credit'), ('another_credit', 'Another Credit')], max_length=15)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Banking_app.accounts')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='Banking_app.transfer')),
            ],
        ),
    ]
