sanjayDict = {"fName": "Sanjay",
              "lName": "Chopra",
              "address": "11 Oak Dr",
              }

print("My name: ", sanjayDict["fName"])

sanjayDict["address"] = "123 Main St"

sanjayDict["city"] = "Pittsburgh"

print("is there a city :", "city" in sanjayDict)

print(sanjayDict.values())

print(sanjayDict.keys())

for k, v in sanjayDict.items():
    print(k, v)

print(sanjayDict.get("lName", "Not Here"))

del sanjayDict["fName"]

for i in sanjayDict:
    print (i)

sanjayDict.clear()

employees = []

#fname, lName = input("Enter employee name: ").split()

#employees.append({"fName": fname,
#                  "lName": lName
#                  })

#print(employees)

# Enter customer (yes or No): y
# Enter customer name: Sanjay Chopra
# Enter customer (yes or No): y
# Enter customer name: Gerry Adams

customer_data = []

while True:
    to_add_customer = input("Enter a customer (yes or no): ")
    to_add_customer = to_add_customer[0].lower()

    if to_add_customer == "y":

        Name1, Name2 = input("Enter customer name: ").split()

        customer_data.append({"Name1": Name1, "Name2": Name2})


    elif to_add_customer == "n":
        break

for i in customer_data:
    print(i["Name1"], i["Name2"])

