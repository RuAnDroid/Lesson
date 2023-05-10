# Generated by Django 4.1.7 on 2023-04-15 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('featured_image', models.ImageField(default='default.jpg', upload_to='projects/%Y/%m/%d/')),
                ('price', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Cards',
        ),
    ]