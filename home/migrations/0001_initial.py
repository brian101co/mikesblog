# Generated by Django 3.0.9 on 2020-08-14 04:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('lead_text', models.CharField(blank=True, help_text='Subheading text under the banner title', max_length=150)),
                ('button_text_one', models.CharField(default='See Gallery', help_text='Button Text', max_length=50)),
                ('button_text_two', models.CharField(default='Read Blog', help_text='Read Blog', max_length=50)),
                ('banner_background_image', models.ForeignKey(help_text='Banner background image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('button_one', models.ForeignKey(blank=True, help_text='Select an optional page to link to', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page')),
                ('button_two', models.ForeignKey(blank=True, help_text='Select an optional page to link to', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
