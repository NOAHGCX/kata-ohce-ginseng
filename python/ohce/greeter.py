from datetime import datetime


class SystemClock:
    def current_hour(self):
        now = datetime.now()
        return now.hour


class FakeClock:
    def __init__(self, hour):
        self.hour = hour
        
    def get_current_hour(self):
        return self.hour


class Greeter:
    def __init__(self, clock):
        self.clock = clock
        
    def greet(self):
        hour = self.clock.get_current_hour()
        if 6 <= hour < 12:
            return "Good morning"
        elif 12 <= hour <= 19:
            return "Good afternoon"
        else:  # hour >= 20 or hour < 6
            return "Good night"
