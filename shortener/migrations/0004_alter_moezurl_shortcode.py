# Generated by Django 5.1.4 on 2024-12-17 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0003_alter_moezurl_shortcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moezurl',
            name='shortcode',
            field=models.CharField(blank=True, default='R7mZ3V', max_length=20),
        ),
    ]
