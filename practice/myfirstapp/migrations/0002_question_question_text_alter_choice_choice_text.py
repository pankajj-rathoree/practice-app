# Generated by Django 4.1.7 on 2023-03-22 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfirstapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_text',
            field=models.CharField(default='what', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(max_length=200),
        ),
    ]
