# Generated by Django 4.2.9 on 2024-03-12 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AgentApp', '0002_alter_packagesplit_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='packagemodel',
            name='activities',
        ),
        migrations.AddField(
            model_name='activitiesmodel',
            name='activity_images',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='packagemodel',
            name='status',
            field=models.CharField(default='active', max_length=255),
        ),
    ]