from django.contrib.auth import get_user_model
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from uniauth.utils import get_idp_config, get_idp_sp_config


class Command(BaseCommand):
    help = 'Attribute release query'

    def add_arguments(self, parser):
        parser.epilog='Example: ./manage.py aacli -e https://auth.unical.it/idp/metadata/ -u joe'
        parser.add_argument('-e', required=True,
                            help="Entity to request metadata for")
        parser.add_argument('-u', required=True,
                            help="username to test")
        parser.add_argument('-debug', required=False, action="store_true",
                            help="see debug message")

    def handle(self, *args, **options):
        sp = get_idp_sp_config()
        #import pdb; pdb.set_trace()
        raise Exception('Not yet implemented')
