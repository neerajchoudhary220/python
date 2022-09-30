world_cities_file = open('world_cities.txt',encoding="utf8")
world_cities_array = open('worldCities.sql','a',encoding="utf8")

cities = world_cities_file.readlines()
sql_script = 'insert into `cities` (`city`,`city_ascii`,`lat`,`lng`,`country`,`iso2`,`iso3`,`admin_name`,`capital`,`population`,`country_id`) VALUES\n'
world_cities_array.write(sql_script)

for line in cities:
    city = line.strip()
    world_cities_array.write("("+city+"),\n")

world_cities_array.write(";")
world_cities_array.close()
world_cities_file.close()
print('done')