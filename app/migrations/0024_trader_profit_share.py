from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_add_target_to_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='trader',
            name='profit_share',
            field=models.PositiveSmallIntegerField(default=50, help_text='Percentage of profits shared with the trader (e.g. 50 means 50%)'),
        ),
    ]
