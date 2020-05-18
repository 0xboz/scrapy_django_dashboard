# Generated by Django 3.0.6 on 2020-05-18 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('scrapy_django_dashboard', '0001_initial_fork'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsWebsite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('url', models.URLField()),
                ('scraper', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='scrapy_django_dashboard.Scraper')),
                ('scraper_runtime', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='scrapy_django_dashboard.SchedulerRuntime')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('url', models.URLField(blank=True)),
                ('thumbnail', models.CharField(blank=True, max_length=200)),
                ('checker_runtime', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='scrapy_django_dashboard.SchedulerRuntime')),
                ('news_website', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='open_news.NewsWebsite')),
            ],
        ),
    ]