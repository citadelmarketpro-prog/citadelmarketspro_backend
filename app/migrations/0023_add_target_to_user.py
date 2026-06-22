from django.db import migrations, models


class Migration(migrations.Migration):
    """
    The 'target' column already exists in the DB (NOT NULL, no default),
    which causes registration to fail. This migration:
    1. Updates Django's state so it knows about the field (state_operations).
    2. Sets the DB-level default so existing rows and new rows get 50000 if
       no value is supplied (database_operations).
    """

    dependencies = [
        ('app', '0022_add_card_model'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.AddField(
                    model_name='customuser',
                    name='target',
                    field=models.DecimalField(
                        verbose_name='Deposit Target',
                        max_digits=20,
                        decimal_places=2,
                        default=50000.00,
                        help_text="Admin-set deposit target shown as a progress bar on the user's portfolio page."
                    ),
                ),
            ],
            database_operations=[
                migrations.RunSQL(
                    sql="ALTER TABLE app_customuser ALTER COLUMN target SET DEFAULT 50000.00;",
                    reverse_sql="ALTER TABLE app_customuser ALTER COLUMN target DROP DEFAULT;",
                ),
            ],
        ),
    ]
