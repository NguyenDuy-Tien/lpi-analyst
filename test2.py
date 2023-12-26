import pandas as pd

# Load the excel file
file_path = 'data/gov_eff.xlsx'

# Skipping rows to the point where actual data starts
data = pd.read_excel(file_path, skiprows=14)

# # Display the first few rows of the actual data to confirm
# print(data.columns)

# Identifying columns that are 'Estimate' columns
estimate_columns = [col for col in data.columns if 'Estimate' in col]

# Listing of Asian countries (as per United Nations geoscheme for Asia)
asian_countries = ["Afghanistan", "Armenia", "Azerbaijan", "Bahrain", "Bangladesh", "Bhutan", "Brunei Darussalam", "Cambodia", "China", "Georgia", "India", "Indonesia",
                   "Iran, Islamic Rep.", "Iraq", "Israel", "Japan", "Jordan", "Kazakhstan", "Korea, Dem. Rep.", "Korea, Rep.", "Kuwait", "Kyrgyz Republic", "Lao PDR",
                   "Lebanon", "Malaysia", "Maldives", "Mongolia", "Myanmar", "Nepal", "Oman", "Pakistan", "Philippines", "Qatar", "Saudi Arabia", "Singapore", "Sri Lanka",
                   "Syrian Arab Republic",  "Tajikistan", "Thailand", "Timor-Leste", "Turkmenistan", "United Arab Emirates", "Uzbekistan", "Viet Nam", "Yemen, Rep."]

# print(data['Country/Territory'])

# Filtering the data for only Asian countries and 'Estimate' columns
asian_data = data[data['Country/Territory'].isin(asian_countries)][['Code', 'Country/Territory'] + estimate_columns]

print(asian_data.head())