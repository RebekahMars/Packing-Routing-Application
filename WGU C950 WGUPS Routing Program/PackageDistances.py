#Rebekah Mars WGU Student ID 001247660
#Purpose: The purpose of this file is to import the package distance data provided for the project and use the distances
#to calculate the best routing for all three trucks, depicting the algorithm I used and how it sorts packages/calculates
#the best routing for each package.

import csv
import datetime
import PackageDetailsCSV

#List for truck packages
truck_1_packages = []
truck_2_packages = []
truck_3_packages = []

#List for truck package index list
truck_1_index_list = []
truck_2_index_list = []
truck_3_index_list = []

#List for truck distances
truck_1_distance = []
truck_2_distance = []
truck_3_distance = []

#Opens the WGUDistanceDetails and imports CSV file into a list
with open('WGUDistanceDetails.csv') as csvfile:
    distance_list = list(csv.reader(csvfile, delimiter = ','))
#Opens the WGUPackageAddresses and imports CSV file into a list
with open('WGUPackageAddresses.csv') as csvfile_1:
    address_list = list(csv.reader(csvfile_1, delimiter = ','))


#This function reads the distance data imported from the WGUDistanceDetails CSV file and calculates package distance
#If distance is blank, it looks at the column and row value instead. 
def calculate_package_distance(row, column):
     package_distance = distance_list[row][column]
     if package_distance == '':
         package_distance = distance_list[column][row]
     return float(package_distance)

#Greedy algorithm for sorting the packages into the trucks. 
def calculate_shortest_distance(package_distance_list, truck_num, current_location):
    if len(package_distance_list) == 0: #base case. If I reach the end of my package list, returns the list
        return package_distance_list
   
    else:
        location = 0 #location set to 0
        smallest_index = 25.0 #set smallest index value to some random float value
        for index in package_distance_list: #iterate through index in package list for truck
            num = (calculate_package_distance(current_location, int(index[1]))) #call package distance function at index 1 of list (index 1 should contain column number of package from CSV file)
            if num <= smallest_index: #if the package distance calculated is smaller than or equal to the smallest_index value
                smallest_index = num #set my smallest_index to be the package distance calculated
                location = int(index[1])  #location is set to column of package (which should be located at index 1 of list)                 

        for index in package_distance_list: #iterate through index in package list for truck
            num = calculate_package_distance(current_location, int(index[1])) #package distance function is called at index 1 of list (index 1 should contain column number of package from CSV file)
            if num == smallest_index: #if it is actually the smallest index, go here next!
                if truck_num == 1: #if the truck number is 1
                    truck_1_packages.append(index) #puts package info on truck 1 package list
                    truck_1_index_list.append(index[1]) #puts package index in a list
                    truck_1_distance.append(num) #takes the package distance calculated and adds it to the truck_1_distance list
                    package_distance_list.pop(package_distance_list.index(index)) #removes value from list so we don't go to the same location twice
                    current_location = location #sets current location 
                    calculate_shortest_distance(package_distance_list, 1, current_location) #recurisve function
                if truck_num == 2: #if the truck number is 2
                    truck_2_packages.append(index) #puts package info on truck 2 package list
                    truck_2_index_list.append(index[1]) #puts package index in a list
                    truck_2_distance.append(num) #takes the package distance calculated and adds it to the truck_2_distance list
                    package_distance_list.pop(package_distance_list.index(index)) #removes value from list so we don't go to the same location twice
                    current_location = location #sets current location 
                    calculate_shortest_distance(package_distance_list, 2, current_location) #recurisve function
                if truck_num == 3: #if the truck number is 2
                    truck_3_packages.append(index)  #puts package info on truck 3 package list
                    truck_3_index_list.append(index[1]) #puts package index in a list
                    truck_3_distance.append(num) #takes the package distance calculated and adds it to the truck_3_distance list
                    package_distance_list.pop(package_distance_list.index(index)) #removes value from list so we don't go to the same location twice
                    current_location = location #sets current location 
                    calculate_shortest_distance(package_distance_list, 3, current_location) #recurisve function


#This puts the starting location of 0 (the WGU hub) for each truck
truck_1_index_list.insert(0, '0')
truck_2_index_list.insert(0, '0')
truck_3_index_list.insert(0, '0')


#Gets the Truck 1 packages
def truck_1_package_list():
    return truck_1_packages

#Gets the Truck 2 packages
def truck_2_package_list():
    return truck_2_packages

#Gets the Truck 3 packages
def truck_3_package_list():
    return truck_3_packages

#Gets the Truck 1 package index list
def truck_1_package_index_list():
    return truck_1_index_list

#Gets the Truck 2 package index list
def truck_2_package_index_list():
    return truck_2_index_list

#Gets the Truck 3 package index list
def truck_3_package_index_list():
    return truck_3_index_list

#Gets the Truck 1 miles
def truck_1_package_miles():
    return truck_1_distance

#Gets the Truck 2 miles
def truck_2_package_miles():
    return truck_2_distance

#Gets the Truck 3 miles
def truck_3_package_miles():
    return truck_3_distance

#Gets all addresses for all packages on Trucks 1, 2, and 3
def get_package_address():
    return address_list


