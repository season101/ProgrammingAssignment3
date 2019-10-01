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

#Display for Ticket Options
print("="*24+" {0:^16s} ".format(" TICKET OPTIONS ")+"="*24)

print()

print("{0:^65s}".format("+"+"-"*56+"+"))
print(" "*3+"| {0:^55}|".format("  UNIVERSAL STUDIOS "))
print("{0:^64s}".format("+-----+"+"-"*24+"+"+"-"*25+"+"))

#Menu Items
print(" "*3+"|{0:^5s}".format("DAY")+"| {0:^22s} |".format("ADULT TICKET")+" {0:^23s} |".format("CHILD TICKET"))
print("{0:^64s}".format("+-----+"+"-"*24+"+"+"-"*25+"+"))
print(" "*3+"|{0:^5d}".format(1)+"| {0:^22s} |".format("$105.00")+" {0:^23s} |".format("$100.00"))
print("{0:^64s}".format("+-----+"+"-"*24+"+"+"-"*25+"+"))
print(" "*3+"|{0:^5d}".format(2)+"| {0:^22s} |".format("$184.99")+" {0:^23s} |".format("$174.99"))
print("{0:^64s}".format("+-----+"+"-"*24+"+"+"-"*25+"+"))
print(" "*3+"|{0:^5d}".format(3)+"| {0:^22s} |".format("$204.99")+" {0:^23s} |".format("$194.99"))
print("{0:^64s}".format("+-----+"+"-"*24+"+"+"-"*25+"+"))
print()
print()
choice2ForNumberOfDays = int(input("Choose number of days (1-3): "))
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
print(" "*20+"| {0:^24s} |".format("UNIVERSAL STUDIOS"))
print("{0:^68s}".format("+----"+"-"*22+"+"))
print(" "*20+ "| {0:^24s} |".format("Adults       3*$184.99"))
print("{0:^68s}".format("+----"+"-"*22+"+"))
print(" "*20+"| {0:^24s} |".format("Children      4*$174.99"))
print("{0:^68s}".format("+----"+"-"*22+"+"))

#Taking userconfirmation for Orders
print()
print()
userConfirmation = input("Do you need to modify your order ? (y/n): ")
print()

#Display for Checkout
print("="*24+" {0:^16s} ".format(" CHECKOUT ")+"="*24)
print()
print()
print("=-"*14)
print("{0:^28s}".format("Ticket Order"))
print("=-"*14)
print("{0:^28s}".format("MAGIC KINGDOM"))
print()
print()
print(" "+"Adult        4 * $174.99")
print()
print(" "+"Children     4 * $174.99")
print()
print("-"*28)
print("Subtotal:          $1,716.00")
print("Tax:                 $188.76")
print("Total:             $1,904.76")
print("=-"*14)
print()
print()


#Displaying Thank You Prompt
print(" "*2+"=-"*30)
print("{0:^64s}".format("Thank you! Please come again!"))
print(" "*2+"=-"*30)
