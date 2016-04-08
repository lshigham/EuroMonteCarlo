import numpy as np
import option    

def europeanMonteCarloPricer(spot, rate, volatility, the_option,
                             steps, replications):
    
    the_expiry = the_option.get_expiry
    the_strike = the_option.get_strike
    dt = the_expiry / steps
    nudt = (rate - 0.5 * volatility * volatility) * dt
    sigsdt = volatility * np.sqrt(dt)
    sumCT = 0.0
    
    for j in range(replications):
        lnSt = np.log(spot)
        z = np.random.normal(size=steps)
        
        for i in range(steps):
            lnSt = lnSt + nudt + sigsdt * z[i]
        
        ST = np.exp(lnSt)
            # here is where the oop will be -- focus on how to make this.
        sumCT += the_option.payoff(ST) # Sum of the total (replications) call price 


       
    sumCT /= replications # expected option payoff
    price = np.exp(-rate * the_expiry) * sumCT # Discounted factor to get PV
    
    return price
    

def main():
    spot = 42.0
    strike = 40.0
    rate = 0.10
    volatility = 0.20
    expiry = 0.5
    steps = 1 #int(252.0 / 2.0)
    replications = 50000
    
    the_call = option.VanillaCallOption(strike, expiry)
    the_put = option.VanillaPutOption(strike, expiry)
    
    callPrice = europeanMonteCarloPricer(spot, rate, volatility, the_call,
                                         steps, replications)
    putPrice = europeanMonteCarloPricer(spot, rate, volatility, the_put, steps, replications)
                                       
    print("The Call Price is: {}".format(callPrice))
    print("The Put Price is: {}".format(putPrice))
    
            
    
