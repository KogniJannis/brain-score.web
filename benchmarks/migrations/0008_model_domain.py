# Generated by Django 3.2.14 on 2023-02-15 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('benchmarks', '0007_rename_number_of_images_benchmarkmeta_number_of_stimuli'),
    ]

    operations = [
        migrations.AddField(
            model_name='model',
            name='domain',
            field=models.CharField(default='vision', max_length=200, null=True),
        ),
    ]