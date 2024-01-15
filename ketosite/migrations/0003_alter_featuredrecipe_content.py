from django.db import migrations, models
import ckeditor.fields

class Migration(migrations.Migration):

    dependencies = [
        ('ketosite', '0002_alter_blogpost_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featuredrecipe',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
