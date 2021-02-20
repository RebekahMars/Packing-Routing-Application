#Rebekah Mars WGU Student ID 001247660
#Purpose: The purpose of this file is to create the Hash Table class in order to store the WGUPS Package File data

class HashMap:
    #This function initializes the HashMap, sets the capacity of the HashMap to 50 and its contents to 'None'
    def __init__(self, capacity = 50):
        self.table = [None] * capacity

    #This function is the hashing function of the HashMap. Use this function to retrieve values in the HashMap
    def get_hash(self, key):
        length = len(self.table)

        return int(key) % length

    #This function inserts a value into the HashMap at an index within the HashMap. If the HashMap is empty, the value is appended at that index as a list.
    #If not empty, then the existing value gets replaced.
    def insert(self, key, value):
        index = self.get_hash(key)
        key_value = [key, value]

        if self.table[index] is None:
            self.table[index] = list([value])
            return True
        else:
            for pair in self.table[index]:
                if pair[0] == key:
                    pair[1]= value
                    return True
        self.table[index].append(key_value)
        return True
    
    #This function allows the HashMap to get the information mapped to an index of desired key
    def get(self, key):
        index = self.get_hash(key)
        if self.table[index] is not None:
            for pair in self.table[index]:
                if pair[0] == key:
                    return pair
        return None

    #This function allows the HashMap to update a value within the HashMap. The HashMap is searched for a specific key. When found, that value is updated with a new value and returned.
    #If an error occurs (no value exists), an error message is printing
    def update(self, key, value):
        index = self.get_hash(key)
        if self.table[index] is not None:
            for pair in self.table[index]:
                if pair[0] == key:
                    pair[1] = value
                    print(pair[1])
                    return True
        else:
            print('ERROR WITH UPDATING ' + key)

    #This functions allows the HashMap to delete a value within the HashMap. The HashMap is searched for a key, then that value at that index is removed.
    def delete(self, key):
        index = self.get_hash(key)
        if self.table[index] is None:
            return False
        for i in range (0, len(self.table[index])):
            if self.table[index][i][0] == key:
                self.table[index].pop(i)
                return True

    #This function allows the HashMap to print a copy of itself to the user if called. If the HashMap is not empty at that index, it will print information stored at that index.
    def print(self):
        for object in self.table:
            if object is not None:
                print(str(object))

#Creates the HashTableEntry class, containing a key and an item
class HashTableEntry:
    def _init_(self, key, item):
        self.key = key
        self.item = item

