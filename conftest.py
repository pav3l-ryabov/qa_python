import pytest
from main import BooksCollector

@pytest.fixture
def book_with_genre():
    collector = BooksCollector()
    collector.add_new_book('Гордость и предубеждение и зомби')
    collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
    return collector