# Generated by Django 3.0.8 on 2020-07-14 15:09

from django.db import migrations, models
import jsignature.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JSignatureModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signature', jsignature.fields.JSignatureField(blank=True, null=True, verbose_name='Signature')),
                ('signature_date', models.DateTimeField(blank=True, null=True, verbose_name='Signature date')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
