import math

def create_vector(x, y, z):
    return {'x': x, 'y': y, 'z': z}

def vector_add(v1, v2):
    return create_vector(v1['x'] + v2['x'], v1['y'] + v2['y'], v1['z'] + v2['z'])

def vector_subtract(v1, v2):
    return create_vector(v1['x'] - v2['x'], v1['y'] - v2['y'], v1['z'] - v2['z'])

def vector_scale(v, scalar):
    return create_vector(v['x'] * scalar, v['y'] * scalar, v['z'] * scalar)

def calculate_distance(v1, v2):
    return math.sqrt((v1['x'] - v2['x'])**2 + (v1['y'] - v2['y'])**2 + (v1['z'] - v2['z'])**2)

def convert_to_spherical(v):
    radius = math.sqrt(v['x']**2 + v['y']**2 + v['z']**2)
    inclination = math.atan2(math.sqrt(v['x']**2 + v['y']**2), v['z'])  #Угол
    azimuth = math.atan2(v['y'], v['x'])  
    return radius, math.degrees(inclination), math.degrees(azimuth)

def calculate_relative_coordinates(radar_pos, object_pos):
    relative_pos = vector_subtract(object_pos, radar_pos)
    return convert_to_spherical(relative_pos)

def forecast_object_position(radar_pos, object_pos, object_vel, time):
    future_pos = vector_add(object_pos, vector_scale(object_vel, time))
    relative_pos = vector_subtract(future_pos, radar_pos)
    return convert_to_spherical(relative_pos)

def main():
    radar_pos = create_vector(0, 0, 0)  

    num_objects = int(input("Введите количество летающих объектов: "))
    objects = []

    for i in range(num_objects):
        x, y, z = map(float, input(f"Введите координаты объекта № {i + 1} (x y z): ").split())
        vx, vy, vz = map(float, input(f"Введите скорость объекта № {i + 1} (Vx Vy Vz): ").split())
        objects.append({'position': create_vector(x, y, z), 'velocity': create_vector(vx, vy, vz)})

    print("\nТекущие сферические координаты:")
    for i, obj in enumerate(objects):
        r, theta, phi = calculate_relative_coordinates(radar_pos, obj['position'])
        print(f"Объект № {i + 1}: R={r:.2f} m, θ = {theta:.2f}°, φ (azimuth) = {phi:.2f}°")

    time_interval = float(input("\nВведите время(в сек): "))
    print("\nСферические координаты через заданное время:")
    for i, obj in enumerate(objects):
        r, theta, phi = forecast_object_position(radar_pos, obj['position'], obj['velocity'], time_interval)
        print(f"Объект № {i + 1}: R={r:.2f} m, θ = {theta:.2f}°, φ (azimuth) = {phi:.2f}°")

if __name__ == "__main__":
    main()

