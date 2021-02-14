from unittest import TestCase
from main import Mini_max_sum

class TestMiniMaxSum(TestCase):
    def tests_if_there_is_Mini_max_sum_class(self):
        if Mini_max_sum([1, 2, 3, 4, 5]):
            return

    def tests_if_mini_max_sum_is_recieving_an_argument(self):
        if Mini_max_sum([1, 2, 3, 4, 5]):
            return

    def tests_if_mini_max_sum_is_reading_the_argument(self):
        assert result.arr == [1, 2, 3, 4, 5]

    def test_if_calculate_sum_exists(self):
        if result.create_new_lists():
            return

    def test_if_calculate_sum_is_excludin_the_elements(self):
        assert result.create_new_lists() == ([[2, 3, 4, 5], [1, 3, 4, 5], [1, 2, 4, 5], [1, 2, 3, 5], [1, 2, 3, 4]])

    def test_if_calculate_max_exists(self):
        if result.calculate_max():
            return

    def test_calculate_max(self):
        assert result.calculate_max() == ([14, 13, 12, 11, 10])

    def test_if_comparing_exists(self):
        if result.comparing():
            return

result = Mini_max_sum([1, 2, 3, 4, 5])