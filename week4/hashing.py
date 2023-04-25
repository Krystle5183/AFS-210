class HashTable:
    def __init__(self):
        self.size = 10
        self.slots = [None] * self.size
        self.data = [None] * self.size
        self.count = 0

    def hashFunction(self,key):
        return key % self.size

    def rehashFunction(self,key):
        return key // self.size
    
    def put(self,key,data):
        h = self.hashFunction(key)

        if self.slots[h] == None:
            self.data[h] = data
            self.slots[h] = key
        else:
            h = self.rehashFunction(key)
            if self.slots[h] == None:
                self.data[h] = data
                self.slots[h] = key
            else:
                print("collision")

    def get(self,key):
        h = self.hashFunction(key)
        data = None
        stop = False
        found = False
        place = h
        while self.slots[place] is not None and not found and not stop:
            if self.slots[place] == key:
                found = True
                data = self.data[place]
            else:
                place = self.rehashFunction(place)
                if place == h:
                    stop = True
        return data
            
     def __setitem__ (self,key,data):
        self.put(key,data)


H = HashTable()
H[69] = 'A'
H[66] = 'B'
H[80] = 'C'
H[35] = 'D'
H[18] = 'E'
H[52] = 'F'
H[89] = 'G'
H[70] = 'H'
H[12] = 'I'

print(H.slots)

print(H.data)

print(H.get(52))
