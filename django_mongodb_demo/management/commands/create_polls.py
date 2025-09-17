import os
import random
from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
from django_mongodb_demo.models import Poll, Question, Choice


class Command(BaseCommand):
    help = "Create polls with questions and choices using Faker. Optionally set MONGODB_URI."

    def add_arguments(self, parser):
        parser.add_argument("num_polls", type=int, help="Number of polls to create")
        parser.add_argument(
            "num_questions", type=int, help="Number of questions per poll"
        )
        parser.add_argument(
            "num_choices", type=int, help="Number of choices per question"
        )
        parser.add_argument(
            "--flush",
            action="store_true",
            help="Delete all existing polls before creating new ones",
        )
        parser.add_argument(
            "--mongodb-uri",
            type=str,
            help="MongoDB connection URI to set as MONGODB_URI env var",
        )

    def handle(self, *args, **options):
        fake = Faker()

        num_polls = options["num_polls"]
        num_questions = options["num_questions"]
        num_choices = options["num_choices"]

        # Set the MONGODB_URI env var if provided
        if options.get("mongodb_uri"):
            os.environ["MONGODB_URI"] = options["mongodb_uri"]
            self.stdout.write(
                self.style.SUCCESS(f"MONGODB_URI set to: {options['mongodb_uri']}")
            )

        if options["flush"]:
            Poll.objects.all().delete()
            self.stdout.write(self.style.WARNING("Deleted all existing polls."))

        for _ in range(num_polls):
            poll = Poll.objects.create(
                title=fake.sentence(nb_words=5),
                description=fake.paragraph(nb_sentences=3),
                pub_date=timezone.now(),
            )
            self.stdout.write(self.style.SUCCESS(f"Created Poll: {poll.title}"))

            for _ in range(num_questions):
                question = Question.objects.create(
                    poll=poll, question_text=fake.sentence(nb_words=8)
                )
                self.stdout.write(f"  Added Question: {question.question_text}")

                for _ in range(num_choices):
                    choice = Choice.objects.create(
                        question=question,
                        choice_text=fake.word(),
                        votes=random.randint(0, 50),
                    )
                    self.stdout.write(
                        f"    Added Choice: {choice.choice_text} ({choice.votes} votes)"
                    )

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully created {num_polls} poll(s) with {num_questions} questions and {num_choices} choices each."
            )
        )
