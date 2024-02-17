from flask import Flask, render_template, request
import pandas as pd
import numpy as np

app = Flask(__name__)

# Function to generate random ESG data for a company
def generate_random_esg_data():
    return {
        'carbon_emissions': np.random.uniform(0, 100),
        'resource_usage': np.random.uniform(0, 100),
        'labor_practices': np.random.uniform(0, 100),
        'diversity_inclusion': np.random.uniform(0, 100),
        'human_rights': np.random.uniform(0, 100),
        'community_relations': np.random.uniform(0, 100),
        'board_structure': np.random.uniform(0, 100),
        'executive_compensation': np.random.uniform(0, 100),
        'shareholder_rights': np.random.uniform(0, 100),
        'anti_corruption_policies': np.random.uniform(0, 100),
        'esg_risk_exposure': np.random.uniform(0, 100),
        'data_accuracy': np.random.uniform(0, 100),
    }

# Function to calculate ESG rating based on sophisticated factors
def calculate_esg_rating(esg_data, weights):
    environmental_score = (esg_data['carbon_emissions'] + esg_data['resource_usage']) / 2
    social_score = (esg_data['labor_practices'] + esg_data['diversity_inclusion'] +
                    esg_data['human_rights'] + esg_data['community_relations']) / 4
    governance_score = (esg_data['board_structure'] + esg_data['executive_compensation'] +
                        esg_data['shareholder_rights'] + esg_data['anti_corruption_policies']) / 4

    total_score = (
        environmental_score * weights['environmental'] +
        social_score * weights['social'] +
        governance_score * weights['governance']
    )

    return total_score

# Function to simulate ESG ratings for a given number of companies and years
def simulate_esg_ratings(num_companies, num_years, weights):
    companies = {}

    for i in range(1, num_companies + 1):
        esg_data = generate_random_esg_data()
        esg_ratings = []

        for _ in range(num_years):
            esg_rating = calculate_esg_rating(esg_data, weights)
            esg_ratings.append(esg_rating)

            # Simulate changes in ESG factors over time (for demonstration purposes)
            for factor in esg_data:
                esg_data[factor] += np.random.uniform(-1, 1)

        companies[f'Company_{i}'] = esg_ratings

    return companies

# Flask routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    num_companies = int(request.form['num_companies'])
    num_years = int(request.form['num_years'])

    weights = {
        'environmental': float(request.form['weight_environmental']),
        'social': float(request.form['weight_social']),
        'governance': float(request.form['weight_governance']),
    }

    esg_ratings = simulate_esg_ratings(num_companies, num_years, weights)

    return render_template('result.html', esg_ratings=esg_ratings)

if __name__ == '__main__':
    app.run(debug=True)

#Test