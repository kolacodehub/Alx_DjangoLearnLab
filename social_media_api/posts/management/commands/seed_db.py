import random
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from posts.models import Post, Comment
from faker import Faker

User = get_user_model()


class Command(BaseCommand):
    help = "Floods the database with dummy data for testing"

    def handle(self, *args, **kwargs):
        fake = Faker()

        self.stdout.write("Seeding database...")

        # 1. Create 5 Dummy Users
        users = []
        for i in range(5):
            # We use get_or_create so we don't crash if the script is run twice
            user, created = User.objects.get_or_create(
                username=fake.user_name(),
                email=fake.email(),
            )
            if created:
                # Give them all the same password so you can easily log in as them in Postman!
                user.set_password("testpass123")
                user.save()
            users.append(user)

        self.stdout.write(f"Created {len(users)} users.")

        # 2. Create 20 Dummy Posts
        posts = []
        for _ in range(20):
            post = Post.objects.create(
                author=random.choice(users),  # Pick a random user to be the author
                title=fake.sentence(nb_words=6),
                content=fake.paragraph(nb_sentences=5),
            )
            posts.append(post)

        self.stdout.write(f"Created {len(posts)} posts.")

        # 3. Create 50 Dummy Comments
        for _ in range(50):
            Comment.objects.create(
                post=random.choice(posts),  # Attach to a random post
                author=random.choice(users),  # Written by a random user
                content=fake.sentence(),
            )

        self.stdout.write(self.style.SUCCESS("Successfully seeded the database!"))
