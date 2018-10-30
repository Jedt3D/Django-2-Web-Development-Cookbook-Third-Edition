# Generated by Django 2.1.1 on 2018-09-30 22:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='CSSExtension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_item_css_class', models.CharField(blank=True, choices=[('featured', '.featured')], max_length=200, verbose_name='Menu Item CSS Class')),
                ('body_css_class', models.CharField(blank=True, choices=[('serious', '.serious'), ('playful', '.playful')], max_length=200, verbose_name='Body CSS Class')),
                ('extended_object', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='cms.Page')),
                ('public_extension', models.OneToOneField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='draft_extension', to='cms_extensions.CSSExtension')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
