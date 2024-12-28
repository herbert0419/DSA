# celcius to farhenheit

def conversion(temperature,unit):
    if unit == 'C':
        return temperature * 9/5 +32
    elif unit == 'F':
        return 5/9 * (temperature-32)
    else:
        return None
    
print(conversion(0,'F'))