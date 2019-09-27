# ###################### Introduction #############################
#                                                                 #
#    #Name: Sijan Malla              Date Assigned:?????????????  #
#    #                                                            #
#    #Course: 2000-44306        Date Due: ??:?????, ???????????   #
#    #                                                            #
#    #File name: Programming Assignment 2                         #
#    #                                                            #
#    #Program Description: ????????????????????????????????       #
#                          ?????????????????????????????????????  #
#                                                                 #
##################### Program Begins ##############################
print()
print(" "*2+"=-"*32)
print("{0:^64s}".format("Welcome! please complete your ticket order below!"))
print(" "*2+"=-"*32)
print()
print()

#Display for Theme Park Options
print("="*24+" {0:^16s} ".format("THEME PARK OPTIONS")+"="*24)

#Menu Items
print("{0:^68s}".format("+"+"-"*26+"+"))
print(" "*20+"| {0:^24s} |".format("THEME PARK"))
print("{0:^68s}".format("+---+"+"-"*22+"+"))
print(" "*20+"|{0:^3d}".format(1)+"| {0:^20s} |".format("Universal Studios"))
print("{0:^68s}".format("+---+"+"-"*22+"+"))
print(" "*20+"|{0:^3d}".format(2)+"| {0:^20s} |".format("Magic Kingdom"))
print("{0:^68s}".format("+---+"+"-"*22+"+"))
print(" "*20+"|{0:^3d}".format(3)+"| {0:^20s} |".format("Epcot"))
print("{0:^68s}".format("+---+"+"-"*22+"+"))
print()
print()
choice1ForThemePark = int(input("Choose a theme park (1-3): "))
print()

#Display for Ticket Options
print("="*24+" {0:^16s} ".format(" TICKET OPTIONS ")+"="*24)

print()

print("{0:^68s}".format("+"+"-"*26+"+"))
print(" "*20+"| {0:^24s} |".format("UNIVERSAL STUDIOS"))
print("{0:^69s}".format("+---+"+"-"*11+"+"+"-"*10+"+"))

#Menu Items
print(" "*20+"|{0:^3d}".format(1)+"| {0:^20s} |".format("Universal Studios"))
print("{0:^68s}".format("+---+"+"-"*22+"+"))
print(" "*20+"|{0:^3d}".format(2)+"| {0:^20s} |".format("Magic Kingdom"))
print("{0:^68s}".format("+---+"+"-"*22+"+"))
print(" "*20+"|{0:^3d}".format(3)+"| {0:^20s} |".format("Epcot"))
print("{0:^68s}".format("+---+"+"-"*22+"+"))
