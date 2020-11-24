class Bus:
    def __init__(self, route_number, destination):
        self.route_number = 22
        self.destination = 'Ocean Terminal'
        self.passengers = []
    
    def drive(self):
        return "Brum brum"
    
    def passenger_count(self):
        return len(self.passengers)

    def pick_up(self, name):
        self.passengers.append(name)
    
    def drop_off(self, name):
        self.passengers.remove(name)
    
    def empty(self):
        self.passengers = []

    def pick_up_from_stop(self, bus_stop):
        self.passengers.extend(bus_stop.queue)
        bus_stop.clear()
                                                        