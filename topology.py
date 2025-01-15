import json
from tkinter import Tk, Canvas

def decode_arc(arc, transform):
    scale = transform["scale"]
    translate = transform["translate"]
    x, y = 0, 0
    coordinates = []
    breaks = []
    last_lon, last_lat = None, None
    
    for dx, dy in arc:
        x += dx
        y += dy
        lon = (x * scale[0] + translate[0])
        lat = (y * scale[1] + translate[1])

        if last_lon is not None and abs(lon - last_lon) > 180:
            breaks.append(len(coordinates))
        elif last_lat is not None and abs(lat - last_lat) > 90:
            breaks.append(len(coordinates))
        
        last_lon, last_lat = lon, lat

        coordinates.append([lon, lat])
    return coordinates, breaks

def draw_map(topo, canvas, width, height):
    arcs = topo["arcs"]
    transform = topo["transform"]
    geometries = topo["objects"]["land"]["geometries"]

    for geometry in geometries:
        for arc_group in geometry["arcs"]:
            for arc_list in arc_group:
                for arc_index in arc_list:
                    arc_data = arcs[abs(arc_index)]
                    arc_coordinates, breaks = decode_arc(arc_data, transform)

                    segments = []
                    last_break = 0
                    for b in breaks:
                        segments.append(arc_coordinates[last_break:b])
                        last_break = b
                    segments.append(arc_coordinates[last_break:])

                    for segment in segments:
                        coords_scaled = []
                        for lon, lat in segment:
                            x = (lon + 180) * (width / 360)
                            y = (90 - lat) * (height / 180)
                            coords_scaled.extend([x, y])

                        canvas.create_polygon(coords_scaled, fill='', outline='blue')