def fahrenheit2celsius(fahrenheit): 
    F = fahrenheit
    celsius = (F - 32) * 5 / 9
    return celsius

def what_to_wear(celsius):
    a = int(celsius)
    if a < -10:
        print ("Puffy jacket")
    if  -10 < a < 0:
        print("Scarf")
    if 0 < a < 10: 
        print("Sweater")
    if 10 < a < 20:
        print("Light jacket")
    else:
        print("T-shirt")

fahrenheit = 90
what_to_wear(fahrenheit2celsius(fahrenheit))