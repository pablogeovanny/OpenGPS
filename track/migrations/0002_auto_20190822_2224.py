# Generated by Django 2.2.1 on 2019-08-22 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ana_0684_2019_07_17',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Timestamp', models.CharField(max_length=100)),
                ('Latitude', models.FloatField()),
                ('Longitude', models.FloatField()),
                ('Altitude', models.IntegerField()),
                ('Distance', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='ana_0684_2019_07_18',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Timestamp', models.CharField(max_length=100)),
                ('Latitude', models.FloatField()),
                ('Longitude', models.FloatField()),
                ('Altitude', models.IntegerField()),
                ('Distance', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='ana_0684_2019_07_19',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Timestamp', models.CharField(max_length=100)),
                ('Latitude', models.FloatField()),
                ('Longitude', models.FloatField()),
                ('Altitude', models.IntegerField()),
                ('Distance', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='juan_8356_2019_07_05',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Timestamp', models.CharField(max_length=100)),
                ('Latitude', models.FloatField()),
                ('Longitude', models.FloatField()),
                ('Altitude', models.IntegerField()),
                ('Distance', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='juan_8356_2019_07_06',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Timestamp', models.CharField(max_length=100)),
                ('Latitude', models.FloatField()),
                ('Longitude', models.FloatField()),
                ('Altitude', models.IntegerField()),
                ('Distance', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='juan_8356_2019_07_09',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Timestamp', models.CharField(max_length=100)),
                ('Latitude', models.FloatField()),
                ('Longitude', models.FloatField()),
                ('Altitude', models.IntegerField()),
                ('Distance', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='juan_9012_2019_07_13',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Timestamp', models.CharField(max_length=100)),
                ('Latitude', models.FloatField()),
                ('Longitude', models.FloatField()),
                ('Altitude', models.IntegerField()),
                ('Distance', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='juan_9012_2019_07_16',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Timestamp', models.CharField(max_length=100)),
                ('Latitude', models.FloatField()),
                ('Longitude', models.FloatField()),
                ('Altitude', models.IntegerField()),
                ('Distance', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='superlimpio_6468_2019_07_29',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Timestamp', models.CharField(max_length=100)),
                ('Latitude', models.FloatField()),
                ('Longitude', models.FloatField()),
                ('Altitude', models.IntegerField()),
                ('Distance', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='superlimpio_6468_2019_07_30',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Timestamp', models.CharField(max_length=100)),
                ('Latitude', models.FloatField()),
                ('Longitude', models.FloatField()),
                ('Altitude', models.IntegerField()),
                ('Distance', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='superlimpio_6468_2019_07_31',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Timestamp', models.CharField(max_length=100)),
                ('Latitude', models.FloatField()),
                ('Longitude', models.FloatField()),
                ('Altitude', models.IntegerField()),
                ('Distance', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='ventasexpres_1847_2019_07_20',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Timestamp', models.CharField(max_length=100)),
                ('Latitude', models.FloatField()),
                ('Longitude', models.FloatField()),
                ('Altitude', models.IntegerField()),
                ('Distance', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='ventasexpres_1847_2019_07_22',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Timestamp', models.CharField(max_length=100)),
                ('Latitude', models.FloatField()),
                ('Longitude', models.FloatField()),
                ('Altitude', models.IntegerField()),
                ('Distance', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='ventasexpres_1847_2019_07_23',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Timestamp', models.CharField(max_length=100)),
                ('Latitude', models.FloatField()),
                ('Longitude', models.FloatField()),
                ('Altitude', models.IntegerField()),
                ('Distance', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='ventasexpres_9656_2019_07_24',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Timestamp', models.CharField(max_length=100)),
                ('Latitude', models.FloatField()),
                ('Longitude', models.FloatField()),
                ('Altitude', models.IntegerField()),
                ('Distance', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='ventasexpres_9656_2019_07_25',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Timestamp', models.CharField(max_length=100)),
                ('Latitude', models.FloatField()),
                ('Longitude', models.FloatField()),
                ('Altitude', models.IntegerField()),
                ('Distance', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.RemoveField(
            model_name='juan_8356_2019_07_03',
            name='Description',
        ),
    ]
