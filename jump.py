class Jump:
    def __init__(self, date, event, attempts):
        self.date = date
        self.event = event
        self.attempts = attempts
    def best_attempt(self):
        best = 0
        for attempt in self.attempts:
            if attempt == "F" or attempt == "f":
                continue 
            if attempt > best:
                best = attempt
        return best 