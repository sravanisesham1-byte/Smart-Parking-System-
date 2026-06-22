# Smart Parking System using Python

total_slots = 10
parked_vehicles = []

while True:
    print("\n===== SMART PARKING SYSTEM =====")
    print("1. Park Vehicle")
    print("2. Remove Vehicle")
    print("3. Check Parking Status")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        if len(parked_vehicles) < total_slots:
            vehicle_no = input("Enter Vehicle Number: ")
            parked_vehicles.append(vehicle_no)
            print("Vehicle parked successfully.")
        else:
            print("Parking is Full!")

    elif choice == "2":
        vehicle_no = input("Enter Vehicle Number to Remove: ")
        if vehicle_no in parked_vehicles:
            parked_vehicles.remove(vehicle_no)
            print("Vehicle removed successfully.")
        else:
            print("Vehicle not found.")

    elif choice == "3":
        print("\n----- Parking Status -----")
        print("Total Slots      :", total_slots)
        print("Occupied Slots   :", len(parked_vehicles))
        print("Available Slots  :", total_slots - len(parked_vehicles))
        print("Parked Vehicles  :", parked_vehicles)

    elif choice == "4":
        print("Thank you for using Smart Parking System!")
        break

    else:
        print("Invalid choice. Please try again.")
