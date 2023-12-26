import pandas as pd

file_path = 'cleaned/Transformed_Data.xlsx'

data = pd.read_excel(file_path)

# Checking the distribution of each column and the presence of outliers
distribution_info = data.describe()

# Checking for skewness to understand the distribution better
skewness_info = data.skew(numeric_only=True)

# Combining the distribution and skewness information
distribution_summary = pd.concat([distribution_info, skewness_info.rename('Skewness')], axis=1)

print(distribution_summary)
transformed_file_path = 'cleaned/Skewness.xlsx'
distribution_summary.to_excel(transformed_file_path, index=True)


# Function to fill missing values with mean or median of the same year
def fill_missing_values(pre_data, column, method='mean'):
    if method == 'mean':
        return pre_data.groupby('Year')[column].transform(lambda x: x.fillna(x.mean()))
    elif method == 'median':
        return pre_data.groupby('Year')[column].transform(lambda x: x.fillna(x.median()))


# Applying the chosen methods for each column
data['Political Stability'] = fill_missing_values(data, 'Political Stability', 'mean')
data['GDP per capita'] = fill_missing_values(data, 'GDP per capita', 'median')
data['Global Innovation Index'] = fill_missing_values(data, 'Global Innovation Index', 'mean')
data['Labor Participant Rate'] = fill_missing_values(data, 'Labor Participant Rate', 'mean')
data['Corruption Control'] = fill_missing_values(data, 'Corruption Control', 'mean')
data['LPI Customs'] = fill_missing_values(data, 'LPI Customs', 'mean')
data['LPI Infra'] = fill_missing_values(data, 'LPI Infra', 'mean')
data['LPI International Shipment'] = fill_missing_values(data, 'LPI International Shipment', 'mean')
data['LPI Tracing'] = fill_missing_values(data, 'LPI Tracing', 'mean')
data['LPI Logistics Competence'] = fill_missing_values(data, 'LPI Logistics Competence', 'mean')
data['LPI Timeliness'] = fill_missing_values(data, 'LPI Timeliness', 'mean')
data['LPI Overall'] = fill_missing_values(data, 'LPI Overall', 'mean')

# Displaying the first few rows to verify the changes
data.head()
transformed_file_path = 'cleaned/Transformed_Data_Updated_Missing_Value.xlsx'
data.to_excel(transformed_file_path, index=False)