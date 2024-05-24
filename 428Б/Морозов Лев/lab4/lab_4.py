from math import hypot, degrees, acos, atan2
from random import randint

class Radar:

    _instance = None #singleton

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, x_radar, y_radar, z_radar):
        if not hasattr(self, 'x_radar'):
            self.x_radar = x_radar
            self.y_radar = y_radar
            self.z_radar = z_radar

    def coordinates_radar_relative(self, x_object, y_object, z_object):
        x_radar_relative = x_object - self.x_radar
        y_radar_relative = y_object - self.y_radar
        z_radar_relative = z_object - self.z_radar
        return x_radar_relative, y_radar_relative, z_radar_relative

    def dekart_to_spheric(self, x_object, y_object, z_object):
        r = round(hypot(x_object, y_object, z_object), 1)
        theta = round(degrees(acos(z_object / r)), 1)
        phi = degrees(atan2(y_object, x_object))
        phi = (phi + 360) % 360
        phi = round(phi, 1)
        return [r, theta, phi]
        
class Flying_object:
    
    def __init__(self,x_object,y_object,z_object,vx_object,vy_object,vz_object):
        self.x_object = x_object
        self.y_object = y_object
        self.z_object = z_object
        self.vx_object = vx_object
        self.vy_object = vy_object
        self.vz_object = vz_object
        
    def coordinates_update(self,t):
        self.x_object+=self.vx_object*t
        self.y_object+=self.vy_object*t
        self.z_object+=self.vz_object*t
    
class Objects_creator:
    
    N = int(input("\nВведите количество летающих объектов: "))
    
    flying_objects = []
    
    def objects_creation(x_radar,y_radar):
        for i in range (Objects_creator.N):
            x_object = randint(x_radar-10000,x_radar+10000)
            y_object = randint(y_radar-10000,y_radar+10000)
            z_object = randint(0,10000)
            vx_object = randint(-555,555)
            vy_object = randint(-555,555)
            vz_object = randint(0,555)
            while vx_object==0 or vy_object==0 or vz_object==0:
                vx_object = randint(-555,555)
                vy_object = randint(-555,555)
                vz_object = randint(0,100)
            Objects_creator.flying_objects.append(Flying_object(x_object,y_object,z_object,vx_object,vy_object,vz_object))
        return Objects_creator.flying_objects
    
class Radar_creator:
    
    def radar_creation():
        
        x_radar = randint(-10000,10000)
        y_radar = randint(-10000,10000)
        z_radar = 0
    
        radar = Radar(x_radar,y_radar,z_radar)
        
        return radar
    
class Coordinates_shower:
    
    def coordinates_showing(radar, flying_objects):
        print("\n№\t\tr(м)\t\ttheta(°)\t  phi(°)")
        counter = 1
        for flying_object in flying_objects:
            spheric_coordinates = radar.dekart_to_spheric(flying_object.x_object,flying_object.y_object,flying_object.z_object)
            print(f"{counter}\t\t{spheric_coordinates[0]}\t\t{spheric_coordinates[1]}\t\t  {spheric_coordinates[2]}")
            counter+=1
            
class Radar_shower:
    
    def radar_showing(radar):
        print("\nИнформация о радаре:")
        print (f"\nX-координата: {radar.x_radar} м\nY-координата: {radar.y_radar} м\nZ-координата: {radar.z_radar} м")
            
class Flying_objects_shower:
    
    def flying_objects_showing(flying_objects):
        print("\nИнформация о летающих объектах:")
        counter = 1
        for flying_object in flying_objects:
            print(f"\n{counter}:")
            print (f"\nX-координата: {flying_object.x_object} м\nY-координата: {flying_object.y_object} м\nZ-координата: {flying_object.z_object} м")
            print (f"\nVx-скорость: {flying_object.vx_object} м/с\nVy-скорость: {flying_object.vy_object} м/с\nVz-скорость: {flying_object.vz_object} м/с")
            counter+=1
def main():
    
    radar = Radar_creator.radar_creation()
    
    Radar_shower.radar_showing(radar)
    
    flying_objects = Objects_creator.objects_creation(radar.x_radar, radar.y_radar)
    
    Flying_objects_shower.flying_objects_showing(flying_objects)
    
    print("\nТекущие сферические координаты летающих объектов относительно радара:")

    Coordinates_shower.coordinates_showing(radar, flying_objects)

    t = int(input("\nВведите время в секундах, по прошествии которого нужно определить координаты объектов: "))

    for flying_object in flying_objects:
        flying_object.coordinates_update(t)
        
    print(f"\nСферические координаты летающих объектов относительно радара через {t} с:")

    Coordinates_shower.coordinates_showing(radar, flying_objects)

if __name__ == "__main__":
    main()