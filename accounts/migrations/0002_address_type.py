# Generated by Django 2.1.4 on 2018-12-20 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='type',
            field=models.CharField(choices=[('H', 'Home'), ('N', 'Neibour'), ('R', 'Relative'), ('O', 'Office')], default='H', max_length=50),
        ),
    ]
