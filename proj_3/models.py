import numpy as np

class Economy:
    def __init__(self, gdp_growth_rate, population_growth_rate):
        self.gdp_growth_rate = gdp_growth_rate
        self.population_growth_rate = population_growth_rate

    def apply_natural_disaster_impact(self, disaster_severity):
        # Simulate impact on GDP and population growth rates
        self.gdp_growth_rate -= disaster_severity * 0.02  # Example impact
        self.population_growth_rate -= disaster_severity * 0.01

    def update(self):
        # Update GDP and population for a new time step
        self.gdp_growth_rate += np.random.normal(0, 0.01)  # Random fluctuation
        self.population_growth_rate += np.random.normal(0, 0.005)
