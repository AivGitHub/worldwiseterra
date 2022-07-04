from django.core.management.base import BaseCommand

from utils.general import General


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('-tso', '--to-stdout', action='store_true')
        parser.add_argument('-gsk', '--generate-secret_key', action='store_true')
        parser.add_argument('-kl', '--key-length', type=int)
        parser.add_argument('-ac', '--allowed-chars', type=str)

    def handle(self, *args, **options):
        if options.get('generate_secret_key'):
            self.handle_generate_secret_key(
                options.get('key_length'),
                options.get('allowed_chars'),
                options.get('to_stdout')
            )

    def handle_generate_secret_key(self, key_length, allowed_chars, to_stdout=False):
        secret_key = General.generate_secret_key(
            key_length=key_length,
            allowed_chars=allowed_chars
        )

        if to_stdout:
            self.stdout.write(secret_key)
        else:
            return secret_key
