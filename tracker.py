import csv
from jump import Jump
# I asked AI how to structure a save function using csv.writer and wrote this based on the response
def save_jumps(jumps, filename):
   with open(filename, "a", newline="") as file: 
        writer = csv.writer(file)
        for jump in jumps:
            # I asked ai how to join a list into a string for CSV storage and wrote this based on its response
            writer.writerow([jump.date, jump.event, ",".join(str(attempt) for attempt in jump.attempts)])

# I asked ai how to load data from a CSV file back into objects and wrote this based on the response
def load_jumps(filename):
    jumps = [] 
    try:
         with open(filename, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                date = row[0]
                event = row[1]
                attempts = row[2].split(",")
                jumps.append(Jump(date, event, attempts))
    except FileNotFoundError:
        return jumps
    return jumps