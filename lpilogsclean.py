import pandas as pd

file_path = 'data/API_LP.LPI.LOGS.XQ_DS2_en_excel_v2_6299446.xls'

lpi_logs_data = pd.read_excel(file_path, skiprows=3)

asian_countries = ["Afghanistan", "Armenia", "Azerbaijan", "Bahrain", "Bangladesh", "Bhutan", "Brunei Darussalam",
                   "Cambodia", "China", "Georgia", "India", "Indonesia", "Iran, Islamic Rep.", "Iraq", "Israel",
                   "Japan", "Jordan", "Kazakhstan", "Korea, Dem. Rep.", "Korea, Rep.", "Kuwait", "Kyrgyz Republic",
                   "Lao PDR", "Lebanon", "Malaysia", "Maldives", "Mongolia", "Myanmar", "Nepal", "Oman", "Pakistan",
                   "Philippines", "Qatar", "Saudi Arabia", "Singapore", "Sri Lanka", "Syrian Arab Republic",
                    "Tajikistan", "Thailand", "Timor-Leste", "Turkmenistan","United Arab Emirates",
                   "Uzbekistan", "Viet Nam", "Yemen, Rep."]

# Filter Asian countries
filtered_lpi_logs_data = lpi_logs_data[lpi_logs_data['Country Name'].isin(asian_countries)]

# Melting the dataframe to get a long format with Country, Code, Year, and Value
melted_lpi_logs_data = filtered_lpi_logs_data.melt(id_vars=['Country Name', 'Country Code'],
                                         var_name='Year',
                                         value_name='LPI Logistics Competence')

from constant import years_to_keep, countries_to_keep, years_to_keep_s
melted_lpi_logs_data = melted_lpi_logs_data[melted_lpi_logs_data['Year'].isin(years_to_keep + years_to_keep_s)]
melted_lpi_logs_data = melted_lpi_logs_data[melted_lpi_logs_data['Country Name'].isin(countries_to_keep)]
# Saving the transformed dataframe to a new Excel file
transformed_file_path = 'cleaned/Transformed_LPI_Logistics.xlsx'
melted_lpi_logs_data.to_excel(transformed_file_path, index=False)

print(melted_lpi_logs_data.head())
