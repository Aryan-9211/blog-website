# Generated by Django 4.2.3 on 2023-07-16 11:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0004_alter_blogmodel_image_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
