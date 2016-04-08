import numpy as np

class VanillaOption(object):
    def __init__(self, strike, expiry):
        self.strike = strike
        self.expiry = expiry
        
    def payoff(self):
        pass
    
class VanillaCallOption(VanillaOption):
    def __init__(self, strike, expiry):
        super(VanillaCallOption, self).__init__(strike, expiry)
        
    def payoff(self, spot):
        return np.maximum(spot - self.strike, 0.0)
        
class VanillaPutOption(VanillaOption):
    def __init__(self, strike, expiry):
        super(VanillaPutOption, self).__init__(strike, expiry)

    def payoff(self, spot):
        return np.maximum(self.strike - spot, 0.0)        

if __name__ == "__main__":
    print("This is a module, not a user level script.")