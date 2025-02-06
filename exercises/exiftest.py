from exif import Image

with open('IMG_20250205_174349.jpg', 'rb') as image_file:
    my_image = Image(image_file)
    print(f"Longitude: {my_image.gps_longitude} Ref: {my_image.gps_longitude_ref}")
    print(f"Latitude: {my_image.gps_latitude} Ref: {my_image.gps_latitude_ref}")

# longitude_final = f"{my_image.gps_longitude[0]} + {my_image.gps_longitude[1] / 60} + {round(my_image.gps_longitude[2] / 3600, 5)}"
longitude_test = str(my_image.gps_longitude[0] + my_image.gps_longitude[1] / 60 + round(my_image.gps_longitude[2] / 3600, 5)).replace(".", "")

longitude_list_mode = []

for i in longitude_test:
    longitude_list_mode.append(int(i))

print(longitude_list_mode)

# Minutes
minutes = [0, longitude_list_mode[2],longitude_list_mode[3], longitude_list_mode[4], longitude_list_mode[5]]
sub_minutes = int(("".join(str(i) for i in minutes)))*60
ml = []
for i in str(sub_minutes):
    ml.append(int(i))

ml_calc = [ml[2], ml[3], ml[4]]
ml_lp = int(("".join(str(i) for i in ml_calc))) * 60
ml_fm = str(ml_lp).replace('0', '')

# Degrees
longitude_calc = f"""{longitude_list_mode[0]}{longitude_list_mode[1]}º{ml[0]}{ml[1]}'{ml_fm[:2] + "." + ml_fm[2:]}"{my_image.gps_longitude_ref}"""
print(longitude_calc)
# print(minutes)
# print(sub_minutes)
# print(ml)
# print(ml_lp)
# print(longitude_final)
# print(longitude_test)
# print(len(longitude_test))

# 43 degrees / 24.906(0.4151/60) / 24 minutes / 906 remainder(*60) / 54.36 seconds = 43º24'54.36" W

latitude_test = my_image.gps_latitude[0] + (my_image.gps_latitude[1] / 60) + (my_image.gps_latitude[2] / 3600)

# print(my_image.gps_latitude[0], my_image.gps_latitude[1], my_image.gps_latitude[2]) # Test

latitude_test_str = str(latitude_test)

latitude_list_mode = [int(i) for i in latitude_test_str if i.isdigit()]

# for i in latitude_test:
#     latitude_list_mode.append(int(i))
print(latitude_test)
print(latitude_test_str)
print(latitude_list_mode)

# Minutes
# minutes = [0,  latitude_list_mode[2],latitude_list_mode[3], latitude_list_mode[4], latitude_list_mode[5]]
# sub_minutes = int(("".join(str(i) for i in minutes)))*60

# minutes = int((latitude_test - int(latitude_test)) * 60)
# seconds = round(((latitude_test - int(latitude_test)) * 60 - minutes) * 60, 4)
#
# # ml = []
# # for i in str(sub_minutes):
# #     ml.append(int(i))
#
# print(minutes)
# print(sub_minutes)
# print(f" {ml} minutes ")
#
#
#
#
# ml_calc = [ml[2], ml[3], ml[4]]
# ml_lp = int(("".join(str(i) for i in ml_calc))) * 60
# ml_fm = str(ml_lp)
# print(ml_lp)
# print(ml_lp)



# if minutes >= 60:
#     degrees += minutes // 60
#     minutes = minutes % 60

# if int(ml_lp) >= 60:
#     extra_degrees = int(ml_lp) // 60
#     ml_lp = str(int(ml_lp) % 60)
#     latitude_list_mode[0] += extra_degrees


decimal_part = latitude_test - int(latitude_test)  # Parte decimal da latitude
degrees = int(latitude_test)  # Graus inteiros
minutes = int(decimal_part * 60)  # Converte a parte decimal para minutos
seconds = round((decimal_part * 60 - minutes) * 60, 4)  # Converte a parte decimal dos minutos para segundos

print(f"Minutos: {minutes}, Segundos: {seconds}")  # Imprime os minutos e segundos calculados

# Degrees
# latitude_calc = f"""{latitude_list_mode[0]}{latitude_list_mode[1]}º{ml[0]}{ml[1]}'{ml_fm[:2] + "." + ml_fm[2:]}"{my_image.gps_latitude_ref}"""
latitude_calc2 = f"{latitude_list_mode[0]}{latitude_list_mode[1]}º{minutes}´{seconds}\"{my_image.gps_latitude_ref}"
# print(latitude_calc)
print(latitude_calc2)