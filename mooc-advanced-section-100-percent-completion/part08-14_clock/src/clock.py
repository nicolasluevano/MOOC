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


class Clock:
    def __init__(self, hour: int, minutes: int, seconds: int):
        self.hour = hour
        self.minutes = minutes
        self.seconds = seconds

    def time(self):
        print(f'{self.hour:02d}:{self.minutes:02d}:{self.seconds:02d}')

    def tick(self):
        if self.seconds < 59:
            self.seconds += 1
        elif self.minutes < 59:
            self.seconds = 0
            self.minutes += 1
        elif self.hour < 23:
            self.seconds = 0
            self.minutes = 0
            self.hour += 1
        else:
            self.seconds = 0
            self.minutes = 0
            self.hour = 0

    def set(self, hour, minutes):
        self.hour = hour
        self.minutes = minutes
        self.seconds = 00

    def __str__(self):
        return f'{self.hour:02d}:{self.minutes:02d}:{self.seconds:02d}'

if __name__ == "__main__":
    clock = Clock(23, 59, 55)
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)

    clock.set(12, 5)
    print(clock)