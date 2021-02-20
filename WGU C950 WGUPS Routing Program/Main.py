#Rebekah Mars WGU Student ID 001247660
#Purpose: The purpose of this file is to include a user menu and commands for the application to run, in which package information can be displayed at various
#times and successfully depict the WGUPS Routing Program.

import PackageDetailsCSV
import PackageDistances
import PackageRouting
import datetime

class Main:
    #User Interface
    print('**********************************************************************')
    print('* Welcome to the WGUPS Package Routing Application!                  *')
    print('*                                                                    *')
    print('* All 40 packages were delivered in ' "{0:.2f}".format(PackageRouting.trucks_total_distance), 'miles.                     *')
    print('**********************************************************************')

    #Main Menu function
    menu = {}
    menu['1'] = "Individual Package Status"
    menu['2'] = "Lookup All Packages at a Given Time"
    menu['3'] = "Exit Application"
    while True: #while the user has not selected exit
        menu_options = menu.keys()    
        for value in sorted(menu_options):
            print(value, menu[value])

        user_input = input('What would you like to do?: ') #receives user input for a main menu selection

        if user_input == '1': #individual package lookup
            try:
                package_num = input('Please enter the Package ID number (1-40) of the Package you would like to view.\n') #receives usr input for package number selection
                start_time = PackageDetailsCSV.hashTableData.get(str(package_num))[8] #gets the package start time
                delivered_time = PackageDetailsCSV.hashTableData.get(str(package_num))[9] #gets the package delivery time

                print('Please enter the time you would like to check the status of Package #', package_num, 'in the (H:M:S) format: \n')
                input_time = input('Time (0:00:00 format): ') #receives user input of a time point
                (h, m, s) = input_time.split(':')
                converted_input_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s)) #converts user entered time point into H:M:S format
                (h, m, s) = start_time.split(':')
                converted_start_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s)) #converts start time into H:M:S format
                (h, m, s) = delivered_time.split(':')
                converted_delivered_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s)) #converts delivered time into H:M:S format

                if(converted_input_time <= converted_start_time): #if the package has NOT left the Hub yet
                    PackageDetailsCSV.get_hash_table().get(str(package_num))[10] = 'At the Hub' #set package status 
                    print('******PACKAGE', package_num, 'DETAILS******')
                    print('Package', package_num, 'is located:',PackageDetailsCSV.get_hash_table().get(str(package_num))[10]) #package location
                    print('Package', package_num, 'leaves at:', start_time) #package start time
                    print('Package ID number:', PackageDetailsCSV.get_hash_table().get(str(package_num))[0]) #package ID number
                    print('Package Address:', PackageDetailsCSV.get_hash_table().get(str(package_num))[1],',',PackageDetailsCSV.get_hash_table().get(str(package_num))[2],',',PackageDetailsCSV.get_hash_table().get(str(package_num))[3],',', PackageDetailsCSV.get_hash_table().get(str(package_num))[4]) #package full address
                    print('Package Delivery Deadline:', PackageDetailsCSV.get_hash_table().get(str(package_num))[5]) #package delivery deadline
                    print('Package Weight:', PackageDetailsCSV.get_hash_table().get(str(package_num))[6], 'kilos') #package weight in kilos
                    print('Package Truck Status:', PackageDetailsCSV.get_hash_table().get(str(package_num))[10]) #status of the truck the package is assigned to
                    print('Expected Package Delivery Time:', PackageDetailsCSV.get_hash_table().get(str(package_num))[9]) #expected package delivery time

                if(converted_input_time > converted_start_time): #if the package has left the Hub

                    if(converted_input_time < converted_delivered_time): #if the package has NOT been delivered and is still in transit
                        PackageDetailsCSV.get_hash_table().get(str(package_num))[10] = 'En Route' #set package status 
                        print('******PACKAGE', package_num, 'DETAILS******')
                        print('Package', package_num, 'is located:',PackageDetailsCSV.get_hash_table().get(str(package_num))[10]) #package location
                        print('Package', package_num, 'left at:', start_time) #package start time
                        print('Package ID number:', PackageDetailsCSV.get_hash_table().get(str(package_num))[0]) #package ID number
                        print('Package Address:', PackageDetailsCSV.get_hash_table().get(str(package_num))[1],',',PackageDetailsCSV.get_hash_table().get(str(package_num))[2],',',PackageDetailsCSV.get_hash_table().get(str(package_num))[3],',', PackageDetailsCSV.get_hash_table().get(str(package_num))[4]) #package full address
                        print('Package Delivery Deadline:', PackageDetailsCSV.get_hash_table().get(str(package_num))[5]) #package delivery deadline
                        print('Package Weight:', PackageDetailsCSV.get_hash_table().get(str(package_num))[6], 'kilos') #package weight in kilos
                        print('Package Truck Status:', PackageDetailsCSV.get_hash_table().get(str(package_num))[10]) #status of the truck the package is assigned to
                        print('Expected Package Delivery Time:', PackageDetailsCSV.get_hash_table().get(str(package_num))[9]) #expected package delivery time

                    if(converted_input_time >= converted_delivered_time): #if the package has been delivered
                        PackageDetailsCSV.get_hash_table().get(str(package_num))[10] = 'Delivered' #set package status 
                        print('******PACKAGE', package_num, 'DETAILS******')
                        print('Package', package_num, 'is located:',PackageDetailsCSV.get_hash_table().get(str(package_num))[10]) #package location
                        print('Package', package_num, 'left at:', start_time) #package start time
                        print('Package ID number:', PackageDetailsCSV.get_hash_table().get(str(package_num))[0]) #package ID number
                        print('Package Address:', PackageDetailsCSV.get_hash_table().get(str(package_num))[1],',',PackageDetailsCSV.get_hash_table().get(str(package_num))[2],',',PackageDetailsCSV.get_hash_table().get(str(package_num))[3],',', PackageDetailsCSV.get_hash_table().get(str(package_num))[4]) #package full address
                        print('Package Delivery Deadline:', PackageDetailsCSV.get_hash_table().get(str(package_num))[5]) #package delivery deadline
                        print('Package Weight:', PackageDetailsCSV.get_hash_table().get(str(package_num))[6], 'kilos') #package weight in kilos
                        print('Package Truck Status:', PackageDetailsCSV.get_hash_table().get(str(package_num))[10]) #status of the truck the package is assigned to
                        print('Package Delivered at:', PackageDetailsCSV.get_hash_table().get(str(package_num))[9]) #expected package delivery time
            except:
                print('Invalid entry! Please try again.\n') #user has entered an innapropriate response
                continue

        elif user_input == '2': #all package information at a specific time point
            try:
                time_lookup = input('Please enter the time in the (H:M:S) format that you would like to lookup.\n') #receives user input of a time point
                (h, m, s) = time_lookup.split(':')
                converted_time_lookup = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s)) #converts user entered time point into H:M:S format
                for package_num in range(1,41):
                    start_lookup_time = PackageDetailsCSV.hashTableData.get(str(package_num))[8] #gets the package start time
                    delivered_lookup_time = PackageDetailsCSV.hashTableData.get(str(package_num))[9] #gets the package delivery time
                    (h, m, s) = start_lookup_time.split(':')
                    converted_start_lookup_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s)) #converts start time into H:M:S format
                    (h, m, s) = delivered_lookup_time.split(':')
                    converted_delivered_lookup_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s)) #converts deilivery time into H:M:S format

                    if(converted_time_lookup <= converted_start_lookup_time): #if package has NOT left the Hub yet
                       PackageDetailsCSV.get_hash_table().get(str(package_num))[10] = 'At the Hub' #set package status 
                       print('******PACKAGE', package_num, 'DETAILS******')
                       print('Package', package_num, 'is located:',PackageDetailsCSV.get_hash_table().get(str(package_num))[10]) #package location
                       print('Package', package_num, 'leaves at:', start_lookup_time) #package start time
                       print('Package ID number:', PackageDetailsCSV.get_hash_table().get(str(package_num))[0]) #package ID number
                       print('Package Address:', PackageDetailsCSV.get_hash_table().get(str(package_num))[1],',',PackageDetailsCSV.get_hash_table().get(str(package_num))[2],',',PackageDetailsCSV.get_hash_table().get(str(package_num))[3],',', PackageDetailsCSV.get_hash_table().get(str(package_num))[4]) #package full address
                       print('Package Delivery Deadline:', PackageDetailsCSV.get_hash_table().get(str(package_num))[5]) #package delivery deadline
                       print('Package Weight:', PackageDetailsCSV.get_hash_table().get(str(package_num))[6], 'kilos') #package weight in kilos
                       print('Package Truck Status:', PackageDetailsCSV.get_hash_table().get(str(package_num))[10]) #status of the truck the package is assigned to
                       print('Expected Package Delivery Time:', PackageDetailsCSV.get_hash_table().get(str(package_num))[9]) #expected package delivery time

                    if(converted_time_lookup > converted_start_lookup_time):
                        if(converted_time_lookup < converted_delivered_lookup_time):
                            PackageDetailsCSV.get_hash_table().get(str(package_num))[10] = 'En Route' #set package status
                            print('******PACKAGE', package_num, 'DETAILS******')
                            print('Package', package_num, 'is located:',PackageDetailsCSV.get_hash_table().get(str(package_num))[10]) #package location
                            print('Package', package_num, 'left at:', start_lookup_time) #package start time
                            print('Package ID number:', PackageDetailsCSV.get_hash_table().get(str(package_num))[0]) #package ID number
                            print('Package Address:', PackageDetailsCSV.get_hash_table().get(str(package_num))[1],',',PackageDetailsCSV.get_hash_table().get(str(package_num))[2],',',PackageDetailsCSV.get_hash_table().get(str(package_num))[3],',', PackageDetailsCSV.get_hash_table().get(str(package_num))[4]) #package full address
                            print('Package Delivery Deadline:', PackageDetailsCSV.get_hash_table().get(str(package_num))[5]) #package delivery deadline
                            print('Package Weight:', PackageDetailsCSV.get_hash_table().get(str(package_num))[6], 'kilos') #package weight in kilos
                            print('Package Truck Status:', PackageDetailsCSV.get_hash_table().get(str(package_num))[10]) #status of the truck the package is assigned to
                            print('Expected Package Delivery Time:', PackageDetailsCSV.get_hash_table().get(str(package_num))[9]) #expected package delivery time

                        if(converted_time_lookup >= converted_delivered_lookup_time):
                            PackageDetailsCSV.get_hash_table().get(str(package_num))[10] = 'Delivered' #set package status
                            print('******PACKAGE', package_num, 'DETAILS******')
                            print('Package', package_num, 'is located:',PackageDetailsCSV.get_hash_table().get(str(package_num))[10]) #package location
                            print('Package', package_num, 'left at:', start_lookup_time) #package start time
                            print('Package ID number:', PackageDetailsCSV.get_hash_table().get(str(package_num))[0]) #package ID number
                            print('Package Address:', PackageDetailsCSV.get_hash_table().get(str(package_num))[1],',',PackageDetailsCSV.get_hash_table().get(str(package_num))[2],',',PackageDetailsCSV.get_hash_table().get(str(package_num))[3],',', PackageDetailsCSV.get_hash_table().get(str(package_num))[4]) #package full address
                            print('Package Delivery Deadline:', PackageDetailsCSV.get_hash_table().get(str(package_num))[5]) #package delivery deadline
                            print('Package Weight:', PackageDetailsCSV.get_hash_table().get(str(package_num))[6], 'kilos') #package weight in kilos
                            print('Package Truck Status:', PackageDetailsCSV.get_hash_table().get(str(package_num))[10]) #status of the truck the package is assigned to
                            print('Package Delivered at:', PackageDetailsCSV.get_hash_table().get(str(package_num))[9]) #expected package delivery time
            except:
                print('Invalid entry! Please try again.\n') #if the user enters an inappropriate value
                continue
        elif user_input == '3': #user selects to exit
            print('You have chosen to exit the application.\n')
            break
        else:
            print('Invalid entry! Please try again.\n') #if the user does not select a valid menu option (1-3)
            continue
            






