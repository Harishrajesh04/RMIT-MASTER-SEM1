#Name: Harish Rajesh
#STudent ID: S4216549
#Assignment 1 of Programming fundamnetlas 
#Date of start is 20-03-2026
#The things I understand from the pdf is: I need to create the car repair shop management for customers and the basic data is Tim and Rose
#In this assignment, you are developing a management system for a car repairshop. The receptionists or mechanics at the shop are the ones that use this system to process service jobs and print out the receipts for the customers. You are required to implement the program following the below requirements

#creating datas for the management system

customer_data = {"Tim": True, "Rose": False} #this is the data that is given in the pdf

#this service data is also given in the pdf
services_data = {"inspection":{"hours":1.0, "input_hours": False, "parts_needed": False},
                 "diagnostic":{"hours":1.0, "input_hours": False, "parts_needed": False},
                 "maintenance":{"hours":2.0, "input_hours": False, "parts_needed": True},
                 "repair":{"hours":None, "input_hours": True, "parts_needed": True}}

#parts data is there in the page no 4 in the pdf

parts = {"oil": 35.0,"filter": 25.0, "brake":120.0, "battery": 180.0, "radiator": 420.0, "motor": 280.0}

#getting name from the cuustomer
def perform_service():
    while True:
        customer_name = input("Enter the customer name: ").strip()  #getting name from customer
        if customer_name.isalpha():
            break
        print("Invalid name, try again")  #throwing error because name contains oonly alphabets

#next we need to ask for the services that is required

    while True:
        service_required = input("Enter the service required: ").strip().lower()
        if service_required in services_data: #in service_data we have the data like the services that are present
            break
        print("Invalid service, try again")  
    if customer_name not in customer_data:
        customer_data[customer_name] = False #if not in the data then it shows tthe error because there is no serviice likethat 


#service hours for repair and parts thar are needed

    if service_required == "repair":
        while True:
            value = input("Enter the number of hours: ") #customer can give number of hours that work can be done
            try:
                hours = float(value)
                if hours >= 1 and (hours * 2).is_integer():
                    break
                else:
                    print("Invalid hours") #throws error because hours can only be in integer
            except:
                print("Invalid input")
    else:
        hours = services_data[service_required]["hours"]

#next this is fo rthe parts needed for service or repair
    
    if services_data[service_required]["parts_needed"]:
        while True:
            part_name = input("Enter part name: ").strip().lower()
            if part_name in parts: #parts are present in the parts data 
                part_cost = parts[part_name]
                break
            print("Invalid part, try again")
    else:
        part_name = None
        part_cost = 0


#now we need to add the cost calculation where this requires to use our brain

    rate = 40.0

    service_cost = hours * rate   #servicecost is 40 per hour is old customer then he or she has discount of .10
    original_cost = service_cost + part_cost

    if customer_data[customer_name]:
        discount = original_cost * 0.10 #this is for the old customer
    else:
        discount = 0 #this is for the new customer because theyy are new

    total_cost = original_cost - discount

#now we need to print thr receipt format
#design is given in the pdf
    print("-" * 50)
    print("Receipt")
    print("-" * 50)
    print(f"{service_required}: {hours} x 40")
#basic design and the required things to print
    if part_name:
        print(f"{part_name}: {part_cost}")

    print("-" * 50)
    print(f"Original cost: {original_cost:.2f} (AUD)")
    print(f"Discount: {discount:.2f} (AUD)")
    print(f"Total cost: {total_cost:.2f} (AUD)")
    print(f"Discount: {discount}")
    print(f"Total cost: {total_cost}")
    print("-" * 50)
#asking the customer to become the member

    if not customer_data[customer_name]:
        member_choice = input("Become member? (yes/no): ").strip().lower()
        if member_choice == "yes":
            customer_data[customer_name] = True
            print("Now you are a member.") #this prints the membership for the customer

        if member_choice == "no":
            print("Thankyou")

#displaying the customers who is member
def display_customers():
    for name, member in customer_data.items():
        print(name, "->", member)

#next we need to show the services that is present 
def display_services():
    for service_name, details in services_data.items():
        print(service_name, "->", details)

#after servivces we need to show the parts
def display_parts():
    for part_name, price in parts.items():
        print(part_name, "->", price)

#updating services for the customer
def update_services():
    service_name = input("Enter service name to update: ").strip().lower()

    if service_name in services_data:
        new_value = input("Enter new hours or na: ").strip().lower()

        if new_value == "na":
            services_data[service_name]["hours"] = None
            services_data[service_name]["input_hours"] = True
        else:
            services_data[service_name]["hours"] = float(new_value)
            services_data[service_name]["input_hours"] = False

        print("Service updated") #if service is ok then this will update the serviice
    else:
        print("Service not found") #if not this will show

#updating the parts for the customers
def update_parts():
    action = input("Add or remove part? (a/r): ").strip().lower()

    if action == "a":
        part_name = input("Enter new part name: ").strip().lower()
        price = float(input("Enter price: "))
        parts[part_name] = price
        print("Part added")
    elif action == "r":
        part_name = input("Enter part name to remove: ").strip().lower()
        if part_name in parts:
            del parts[part_name]
            print("Part removed")
        else:
            print("Part not found")
    else:
        print("Invalid choice")
#printing options to show for customers
while True:
    print("\n1. Perform service")
    print("2. Display customers")
    print("3. Display services")
    print("4. Display parts")
    print("5. Update services")
    print("6. Update parts")
    print("0. Exit")
#asking customer to pick the choices
    choice = input("Choose: ").strip()

    if choice == "1":
        perform_service()
    elif choice == "2":
        display_customers()
    elif choice == "3":
        display_services()
    elif choice == "4":
        display_parts()
    elif choice == "5":
        update_services()
    elif choice == "6":
        update_parts()
    elif choice == "0":
        print("Thank you")
        break
    else:
        print("Invalid choice")


# -------------------- Design Justification --------------------

# 1. Design decisions and rationales
# I used dictionary for storing customers, services and parts because it was simple for me
# to understand and easy to access values using key. I did not want to use complex structure.
# Initially I wrote everything in one block but it was getting confusing, so later I changed
# and created a function perform_service to handle main work.
# I used while loop for input because sometimes user can enter wrong value, so instead of
# stopping program it will ask again. That was my idea.
# I also added menu so user can choose option again and again without closing program.
# I created few functions like display_customers and update_parts just to reduce code size
# and make it little bit clean.

# 2. Challenges and limitations
# I had problem with invalid input handling. For example if user enters string instead of number
# it was giving error. I fixed it using try except but it took time to understand properly.
# Another issue was with menu flow, sometimes it was not going to correct option because of
# indentation mistake.
# One limitation is customer name only accepts alphabets, so if name has space it will not work.
# Also program is not saving any data, once it stops everything is gone which is not good.

# 3. References
# I mostly followed class notes and example programs given in lecture.
# Sometimes I checked python documentation and google for small doubts.

