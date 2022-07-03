import unittest
from temperature import *

def measure_temperature(test_file, sigma):
    with open(test_file, 'r') as f:
        unit = f.readline().replace('\n', '').split(',')
        measurements = f.readlines()
        for measurement in measurements:
            measurement = measurement.replace('\n', '')
            measur = [int(i) for i in measurement.split(',')]
            height = measur[1] * 0.3048 if unit[1] == "Alt[ft]" else measur[1]
            temp =  get_temperature(height)
            if abs(temp - measur[0]) > sigma:
                return False
    return True


class TemperatureTest(unittest.TestCase):
    def test_test_1_file(self):
        self.assertTrue(measure_temperature("Test_1.txt", 0.667))

    def test_test_2_file(self):
        self.assertTrue(measure_temperature("Test_2.txt", 9))

    def test_test_3_file(self):
        self.assertTrue(measure_temperature("Test_3.txt", 16))


if __name__ == '__main__':
    unittest.main()
