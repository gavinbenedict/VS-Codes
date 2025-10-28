def vaccumWorld():
    goal = {'A': '0', 'B': '0'}
    cost = 0
    
    location = input("Enter location of vacuum: ")
    status_of_location = input("Enter state of " + location + ": ")
    oppLocation_status = input("Enter state of other room: ")

    if location == 'A': #current location is A
        print("Vacuum is placed in Location A")
        if status_of_location == '1': #location A is dirty
            print("Location A is Dirty")
            goal['A'] = '0'
            cost += 1
            print("COST for CLEANING A " + str(cost))
            print("Location A has been cleaned") # A cleaned

            if oppLocation_status == '1': #location B is dirty
                print("Location B is Dirty")
                print("Moving right to the location B")
                cost += 1
                print("COST for moving RIGHT " + str(cost))
                goal['B'] = '0'
                cost += 1
                print("COST for SUCK " + str(cost))
                print("Location B has been cleaned") #location B cleaned
            else: # location B is already cleaned
                print("No action " + str(cost))
                print("Location B is already clean")

        elif status_of_location == '0': # A is already clean
            print("Location A is already clean")
            if oppLocation_status == '1': # if B is dirty
                print("Location B is Dirty")
                print("Moving right to the location B")
                cost += 1
                print("COST for moving RIGHT " + str(cost))
                goal['B'] = '0'
                cost += 1
                print("COST for SUCK " + str(cost))
                print("Location B has been cleaned")
            else: #B is already clean
                print("No action " + str(cost))
                print("Location B is already clean")
    
    elif location == 'B': #location is B
        print("Vacuum is placed in Location B")
        
        if status_of_location == '1': # B is dirty
            print("Location B is Dirty")
            goal['B'] = '0'
            cost += 1
            print("COST for CLEANING B " + str(cost))
            print("Location B has been cleaned")

            if oppLocation_status == '1': #if A is dirty
                print("Location A is Dirty")
                print("Moving LEFT to the location A")
                cost += 1
                print("COST for moving LEFT " + str(cost))
                goal['A'] = '0'
                cost += 1
                print("COST for SUCK " + str(cost))
                print("Location A has been cleaned")
            else: # if A is already clean
                print("No action " + str(cost))
                print("Location A is already clean")

        elif status_of_location == '0': #If B is already clean
            print("Location B is already clean")
            
            if oppLocation_status == '1': # If A is dirty
                print("Location A is Dirty")
                print("Moving LEFT to the location A")
                cost += 1
                print("COST for moving LEFT " + str(cost))
                goal['A'] = '0'
                cost += 1
                print("COST for SUCK " + str(cost))
                print("Location A has been cleaned")
            else: # If A is clean 
                print("No action " + str(cost))
                print("Location A is already clean")

    print("GOAL STATE: ")
    print(goal)
    print("Performance measurement " + str(cost))

vaccumWorld()