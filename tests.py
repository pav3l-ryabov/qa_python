import pytest
from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == ''

    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Фантастика'

    def test_get_books_with_specific_genre(self, book_with_genre):
        assert book_with_genre.get_books_with_specific_genre('Фантастика') == ['Гордость и предубеждение и зомби']

    def test_get_books_genre(self, book_with_genre):
        assert book_with_genre.get_books_genre() == {'Гордость и предубеждение и зомби': 'Фантастика'}

    def test_get_books_for_children(self, book_with_genre):
        assert book_with_genre.get_books_for_children() == ['Гордость и предубеждение и зомби']

    def test_add_book_in_favorites(self, book_with_genre):
        book_with_genre.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert book_with_genre.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби']

    def test_delete_book_from_favorites(self, book_with_genre):
        book_with_genre.add_book_in_favorites('Гордость и предубеждение и зомби')
        book_with_genre.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert book_with_genre.get_list_of_favorites_books() == []

    def test_add_duplicate_book(self, book_with_genre):
        book_with_genre.add_new_book('Гордость и предубеждение и зомби')
        assert len(book_with_genre.get_books_genre()) == 1

    @pytest.mark.parametrize("book_name, expected_result",
    [
        ('Война и мир', True),
        ('1984', True),
        ('A', True)
    ]
                             )
    def test_add_new_book_with_valid_names(self,book_with_genre, book_name, expected_result):
        book_with_genre.add_new_book(book_name)
        books = book_with_genre.get_books_genre()
        assert (book_name in books) == expected_result

    @pytest.mark.parametrize("book_name, expected_result",
    [
        ('', False),
        ('A' * 41, False)
    ]
                             )
    def test_add_new_book_with_valid_names(self,book_with_genre, book_name, expected_result):
        book_with_genre.add_new_book(book_name)
        books = book_with_genre.get_books_genre()
        assert (book_name in books) == expected_result