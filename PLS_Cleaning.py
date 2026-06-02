# 1. Set-Up Environment
# 1a. Import Libraries
import pandas as pd
import numpy as np

#1b. Load Datasets
pls2023_raw = pd.read_csv('Data/Raw/PLS_FY23_AE_pud23i.csv', encoding='latin-1', low_memory=False)
pls2022_raw = pd.read_csv('Data/Raw/PLS_FY22_AE_pud22i.csv', encoding='latin-1', low_memory=False)
pls2021_raw = pd.read_csv('Data/Raw/PLS_FY21_AE_pud21i.csv', encoding='latin-1', low_memory=False)
pls2020_raw = pd.read_csv('Data/Raw/PLS_FY20_AE_pud20i.csv', encoding='latin-1', low_memory=False)
pls2019_raw = pd.read_csv('Data/Raw/PLS_FY19_AE_pud19i.csv', encoding='latin-1', low_memory=False)

# 2. Data Cleaning
# 2a. Locale Maps
locale_type_map = {
    11: 'City', 12: 'City', 13: 'City',
    21: 'Suburban', 22: 'Suburban', 23: 'Suburban',
    31: 'Town', 32: 'Town', 33: 'Town',
    41: 'Rural', 42: 'Rural', 43: 'Rural'}

locale_size_map = {
    11: 'Large', 12: 'Mid-size', 13: 'Small',
    21: 'Large', 22: 'Mid-size', 23: 'Small',
    31: 'Fringe', 32: 'Distant', 33: 'Remote',
    41: 'Fringe', 42: 'Distant', 43: 'Remote'}

# 2b. PLS 2023 Dataset Cleaning
pls2023_cleaned = (pls2023_raw
    # Select Relevant Columns
    .loc[:, ['LIBNAME', 'STABR', 'CNTY', 'LOCALE_ADD', 'POPU_LSA', 'TOTSTAFF', 'BRANLIB', 'TOTINCM', 'LOCGVT',
             'STAFFEXP', 'PRMATEXP', 'ELMATEXP', 'BKVOL', 'EBOOK', 'VISITS', 'TOTCIR', 'ELMATCIR', 'PHYSCIR', 'TOTPRO',
             'GPTERMS', 'WIFISESS', 'FSCSKEY', 'LONGITUD', 'LATITUDE']]
    # Remove Libraries in Territories
    .query('STABR not in ["GU", "VI", "MP", "AS", "PR"]')
    # Remove Law Libraries
    .query('POPU_LSA != -9')
    # Remove Temporarily Closed Libraries
    .query('POPU_LSA != -3')
    # Replace Remaining Unreported Values with NULL
    .replace([-1, -9], np.nan)
    .assign(
    # Add Year
        YEAR=2023,
    # Locale Mapping
        LOCALE_TYPE=lambda x: x['LOCALE_ADD'].map(locale_type_map),
        LOCALE_SIZE=lambda x: x['LOCALE_ADD'].map(locale_size_map)))

# 2c. PLS 2022 Dataset Cleaning
pls2022_cleaned = (pls2022_raw
    # Select Relevant Columns
    .loc[:, ['LIBNAME', 'STABR', 'CNTY', 'LOCALE_ADD', 'POPU_LSA', 'TOTSTAFF', 'BRANLIB', 'TOTINCM', 'LOCGVT',
         'STAFFEXP', 'PRMATEXP', 'ELMATEXP', 'BKVOL', 'EBOOK', 'VISITS', 'TOTCIR', 'ELMATCIR', 'PHYSCIR', 'TOTPRO',
         'GPTERMS', 'WIFISESS', 'FSCSKEY', 'LONGITUD', 'LATITUDE']]
    # Remove Libraries in Territories
    .query('STABR not in ["GU", "VI", "MP", "AS", "PR"]')
    # Remove Law Libraries
    .query('POPU_LSA != -9')
    # Remove Temporarily Closed Libraries
    .query('POPU_LSA != -3')
    # Replace Remaining Unreported Values with NULL
    .replace([-1, -9], np.nan)
    .assign(
    # Add Year
        YEAR=2022,
    # Locale Mapping
        LOCALE_TYPE=lambda x: x['LOCALE_ADD'].map(locale_type_map),
        LOCALE_SIZE=lambda x: x['LOCALE_ADD'].map(locale_size_map)))

# 2d. PLS 2021 Dataset Cleaning
pls2021_cleaned = (pls2021_raw
    # Select Relevant Columns
    .loc[:, ['LIBNAME', 'STABR', 'CNTY', 'LOCALE_ADD', 'POPU_LSA', 'TOTSTAFF', 'BRANLIB', 'TOTINCM', 'LOCGVT',
         'STAFFEXP', 'PRMATEXP', 'ELMATEXP', 'BKVOL', 'EBOOK', 'VISITS', 'TOTCIR', 'ELMATCIR', 'PHYSCIR', 'TOTPRO',
         'GPTERMS', 'WIFISESS', 'FSCSKEY', 'LONGITUD', 'LATITUDE']]
    # Remove Libraries in Territories
    .query('STABR not in ["GU", "VI", "MP", "AS", "PR"]')
    # Remove Law Libraries
    .query('POPU_LSA != -9')
    # Remove Temporarily Closed Libraries
    .query('POPU_LSA != -3')
    # Replace Remaining Unreported Values with NULL
    .replace([-1, -9], np.nan)
    .assign(
    # Add Year
        YEAR=2021,
    # Locale Mapping
        LOCALE_TYPE=lambda x: x['LOCALE_ADD'].map(locale_type_map),
        LOCALE_SIZE=lambda x: x['LOCALE_ADD'].map(locale_size_map)))

# 2e. PLS 2020 Dataset Cleaning
pls2020_cleaned = (pls2020_raw
    # Select Relevant Columns
    .loc[:, ['LIBNAME', 'STABR', 'CNTY', 'LOCALE_ADD', 'POPU_LSA', 'TOTSTAFF', 'BRANLIB', 'TOTINCM', 'LOCGVT',
         'STAFFEXP', 'PRMATEXP', 'ELMATEXP', 'BKVOL', 'EBOOK', 'VISITS', 'TOTCIR', 'ELMATCIR', 'PHYSCIR', 'TOTPRO',
         'GPTERMS', 'WIFISESS', 'FSCSKEY', 'LONGITUD', 'LATITUDE']]
    # Remove Libraries in Territories
    .query('STABR not in ["GU", "VI", "MP", "AS", "PR"]')
    # Remove Law Libraries
    .query('POPU_LSA != -9')
    # Remove Temporarily Closed Libraries
    .query('POPU_LSA != -3')
    # Replace Remaining Unreported Values with NULL
    .replace([-1, -9], np.nan)
    .assign(
    # Add Year
        YEAR=2020,
    # Locale Mapping
        LOCALE_TYPE=lambda x: x['LOCALE_ADD'].map(locale_type_map),
        LOCALE_SIZE=lambda x: x['LOCALE_ADD'].map(locale_size_map)))

# 2f. PLS 2019 Dataset Cleaning
pls2019_cleaned = (pls2019_raw
    # Select Relevant Columns
    .loc[:, ['LIBNAME', 'STABR', 'CNTY', 'LOCALE_ADD', 'POPU_LSA', 'TOTSTAFF', 'BRANLIB', 'TOTINCM', 'LOCGVT',
         'STAFFEXP', 'PRMATEXP', 'ELMATEXP', 'BKVOL', 'EBOOK', 'VISITS', 'TOTCIR', 'ELMATCIR', 'PHYSCIR', 'TOTPRO',
         'GPTERMS', 'WIFISESS', 'FSCSKEY', 'LONGITUD', 'LATITUDE']]
    # Remove Libraries in Territories
    .query('STABR not in ["GU", "VI", "MP", "AS", "PR"]')
    # Remove Law Libraries
    .query('POPU_LSA != -9')
    # Remove Temporarily Closed Libraries
    .query('POPU_LSA != -3')
    # Replace Remaining Unreported Values with NULL
    .replace([-1, -9], np.nan)
    .assign(
    # Add Year
        YEAR=2019,
    # Locale Mapping
        LOCALE_TYPE=lambda x: x['LOCALE_ADD'].map(locale_type_map),
        LOCALE_SIZE=lambda x: x['LOCALE_ADD'].map(locale_size_map)))

# 3. Join Datasets
pls_final = pd.concat([pls2023_cleaned, pls2022_cleaned, pls2021_cleaned, pls2020_cleaned, pls2019_cleaned],
                      ignore_index=True)

# 4. Export Final Dataset
pls_final.to_csv('Data/Processed/pls_final.csv', index=False)

# 5. Calculate 1st Percentile Thresholds for Dashboard Filter
pls_2019_libs = (pls_final
    .query('YEAR == 2019')
    .groupby('FSCSKEY', as_index=False)
    .agg(VISITS=('VISITS', 'sum'), TOTCIR=('TOTCIR', 'sum'))
    .query('VISITS > 0 and TOTCIR > 0')  # Gate 1: remove zero-value records
)

p01_visits = pls_2019_libs['VISITS'].quantile(0.01)
p01_totcir = pls_2019_libs['TOTCIR'].quantile(0.01)

print(f'Tableau Filter Thresholds (1st Percentile):')
print(f'  VISITS >= {p01_visits:.0f}')
print(f'  TOTCIR >= {p01_totcir:.0f}')