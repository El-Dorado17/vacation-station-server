# Generated by Django 4.2.2 on 2023-06-16 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vacationstationapi', '0003_remove_vacation_user_vacation_vacation_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacation',
            name='vacation_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vacationstationapi.vacationuser'),
        ),
    ]