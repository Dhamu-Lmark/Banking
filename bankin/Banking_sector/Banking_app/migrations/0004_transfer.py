# Generated by Django 5.1 on 2024-08-08 11:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Banking_app', '0003_alter_accounts_ph_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver_transfer', to='Banking_app.accounts')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Senter_transfer', to='Banking_app.accounts')),
            ],
        ),
    ]
