# Generated by Django 3.1.6 on 2021-03-02 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='province',
            field=models.CharField(choices=[('Gauteng', 'Gauteng'), ('Mpumalanga', 'Mpumalanga'), ('KwaZulu Natal', 'KwaZulu Natal'), ('Free State', 'Free State'), ('Limpopo', 'Limpopo'), ('North West', 'North West'), ('Eastern Cape', 'Eastern Cape'), ('Western Cape', 'Western Cape'), ('Northern Cape', 'Northern Cape')], max_length=150, null=True),
        ),
    ]
