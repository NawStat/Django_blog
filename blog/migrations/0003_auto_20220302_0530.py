# Generated by Django 3.0.14 on 2022-03-02 05:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_auto_20220223_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='blog_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True, unique_for_date='publish'),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(blank=True, choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
