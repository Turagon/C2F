celcius = input("Please input the temperature in celcius :")
default_value = False
while default_value ==False :
    try :
        celcius == float(celcius)
        default_value = True
    except :
        celcius = input("The data is invalid, please input again :")
celcius = float(celcius)
farenheit = celcius * 9 / 5 + 32
print("The temperature you input is ", celcius, "C", "which is equal to ", farenheit, " F") 