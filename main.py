from tracker import save_jumps, load_jumps
from jump import Jump 
FILENAME = "jumps.csv"
def main():
    jumps = load_jumps(FILENAME)
    while True:
        print(" Welcome to JumpTrack!")
        print("1. Add a jump")
        print("2. View jumps")
        print("3. View personal best")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            # Add a jump
            input_date = input("Enter the date of the jump (YYYY-MM-DD):")
            input_event = input("Enter the event(long jump or triple jump):")
            input_distance1 = input("enter attempt 1 of the jump(or f for foul) in meters:")
            input_distance2 = input("enter attempt 2 of the jump(or f for foul) in meters:")
            input_distance3 = input("enter attempt 3 of the jump(or f for foul) in meters:")
            input_distance4 = input("enter attempt 4 of the jump(or f for foul) in meters:")
            attempts = [input_distance1, input_distance2, input_distance3, input_distance4]
            jumps.append(Jump(input_date, input_event, attempts))
            save_jumps(jumps, FILENAME)
            print("Jump added successfully!")
        elif choice == "2":
            # view jumps
            if len(jumps) == 0:
                print("No jumps logged yet!")
            else:
                for jump in jumps:
                    print(f"Date: {jump.date}, Event: {jump.event}, Attempts: {jump.attempts}")
        elif choice == "3":
            # view personal best
            pass
        elif choice == "4":
            save_jumps(jumps, FILENAME)
            print("Goodbye!")
            break
        
       