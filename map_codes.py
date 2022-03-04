from pygal_maps_world import i18n
import json
filename = 'json_files/population_data.json'

# for country_code, country in sorted(i18n.COUNTRIES.items()):
#     print(country_code, country)

with open(filename) as f:
    custome = json.load(f)
names = []
for dict in custome:
    if dict['Year'] == '2010':
        country_name = dict['Country Name']
        names.append(country_name)
def get_country_code(country_name):
    for code, name in i18n.COUNTRIES.items():
        if country_name == name:
            return code
        if country_name == 'Vietnam':
            return 'vn'
        elif country_name == 'Korea, Rep.':
            return 'kr'
        elif country_name == 'Yemen, Rep.':
            return 'ye'
        elif country_name == 'Hong Kong SAR, China':
            return 'hk'
        elif country_name == 'Congo, Rep.':
            return 'cg'
        elif country_name == 'Egypt, Arab Rep.':
            return 'eg'
    return None

# for name in names:
#     new_code = get_country_code(name)
#     if new_code == None:
#         print(name)

# print(get_country_code('Andorra'))
# print(get_country_code('United Arab Emirates'))
# print(get_country_code('Afghanistan'))  