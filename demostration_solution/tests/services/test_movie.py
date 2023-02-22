from unittest.mock import MagicMock
import pytest

from dao.model.movie import Movie
from dao.movie import MovieDAO
from service.movie import MovieService


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    m1 = Movie(id=1, title='title1')
    m2 = Movie(id=2, title='title2')
    m3 = Movie(id=3, title='title3')

    movie_dao.get_one = MagicMock(return_value=m1)
    movie_dao.get_all = MagicMock(return_value=[m1, m2, m3])
    movie_dao.create = MagicMock(return_value=Movie(id=3))
    movie_dao.update = MagicMock()
    movie_dao.delete = MagicMock()
    return movie_dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)

        assert movie is not None
        assert movie.id is not None

    def test_get_all(self):
        movies = self.movie_service.get_all()

        assert len(movies) > 0

    def test_create(self):
        movie_data = {
            'title': 'movie4',
        }

        movie = self.movie_service.create(movie_data)

        assert movie.id is not None

    def test_update(self):
        movie_data = {
            'id': 4,
            'title': 'title4',
        }

        self.movie_service.update(movie_data)

    def test_delete(self):
        self.movie_service.delete(1)
