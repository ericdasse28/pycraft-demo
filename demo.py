class Skyscraper:
    MIN_HEIGHT=100 #meters
    def __init__(self,name,h,location,nicknames=[]):
        self.name=name
        self.h= h
        self.location=location
        self.nicknames=nicknames
    @property
    def heigh_in_feet(self):
        return self.h*3.28