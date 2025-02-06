from exif import Image
import webbrowser

with open('IMG_20250205_174349.jpg', 'rb') as image_file:
    my_image = Image(image_file)
    print(f"Longitude: {my_image.gps_longitude} Ref: {my_image.gps_longitude_ref}")
    print(f"Latitude: {my_image.gps_latitude} Ref: {my_image.gps_latitude_ref}")

# My ugly way!

longitude_test = str(my_image.gps_longitude[0] + my_image.gps_longitude[1] / 60 + round(my_image.gps_longitude[2] / 3600, 5)).replace(".", "")

longitude_test_str = longitude_test

longitude_list_mode = [int(i) for i in longitude_test_str if i.isdigit()]

# Minutes
minutes = [0, longitude_list_mode[2],longitude_list_mode[3], longitude_list_mode[4], longitude_list_mode[5]]
sub_minutes = int(("".join(str(i) for i in minutes)))*60
ml = [int(i) for i in str(sub_minutes)]

ml_calc = [ml[2], ml[3], ml[4]]
ml_lp = int(("".join(str(i) for i in ml_calc))) * 60
ml_fm = str(ml_lp).replace('0', '')

if my_image.gps_longitude_ref == "W":
    longitude_calc = f"""-{longitude_list_mode[0]}{longitude_list_mode[1]}º{ml[0]}{ml[1]}'{ml_fm[:2] + "." + ml_fm[2:]}"{my_image.gps_longitude_ref}"""
else:
    longitude_calc = f"""{longitude_list_mode[0]}{longitude_list_mode[1]}º{ml[0]}{ml[1]}'{ml_fm[:2] + "." + ml_fm[2:]}"{my_image.gps_longitude_ref}"""

print(longitude_calc)

# 43 degrees / 24.906(0.4151/60) / 24 minutes / 906 remainder(*60) / 54.36 seconds = 43º24'54.36" W // Calc here!

# Smart way!

latitude_test = my_image.gps_latitude[0] + (my_image.gps_latitude[1] / 60) + (my_image.gps_latitude[2] / 3600)

latitude_test_str = str(latitude_test)

latitude_list_mode = [int(i) for i in latitude_test_str if i.isdigit()]

decimal_part = latitude_test - int(latitude_test)
degrees = int(latitude_test)
minutes = int(decimal_part * 60)
seconds = round((decimal_part * 60 - minutes) * 60, 4)

if my_image.gps_latitude_ref == "S":
    latitude_calc = f"-{latitude_list_mode[0]}{latitude_list_mode[1]}º{minutes}'{seconds}\"{my_image.gps_latitude_ref}"
else:
    latitude_calc = f"{latitude_list_mode[0]}{latitude_list_mode[1]}º{minutes}'{seconds}\"{my_image.gps_latitude_ref}"

print(latitude_calc)

url = f"https://www.google.com/maps/search/{latitude_calc.replace('-', '')} {longitude_calc.replace('-', '')}"
webbrowser.open_new(url)