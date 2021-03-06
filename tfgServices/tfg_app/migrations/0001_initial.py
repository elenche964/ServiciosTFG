# Generated by Django 2.2.8 on 2021-04-06 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'carer',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.IntegerField()),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('picture', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'contact',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fav_contact', models.ForeignKey(db_column='fav_contact', on_delete=django.db.models.deletion.DO_NOTHING, to='tfg_app.Contact')),
            ],
            options={
                'db_table': 'patient',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('surname', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('picture', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'user',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='UserSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_option', models.CharField(blank=True, max_length=255, null=True)),
                ('second_option', models.CharField(blank=True, max_length=255, null=True)),
                ('id_user', models.ForeignKey(db_column='id_user', on_delete=django.db.models.deletion.DO_NOTHING, to='tfg_app.User')),
            ],
            options={
                'db_table': 'user_settings',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PatientSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('danger_color', models.IntegerField(blank=True, null=True)),
                ('warning_color', models.IntegerField(blank=True, null=True)),
                ('right_color', models.IntegerField(blank=True, null=True)),
                ('id_patient', models.ForeignKey(db_column='id_patient', on_delete=django.db.models.deletion.DO_NOTHING, to='tfg_app.Patient')),
            ],
            options={
                'db_table': 'patient_settings',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PatientInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info_type', models.CharField(max_length=255)),
                ('info', models.CharField(max_length=255)),
                ('id_patient', models.ForeignKey(db_column='id_patient', on_delete=django.db.models.deletion.DO_NOTHING, to='tfg_app.Patient')),
            ],
            options={
                'db_table': 'patient_info',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PatientCarer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_carer', models.ForeignKey(db_column='id_carer', on_delete=django.db.models.deletion.DO_NOTHING, to='tfg_app.Carer')),
                ('id_patient', models.ForeignKey(db_column='id_patient', on_delete=django.db.models.deletion.DO_NOTHING, to='tfg_app.Patient')),
            ],
            options={
                'db_table': 'patient_carer',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='patient',
            name='id_user',
            field=models.ForeignKey(db_column='id_user', on_delete=django.db.models.deletion.DO_NOTHING, to='tfg_app.User'),
        ),
        migrations.CreateModel(
            name='NfcSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.IntegerField()),
                ('card_info_type', models.CharField(max_length=255)),
                ('card_info', models.CharField(max_length=255)),
                ('id_patient', models.ForeignKey(db_column='id_patient', on_delete=django.db.models.deletion.DO_NOTHING, to='tfg_app.Patient')),
            ],
            options={
                'db_table': 'nfc_settings',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DistanceSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('latitude_x', models.FloatField()),
                ('longitude_y', models.FloatField()),
                ('short_radius', models.IntegerField(blank=True, null=True)),
                ('medium_radius', models.IntegerField(blank=True, null=True)),
                ('long_radius', models.IntegerField(blank=True, null=True)),
                ('id_patient', models.ForeignKey(db_column='id_patient', on_delete=django.db.models.deletion.DO_NOTHING, to='tfg_app.Patient')),
            ],
            options={
                'db_table': 'distance_settings',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='contact',
            name='id_patient',
            field=models.ForeignKey(db_column='id_patient', on_delete=django.db.models.deletion.DO_NOTHING, to='tfg_app.Patient'),
        ),
        migrations.CreateModel(
            name='CarerSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_option', models.CharField(blank=True, max_length=255, null=True)),
                ('second_option', models.CharField(blank=True, max_length=255, null=True)),
                ('id_carer', models.ForeignKey(db_column='id_carer', on_delete=django.db.models.deletion.DO_NOTHING, to='tfg_app.Carer')),
            ],
            options={
                'db_table': 'carer_settings',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='carer',
            name='id_user',
            field=models.ForeignKey(db_column='id_user', on_delete=django.db.models.deletion.DO_NOTHING, to='tfg_app.User'),
        ),
    ]
