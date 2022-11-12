# Note: 
# - Your program should be uploaded to github before 4pm
# - Record a demo presenting your program
# - Send the demo or link of demo directly to my messenger

#   Display a menu of options
# 	Menu:#   
#   1 -> Add an item
# 	2 -> Search
# 	3 -> Exit (y/n)
#   Perform the selected option
# 		- Option 1: Ask personal data for contact tracing (Listed are sample only, add more)
# 				   Use dictionary to store the info
# 				   Use the full name as key
# 				   The value is another dictionary of personal information
# 		- Option 2: Search, ask full name then display the record
# 		- Option 3: Ask the user if want to exit or retry.
import datetime
time_today = datetime.datetime.now()

print("\nMenu")
print(" 1 -> Add an item")
print(" 2 -> Search")
print(" 3 -> Exit [y/n]")

database = {
    "Adrian R. Esguerra": {
        "Fullname": "Adrian R. Esguerra",
        "Sex": "Male",
        "Age": 19,
        "Address": "Taltal, Masinloc, Zambales",
        "Phone Number": "0912 345 6789",
        "Temperature": 36.2,
        "Comorbidities": "None",
        "Time": time_today
    },
    "Fullname": {
        "Fullname": "",
        "Sex": "", 
        "Age": 0,
        "Address": "", 
        "Phone Number": 0, 
        "Temperature": 0.0,
        "Comorbidities": "",
        "Time": time_today
    }
} 

def get_info():
    data_name = input
    # first info
    database["Name"]["Fullname"] = str(input("Fullname: ")).title()
    # second info
    database["Name"]["Fullname"] = str(input("Sex: ")).title()
    # third info
    database["Name"]["Fullname"] = int(input("Age: "))
    # forth info
    database["Name"]["Fullname"] = input("Address: ").title()
    # fifth info
    database["Name"]["Fullname"] = input("Phone Number: ")
    # sixth info
    database["Name"]["Fullname"] = float(input("Temperature: "))
    # seventh info
    database["Name"]["Fullname"] = str(input("Any Comorbidities: ")).title()

def do_search():
    user_name = str(input("Enter the user name: "))
    for key, value in database[user_name].items():   
        print(f"{key}: {value}")
        print()

# Allow user to select item in the menu (check if valid)
user_req = int(input("\nWhat do you want to do? "))
if user_req > 3 or user_req < 1:
    print("\nYour input is OUT OF RANGE.\nThe program only has options of 1, 2 and 3.")
elif user_req == 1:
    get_info()
    print("\nYour information was saved!")
    for data in database["Name"].items():
        print(data)
elif user_req == 2:
    do_search()
elif user_req == 3:
    breakpoint()