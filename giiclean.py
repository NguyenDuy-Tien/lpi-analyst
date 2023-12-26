import pandas as pd

from constant import years_to_keep, countries_to_keep, years_to_keep_s

file_path = 'data/GII.xlsx'

corruption_data = pd.read_excel(file_path)
corruption_data.rename(columns={'Economies': 'Country Name'}, inplace=True)

country_name_mapping = {
    "Republic of Korea (the)": "Korea, Rep.",
    "Kyrgyzstan": "Kyrgyz Republic",
    "Lao People's Democratic Republic": "Lao PDR",
    "Yemen": "Yemen, Rep.",
    "Iran (Islamic Republic of)": "Iran, Islamic Rep.",
    "Vietnam": "Viet Nam"
}

corruption_data['Country Name'] = corruption_data['Country Name'].replace(country_name_mapping)

asian_countries = ["Afghanistan", "Armenia", "Azerbaijan", "Bahrain", "Bangladesh", "Bhutan", "Brunei Darussalam",
                   "Cambodia", "China", "Georgia", "India", "Indonesia", "Iran, Islamic Rep.", "Iraq", "Israel",
                   "Japan", "Jordan", "Kazakhstan", "Korea, Dem. Rep.", "Korea, Rep.", "Kuwait", "Kyrgyz Republic",
                   "Lao PDR", "Lebanon", "Malaysia", "Maldives", "Mongolia", "Myanmar", "Nepal", "Oman", "Pakistan",
                   "Philippines", "Qatar", "Saudi Arabia", "Singapore", "Sri Lanka", "Syrian Arab Republic",
                   "Tajikistan", "Thailand", "Timor-Leste", "Turkmenistan", "United Arab Emirates",
                   "Uzbekistan", "Viet Nam", "Yemen, Rep."]

# Filter Asian countries
filtered_corruption_data = corruption_data[corruption_data['Country Name'].isin(asian_countries)]

country_codes_mapping = {
    "Afghanistan": "AFG",
    "United Arab Emirates": "ARE",
    "Armenia": "ARM",
    "Azerbaijan": "AZE",
    "Bangladesh": "BGD",
    "Bahrain": "BHR",
    "Brunei Darussalam": "BRN",
    "Bhutan": "BTN",
    "China": "CHN",
    "Georgia": "GEO",
    "Indonesia": "IDN",
    "India": "IND",
    "Iran, Islamic Rep.": "IRN",
    "Iraq": "IRQ",
    "Israel": "ISR",
    "Jordan": "JOR",
    "Japan": "JPN",
    "Kazakhstan": "KAZ",
    "Kyrgyz Republic": "KGZ",
    "Cambodia": "KHM",
    "Korea, Rep.": "KOR",
    "Kuwait": "KWT",
    "Lao PDR": "LAO",
    "Lebanon": "LBN",
    "Sri Lanka": "LKA",
    "Maldives": "MDV",
    "Myanmar": "MMR",
    "Mongolia": "MNG",
    "Malaysia": "MYS",
    "Nepal": "NPL",
    "Oman": "OMN",
    "Pakistan": "PAK",
    "Philippines": "PHL",
    "Qatar": "QAT",
    "Saudi Arabia": "SAU",
    "Singapore": "SGP",
    "Syrian Arab Republic": "SYR",
    "Thailand": "THA",
    "Tajikistan": "TJK",
    "Turkmenistan": "TKM",
    "Timor-Leste": "TLS",
    "Uzbekistan": "UZB",
    "Viet Nam": "VNM",
    "Yemen, Rep.": "YEM"
}


def map_country_to_code(country_name):
    for long_name, code in country_codes_mapping.items():
        if country_name in long_name:
            return code
    return None  # If no mapping is found, return None


# Apply the mapping function to the 'Economies' column
filtered_corruption_data['Country Code'] = filtered_corruption_data['Country Name'].apply(map_country_to_code)

df = pd.DataFrame(filtered_corruption_data)
data = df.sort_values(by=['Year', 'Country Code'])
print(data.head())

data = data[data['Year'].isin(years_to_keep + years_to_keep_s)]
data = data[data['Country Name'].isin(countries_to_keep)]
# Saving the transformed dataframe to a new Excel file
transformed_file_path = 'cleaned/Transformed_GII.xlsx'
data.to_excel(transformed_file_path, index=False)
