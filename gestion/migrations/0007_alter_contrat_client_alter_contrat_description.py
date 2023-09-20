# Generated by Django 4.2.4 on 2023-09-17 02:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0006_delete_commande'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrat',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.client'),
        ),
        migrations.AlterField(
            model_name='contrat',
            name='description',
            field=models.TextField(),
        ),
    ]