import math

class Radar:
    
    _instance = None
    
    def __init__(self, pos_x, pos_y, pos_z):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos_z = pos_z
        
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def get_spherical_coords(self, objects):
        for obj in objects:
            obj.print_spherical_coords(self.pos_x, self.pos_y, self.pos_z)

    def get_spherical_coords_after_time(self, objects, time):
        for obj in objects:
            obj.update_coords(time, obj.speed_proj_x, obj.speed_proj_y, obj.speed_proj_z)
        self.get_spherical_coords(objects)

class FlyingObject:
    
    def __init__(self, pos_x, pos_y, pos_z, speed_proj_x, speed_proj_y, speed_proj_z):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos_z = pos_z
        self.speed_proj_x = speed_proj_x
        self.speed_proj_y = speed_proj_y
        self.speed_proj_z = speed_proj_z

    def update_coords(self, time,speed_proj_x, speed_proj_y, speed_proj_z):
        self.pos_x += time * speed_proj_x
        self.pos_y += time * speed_proj_y
        self.pos_z += time * speed_proj_z

    def print_spherical_coords(self, radar_x, radar_y, radar_z):
        r = math.sqrt((self.pos_x - radar_x) ** 2 + (self.pos_y - radar_y) ** 2 + (self.pos_z - radar_z) ** 2)
        phi = math.degrees(math.atan2(self.pos_y - radar_y, self.pos_x - radar_x))
        if phi < 0:
            phi += 360
        thetta = math.degrees(math.atan2(self.pos_z - radar_z, math.sqrt((self.pos_x - radar_x) ** 2 + (self.pos_y - radar_y) ** 2)))
        if thetta < 0:
            thetta += 180
            
        print(f'Object: r={r:.2f}m, phi={phi:.2f}°, thetta={thetta:.2f}°')

class RadarSystem:
    def __init__(self, radar_x, radar_y, radar_z, num_objects):
        self.radar = Radar(radar_x, radar_y, radar_z)
        self.objects = []
        for _ in range(num_objects):
            pos_x, pos_y, pos_z, speed_proj_x, speed_proj_y, speed_proj_z = self.get_object_data()
            self.objects.append(FlyingObject(pos_x, pos_y, pos_z, speed_proj_x, speed_proj_y, speed_proj_z))

    def get_object_data(self):
        pos_x = float(input('Enter object x-coordinate (m): '))
        pos_y = float(input('Enter object y-coordinate (m): '))
        pos_z = float(input('Enter object z-coordinate (m): '))
        speed_proj_x = float(input('Enter object x-speed projection (m/s): '))
        speed_proj_y = float(input('Enter object y-speed projection (m/s): '))
        speed_proj_z = float(input('Enter object z-speed projection (m/s): '))
        return pos_x, pos_y, pos_z, speed_proj_x, speed_proj_y, speed_proj_z

    def run(self):
        self.radar.get_spherical_coords(self.objects)
        time = float(input('\nEnter time (s) to display new spherical coordinates: '))
        self.radar.get_spherical_coords_after_time(self.objects, time)

if __name__ == '__main__':
    # Задаем координаты радара 
    radar_x = 10.0
    radar_y = 20.0
    radar_z = 30.0
    num_objects = int(input('Enter number of flying objects: '))
    radar_system = RadarSystem(radar_x, radar_y, radar_z, num_objects)
    radar_system.run()