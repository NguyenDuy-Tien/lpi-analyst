import pandas as pd

file_path = 'data/API_SL.TLF.CACT.NE.ZS_DS2_en_excel_v2_6298400.xls'

labor_data = pd.read_excel(file_path, skiprows=3)

asian_countries = ["Afghanistan", "Armenia", "Azerbaijan", "Bahrain", "Bangladesh", "Bhutan", "Brunei Darussalam",
                   "Cambodia", "China", "Georgia", "India", "Indonesia", "Iran, Islamic Rep.", "Iraq", "Israel",
                   "Japan", "Jordan", "Kazakhstan", "Korea, Dem. Rep.", "Korea, Rep.", "Kuwait", "Kyrgyz Republic",
                   "Lao PDR", "Lebanon", "Malaysia", "Maldives", "Mongolia", "Myanmar", "Nepal", "Oman", "Pakistan",
                   "Philippines", "Qatar", "Saudi Arabia", "Singapore", "Sri Lanka", "Syrian Arab Republic",
                    "Tajikistan", "Thailand", "Timor-Leste", "Turkmenistan","United Arab Emirates",
                   "Uzbekistan", "Viet Nam", "Yemen, Rep."]

# Filter Asian countries
filtered_labor_data = labor_data[labor_data['Country Name'].isin(asian_countries)]

# Melting the dataframe to get a long format with Country, Code, Year, and Value
melted_labor_data = filtered_labor_data.melt(id_vars=['Country Name', 'Country Code'],
                                         var_name='Year',
                                         value_name='Labor Participant Rate')

from constant import years_to_keep, countries_to_keep, years_to_keep_s
melted_labor_data = melted_labor_data[melted_labor_data['Year'].isin(years_to_keep + years_to_keep_s)]
melted_labor_data = melted_labor_data[melted_labor_data['Country Name'].isin(countries_to_keep)]
# Saving the transformed dataframe to a new Excel file
transformed_file_path = 'cleaned/Transformed_Labor_Rate.xlsx'
melted_labor_data.to_excel(transformed_file_path, index=False)

print(melted_labor_data.head())
