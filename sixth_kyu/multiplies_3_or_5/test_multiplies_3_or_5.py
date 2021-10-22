from unittest import TestCase
import multiplies_3_or_5

class Test(TestCase):
    def test_solution(self):
        self.assertEqual(multiplies_3_or_5.solution(10), 23)
        self.assertEqual(multiplies_3_or_5.solution(4), 3)
        self.assertEqual(multiplies_3_or_5.solution(6), 8)
        self.assertEqual(multiplies_3_or_5.solution(16), 60)
        self.assertEqual(multiplies_3_or_5.solution(3), 0)
        self.assertEqual(multiplies_3_or_5.solution(15), 45)
