import math
import unittest

class Paint(object):
	def __init__(self, name, sizeOfCan, price, areaCanCover):
		self.name = name
		self.sizeOfCan = sizeOfCan
		self.price = price
		self.areaCanCover = areaCanCover
		self.totalArea = self.sizeOfCan * self.areaCanCover
		self.pricePerMeter =  self.price / self.totalArea

def cheapest (toCover):
	cheapoMax = Paint("CheapoMax", 20, 19.99, 10)
	averageJoes = Paint("AverageJoes", 15, 17.99, 11)
	duluxourousPaints = Paint("DuluxourousPaints", 10, 25, 20)
	cost1 = math.floor(toCover / cheapoMax.totalArea)
	if toCover % cheapoMax.totalArea > 0:
		cost1+=1
	cost1 = cost1 * cheapoMax.price
	cost2 = math.floor(toCover / averageJoes.totalArea)
	if toCover % averageJoes.totalArea > 0:
		cost2+=1
	cost2 = cost2 * averageJoes.price
	cost3 = math.floor(toCover / duluxourousPaints.totalArea)
	if toCover % duluxourousPaints.totalArea > 0:
		cost3+=1
	cost3 = cost3 * duluxourousPaints.price
	if cost1 < cost2 and cost1 < cost3:
		print("In order to cover " + str(toCover) + "meters squared, " + cheapoMax.name +  
		" is the cheapest option, costing £" + str(cost1))
		return cost1
	elif cost2 < cost1 and cost2 < cost3:
		print("In order to cover " + str(toCover) + "meters squared, " + averageJoes.name +  
		" is the cheapest option, costing £" + str(cost2))
		return cost2 
	elif cost3 < cost1 and cost3 < cost2:
		print("In order to cover " + str(toCover) + "meters squared, " + duluxourousPaints.name +  
		" is the cheapest option, costing £" + str(cost3))
		return cost3
	elif cost1 == cost2:
		print("In order to cover " + str(toCover) + "meters squared, " + cheapoMax.name + 
		" and " + averageJoes.name + " are the cheapest option, both costing £" + str(cost1))
		return cost1
	elif cost1 == cost3:
		print("In order to cover " + str(toCover) + "meters squared, " + cheapoMax.name +  
		" and " + duluxourousPaints.name + " are the cheapest option, both costing £" + str(cost1))
		return cost1
	elif cost2 == cost3:
		print("In order to cover " + str(toCover) + "meters squared, " + averageJoes.name +  
		" and " + duluxourousPaints.name + " are the cheapest option, both costing £" + str(cost2))
		return cost2
	else:
		print("This should not be mathmatically possible")
		return null

cheapest(300)
cheapest(347)
cheapest(125)

def leastWaste (toCover):
	cheapoMax = Paint("CheapoMax", 20, 19.99, 10)
	averageJoes = Paint("AverageJoes", 15, 17.99, 11)
	duluxourousPaints = Paint("DuluxourousPaints", 10, 25, 20)
	waste1 = toCover % cheapoMax.areaCanCover
	waste2 = toCover % averageJoes.areaCanCover
	waste3 = toCover % duluxourousPaints.areaCanCover
	if waste1 < waste2 and waste1 < waste3:
		print("The paint with the least waste is " + cheapoMax.name)
		return cheapoMax.name
	elif waste2 < waste1 and waste2 < waste3:
		print("The paint with the least waste is " + averageJoes.name)
		return averageJoes.name
	elif waste3 < waste1 and waste3 < waste2:
		print("The paint with the least waste is " + duluxourousPaints.name)
		return duluxourousPaints.name
	elif waste1 == waste2:
		print("The paints with the least waste are " + cheapoMax.name + " and " + averageJoes.name)
		return cheapoMax.name
	elif waste1 == waste3:
		print("The paints with the least waste are " + cheapoMax.name + " and " + duluxourousPaints.name)
		return cheapoMax.name
	elif waste2 == waste3:
		print("The paints with the least waste are " + averageJoes.name + " and " + duluxourousPaints.name)
		return averageJoes.name
	else:
		print("This should not be mathmatically possible")
		return null

leastWaste(300)
leastWaste(347)
leastWaste(450)

class TestPaintWizard(unittest.TestCase):
	def test_cheapest_300(self):
		self.assertEqual(35.98, cheapest(300))
	def test_cheapest_347(self):
		self.assertEqual(39.98, cheapest(347))
	def test_leastWaste_300(self):
		self.assertEqual("CheapoMax", leastWaste(300))
	def test_leastWaste_347(self):
		self.assertEqual("AverageJoes", leastWaste(347))
if __name__ == '__main__':
	unittest.main()























