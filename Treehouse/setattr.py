class RaceCar:
    def __init__(self, color, fuel_remaining,  laps=0, **kwargs):
        self.color = color
        self.fuel_remaining = fuel_remaining
        self.laps = laps

        for key, value in kwargs.items():
            setattr(self, key, value)

    # TODO add a lap each time method gets called and update fuel_reamining
    def run_lap(self, length):
        self.fuel_remaining -= length * 0.125
        self.laps += 1
