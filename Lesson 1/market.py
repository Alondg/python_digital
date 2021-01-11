print("Now we will calculate your marketing:\nPrices:\nTomato=3 NIS\nCucumber=2 NIS\nCola=5 NIS\nChicken=20 NIS\n")
tomatos=int(input("How many tomatos?"))
cucumbers=int(input("How many cucumbers?"))
colas=int(input("How many Colas?"))
chickens=int(input("How many chickens?"))
print("Summary of your order:\ntomatoes: " + str(tomatos) + "\ncucumbers: " + str(cucumbers) + "\ncolas: " + str(colas) + "\nchickens: " + str(chickens))

#sum1=tomatos*3
#sum2=cucumbers*2
#sum3=colas*5
#sum4=chickens*20
#summary=sum1+sum2+sum3+sum4

summary=(chickens*20)+(colas*5)+(cucumbers*2)+(tomatos*3)
print("\nYou have to pay: " + str(summary) + " NIS without tax")
print("\nYou have to pay: " + str("%.2f" % (summary*1.17)) + " NIS with tax")

