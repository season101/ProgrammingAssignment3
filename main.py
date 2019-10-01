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

numberOfAdultTickets = 0
numberOfChildTickets = 0
priceForAdultTickets = 0
priceForChildTickets = 0
themeParkName=""
adultPriceDay1=0
adultPriceDay2=0
adultPriceDay3=0
childPriceDay1=0
childPriceDay2=0
childPriceDay3=0


#Creating Loop For Ticket Confirmation:
userConfirmation = "Y"
while userConfirmation == "Y":
    #Display for Theme Park Options
    print("="*24+" {0:^16s} ".format("THEME PARK OPTIONS")+"="*24)
    print()
    print()

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

    # Assingning theme park name to display title + Ticket price in Ticket Options
    while choice1ForThemePark == 1:
        themeParkName = "UNIVERSAL STUDIOS"
        adultPriceDay1= 105.00
        adultPriceDay2= 184.99
        adultPriceDay3= 204.99
        childPriceDay1= 100.00
        childPriceDay2= 174.99
        childPriceDay3= 194.99
        choice1ForThemePark = 0     #ForReset

    while choice1ForThemePark == 2:
        themeParkName = "MAGICAL KINGDOM"
        adultPriceDay1= 124.00
        adultPriceDay2= 199.00
        adultPriceDay3= 289.00
        childPriceDay1= 118.00
        childPriceDay2= 187.00
        childPriceDay3= 271.00
        choice1ForThemePark = 0     #ForReset


    while choice1ForThemePark == 3:
        themeParkName = "EPCOT"
        adultPriceDay1= 114.00
        adultPriceDay2= 199.00
        adultPriceDay3= 289.00
        childPriceDay1= 108.00
        childPriceDay2= 187.00
        childPriceDay3= 271.00
        choice1ForThemePark = 0     #ForReset


    #Display for Ticket Options
    print("="*24+" {0:^16s} ".format(" TICKET OPTIONS ")+"="*24)

    print()

    print("{0:^65s}".format("+"+"-"*56+"+"))
    print(" "*3+"| {0:^55}|".format(themeParkName))
    print("{0:^64s}".format("+-----+"+"-"*24+"+"+"-"*25+"+"))

    #Menu Items
    print(" "*3+"|{0:^5s}".format("DAY")+"| {0:^22s} |".format("ADULT TICKET")+" {0:^23s} |".format("CHILD TICKET"))
    print("{0:^64s}".format("+-----+"+"-"*24+"+"+"-"*25+"+"))
    print(" "*3+"|{0:^5d}".format(1)+"| {0:^22.2f} |".format(adultPriceDay1)+" {0:^23.2f} |".format(childPriceDay1))
    print("{0:^64s}".format("+-----+"+"-"*24+"+"+"-"*25+"+"))
    print(" "*3+"|{0:^5d}".format(2)+"| {0:^22.2f} |".format(adultPriceDay2)+" {0:^23.2f} |".format(childPriceDay2))
    print("{0:^64s}".format("+-----+"+"-"*24+"+"+"-"*25+"+"))
    print(" "*3+"|{0:^5d}".format(3)+"| {0:^22.2f} |".format(adultPriceDay3)+" {0:^23.2f} |".format(childPriceDay3))
    print("{0:^64s}".format("+-----+"+"-"*24+"+"+"-"*25+"+"))

    print()
    print()

    choice2ForNumberOfDays = int(input("Choose number of days (1-3): "))

    priceForAdultTickets = 0
    priceForChildTickets = 0
    while choice2ForNumberOfDays == 1:
        priceForAdultTickets = adultPriceDay1
        priceForChildTickets = childPriceDay1
        choice2ForNumberOfDays = 0 # For Reset Purpose
    while choice2ForNumberOfDays == 2:
        priceForAdultTickets = adultPriceDay2
        priceForChildTickets = childPriceDay2
        choice2ForNumberOfDays = 0 # For Reset Purpose

    while choice2ForNumberOfDays == 3:
        priceForAdultTickets = adultPriceDay3
        priceForChildTickets = childPriceDay3
        choice2ForNumberOfDays = 0 # For Reset Purpose

    print()

    #Display for Ticket Amounts
    print("="*24+" {0:^16s} ".format(" TICKET AMOUNTS ")+"="*24)

    print()

    numberOfAdultTickets = int(input("Number of Adult Tickets: "))
    numberOfChildTickets = int(input("Number of Child Tickets: "))

    print()

    print("="*24+" {0:^16s} ".format(" REVIEW ORDER ")+"="*24)

    print()
    print()

    #Display for Review Orders
    print("{0:^68s}".format("+"+"-"*26+"+"))
    print(" "*20+"| {0:^24s} |".format(themeParkName))
    print("{0:^68s}".format("+----"+"-"*22+"+"))
    print(" "*20+ "| {0:<11s}{1:>13s} |".format("Adults",str(numberOfAdultTickets)+" * "+"{0:.2f}".format(priceForAdultTickets)))
    print("{0:^68s}".format("+----"+"-"*22+"+"))

    print(" "*20+ "| {0:<11s}{1:>13s} |".format("Children",str(numberOfChildTickets)+" * "+ "{0:.2f}".format(priceForChildTickets)))
    print("{0:^68s}".format("+----"+"-"*22+"+"))

    #Taking userconfirmation for Orders
    print()
    print()
    userConfirmation = input("Do you need to modify your order ? (Y/N): ").capitalize()
    print()


subtotal = (numberOfAdultTickets*priceForAdultTickets) + (numberOfChildTickets * priceForChildTickets)
tax = 0.11 * subtotal
total = subtotal + tax
#Display for Checkout
print("="*27+" {0:^10s} ".format(" CHECKOUT ")+"="*27)
print()
print()
print("=-"*14)
print("{0:^28s}".format("Ticket Order"))
print("=-"*14)
print("{0:^28s}".format(themeParkName))
print()
print(" {0:<11s}{1:>13s} ".format("Adults",str(numberOfAdultTickets)+" * "+str("{0:.2f}".format(priceForAdultTickets))))
print()
print(" {0:<11s}{1:>13s} ".format("Children",str(numberOfChildTickets)+" * "+ str("{0:.2f}".format(priceForChildTickets))))
print()
print("-"*28)
print(" Subtotal:{0:>17.2f}".format(subtotal))
print(" Tax:{0:>22.2f}".format(tax))
print(" Total:{0:>20.2f}".format(total))
print("=-"*14)
print()
print()


#Displaying Thank You Prompt
print(" "*2+"=-"*30)
print("{0:^64s}".format("Thank you! Please come again!"))
print(" "*2+"=-"*30)
