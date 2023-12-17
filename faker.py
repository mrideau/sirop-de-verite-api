from cards.models import Card


def main():
    fake: Faker = Faker()
    for i in range(30):
        task = Card.objects.create(
            # name=fake.
            # name=fake.paragraph(nb_sentences=1),
            # status=random.choice(Task.StatusChoice.choices)[0],
        )

if __name__ == "__main__":
    import os

    from django.core.wsgi import get_wsgi_application

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    application = get_wsgi_application()

    import random

    from faker import Faker
    from todo.models import Task

    main()