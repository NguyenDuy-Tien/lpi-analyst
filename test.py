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
asian_data = data[data['Country/Territory'].isin(asian_countries)][['Country/Territory'] + estimate_columns]
#
# # Displaying the first few rows of the filtered data
print(asian_data.head())
print(len(asian_data.columns))

# Đổi tên các cột "Estimate" để phản ánh năm tương ứng
years = range(1996, 1996 + len(asian_data.columns))
renamed_columns = {old_col: f"Estimate-{year}" for old_col, year in zip(asian_data.columns, years)}
print(renamed_columns)
asian_data_renamed = asian_data.rename(columns=renamed_columns)
#
# print(asian_data_renamed.head())

# Reshape the dataframe to have one row per country per year
df_melted = renamed_columns.melt(id_vars=["Country/Territory"],
                    var_name="year",
                    value_name="gov_eff")

# Rename the columns as requested
# df_melted.rename(columns={"Unnamed: 0": "code"}, inplace=True)

# Extract the year from the 'year' column
df_melted['year'] = df_melted['year'].str.extract('(\d+)').astype(int)

# Preview the transformed data
df_melted.head()

# Lưu dữ liệu vào một tệp Excel mới
output_file_path = 'cleaned/gov_eff_asian.xlsx'
asian_data_renamed.to_excel(output_file_path)

