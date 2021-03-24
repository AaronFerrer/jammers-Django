# Generated by Django 3.1.5 on 2021-02-04 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deformity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="Enter the patient's deformity.", max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Surgeon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='First Name', max_length=200)),
                ('middle_name', models.CharField(help_text='Middle Name', max_length=200)),
                ('last_name', models.CharField(help_text='Last Name', max_length=200)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='First Name', max_length=200)),
                ('middle_name', models.CharField(help_text='Middle Name', max_length=200)),
                ('last_name', models.CharField(help_text='Last Name', max_length=200)),
                ('date_of_birth', models.DateField()),
                ('comment', models.TextField(help_text='Comment or Description of condition.', max_length=200)),
                ('height', models.CharField(help_text='Height', max_length=200)),
                ('weight', models.CharField(help_text='Weight', max_length=200)),
                ('surgery_date', models.DateField()),
                ('deform_class', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='braceconfig.deformity')),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
    ]
