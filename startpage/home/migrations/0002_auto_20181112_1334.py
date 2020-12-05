# Generated by Django 2.1.3 on 2018-11-12 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('priority', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='site',
            name='group',
            field=models.CharField(default='常用', max_length=128),
            preserve_default=False,
        ),
    ]