

def time_to_go(departure_time, travel_time, CHECK_TIME = 180):
    # CHECK_TIME = 180 # 3 hours in minutes
    dep_time_min = (int(departure_time.split(':')[0]) * 60) + int(departure_time.split(':')[1]) # ['12', '30']
    travel_time = int(travel_time.split(':')[0]) * 60 + int(travel_time.split(':')[1]) # ['2', '30']
    go_time = str((dep_time_min - travel_time - CHECK_TIME) // 60) + ":" + str((dep_time_min - travel_time - CHECK_TIME) % 60)
    return go_time
    

# input travel_time
# input departure_time
# return time_to_go
dep_time = input("Enter the departure time[HH:MM]: ") #12:30 = 12*60+30
tr_time = input("Enter the travel time[HH:MM]: ")

# TODO: Проверка ввода времени while

print(f"Time to go: {time_to_go(dep_time, tr_time)}")