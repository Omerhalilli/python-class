x = input("Last of us yoxsa God of war?")
class Phone:
    def __init__(self,color,ram,stroge,model,price,mark,year):
        self.color = color
        self.ram = ram
        self.stroge = stroge
        self.model = model
        self.mark = mark
        self.price = price
        self.year = year


    def __str__(self):
        return f" {self.color} {self.ram } {self.stroge} {self.model} {self.price} {self.mark} {self.year}"
    
    def apple(self):
        if  self.price>1000:
            return f"{self.price} manat 1000 manatdan yuxaridi"
        else:
            return f"{self.price} manat 1000 manatdan asagidi"
    def apple2(self):
        if self.year<2015:
            return f"{self.year} il kohnedi"
        else:
            return f"{self.year} il tezedi"

telefon = Phone(color = "red" , ram = "8gb", stroge = "128gb", model = "Iphone",mark = "apple",price = 800,year = 2003)

class Movie:
    def __init__(self,pixel,hd,inch,name1,color,name2):
        self.pixel = pixel
        self.hd = hd
        self.inch = inch
        self.name1 = name1
        self.color = color
        self.name2 = name2

    def __str__(self):
        return f" {self.pixel} {self.hd} {self.inch} {self.name} {self.color}"
    def films(self):
        if self.name1 == x :
            return f"{self.name1} gozel filimdir"
        elif self.name2 == x:
            return f"{self.name2} pis filimdir"
        

movies1 = Movie(pixel = 1020, hd = "full",inch = 200, name1 ="Last of us", name2 = "God of war",color = "red")



print(movies1.films())




        
        