class Jump:
    # I asked ai how to structure a class with an __init__ method and wrote this based on its response
    def __init__(self, date, event, attempts):
        self.date = date
        self.event = event
        self.attempts = attempts
 
 # I asked ai how to write a method to find the best value in a list while skipping certain values and wrote this based on its response
    def best_attempt(self):
        best = 0
        for attempt in self.attempts:
            if attempt == "F" or attempt == "f":
                continue 
            if attempt > best:
                best = attempt
        return best 