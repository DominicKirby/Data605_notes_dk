import data


application = True

print("1: View available events, 2: Register an attendee for an event, 3: Remove an attendee from an event, 4: View attendee lists, 5: Search for an attendee, 6: Display event statistics, 7: Exit the application")

while application:
    choice = input("\nEnter your choice: ")
    if choice not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("enter a valid choice from 1-6")
    else:
        choice = int(choice)

    if choice == 1:
        """
        View available events
        """
        print("These are the available events and spaces left in each:")
        for event in data.events:
            event.information()

    elif choice == 2:
        """
        Add an attendee to a specific event
        """
        print("1: Python workshop, 2: 5-a-side Football, 3: Basketball, 4: Yoga, 5: Charity fundraiser")
        event_choice = input("Which event would you like to register a participant for? (1-5) ")
        if event_choice not in ["1", "2", "3", "4", "5"]:
            print("Please enter a valid choice from 1-5.")
        else:
            event_choice = data.events[int(event_choice) - 1]

            if len(event_choice.attendees) < event_choice._max_attendees:
                new_id = int(input(f"Which participant would you like to add to {event_choice.name}? (id number) "))

                if new_id not in data.registered_id:
                    print("This id does not exist in the database.")

                else:
                    list_index = new_id - 1

                    if new_id not in event_choice.attendees_id:
                        new_attendee = data.registered_participants[list_index]
                        event_choice.add_attendee([new_attendee])
                        print(f"{new_attendee.name} has now been added to {event_choice.name}.")
                    else:
                        print(f"This participant is already registered for {event_choice.name}.")
            else:
                print(f"This event is full.")

    elif choice == 3:
        """
        Remove an attendee from a specific event
        """
        event_choice = input("What event would you like to remove a participant from? (1-5) ")
        if event_choice not in ["1", "2", "3", "4", "5"]:
            print("Please enter a valid choice from 1-5")
        else:
            event_choice = data.events[int(event_choice) - 1]

        print(f"The current attendee ID's for {event_choice.name} are", event_choice.attendees_id, ".", sep='')

        participant_choice = int(input(f"Which participant ID would you to remove from {event_choice.name}? "))

        if participant_choice not in event_choice.attendees_id:
            print("This id does not exist in this event.")
        else:
            attendee = data.registered_participants[participant_choice - 1]
            event_choice.remove_attendee(attendee)
            print(f"Successfully removed {attendee.name} with id {attendee.id} from this event.")

    elif choice == 4:
        """
        View the attendees for an event
        """
        print("1: Python workshop, 2: 5-a-side Football, 3: Basketball, 4: Yoga, 5: Charity fundraiser")
        event_choice = input("Which event would you like to view participants for? (1-5) ")
        if event_choice not in ["1", "2", "3", "4", "5"]:
            print("Please enter a valid choice from 1-5.")
        else:
            event_choice = data.events[int(event_choice) - 1]
            event_choice.information()
            print(f'The current attendees are {event_choice.attendees}')

    elif choice == 5:
        """
        Search for a participant and their information
        """
        search_id = int(input("What is the integer id number of the participant you would like to view? "))


        if search_id in data.registered_id:
            attendee_name = data.registered_participants[search_id - 1].name

            print(f"This id is found to be for {attendee_name}")

            event_list = []
            for event in data.events:
                if search_id in event.attendees_id:
                    event_list.append(event.name)

            print(f"This participant is registered for {event_list}.")

    elif choice == 6:
        """
        Print general event information
        """
        print("Event Statistics\n")

        current_attendance = 0
        max_attendance = 0
        total_participants = len(data.registered_participants)
        for event in data.events:
            max_attendance += event._max_attendees
            current_attendance += len(event.attendees)
            event.information()

        print("\nCurrent attendance:", current_attendance)
        print("Max attendance:", max_attendance)
        print("Total registered participants:", total_participants)


    elif choice == 7:
        """
        Quit the programme
        """
        print("Application closed.")
        application = False
