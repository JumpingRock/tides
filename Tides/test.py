import tc
import datetime
import unittest

class TestTidesMethods(unittest.TestCase):

	def test_station(self):
		char_harb = tc.Station('SCarolina', '8665530')
		self.assertEqual(str(char_harb),'SCarolina, 8665530')
		self.assertEqual(str(char_harb.site),'SCarolina')
		self.assertEqual(str(char_harb.station_number),'8665530')

	def test_station2(self):
		ash_riv = tc.Station('SCarolina', '8665099')
		self.assertEqual(str(ash_riv),'SCarolina, 8665099')
		self.assertEqual(str(ash_riv.site),'SCarolina')
		self.assertEqual(str(ash_riv.station_number),'8665099')

	def test_tides(self):
		char_harb = tc.Station('SCarolina', '8665530')
		char_harb_tides = tc.Tides(char_harb, tc.Date('1', '2016')).tides
		self.assertEqual(str(char_harb_tides), '[High, 5:48, AM, 5.5, Low, 12:02, PM, 0.1, High, 5:51, PM, 4.8]')		
		self.assertEqual(str(char_harb_tides[2]), 'High, 5:51, PM, 4.8')
		self.assertEqual(str(char_harb_tides[1].level), '0.1')

	def test_tides2(self):
		ash_riv = tc.Station('SCarolina', '8665099')
		ash_riv_tides = tc.Tides(ash_riv, tc.Date('1','2016')).tides
		self.assertEqual(str(ash_riv_tides), '[High, 6:18, AM, 5.9, Low, 12:31, PM, 0.1, High, 6:21, PM, 5.2]')		
		self.assertEqual(str(ash_riv_tides[0]), 'High, 6:18, AM, 5.9')
		self.assertEqual(str(ash_riv_tides[2].level), '5.2')

if __name__ == '__main__':
	unittest.main()