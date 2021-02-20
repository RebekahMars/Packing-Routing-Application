#Rebekah Mars WGU Student ID 001247660
#Purpose: This file will read the PackageDetailsCSV file and incorporate the sorting functions written in the file to
#place each package in its appropriate truck. The truck will then compare addresses and distances from the PackageDistance.py
#in order to determine the order in which the packages will be delivered.
import operator
import datetime
import PackageDistances
import PackageDetailsCSV
import copy

#List of packages on each truck is created
truck_1_delivery = []
truck_2_delivery = []
truck_3_delivery = []

#List of truck details is created to deepycopy to, so original list is not altered
truck_1_hash_table = []
truck_2_hash_table = []
truck_3_hash_table = []

#List of truck distance index is created
truck_1_address_index = []
truck_2_address_index = []
truck_3_address_index = []

#List of truck distance is created
truck_1_miles = 0
truck_2_miles = 0
truck_3_miles = 0
trucks_total_distance = 0

#List of each truck's leave times
truck_1_leave_time = ['8:00:00']
truck_2_leave_time = ['9:05:00'] 
truck_3_leave_time = ['10:10:00']

#List of each truck's delivery time, each index will store the delivery time of each package in order it was delivered
truck_1_package_delivery_times = []
truck_2_package_delivery_times = []
truck_3_package_delivery_times = []

#This function parses first through the truck 1 details in the PackageDetailsCSV file to append the truck_1_leave_time list.
#A copy of the Truck 1 details from the PackageDetailsCSV file is copied to the truck_1_hash_table list
#truck_1_delivery, which is the list of all packages and their information from Truck 1, has data inserted from the truck_1_hash_table
#truck_1_delivery is then iterated through, along with the package address details of each package from the PackageDistances file
#if the value at index 1 of truck_1_delivery is equal to the address at index 2 of the address log
#The index of the address is added to the truck_1_address index list, and the truck_1_delivery list has the address index also added
#This function is prep for calling the greedy algorithm function from PackageDistances file, as it is receiving the address index information
def prep_truck_1_delivery():
    for index, value in enumerate(PackageDetailsCSV.get_truck_1()): 
        PackageDetailsCSV.get_truck_1()[index][8] = truck_1_leave_time[0]
        truck_1_hash_table = copy.deepcopy(PackageDetailsCSV.truck_1)
        truck_1_delivery.append(truck_1_hash_table[index])

    for index, value in enumerate(truck_1_delivery):
        for address in PackageDistances.get_package_address():
            if value[1] == address[2]:
                truck_1_address_index.append(address[0]) 
                truck_1_delivery[index][1] = address[0]

#Call the prep_truck_1_delivery function
prep_truck_1_delivery()
#Call the greedy algorithm to sort the packages on Truck 1 in the PackageDistances file
PackageDistances.calculate_shortest_distance(truck_1_delivery, 1, 0)

#This function parses first through the truck 2 details in the PackageDetailsCSV file to append the truck_2_leave_time list.
#A copy of the Truck 2 details from the PackageDetailsCSV file is copied to the truck_2_hash_table list
#truck_2_delivery, which is the list of all packages and their information from Truck 2, has data inserted from the truck_2_hash_table
#truck_2_delivery is then iterated through, along with the package address details of each package from the PackageDistances file
#if the value at index 1 of truck_2_delivery is equal to the address at index 2 of the address log
#The index of the address is added to the truck_2_address index list, and the truck_2_delivery list has the address index also added
#This function is prep for calling the greedy algorithm function from PackageDistances file, as it is receiving the address index information
def prep_truck_2_delivery():
    for index, value in enumerate(PackageDetailsCSV.get_truck_2()): 
        PackageDetailsCSV.get_truck_2()[index][8] = truck_2_leave_time[0]
        truck_2_hash_table = copy.deepcopy(PackageDetailsCSV.truck_2)
        truck_2_delivery.append(truck_2_hash_table[index])

    for index, value in enumerate(truck_2_delivery):
        for address in PackageDistances.get_package_address():
            if value[1] == address[2]:
                truck_2_address_index.append(address[0]) 
                truck_2_delivery[index][1] = address[0]

#Call the prep_truck_2_delivery function
prep_truck_2_delivery()
#Call the greedy algorithm to sort the packages on Truck 2 in the PackageDistances file
PackageDistances.calculate_shortest_distance(truck_2_delivery, 2, 0)

#This function parses first through the truck 3 details in the PackageDetailsCSV file to append the truck_3_leave_time list.
#A copy of the Truck 3 details from the PackageDetailsCSV file is copied to the truck_3_hash_table list
#truck_3_delivery, which is the list of all packages and their information from Truck 3, has data inserted from the truck_3_hash_table
#truck_3_delivery is then iterated through, along with the package address details of each package from the PackageDistances file
#if the value at index 1 of truck_3_delivery is equal to the address at index 3 of the address log
#The index of the address is added to the truck_3_address index list, and the truck_3_delivery list has the address index also added
#This function is prep for calling the greedy algorithm function from PackageDistances file, as it is receiving the address index information
def prep_truck_3_delivery():
    for index, value in enumerate(PackageDetailsCSV.get_truck_3()): 
        PackageDetailsCSV.get_truck_3()[index][8] = truck_3_leave_time[0]
        truck_3_hash_table = copy.deepcopy(PackageDetailsCSV.truck_3)
        truck_3_delivery.append(truck_3_hash_table[index])

    for index, value in enumerate(truck_3_delivery):
        for address in PackageDistances.get_package_address():
            if value[1] == address[2]:
                truck_3_address_index.append(address[0]) 
                truck_3_delivery[index][1] = address[0]

#Call the prep_truck_3_delivery function
prep_truck_3_delivery()
#Call the greedy algorithm to sort the packages on Truck 3 in the PackageDistances file
PackageDistances.calculate_shortest_distance(truck_3_delivery, 3, 0)

#This function calculates the truck_1_delivery time, by indexing through the truck_1_distances stored from 
#the greedy algorithm and adding the values together. The values are rounded to the 10th.
#The total distance for Truck 1 is then returned as a value.
def calculate_truck_1_delivery_time():
    truck_1_total_distance = 0
    for index in PackageDistances.truck_1_distance:
        truck_1_total_distance += index
        truck_1_total_distance = round(truck_1_total_distance, 2)
    return truck_1_total_distance

#This function calculates the truck_2_delivery time, by indexing through the truck_2_distances stored from 
#the greedy algorithm and adding the values together. The values are rounded to the 10th.
#The total distance for Truck 2 is then returned as a value.
def calculate_truck_2_delivery_time():
    truck_2_total_distance = 0
    for index in PackageDistances.truck_2_distance:
        truck_2_total_distance += index
        truck_2_total_distance = round(truck_2_total_distance, 2)
    return truck_2_total_distance

#This function calculates the truck_3_delivery time, by indexing through the truck_3_distances stored from 
#the greedy algorithm and adding the values together. The values are rounded to the 10th.
#The total distance for Truck 3 is then returned as a value.
def calculate_truck_3_delivery_time():
    truck_3_total_distance = 0
    for index in PackageDistances.truck_3_distance:
        truck_3_total_distance += index
        truck_3_total_distance = round(truck_3_total_distance, 2)
    return truck_3_total_distance

#The total distance is calculated for all three trucks by calling the functions to calculate the delivery times
#for Trucks 1, 2, and 3 and then adding them all together. The value is then rounded to the 10th and returned as 
#the total distance traveled in miles for all three trucks. 
def calculate_trucks_total_distance():
    truck_1_miles = calculate_truck_1_delivery_time()
    truck_2_miles = calculate_truck_2_delivery_time()
    truck_3_miles = calculate_truck_3_delivery_time()
    trucks_total_distance = round(truck_1_miles + truck_2_miles + truck_3_miles, 2)
    return trucks_total_distance

#Function to calculate the total distance of all three trucks is called and set to trucks_total_distance
trucks_total_distance = calculate_trucks_total_distance()

#This function determines the delivery time of each package on Truck 1
#The function first divides the time from the truck_1_package_miles list by 18, as the truck only goes 18 miles per hour
#The function then multiplies by 60 to get the number of minutes it takes to deliver the package. The time is then converted to
#the 24 hour clock and added to the truck_1_leave_time list.
#Then truck_1_leave time is indexed through to convert the time calculated to the H:M:S format by taking each value calculated and totaling it (adding to the truck_1_leave time)
#That value is then added to the truck_1_package_delivery_time list.
#The PackageDistances.truck_1_packages list is then indexed through, and the delivery time added to the list.
#The PackageDetails.get_truck_1() which contains truck 1 package information is then updated to that calculated value
def determine_truck_1_package_delivery_times():
    total = datetime.timedelta()

    for index, value in enumerate (PackageDistances.truck_1_package_miles()):
        time = int(value) / 18
        clock = '{0:02.0f}:{1:02.0f}'.format(*divmod(time * 60, 60)) + ':00'
        truck_1_leave_time.append(clock)

    for index in truck_1_leave_time:
        (h, m, s) = index.split(':')
        minutes = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        total += minutes      
        truck_1_package_delivery_times.append(str(total))

    for index, value in enumerate(PackageDistances.truck_1_packages):
        PackageDistances.truck_1_packages[index][9] = truck_1_package_delivery_times[index +1]

    for index, value in enumerate(PackageDetailsCSV.get_truck_1()):
        for element in PackageDistances.truck_1_packages:
            if value[0] == element[0]:
                PackageDetailsCSV.get_truck_1()[index][9] = element[9]

#Calls the function to determine the delivery time of each package on Truck 1
determine_truck_1_package_delivery_times()

#The HashMap is now updated with the start time and leave time of each package by updating it with the packing information in the PackageDetailsCSV file for Truck 1.
#The HashMap is iterated through and updated at that index containing the matching package ID (index 0)
#This was updated using the previous function.
def update_hash_table_truck_1():
    for index, value in enumerate(PackageDetailsCSV.get_truck_1()):
        PackageDetailsCSV.get_hash_table().update(int(PackageDistances.truck_1_package_list()[index][0]), PackageDetailsCSV.get_truck_1())

#Calls the update_hash_table function for Truck 1
update_hash_table_truck_1()

#This function determines the delivery time of each package on Truck 2
#The function first divides the time from the truck_2_package_miles list by 18, as the truck only goes 18 miles per hour
#The function then multiplies by 60 to get the number of minutes it takes to deliver the package. The time is then converted to
#the 24 hour clock and added to the truck_2_leave_time list.
#Then truck_2_leave time is indexed through to convert the time calculated to the H:M:S format by taking each value calculated and totaling it (adding to the truck_2_leave time)
#That value is then added to the truck_2_package_delivery_time list.
#The PackageDistances.truck_2_packages list is then indexed through, and the delivery time added to the list.
#The PackageDetails.get_truck_2() which contains truck 2 package information is then updated to that calculated value
def determine_truck_2_package_delivery_times():
    total = datetime.timedelta()

    for index, value in enumerate (PackageDistances.truck_2_package_miles()):
        time = int(value) / 18
        clock = '{0:02.0f}:{1:02.0f}'.format(*divmod(time * 60, 60)) + ':00'
        truck_2_leave_time.append(clock)

    for index in truck_2_leave_time:
        (h, m, s) = index.split(':')
        minutes = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        total += minutes
        truck_2_package_delivery_times.append(str(total))

    for index, value in enumerate(PackageDistances.truck_2_packages):
        PackageDistances.truck_2_packages[index][9] = truck_2_package_delivery_times[index +1]

    for index, value in enumerate(PackageDetailsCSV.get_truck_2()):
        for element in PackageDistances.truck_2_packages:
            if value[0] == element[0]:
                PackageDetailsCSV.get_truck_2()[index][9] = element[9]

#Calls the function to determine the delivery time of each package on Truck 2
determine_truck_2_package_delivery_times()

#The HashMap is now updated with the start time and leave time of each package by updating it with the packing information in the PackageDetailsCSV file for Truck 2.
#The HashMap is iterated through and updated at that index containing the matching package ID (index 0)
#This was updated using the previous function.
def update_hash_table_truck_2():
    for index, value in enumerate(PackageDetailsCSV.get_truck_2()):
        PackageDetailsCSV.get_hash_table().update(int(PackageDistances.truck_2_package_list()[index][0]), PackageDetailsCSV.get_truck_2())

#Calls the update_hash_table function for Truck 2
update_hash_table_truck_2()

#This function determines the delivery time of each package on Truck 3
#The function first divides the time from the truck_3_package_miles list by 18, as the truck only goes 18 miles per hour
#The function then multiplies by 60 to get the number of minutes it takes to deliver the package. The time is then converted to
#the 24 hour clock and added to the truck_3_leave_time list.
#Then truck_3_leave time is indexed through to convert the time calculated to the H:M:S format by taking each value calculated and totaling it (adding to the truck_3_leave time)
#That value is then added to the truck_3_package_delivery_time list.
#The PackageDistances.truck_3_packages list is then indexed through, and the delivery time added to the list.
#The PackageDetails.get_truck_23) which contains truck 3 package information is then updated to that calculated value
def determine_truck_3_package_delivery_times():
    total = datetime.timedelta()

    for index, value in enumerate (PackageDistances.truck_3_package_miles()):
        time = int(value) / 18
        clock = '{0:02.0f}:{1:02.0f}'.format(*divmod(time * 60, 60)) + ':00'
        truck_3_leave_time.append(clock)


    for index in truck_3_leave_time:
        (h, m, s) = index.split(':')
        minutes = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        total += minutes
        truck_3_package_delivery_times.append(str(total))

    for index, value in enumerate(PackageDistances.truck_3_packages):
        PackageDistances.truck_3_packages[index][9] = truck_3_package_delivery_times[index+1]

    for index, value in enumerate(PackageDetailsCSV.get_truck_3()):
        for element in PackageDistances.truck_3_packages:
            if value[0] == element[0]:
                PackageDetailsCSV.get_truck_3()[index][9] = element[9]

#Calls the function to determine the delivery time of each package on Truck 3
determine_truck_3_package_delivery_times()

#The HashMap is now updated with the start time and leave time of each package by updating it with the packing information in the PackageDetailsCSV file for Truck 3.
#The HashMap is iterated through and updated at that index containing the matching package ID (index 0)
#This was updated using the previous function.
def update_hash_table_truck_3():
    for index, value in enumerate(PackageDetailsCSV.get_truck_3()):
        PackageDetailsCSV.get_hash_table().update(int(PackageDistances.truck_3_package_list()[index][0]), PackageDetailsCSV.truck_3[0])

#Calls the update_hash_table function for Truck 3
update_hash_table_truck_3()


