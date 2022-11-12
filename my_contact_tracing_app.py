# Note: 
# - Your program should be uploaded to github before 4pm
# - Record a demo presenting your program
# - Send the demo or link of demo directly to my messenger

#   Display a menu of options
# 	Menu:#   
#   1 -> Add an item
# 	2 -> Search
# 	3 -> Exit (y/n)
print("Menu")
print("1 -> Add an item")
print("2 -> Search")
print("3 -> Exit [y/n]")
#   Allow user to select item in the menu (check if valid)
user_req = int(input("\nWhat do you want to do? "))
if user_req > 3 or user_req < 1:
    print("\nYour input is OUT OF RANGE.\nThe program only has options of 1, 2 and 3.")
#   Perform the selected option
# 		- Option 1: Ask personal data for contact tracing (Listed are sample only, add more)
# 				   Use dictionary to store the info
# 				   Use the full name as key
# 				   The value is another dictionary of personal information
# 		- Option 2: Search, ask full name then display the record
# 		- Option 3: Ask the user if want to exit or retry.

# For option 1
# Ask personal data for contact tracing
# first info
user_name = str(input("Fullname: ")).title()
# second info
user_sex = str(input("Sex: ")).title()
# third info
user_age = int(input("Age: "))
# forth info
user_address = input("Address: ")
# fifth info
user_contact = int(input("Phone Number: "))
# sixth info
user_temp = float(input("Temperature: "))
# seventh info
user_comorb = input("Any Comorbidities: ")
# eighth info
user_temp = input("Ever been diagnosed positive for COVID-19? [Yes/No]: ")

user_database = {
    "Fullname": user_name,
    "Sex": user_sex,
    "Age": user_age,
    "Address": user_address,
    "Phone Number": user_contact,
    "Temperature": user_temp,
    "Any Comorbidities": user_temp,
    "Ever been diagnosed positive for COVID-19? [Yes/No]": user_temp
}

for form, answer in user_database.items():
    print(f"{form}: {answer}")
