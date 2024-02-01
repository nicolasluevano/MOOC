# Write your solution here:
class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0

    def tick(self):
        if self.seconds < 59:
            self.seconds += 1
        elif self.minutes == 59 and self.seconds == 59:
            self.seconds = 0
            self.minutes = 0
        else:
            self.seconds = 0
            self.minutes += 1

    def __str__(self):
        return f'{format(self.minutes, "02")}:{format(self.seconds, "02")}'

if __name__ == "__main__":
    watch = Stopwatch()
    for i in range(3600):
        print(watch)
        watch.tick()
