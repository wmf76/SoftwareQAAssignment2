import unittest


from bmi import bmi

class BMITest(unittest.TestCase):
    
    def test_Underwieght(self):
        self.assertEqual(bmi(92.5,5,0),18.5,"Under weight")
        self.assertEqual(bmi(92,5,0),18.4,"Under weight")

    def test_Overwieght(self):
        self.assertEqual(bmi(200.5,6,4),25.1,"Over weight")
        self.assertEqual(bmi(210,6,4),26.2,"Over weight")

    def test_obese(self):
        self.assertEqual(bmi(120,4,4),32.0,"Obese")
        self.assertEqual(bmi(111,4,3.6),30.0,"Obese")

    def test_normal(self):
        self.assertEqual(bmi(95,5,0),19.0,"Normal weight")
        self.assertEqual(bmi(120,5,0),24.0,"Normal weight")
        
