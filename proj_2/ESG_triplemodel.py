import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from flask import Flask, render_template, request

def generate_esg_data(num_companies=100):
    # Simulate ESG data for each company with a specified range
    data = {
        'Company_Number': list(range(1, num_companies + 1)),
        'Company_Name': [f'Company_{i+1}' for i in range(num_companies)],
        'Carbon_Emissions': np.random.uniform(0, 100, num_companies),
        'Resource_Usage': np.random.uniform(0, 100, num_companies),
        'Labor_Practices': np.random.uniform(0, 100, num_companies),
        'Diversity_Inclusion': np.random.uniform(0, 100, num_companies),
        'Human_Rights': np.random.uniform(0, 100, num_companies),
        'Community_Relations': np.random.uniform(0, 100, num_companies),
        'Board_Structure': np.random.uniform(0, 100, num_companies),
        'Executive_Compensation': np.random.uniform(0, 100, num_companies),
        'Shareholder_Rights': np.random.uniform(0, 100, num_companies),
        'Anti_Corruption_Policies': np.random.uniform(0, 100, num_companies),
        'ESG_Risk_Exposure': np.random.uniform(0, 100, num_companies),
        'Data_Accuracy': np.random.uniform(0, 100, num_companies),
    }

    df = pd.DataFrame(data)

    # Simulate ESG score as a weighted sum of selected factors
    weights = {
        'Carbon_Emissions': 0.2,
        'Diversity_Inclusion': 0.3,
        'Human_Rights': 0.5,
        'Anti_Corruption_Policies': 0.1,
        'ESG_Risk_Exposure': 0.4,
}

    df['ESG_Score'] = np.dot(df[['Carbon_Emissions', 'Diversity_Inclusion', 'Human_Rights', 'Anti_Corruption_Policies', 'ESG_Risk_Exposure']], list(weights.values()))

    return df

def save_to_csv(df, filename='esg_data.csv'):
    # Save DataFrame to CSV file
    df.to_csv(filename, index=False)
    print(f'Data saved to {filename}')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    # Retrieve weights from the HTML form
    weights = {
        'Carbon_Emissions': float(request.form['carbon']),
        'Diversity_Inclusion': float(request.form['diversity']),
        'Human_Rights': float(request.form['human_rights']),
        'Anti_Corruption_Policies': float(request.form['anti_corruption']),
        'ESG_Risk_Exposure': float(request.form['risk_exposure']),
    }

    # Generate simulated ESG data
    esg_data = generate_esg_data()

    # ... (rest of the script remains the same)

    # Simulate ESG score as a weighted sum of selected factors using user-adjusted weights
    df['ESG_Score'] = np.dot(df[['Carbon_Emissions', 'Diversity_Inclusion', 'Human_Rights', 'Anti_Corruption_Policies', 'ESG_Risk_Exposure']], list(weights.values()))

    return render_template('result.html', esg_data=df)

if __name__ == "__main__":
    app.run(debug=True)