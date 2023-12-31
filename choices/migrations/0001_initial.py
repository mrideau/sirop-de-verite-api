# Generated by Django 4.2.7 on 2023-12-23 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('selected_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='selected_card', to='cards.card')),
            ],
        ),
    ]
