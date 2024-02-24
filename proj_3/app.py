from flask import Flask, request, render_template
from models import Economy
from database import log_economy_data, engine

app = Flask(__name__)

# Initialize the Economy model
economy = Economy(gdp_growth_rate=0.03, population_growth_rate=0.01)

@app.route('/')
def home():
    return render_template('index.html')  # Create a basic form in templates/index.html

@app.route('/simulate-event', methods=['POST'])
def simulate_event():
    disaster_severity = float(request.form['disaster_severity'])
    economy.apply_natural_disaster_impact(disaster_severity)
    log_economy_data(engine, economy.gdp_growth_rate, economy.population_growth_rate)
    return 'Simulation updated. Check database for changes.'

if __name__ == '__main__':
    app.run(debug=True)
