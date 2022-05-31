import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
    
    def test_innit(self):
        loc = Location("Long Beach", 33.8, -118.2)
        self.assertEqual(loc.name, 'Long Beach')
        self.assertEqual(loc.lat, 33.8)
        self.assertEqual(loc.lon, -118.2)

    def test_eq(self):
        loc1 = Location("Long Beach", 33.8, -118.2)
        loc2 = Location("Long Beach", 33.8, -118.2)
        self.assertEqual(loc1, loc2)

    def test_eq_type(self):
        loc1 = Location("Long Beach", 33.8, -118.2)
        p1 = 'Deez Nuts'
        self.assertFalse(loc1 == p1)  # doesn't crash WOO

    def test_eq_diff_lat(self):
        loc1 = Location("Long Beach", 33.8, -118.2)
        loc2 = Location("Long Beach", 34.8, -118.2)
        self.assertFalse(loc1 == loc2)

    def test_eq_diff_lon(self):
        loc1 = Location("Long Beach", 33.8, -118.2)
        loc2 = Location("Long Beach", 33.8, -119)
        self.assertFalse(loc1 == loc2)

    def test_eq_diff_name(self):
        loc1 = Location("Long Beach", 33.8, -118.2)
        loc2 = Location("Fake Long Beach", 33.8, -118.2)
        self.assertFalse(loc1 == loc2)


if __name__ == "__main__":
        unittest.main()
