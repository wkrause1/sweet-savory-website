# Generated by Django 2.2.1 on 2019-05-07 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donuts', '0007_auto_20190507_0224'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_us', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
