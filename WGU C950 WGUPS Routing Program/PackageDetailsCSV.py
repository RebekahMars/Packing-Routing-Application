#Rebekah Mars WGU Student ID 001247660
#Purpose of File: This file allows for the program to open the WGU Package Details Table provided with the project
#and import the data from the CSV file into a Hash Table using key/value pairings.
# Package 19 on truck 1??

import csv
from HashTable import HashMap

#Opens the WGUPackageDetails and imports CSV file into a list
with open('WGUPackageDetails.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')

    hashTableData = HashMap() #This creates the HashTable object using the HashTable class
    truck_1 = [] #list for Truck 1 contents
    truck_2 = [] #list for Truck 2 contents
    truck_3 = [] #list for Truck 3 contents 

    #reads CSV file for key/value pairs for Hash Table
    for row in readCSV: 
        package_row_ID = row[0] 
        package_address = row[1]
        package_city = row[2]
        package_state = row[3]
        package_zip_code = row[4]
        package_delivery_time = row[5]
        package_weight_in_kilos = row[6]
        package_special_note = row[7]
        package_start = ''
        package_end = ''
        package_status = 'At Hub'

        #iterates through CSV file and saves data into a Package Details list for each package
        package_details = [package_row_ID, package_address, package_city, package_state, package_zip_code, package_delivery_time, package_weight_in_kilos, package_special_note, package_start, package_end, package_status]

        #Fix the incorrect address for package 9, and adds to Truck 3 as address change is AFTER 10:20am
        if 'Wrong address listed' in package_details[7]:
            package_details[1] = '410 S State St'
            package_details[4] = '84111'
            truck_3.append(package_details)
        
        #If package has a delivery window of >10:30am and MUST BE delivered with another package and is NOT delayed, it will be on Truck 1
        if 'EOD' not in package_details[5] or '84115' in package_details[4]:
            if 'Must' in package_details[7] or 'None' in package_details[7]:
                truck_1.append(package_details)

            #If truck 2 or delayed on flight is in notes, package will be placed on truck 2  
        if 'truck 2' in package_details[7] or 'Delayed on fligh' in package_details[7]: 
            truck_2.append(package_details)

        if 'EOD' in package_details[6]:
            truck_3.append(package_details)

        #If package is not sorted into either Truck 1, 2, or 3. Package will be sorted based on whether Truck 2 or 3 is full
        if package_details not in truck_1 and package_details not in truck_2 and package_details not in truck_3:
            if len(truck_2) < len(truck_3):
                truck_2.append(package_details)
            else:
                truck_3.append(package_details)

        #Adds the sorted packages to the Hash Table
        hashTableData.insert(package_row_ID, package_details)
#Gets the Hash Table
def get_hash_table():
    return hashTableData

#Gets Truck 1 contents
def get_truck_1():
    return truck_1

#Gets Truck 2 Contents
def get_truck_2():
    return truck_2

#Gets Truck 3 Contents
def get_truck_3():
    return truck_3







        




