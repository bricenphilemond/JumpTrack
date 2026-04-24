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
    
       