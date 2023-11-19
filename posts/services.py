from .models import Post
from .forms import PostForm
from faker import Faker

faker = Faker("pl_PL")


class ModelService:

    @classmethod
    def list(cls) -> list[Post]:
        posts_list = Post.objects.order_by('-created_at')
        return posts_list

    @classmethod
    def create(cls, request) -> Post:
        post = PostForm(request)
        return post

    @classmethod
    def get(cls, id: int) -> Post:
        ob = Post.objects.get(pk=id)
        return ob

    def delete(id: int):
        Post.objects.filter(pk=id).delete()


class FakerPostService:
    id = 0

    @classmethod
    def list(cls) -> list[Post]:
        n = 4
        return [FakerPostService.create() for _ in range(n)]


    @classmethod
    def create(cls, request=None) -> Post:
        post = Post(
            id=cls.id,
            title=faker.text(50),
            content=faker.text(500),
            created_at=faker.date_time(),
            updated_at=faker.date_time()
        )
        cls.id += 1
        return post

    @classmethod
    def get(cls, id: int) -> Post:
        ob = Post(
            id=id,
            title=faker.text(50),
            content=faker.text(500),
            created_at=faker.date_time(),
            updated_at=faker.date_time()
        )
        return ob

