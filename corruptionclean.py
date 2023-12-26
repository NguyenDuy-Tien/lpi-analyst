import pandas as pd

file_path = 'data/Corruption_Data_Extract_From_Worldwide_Governance_Indicators.xlsx'

corruption_data = pd.read_excel(file_path)

# Renaming year columns from "2000 [YR2000]" to "2000" and so on
year_columns = corruption_data.columns[2:]
renamed_columns = {year: year.split()[0] for year in year_columns}
corruption_data.rename(columns=renamed_columns, inplace=True)

country_name_mapping = {
    "Vietnam": "Viet Nam"
}

corruption_data['Country Name'] = corruption_data['Country Name'].replace(country_name_mapping)

asian_countries = ["Afghanistan", "Armenia", "Azerbaijan", "Bahrain", "Bangladesh", "Bhutan", "Brunei Darussalam",
                   "Cambodia", "China", "Georgia", "India", "Indonesia", "Iran, Islamic Rep.", "Iraq", "Israel",
                   "Japan", "Jordan", "Kazakhstan", "Korea, Dem. Rep.", "Korea, Rep.", "Kuwait", "Kyrgyz Republic",
                   "Lao PDR", "Lebanon", "Malaysia", "Maldives", "Mongolia", "Myanmar", "Nepal", "Oman", "Pakistan",
                   "Philippines", "Qatar", "Saudi Arabia", "Singapore", "Sri Lanka", "Syrian Arab Republic",
                    "Tajikistan", "Thailand", "Timor-Leste", "Turkmenistan","United Arab Emirates",
                   "Uzbekistan", "Viet Nam", "Yemen, Rep."]

# Filter Asian countries
filtered_corruption_data = corruption_data[corruption_data['Country Name'].isin(asian_countries)]

# Melting the dataframe to get a long format with Country, Code, Year, and Value
melted_corruption_data = filtered_corruption_data.melt(id_vars=['Country Name', 'Country Code'],
                                         var_name='Year',
                                         value_name='Corruption Control')

df = pd.DataFrame(melted_corruption_data)
data = df.sort_values(by=['Year', 'Country Code'])
print(data.head())

from constant import years_to_keep, countries_to_keep, years_to_keep_s
data = data[data['Year'].isin(years_to_keep + years_to_keep_s)]
data = data[data['Country Name'].isin(countries_to_keep)]
# Saving the transformed dataframe to a new Excel file
transformed_file_path = 'cleaned/Transformed_Corruption.xlsx'
data.to_excel(transformed_file_path, index=False)