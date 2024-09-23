import math

def create_vector(x, y, z):
    return {'x': x, 'y': y, 'z': z}

def add_vectors(v1, v2):
    return create_vector(v1['x'] + v2['x'], v1['y'] + v2['y'], v1['z'] + v2['z'])

def subtract_vectors(v1, v2):
    return create_vector(v1['x'] - v2['x'], v1['y'] - v2['y'], v1['z'] - v2['z'])

def multiply_vector(v, scalar):
    return create_vector(v['x'] * scalar, v['y'] * scalar, v['z'] * scalar)

def distance_between_vectors(v1, v2):
    return math.sqrt((v1['x'] - v2['x'])**2 + (v1['y'] - v2['y'])**2 + (v1['z'] - v2['z'])**2)

def to_spherical(v):
    r = math.sqrt(v['x']**2 + v['y']**2 + v['z']**2)
    theta = math.atan2(math.sqrt(v['x']**2 + v['y']**2), v['z'])  # угол места
    phi = math.atan2(v['y'], v['x'])  # азимут
    return r, math.degrees(theta), math.degrees(phi)

def get_object_coordinates(radar_position, object_position):
    relative_position = subtract_vectors(object_position, radar_position)
    return to_spherical(relative_position)

def predict_object_coordinates(radar_position, object_position, object_velocity, time):
    future_position = add_vectors(object_position, multiply_vector(object_velocity, time))
    relative_position = subtract_vectors(future_position, radar_position)
    return to_spherical(relative_position)

def main():
    radar_position = create_vector(0, 0, 0)  # координаты радара

    num_objects = int(input("Введите количество летающих объектов: "))
    flying_objects = []

    for i in range(num_objects):
        x, y, z = map(float, input(f"Введите координаты объекта {i + 1} (x y z): ").split())
        vx, vy, vz = map(float, input(f"Введите скорость объекта {i + 1} (vx vy vz): ").split())
        flying_objects.append({'position': create_vector(x, y, z), 'velocity': create_vector(vx, vy, vz)})

    print("\nТекущие сферические координаты объектов относительно радара:")
    for i, obj in enumerate(flying_objects):
        r, theta, phi = get_object_coordinates(radar_position, obj['position'])
        print(f"Объект {i + 1}: r={r:.2f} м, θ(угол)={theta:.2f}°, φ(азимут)={phi:.2f}°")

    time = float(input("\nВведите время в секундах: "))
    print("\nСферические координаты объектов относительно радара через это время:")
    for i, obj in enumerate(flying_objects):
        r, theta, phi = predict_object_coordinates(radar_position, obj['position'], obj['velocity'], time)
        print(f"Объект {i + 1}: r={r:.2f} м, θ(угол)={theta:.2f}°, φ(азимут)={phi:.2f}°")

if __name__ == "__main__":
    main()
