import unittest
from client3 import *

class ClientTest(unittest.TestCase):
	def test_getDataPoint_calculatePrice(self):
		quotes = [
			{'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
			{'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
		]
		""" ------------ Add the assertion below ------------ """
		for quote in quotes:
			self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))

	def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
		quotes = [
			{'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
			{'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 127.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
		]
		""" ------------ Add the assertion below ------------ """
		for quote in quotes:
			self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))


	""" ------------ Add more unit tests ------------ """
	def test_getRatio_calculateRatio_AGreaterThanB(self):
		prices = [
			[120.48, 117.87],
			[122.73, 106.06]
		]
		for price in prices:
					self.assertEqual(getRatio(price[0], price[1]), price[0]/price[1])

	def test_getRatio_calculateRatio_BGreaterThanA(self):
		prices = [
			[117.87, 120.48],
			[106.06, 122.73]
		]
		for price in prices:
    			self.assertEqual(getRatio(price[0], price[1]), price[0]/price[1])\

	def test_getRatio_calculateRatio_AIsZero(self):
		prices = [
			[0, 117.87],
			[0, 106.06]
		]
		for price in prices:
			self.assertEqual(getRatio(price[0], price[1]), price[0]/price[1])

	def test_getRatio_calculateRatio_BIsZero(self):
		prices = [
			[117.87, 0],
			[106.06, 0]
		]
		for price in prices:
			self.assertIsNone(getRatio(price[0], price[1]))
	
	def test_getRatio_calculateRatio_AEqualToB(self):
		prices = [
			[117.87, 117.87],
			[106.06, 106.06]
		]
		for price in prices:
			self.assertEqual(getRatio(price[0], price[1]), 1)

if __name__ == '__main__':
		unittest.main()
