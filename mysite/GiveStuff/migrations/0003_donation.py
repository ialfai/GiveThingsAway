# Generated by Django 3.1.7 on 2021-03-04 20:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('GiveStuff', '0002_institution'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('address', models.TextField()),
                ('phone_number', models.IntegerField()),
                ('city', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=9)),
                ('pick_up_date', models.DateField()),
                ('pick_up_time', models.TimeField()),
                ('pick_up_comment', models.TextField()),
                ('categories', models.ManyToManyField(to='GiveStuff.Category')),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GiveStuff.institution')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
