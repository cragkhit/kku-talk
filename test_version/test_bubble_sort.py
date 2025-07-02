import unittest
from main import bubble_sort


class TestBubbleSort(unittest.TestCase):
    
    def test_empty_array(self):
        """Test bubble sort with an empty array"""
        result = bubble_sort([])
        self.assertEqual(result, [])
    
    def test_single_element(self):
        """Test bubble sort with a single element"""
        result = bubble_sort([5])
        self.assertEqual(result, [5])
    
    def test_already_sorted(self):
        """Test bubble sort with an already sorted array"""
        result = bubble_sort([1, 2, 3, 4, 5])
        self.assertEqual(result, [1, 2, 3, 4, 5])
    
    def test_reverse_sorted(self):
        """Test bubble sort with a reverse sorted array"""
        result = bubble_sort([5, 4, 3, 2, 1])
        self.assertEqual(result, [1, 2, 3, 4, 5])
    
    def test_random_order(self):
        """Test bubble sort with randomly ordered elements"""
        result = bubble_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
        self.assertEqual(result, [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])
    
    def test_duplicates(self):
        """Test bubble sort with duplicate elements"""
        result = bubble_sort([3, 3, 3, 3])
        self.assertEqual(result, [3, 3, 3, 3])
    
    def test_negative_numbers(self):
        """Test bubble sort with negative numbers"""
        result = bubble_sort([-3, -1, -4, -1, -5])
        self.assertEqual(result, [-5, -4, -3, -1, -1])
    
    def test_mixed_positive_negative(self):
        """Test bubble sort with mixed positive and negative numbers"""
        result = bubble_sort([-2, 5, -1, 3, 0, -4])
        self.assertEqual(result, [-4, -2, -1, 0, 3, 5])
    
    def test_floating_point_numbers(self):
        """Test bubble sort with floating point numbers"""
        result = bubble_sort([3.14, 2.71, 1.41, 2.71, 0.57])
        self.assertEqual(result, [0.57, 1.41, 2.71, 2.71, 3.14])
    
    def test_two_elements_sorted(self):
        """Test bubble sort with two elements already sorted"""
        result = bubble_sort([1, 2])
        self.assertEqual(result, [1, 2])
    
    def test_two_elements_unsorted(self):
        """Test bubble sort with two elements unsorted"""
        result = bubble_sort([2, 1])
        self.assertEqual(result, [1, 2])
    
    def test_large_array(self):
        """Test bubble sort with a larger array"""
        input_array = [64, 34, 25, 12, 22, 11, 90, 5, 77, 30]
        expected = [5, 11, 12, 22, 25, 30, 34, 64, 77, 90]
        result = bubble_sort(input_array)
        self.assertEqual(result, expected)
    
    def test_array_modification(self):
        """Test that bubble sort modifies the original array"""
        original = [3, 1, 4, 1, 5]
        result = bubble_sort(original)
        # The function modifies the original array
        self.assertEqual(original, [1, 1, 3, 4, 5])
        self.assertEqual(result, [1, 1, 3, 4, 5])
        # Verify they are the same object
        self.assertIs(result, original)


if __name__ == '__main__':
    # Run the tests
    unittest.main()
