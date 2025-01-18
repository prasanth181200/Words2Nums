import unittest
import main

class TestNumberToWords(unittest.TestCase):
    def setUp(self):
        # Create an inflect convert for converting numbers to words
        self.convert = main

    def test_one_digit(self):
        number = 7
        words = "seven"
        result = self.convert.words2nums(words)
        self.assertEqual(result, number)

    def test_two_digits(self):
        number = 57
        words = "fifty-seven"
        result = self.convert.words2nums(words)
        self.assertEqual(result, number)

    def test_three_digits(self):
        number = 231
        words = "two hundred thirty-one"
        result = self.convert.words2nums(words)
        self.assertEqual(result, number)

    def test_four_digits(self):
        number = 3127
        words = "three thousand one hundred twenty-seven"
        result = self.convert.words2nums(words)
        self.assertEqual(result, number)

    def test_five_digits(self):
        number = 45689
        words = "forty-five thousand six hundred eighty-nine"
        result = self.convert.words2nums(words)
        self.assertEqual(result, number)

    def test_six_digits(self):
        number = 678945
        words = "six hundred seventy-eight thousand nine hundred forty-five"
        result = self.convert.words2nums(words)
        self.assertEqual(result, number)

    def test_seven_digits(self):
        number = 1234567
        words = "one million two hundred thirty-four thousand five hundred sixty-seven"
        result = self.convert.words2nums(words)
        self.assertEqual(result, number)

    def test_eight_digits(self):
        number = 23456789
        words = "twenty-three million four hundred fifty-six thousand seven hundred eighty-nine"
        result = self.convert.words2nums(words)
        self.assertEqual(result, number)

    def test_nine_digits(self):
        number = 345678901
        words = "three hundred forty-five million six hundred seventy-eight thousand nine hundred one"
        result = self.convert.words2nums(words)
        self.assertEqual(result, number)

    def test_ten_digits(self):
        number = 1234567891
        words = "one billion two hundred thirty-four million five hundred sixty-seven thousand eight hundred ninety-one"
        result = self.convert.words2nums(words)
        self.assertEqual(result, number)

if __name__ == "__main__":
    unittest.main()
