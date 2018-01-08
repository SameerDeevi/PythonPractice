class Car():
    Color = ''
    Make = ''
    Year  = ''
    Price = 0
    ##def __repr__(self):
        ##print('Car Class')

    def __init__(self,Color, Make, Year, Price):
        self.Color = Color
        self.Make = Make
        self.Year = Year
        self.Price = Price

Subaru = Car(Color = 'red', Make = 'Subaru', Year = '2018',Price = 30000)

print(Subaru.Color)
