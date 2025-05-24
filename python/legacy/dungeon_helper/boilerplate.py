import math

def get_prime_numbs_in_range(lower_end : int, upper_end : int, update = True):
    assert lower_end > 0 and upper_end > 0, "lower_end und upper_end müssen beide positiv sein"
    assert upper_end > lower_end, "upper_end muss größer sein als lower_end"

    prime_numbs = []
    for numb in range (lower_end, upper_end):
        div = numb
        if numb == 2:
            is_prime = False
        else:
            is_prime = True

        while div > 2:
            div -= 1
            if numb % div == 0:
                is_prime = False
                break

        if is_prime:
            if update: print(f"--> {numb}")
            prime_numbs.append(numb)

    if update: print(f"{len(prime_numbs)} prime numbers found between {lower_end} and {upper_end}")
    return prime_numbs


def get_circle_val(radius = None, diameter = None, area = None, circumference = None, rounding = None):
    pi = 3.14159265359

    if diameter:
        radius = diameter / 2
    
    if area:
        radius = math.sqrt(area / pi)

    if circumference:
        radius = (circumference / pi) / 2

    diameter = radius * 2
    area = pi * (radius * radius)
    circumference = (radius * 2) * pi

    if rounding:
        return round(radius, rounding), round(diameter, rounding), round(area, rounding), round(circumference, rounding)
    return radius, diameter, area, circumference
            
print(get_circle_val(area = 3, rounding=1))


