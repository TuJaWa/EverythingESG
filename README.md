# EverythingESG
ESG Ratings Random Generator
* Generates random data for a number of companies over a number of years
* Each year will have an ESG rating of +- 1 from the year before (assumed)
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
   * Number of years is how 



