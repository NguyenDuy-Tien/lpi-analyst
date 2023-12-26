import pandas as pd

file_path = 'data/API_NY.GDP.PCAP.CD_DS2_en_excel_v2_6298460.xls'

gdp_data = pd.read_excel(file_path, skiprows=3)

asian_countries = ["Afghanistan", "Armenia", "Azerbaijan", "Bahrain", "Bangladesh", "Bhutan", "Brunei Darussalam",
                   "Cambodia", "China", "Georgia", "India", "Indonesia", "Iran, Islamic Rep.", "Iraq", "Israel",
                   "Japan", "Jordan", "Kazakhstan", "Korea, Dem. Rep.", "Korea, Rep.", "Kuwait", "Kyrgyz Republic",
                   "Lao PDR", "Lebanon", "Malaysia", "Maldives", "Mongolia", "Myanmar", "Nepal", "Oman", "Pakistan",
                   "Philippines", "Qatar", "Saudi Arabia", "Singapore", "Sri Lanka", "Syrian Arab Republic",
                    "Tajikistan", "Thailand", "Timor-Leste", "Turkmenistan","United Arab Emirates",
                   "Uzbekistan", "Viet Nam", "Yemen, Rep."]

# Filter Asian countries
filtered_gdp_data = gdp_data[gdp_data['Country Name'].isin(asian_countries)]

# Melting the dataframe to get a long format with Country, Code, Year, and Value
melted_gdp_data = filtered_gdp_data.melt(id_vars=['Country Name', 'Country Code'],
                                         var_name='Year',
                                         value_name='GDP per capita')

from constant import years_to_keep, countries_to_keep, years_to_keep_s
melted_gdp_data = melted_gdp_data[melted_gdp_data['Year'].isin(years_to_keep + years_to_keep_s)]
melted_gdp_data = melted_gdp_data[melted_gdp_data['Country Name'].isin(countries_to_keep)]
# Saving the transformed dataframe to a new Excel file
transformed_file_path = 'cleaned/Transformed_GDP_capita.xlsx'
melted_gdp_data.to_excel(transformed_file_path, index=False)

print(melted_gdp_data.head())
