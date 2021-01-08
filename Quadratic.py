def main(e):
    try:
        arr = [float(input("----------------------------\n\nax^2 + bx + c = 0\nInput a:\n>>")),float(input("Input b:\n>>")),float(input("Input c:\n>>"))] if e == 0 else [float(input("\nError...\n----------------------------\n\nax^2 + bx + c = 0\nInput a:\n>>")),float(input("Input b:\n>>")),float(input("Input c:\n>>"))]
        print((lambda result, a=arr[0] , b=arr[1] , c=arr[2] : str("X= " + str((((-b)+(result)**(1/2))/(2*a)))  + " , " + str((((-b)-(result)**(1/2))/(2*a)))) if result > 0 else "X= " + str((((-b))/(2*a))))(arr[1]**2 -4*arr[0]*arr[2]),"\n") if (arr[1]**2 -4*arr[0]*arr[2]) >= 0 else print("Equasion is impossible\n")
        main(0)
    except:
        main(1)
main(0)