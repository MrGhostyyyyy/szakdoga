import csv
from django.core.management.base import BaseCommand, CommandParser
from database.models import CardForm, CharacterForm, AchievementForm


class Command(BaseCommand):
    help = """Imports data from a given .csv file. 
            Accepting: ``cards.csv``, ``achievements.csv`` and ``charactercards.csv``."""

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("file_path", nargs=1, type=str)

    def handle(self, *args, **options):
        self.file_path = options["file_path"][0]
        self.main()

    def main(self):
        with open(self.file_path, "r") as f:
            reader = csv.DictReader(f, delimiter=";")

            for _, row in enumerate(reader):
                if "charactercards.csv" in self.file_path:
                    form = CharacterForm(data=row)
                elif "cards.csv" in self.file_path:
                    form = CardForm(data=row)
                elif "achievements.csv" in self.file_path:
                    form = AchievementForm(data=row)

                if form.is_valid():
                    form.save()
                else:
                    self.stderr.write(f"Error reading {form.errors.items()}!\n")
