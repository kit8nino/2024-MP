import math
import random

class Radar:
	__instance = None

	def __new__(cls):
		if Radar.__instance is None:
			Radar.__instance = object.__new__(cls)
		return Radar.__instance

		# Модель отправки импульса
	def impulse(self, azimuth, elevation):
		pass

# Класс летающего объекта
class Object:
	def __init__(self, coordinates, velocity):
		self.coordinates = coordinates
		self.velocity = velocity

# Класс координат с возможностью перевода в сферические
class Coordinates:
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

	def to_spherical(self):
		r = math.sqrt(self.x**2 + self.y**2 + self.z**2)
		azimuth = math.degrees(math.atan2(self.y, self.x))
		elevation = math.degrees(math.atan2(self.z, math.sqrt(self.x**2 + self.y**2)))
		return r, azimuth, elevation

# Создание радара
radar = Radar()
