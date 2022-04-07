# Generated by Django 4.0.3 on 2022-04-07 08:26

from django.db import migrations, models
import exam_project.utils.validators


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_userprofile_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='', validators=[exam_project.utils.validators.MaxFileSizeInMbValidator]),
        ),
    ]
