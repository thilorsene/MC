# Generated by Django 3.1.3 on 2021-01-07 00:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('date_naiss', models.DateField()),
                ('genre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Activite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_activite', models.DateField()),
                ('heure_debut', models.TimeField()),
                ('heure_fin', models.TimeField()),
                ('caloris', models.FloatField()),
                ('pas', models.IntegerField()),
                ('distance', models.FloatField()),
                ('minute_active', models.IntegerField()),
                ('duree', models.IntegerField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('idparticipant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='active', to='Montre_Connecte.participant')),
            ],
        ),
    ]
