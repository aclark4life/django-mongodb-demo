from django.core.management.base import BaseCommand  
from django.utils.text import slugify  
from faker import Faker  
import random  
  
# Import models from your app  
from django_mongodb_demo.models import Author, Article, Comment  
  
  
class Command(BaseCommand):  
    help = "Create fake authors, articles, and comments using Faker"  
  
    def add_arguments(self, parser):  
        parser.add_argument(  
            "--authors",  
            type=int,  
            default=5,  
            help="Number of authors to create (default 5)",  
        )  
        parser.add_argument(  
            "--articles",  
            type=int,  
            default=5,  
            help="Number of articles per author to create (default 5)",  
        )  
        parser.add_argument(  
            "--comments",  
            type=int,  
            default=3,  
            help="Number of comments per article to create (default 3)",  
        )  
  
    def handle(self, *args, **options):  
        fake = Faker()  
        Faker.seed(0)  
        random.seed(0)  
  
        num_authors = options["authors"]  
        num_articles = options["articles"]  
        num_comments = options["comments"]  
  
        self.stdout.write(  
            self.style.MIGRATE_HEADING(f"Creating {num_authors} authors...")  
        )  
  
        authors = []  
        for _ in range(num_authors):  
            # Ensure unique email  
            email = fake.unique.email()  
            author = Author.objects.create(  
                name=fake.name(),  
                email=email,  
                bio=fake.paragraph(nb_sentences=5),  
            )  
            authors.append(author)  
  
        self.stdout.write(self.style.SUCCESS(f"Created {len(authors)} authors."))  
  
        total_articles = 0  
        total_comments = 0  
  
        self.stdout.write(  
            self.style.MIGRATE_HEADING("Creating articles and comments...")  
        )  
  
        for author in authors:  
            for _ in range(num_articles):  
                title = fake.sentence(nb_words=random.randint(3, 7))  
                slug = slugify(title)  
  
                # Ensure unique slug per author  
                slug_candidate = slug  
                counter = 1  
                while Article.objects.filter(slug=slug_candidate, author=author).exists():  
                    slug_candidate = f"{slug}-{counter}"  
                    counter += 1  
  
                # Prevent ValueError: sample larger than population  
                words_list = fake.words(nb=random.randint(2, 8))  
                k = min(len(words_list), random.randint(2, 5))  
                tags = random.sample(words_list, k=k)  
  
                article = Article.objects.create(  
                    title=title,  
                    slug=slug_candidate,  
                    author=author,  
                    tags=tags,  
                    content="\n\n".join(fake.paragraphs(nb=random.randint(3, 7))),  
                )  
                total_articles += 1  
  
                # Create comments for the article  
                for _ in range(num_comments):  
                    Comment.objects.create(  
                        article=article,  
                        user_name=fake.name(),  
                        text=fake.paragraph(nb_sentences=3),  
                    )  
                    total_comments += 1  
  
        self.stdout.write(  
            self.style.SUCCESS(  
                f"Created {total_articles} articles and {total_comments} comments."  
            )  
        )  
        self.stdout.write(self.style.SUCCESS("Fake data creation complete!"))  
