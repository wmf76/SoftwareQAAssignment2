import unittest

from retirement import savings_per_year, num_years_till_goal, age_when_goal_met

class RetirementTest(unittest.TestCase):
    def test_savings_per_year(self):
        self.assertEqual(savings_per_year(65000,0.1),8775)
        self.assertEqual(savings_per_year(100000,0.15),20250)
    def test_years_till_goal(self):
        self.assertEqual(num_years_till_goal(1500000,8775),171)
        self.assertEqual(num_years_till_goal(500000,20250),25)
