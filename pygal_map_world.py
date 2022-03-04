import json

from map_codes import get_country_code
import pygal
from pygal.style import LightColorizedStyle,  RotateStyle
filename = 'json_files/population_data.json'

with open(filename) as f:
    pop_data = json.load(f)

cc_populations = {}
years = [str(x) for x in range(1960, 2011)]

while True:
    year_choice = input("pick year between 1960 and 2010: \n")
    if year_choice in years:
        break
    else:
        print("Wrong input, try again\n")

for pop_dict in pop_data:
    if pop_dict['Year'] == year_choice:
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population
        else:
            None
cc_1, cc_2, cc_3 = {}, {}, {}
for codes, pop in cc_populations.items():
    if pop < 10000000:
        cc_1[codes] = pop
    elif pop < 1000000000:
        cc_2[codes] = pop
    else:
        cc_3[codes] = pop
print("{} countries have 0-10mil people. {} countries have 10mil-1bil people. {} countries have 1bil or more people.".format(len(cc_1), len(cc_2), len(cc_3)))  
wm_style = RotateStyle('#DC143C', base_style= LightColorizedStyle)
wm_style.background = '#FAEBD7' 
wm = pygal.maps.world.World(style = wm_style)
wm.title = "World population in {}, by country".format(year_choice)
wm.add('0-10 mil', cc_1)
wm.add('10mil - 1 billion', cc_2)
wm.add('>1 billion', cc_3)
wm.render_to_file("World.svg")