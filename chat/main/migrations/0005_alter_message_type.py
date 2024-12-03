# Generated by Django 4.2.15 on 2024-11-28 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_message_conversation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='type',
            field=models.CharField(choices=[('TXT', 'Text'), ('IMG', 'Image'), ('VD', 'Video'), ('VC', 'Voice'), ('ATT', 'Attachment'), ('INVITE', 'Invitation')], default='TXT', max_length=10),
        ),
    ]