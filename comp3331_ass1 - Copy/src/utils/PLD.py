import random
import time

class PLD:
    def __init__(self, pdrop, seed, pdelay=0, maxdelay=0):
        self.seed = seed
        self.pdrop = pdrop
        self.pdelay = pdelay
        self.maxdelay = maxdelay

        random.seed(self.seed)

    def process(self, payload):
        if random.random() >= (1 - pdelay):
            sleep(maxdelay)

        if random.random() >= (1 - self.pdrop)):
            return payload
        else:
            return ""
