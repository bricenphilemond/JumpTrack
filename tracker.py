import csv 
from jump import Jump
def save_jumps(jumps, filename):
   with open(filename, "a", newline="") as file: 
        writer = csv.writer(file)
        for jump in jumps:
            writer.writerow([jump.date, jump.event, jump.attempts])
            