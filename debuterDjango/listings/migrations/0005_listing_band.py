# Generated by Django 4.0.4 on 2022-04-29 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_alter_band_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='band',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.SET_DEFAULT, to='listings.band'),
        ),
    ]