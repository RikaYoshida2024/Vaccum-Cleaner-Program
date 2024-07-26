def agent(percept):
    room, status=percept
    if room=='A':
        if status=='Clean':
            return "Move to Right"
        elif status=='Dirty':
            return 'Suck'
    elif room=='B':
        if status=='Clean':
            return 'Move to Left'
        elif status=='Dirty':
            return 'Suck'
def main():
    rooms =["A","B"]
    clean_status=["Clean","Dirty"]
    percept_table={}
    while True:
        room=input("Enter Room(A/B) or type exit to quit: ")
        if room.lower()=='exit':
            break
        status=input("Enter the cleanliness status(Clean/Dirty):")
        if room not in rooms or status not in clean_status:
            print("Invalid input. Please try again.")
            continue
        percept=(room,status)
        action=agent(percept)
        percept_table[percept]=action
        print("Action",action)
        print(*"\n AGENT FUNCTION Percept-Action Table:")
        print("----------------------------------------------------------------")
        for percept, action in percept_table.items():
            print(f"Percept: {percept}\t\tAction: {action}")
if __name__=='__main__':
    main()
