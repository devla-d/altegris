# Generated by Django 3.2.9 on 2022-01-16 14:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Packages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', models.IntegerField()),
                ('name', models.CharField(max_length=40)),
                ('percent', models.IntegerField()),
                ('min_amount', models.IntegerField(default=0)),
                ('max_amount', models.IntegerField(default=0)),
                ('ref_percent', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wallet_address', models.CharField(blank=True, max_length=50, null=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('coin_tpye', models.CharField(blank=True, max_length=50, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('approved_date', models.DateTimeField(blank=True, null=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('status', models.CharField(default='pending', max_length=40)),
                ('trans_type', models.CharField(max_length=50)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_transactions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('body', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('read', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_notify', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Investments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_invested', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('is_complete', models.BooleanField(default=False)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('active', 'active'), ('inactive', 'inactive'), ('pending', 'pending'), ('completed', 'completed')], default='inactive', max_length=40)),
                ('amount_earn', models.IntegerField(default=0)),
                ('package', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pack', to='users_app.packages')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
