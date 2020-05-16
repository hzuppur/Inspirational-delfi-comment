from django.core.management.base import BaseCommand, CommandError
import konna_web.delfi.table_filler as tf

class Command(BaseCommand):
  #python manage.py add_articles_to_table
  help = 'Adds all delfi front page articles to the database'

  def handle(self, *args, **options):
    tf.add_articles_to_table()
    self.stdout.write(self.style.SUCCESS('Successfully added comments to table'))
