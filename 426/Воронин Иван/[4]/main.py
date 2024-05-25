import random
import math

# class for world environment properties (sound speed in this case) and all objects
class World():
	__instance = None
	
	def __new__(cls):
		if not isinstance(cls.__instance, cls):
			cls.__instance = object.__new__(cls)
		return cls.__instance
	
	def __init__(self):
		self.SOUND_SPEED = 343
		self.objects = set([])
	
	def add_object(self, obj):
		self.objects.add(obj)



class Entity:
	def __init__(self, coords, speed):
		self.coordinates = coords
		self.speed = speed


class Radar(Entity):
	__instance = None
	def __new__(self, environment):
		if not isinstance(self.__instance, self):
			self.__instance = object.__new__(self)
		return self.__instance

	def __init__(self, environment, coords = [0,0,0], speed = [0,0,0]):
		self.environment = environment
		self.coordinates = coords
		self.speed = speed

	def pulse(self, azimuth = 0, elevation = 0):
		objects_array = []
		for object in self.environment.objects:
			if object != self:
				objects_array.append(object)
		for object in objects_array:
			azimuth = math.degrees(math.atan2(object.coordinates[0], object.coordinates[1]))
			elevation = math.degrees(math.atan2(object.coordinates[2], math.sqrt(object.coordinates[0]**2 + object.coordinates[1]**2)))
			print(f"azimuth = {azimuth}, elevation = {elevation}")


world = World()
radar = Radar(world)
world.add_object(radar)

flying_entities_num = input("Type amount of flying object: ")
for _ in range(int(flying_entities_num)):
	x = random.randint(-1000, 1000)
	y = random.randint(-1000, 1000)
	z = random.randint(-1000, 1000)
	dx = random.randint(-100, 100)
	dy = random.randint(-100, 100)
	dz = random.randint(-100, 100)
	world.add_object(Entity([x, y, z], [dx, dy, dz]))
radar.pulse()