# EverythingESG
ESG Ratings Random Generator
* Generates random data for a number of companies over a number of years
* Each year will change the factors by +- 1 from the year before (assumed)
* Data is weighted for three pillars of ESG: Environment, Social, and Governance
* The Ten factors are divided into the three pillars
 * The factors are carbon_emissions, resource_usage, labor_practices, diversity_inclusion, human_rights, community_relations, board_structure, executive_compensation, shareholder_rights, anti_corruption_policies, esg_risk_exposure, data_accuracy
  * Under Environment are carbon_emissions, resource_usage
  * Under Social are labor_practices, diversity_inclusion, human_rights, community_relations
  * Under Government are board_structure, executive_compensation, shareholder_rights, anti_corruption_policies

* The model includes unused factors esg_risk_exposure, data_accuracy

## Using the Application
* On http://127.0.0.1:5000/, you will be presented with 5 form fields:
  * Number of Companies, Number of Years, Weight (Environmental), Weight (Social), Weight (Governance)
   * Number of companies means how many companies you are simulating
   * Number of years is how many years of data you want to generate
   * The weights are relative weights to calculate the ESG score for each company. The weights should add to 1 and be positive. No error checks on this yet.
* By pressing "Calculate", the page will show your companies titled "Company_[number]" followed by a list of sequential ESG ratings simulated for the number of years specified

## How to run the application
* Prerequisites:
 * Must have python3 installed
  * Tested with Python 3.11.7 on Mac
 * ```pip install pandas```
 * ```pip install flask```
 * ```pip install numpy```
 * Clone this repo
 * ```cd proj_1```
 * ```python3 ESG_ratings_simplified.py```


## Areas for Improvement
* Currently, only final scores are outputed. Could add factor series to output as well.
* Changing the variability of factors on a year to year basis to be something other than one
* Creating graphs of the scores
* Edit checks to make sure that weights are 1) normalized or 2) sum to 1

## New projects:
* Generate these factors for a given company
* Look at [GRI Standards](https://www.globalreporting.org/standards)

