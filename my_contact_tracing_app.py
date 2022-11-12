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

print("Menu")
print("1 -> Add an item")
print("2 -> Search")
print("3 -> Exit [y/n]")



database = {
    "Fullname": "Adrian R. Esguerra",
    "Sex": "Male",
    "Age": 19,
    "Address": "Taltal, Masinloc, Zambales",
    "Phone Number": "0912 345 6789",
    "Temperature": 36.2,
    "Comorbidities": "None",
    "Time": time_today
}

# For option 1
# Ask personal data for contact tracing

user_data = {
    "Fullname": str(input("Fullname: ")).title(),
    "Sex": str(input("Sex: ")).title(),
    "Age": int(input("Age: ")),
    "Address": input("Address: ").title(),
    "Phone Number": input("Phone Number: "),
    "Temperature": float(input("Temperature: ")),
    "Comorbidities": str(input("Any Comorbidities: ")).title(),
    "Time": time_today
}

#   Allow user to select item in the menu (check if valid)
user_req = int(input("\nWhat do you want to do? "))
if user_req > 3 or user_req < 1:
    print("\nYour input is OUT OF RANGE.\nThe program only has options of 1, 2 and 3.")







database.update(user_data)
for form, answer in database.items():
    print(f"{form}: {answer}")


