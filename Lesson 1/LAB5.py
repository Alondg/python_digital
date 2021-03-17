my_dict={"Gil":10000,"Alon":34000,"Bob":450000,"Vova":123000,"Polla":23000}
print(my_dict)
print("The summary is: " + str(my_dict["Gil"]+my_dict["Polla"]))
summary=my_dict["Gil"]+my_dict["Polla"]
# my_dict["Philip"]=summary
# print(my_dict)
my_dict.update({"Philip":summary})
print(my_dict)

print("number of Enteries: " + str(len(my_dict)))

print("idan" in my_dict)

