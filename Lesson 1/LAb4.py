
# details_list=["serg ku" , 29 , "serg@hotmail.com" , "0547653404"]
# print("Full name: " + details_list[0]+ "\nAge: " + str(details_list[1])+  "\nMail: " + details_list[2]+ "\nPhone: " + details_list[3])


ip_list=["1.1.1.1","2.2.2.2"]
print(ip_list)
ip_list.append("3.3.3.3")
ip_list.append("4.4.4.4")
ip_list.append("5.5.5.5")
print(ip_list)


ip_list.pop(2)
print("IP List length is: " + str(len(ip_list)) + "\nAnd the IP List: " + str(ip_list))