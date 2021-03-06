# Generated by Django 2.1.1 on 2018-10-14 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=200)),
                ('post_text', models.TextField(max_length=999)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
