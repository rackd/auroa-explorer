import math

def haversine(lon1, lat1, lon2, lat2):
    earth_radius_miles = 3958.8

    lon1 = math.radians(lon1 - 180)
    lat1 = math.radians(lat1)
    lon2 = math.radians(lon2 - 180)
    lat2 = math.radians(lat2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = earth_radius_miles * c
    return distance

def largest_n_in_distance(data, in_lon, in_lat, dist_max):
    auroa_max = 0
    ai = None

    for x in data:
        lon = x[0]
        lat = x[1]
        auroa = x[2]

        dist = haversine(in_lon, in_lat, lat, lon)

        if(dist <= dist_max):
            if(auroa > auroa_max):
                auroa_max = auroa
                ai = x
        
    return ai

def normalize(data):
    for array in data:
        array[0] -= 180