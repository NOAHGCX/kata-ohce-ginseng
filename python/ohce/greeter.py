from datetime import datetime


class SystemClock:
    def current_hour(self):
        now = datetime.now()
        return now.hour


class FakeClock:
    def __init__(self, hour):
        self.hour = hour
        
    def current_hour(self):
        return self.hour



class Greeter:
    def __init__(self, clock):
        self.clock = clock
        
    def greet(self):
        # Get the current hour from the clock
        hour = self.clock.current_hour()
        
        # Return morning greeting between 6am and noon
        if 6 <= hour < 12:
            return "Good morning"
        # Return afternoon greeting between noon and 8pm 
        elif 12 <= hour <= 19:
            return "Good afternoon"
        # Return night greeting between 8pm and 6am
        else:  # hour >= 20 or hour < 6
            return "Good night"
