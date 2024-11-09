import factory
from django.contrib.auth.models import User
from factory.faker import faker

from .models import Post

FAKE = faker.Faker()

# 1. python manage.py shell
# 2. from blog3.factory import PostFactory
# 3. x= PostFactory.create_batch(100)


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Faker("sentence", nb_words=12)
    subtitle = factory.Faker("sentence", nb_words=12)
    slug = factory.Faker("slug")
    author = User.objects.get_or_create(username="d")[0]

    @factory.lazy_attribute
    def content(self):
        x = ""
        for _ in range(0, 5):
            x += "\n" + FAKE.paragraph() + "\n"
        return x

    status = "published"
