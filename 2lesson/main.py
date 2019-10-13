def get_imt(weight, height):
    imt = weight / (height * height)
    if imt < 19:
        print("У вас недовес")
    elif imt > 25:
        print("У вас перевес")
    else:
        print("Ваш вес в норме")

get_imt(100,1.8)

get_imt(80,1.6)

get_imt(50.5,1.9)