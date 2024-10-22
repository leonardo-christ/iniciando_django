import pytest

from iniciando.factories import PostFactory

@pytest.fixture
def post_published():
    return PostFactory(title='Post published')

@pytest.mark.django_db
def test_create_published_post(post_published):
    assert post_published.title == 'Post published'