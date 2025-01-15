from parser import FileParser
from parser import StringParser
import core_math
import topology
import gui
import tkinter as tk
import json
import file_utils
import download

with open('data/ovation_aurora_latest.json', 'r') as file:
	current_parser = FileParser(file)
data = current_parser.Coordinates
core_math.normalize(data)

with open('data/land-110m.json', 'r') as f:
    topo = json.load(f)

def blend_with_black(r, g, b, alpha):
    blended_r = int((1 - alpha) * 0 + alpha * r)
    blended_g = int((1 - alpha) * 0 + alpha * g)
    blended_b = int((1 - alpha) * 0 + alpha * b)
    return blended_r, blended_g, blended_b

def prob_to_color(p):
    alpha = p / 100

    if p < 50:
        r = int((255 * p) / 50)
        g = 255
        b = 0
    else:
        r = 255
        g = int(255 * (100 - p) / 50)
        b = 0

    r, g, b = blend_with_black(r, g, b, alpha)

    hex_color = "#{:02x}{:02x}{:02x}".format(r, g, b)
    return hex_color


def project(data, width, height, canvas):
    for longitude, latitude, prob in data:
        x = (longitude + 180) * (width / 360)
        y = (90 - latitude) * (height / 180)

        if(prob > 0):
            canvas.create_rectangle(x, y, x+5, y+5, outline=prob_to_color(prob), fill=prob_to_color(prob))

width, height = 1000,1000

file_utils.get_filenames_in_dir("data")

data2 = download.sat_data_download()
tparser = StringParser(data2)
print(tparser.ObservationTime)

g = gui.Gui('gui', width, height, 'black')
project(data, width, height, g.canvas)
topology.draw_map(topo, g.canvas, 1000, 1000)
g.run()
