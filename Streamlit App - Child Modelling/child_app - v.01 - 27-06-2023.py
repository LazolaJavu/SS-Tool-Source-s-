import requests
import json
import pandas as pd

#################### ACTIVE CHILDREN #######################################

def get_franchisee_data(franchisor_value):
    url = "https://api.smartstart.org.za/v1/Child/Query/"
    payload = json.dumps({
      "Columns": [
        "Guid",
        "FullName",
        "StartDate",
        "InactiveDate",
        "Status"
      ],
      "Conditions": [
        {
          "Column": "Status",
          "Operator": "Equals",
          "Value": "Active"
        }
      ],
      "Related": [
        {
          "RelatedBy": "Franchisee",
          "Columns": [
            "FullName",
            "IdNumber",
            "Province",
            "ProgrammeType"
          ],
          "Conditions": [
            {
              "Column": "Franchisor",
              "Operator": "Equals",
              "Value": franchisor_value
            }
          ]
        }
      ]
    })
    headers = {
      'Content-Type': 'application/json',
      'API-Key': '4369C387-DAB7-418A-A623-00B91753D0C3'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    if response.status_code == 200:
        json_data = response.json()
        df = pd.json_normalize(json_data)
        return df
    else:
        print(f"Request failed with status code {response.status_code}")
        return None

## 1. KZN Franchisor
df_kzn = get_franchisee_data("5a6b40ec-1e4f-eb11-8345-00155d326100")
## 2. KZN Franchisor
df_KET = get_franchisee_data("3ed99252-d216-ec11-834c-00155d326100")
## 3. Lesedi_Solar
df_Lesedi_Solar = get_franchisee_data("e7b9933d-da35-ed11-8351-00155d326100")
## 4. Letsatsi Solar
df_Letsatsi_Solar = get_franchisee_data("e7b9933d-da35-ed11-8351-00155d326100")
## 5. PPTrust
df_PPTrust = get_franchisee_data("90b04590-6c96-ed11-8356-00155d326100")
## 6. ELRU-NW
df_ELRU_NW = get_franchisee_data("6289ad3f-e278-e611-80c7-0050568109d5")
## 6 GP Branch
df_GP_Branch  = get_franchisee_data("6a89ad3f-e278-e611-80c7-0050568109d5")
## 7 Khululeka
df_Khululeka  = get_franchisee_data("6c89ad3f-e278-e611-80c7-0050568109d5")
## 8 LETCEE
df_LETCEE  = get_franchisee_data("6e89ad3f-e278-e611-80c7-0050568109d5")
## 9 TREE
df_TREE  = get_franchisee_data("7089ad3f-e278-e611-80c7-0050568109d5")
## 10 Siyakholwa
df_Siyakholwa	=	get_franchisee_data('4b16de13-e386-e611-80ca-0050568109d5')
## 11 SAYM
df_SAYM	=	get_franchisee_data('474b1eed-e486-e611-80ca-0050568109d5')
## 12 Diaconia
df_Diaconia	=	get_franchisee_data('cb6f6d1a-e686-e611-80ca-0050568109d5')
## 13 LIMA
df_LIMA	=	get_franchisee_data('f3e19b66-e786-e611-80ca-0050568109d5')
## 14 ELRU
df_ELRU	=	get_franchisee_data('20b4261f-e886-e611-80ca-0050568109d5')
## 15 Lesedi_Educare_Association
df_Lesedi_Educare_Association	=	get_franchisee_data('7911a744-4584-e811-817d-0800274bb0e4')
## 16 3L_Development
df_3L_Development	=	get_franchisee_data('812aa76c-4584-e811-817d-0800274bb0e4')
## 17 df_Molteno
df_Molteno	=	get_franchisee_data('9093d385-4584-e811-817d-0800274bb0e4')
## 18 df_Penreach
df_Penreach	=	get_franchisee_data('0804f6ac-4584-e811-817d-0800274bb0e4')

#################### INACTIVE CHILDREN############################################

def get_franchisee_data(franchisor_value):
    url = "https://api.smartstart.org.za/v1/Child/Query/"
    payload = json.dumps({
      "Columns": [
        "Guid",
        "FullName",
        "StartDate",
        "InactiveDate",
        "Status"
      ],
      "Conditions": [
        {
          "Column": "Status",
          "Operator": "Equals",
          "Value": "Inactive"
        }
      ],
      "Related": [
        {
          "RelatedBy": "Franchisee",
          "Columns": [
            "FullName",
            "IdNumber",
            "Province",
            "ProgrammeType"
          ],
          "Conditions": [
            {
              "Column": "Franchisor",
              "Operator": "Equals",
              "Value": franchisor_value
            }
          ]
        }
      ]
    })
    headers = {
      'Content-Type': 'application/json',
      'API-Key': '4369C387-DAB7-418A-A623-00B91753D0C3'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    if response.status_code == 200:
        json_data = response.json()
        df = pd.json_normalize(json_data)
        return df
    else:
        print(f"Request failed with status code {response.status_code}")
        return None

## 1. KZN Franchisor
df_kzn_inactive = get_franchisee_data("5a6b40ec-1e4f-eb11-8345-00155d326100")
## 2. KZN Franchisor
df_KET_inactive = get_franchisee_data("3ed99252-d216-ec11-834c-00155d326100")
## 3. Lesedi_Solar
df_Lesedi_Solar_inactive = get_franchisee_data("e7b9933d-da35-ed11-8351-00155d326100")
## 4. Letsatsi Solar
df_Letsatsi_Solar_inactive = get_franchisee_data("e7b9933d-da35-ed11-8351-00155d326100")
## 5. PPTrust
df_PPTrust_inactive = get_franchisee_data("90b04590-6c96-ed11-8356-00155d326100")
## 6. ELRU-NW
df_ELRU_NW_inactive = get_franchisee_data("6289ad3f-e278-e611-80c7-0050568109d5")
## 6 GP Branch
df_GP_Branch_inactive  = get_franchisee_data("6a89ad3f-e278-e611-80c7-0050568109d5")
## 7 Khululeka
df_Khululeka_inactive  = get_franchisee_data("6c89ad3f-e278-e611-80c7-0050568109d5")
## 8 LETCEE
df_LETCEE_inactive  = get_franchisee_data("6e89ad3f-e278-e611-80c7-0050568109d5")
## 9 TREE
df_TREE_inactive  = get_franchisee_data("7089ad3f-e278-e611-80c7-0050568109d5")
## 10 Siyakholwa
df_Siyakholwa_inactive	=	get_franchisee_data('4b16de13-e386-e611-80ca-0050568109d5')
## 11 SAYM
df_SAYM_inactive	=	get_franchisee_data('474b1eed-e486-e611-80ca-0050568109d5')
## 12 Diaconia
df_Diaconia_inactive	=	get_franchisee_data('cb6f6d1a-e686-e611-80ca-0050568109d5')
## 13 LIMA
df_LIMA_inactive	=	get_franchisee_data('f3e19b66-e786-e611-80ca-0050568109d5')
## 14 ELRU
df_ELRU_inactive	=	get_franchisee_data('20b4261f-e886-e611-80ca-0050568109d5')
## 15 Lesedi_Educare_Association
df_Lesedi_Educare_Association_inactive	=	get_franchisee_data('7911a744-4584-e811-817d-0800274bb0e4')
## 16 3L_Development
df_3L_Development_inactive	=	get_franchisee_data('812aa76c-4584-e811-817d-0800274bb0e4')
## 17 df_Molteno
df_Molteno_inactive	=	get_franchisee_data('9093d385-4584-e811-817d-0800274bb0e4')
## 18 df_Penreach
df_Penreach_inactive	=	get_franchisee_data('0804f6ac-4584-e811-817d-0800274bb0e4')

# Show the dataframes
frames = [df_kzn, df_KET, df_Lesedi_Solar, df_Letsatsi_Solar, df_PPTrust, df_ELRU_NW, df_GP_Branch, df_Khululeka, df_LETCEE, df_TREE, df_Siyakholwa, df_SAYM, df_Diaconia, df_LIMA, df_ELRU, df_Lesedi_Educare_Association, df_3L_Development, df_Molteno, df_Penreach, df_kzn_inactive, df_KET_inactive, df_Lesedi_Solar_inactive, df_Letsatsi_Solar_inactive, df_PPTrust_inactive, df_ELRU_NW_inactive, df_GP_Branch_inactive, df_Khululeka_inactive, df_TREE_inactive, df_Siyakholwa_inactive, df_SAYM_inactive, df_Diaconia_inactive, df_LIMA_inactive, df_ELRU_inactive, df_Lesedi_Educare_Association_inactive, df_3L_Development_inactive, df_Molteno_inactive, df_Penreach_inactive]
# Concatenate the dataframes
data = pd.concat(frames)
# Save the data into a csv file.
data.to_csv("C:/Users/LazolaJavu/SmartStart/Rabelani Tshidavhu - Child Modelling update_2022/Child Modelling Project/Model Predictions/Time-Series-Forecasting/children_data.csv")
data.to_csv("C:/Users/LazolaJavu/SmartStart/Rabelani Tshidavhu - Child Modelling update_2022/Child Modelling Project/Model Predictions/Time-Series-Forecasting/Data/raw/children_data.csv")


import requests
import json
import pandas as pd
################################### Active FRANCHISEES ####################
url = "https://api.smartstart.org.za/v1/Franchisee/Query"

payload = json.dumps({
  "Columns": [
    "Guid",
    "FullName",
    "IdNumber",
    "PersonalNumber",
    "BirthDate",
    "CountryOfCitizenship",
    "Age",
    "InactivityComments",
    "MonthsSinceFranchisee",
    "IsSouthAfricanCitizen",
    "VerifiedByHomeAffairs",
    "AttendedChildProgress",
    "AttendedBusinessSkills",
    "IsClubLeader",
    "StartDate",
    "InactiveDate",
    "Status",
    "Gender",
    "ProgrammeType",
    "EthnicGroup",
    "Province",
    "ReasonForLeaving",
    "Franchisor",
    "Coach",
    "Principal"
  ],
  "Conditions": [
    {
      "Column": "Status",
      "Operator": "Equals",
      "Value": "Active"
    }
  ],
  "Related": [
    {
      "RelatedBy": "SiteAddress",
      "JoinType": "Outer",
      "Columns": [
        "Municipality",
        "Name",
        "PostalCode",
        "Ward",
        "Area",
        "StreetAddress",
        "SharedFullAddress",
        "Latitude",
        "Longitude",
        "SharedLatitude",
        "SharedLongitude"
      ]
    }
  ]
})
headers = {
  'Content-Type': 'application/json',
  'API-Key': '4369C387-DAB7-418A-A623-00B91753D0C3'
}

response = requests.request("GET", url, headers=headers, data=payload)

if response.status_code == 200:
    data = response.json()
    # Print only the first franchisees
    print(data[1])
else:
    print(f"Request failed with status code {response.status_code}")
# Assuming the JSON data is stored in text
json_data = json.loads(response.text)

# Convert the JSON data to a dataframe
df_active = pd.json_normalize(json_data)

################################### INACTIVE FRANCHISEES ####################

url = "https://api.smartstart.org.za/v1/Franchisee/Query"

payload = json.dumps({
  "Columns": [
    "Guid",
    "FullName",
    "IdNumber",
    "PersonalNumber",
    "BirthDate",
    "CountryOfCitizenship",
    "Age",
    "InactivityComments",
    "MonthsSinceFranchisee",
    "IsSouthAfricanCitizen",
    "VerifiedByHomeAffairs",
    "AttendedChildProgress",
    "AttendedBusinessSkills",
    "IsClubLeader",
    "StartDate",
    "InactiveDate",
    "Status",
    "Gender",
    "ProgrammeType",
    "EthnicGroup",
    "Province",
    "ReasonForLeaving",
    "Franchisor",
    "Coach",
    "Principal"
  ],
  "Conditions": [
    {
      "Column": "Status",
      "Operator": "Equals",
      "Value": "Inactive"
    }
  ],
  "Related": [
    {
      "RelatedBy": "SiteAddress",
      "JoinType": "Outer",
      "Columns": [
        "Municipality",
        "Name",
        "PostalCode",
        "Ward",
        "Area",
        "StreetAddress",
        "SharedFullAddress",
        "Latitude",
        "Longitude",
        "SharedLatitude",
        "SharedLongitude"
      ]
    }
  ]
})
headers = {
  'Content-Type': 'application/json',
  'API-Key': '4369C387-DAB7-418A-A623-00B91753D0C3'
}

response = requests.request("GET", url, headers=headers, data=payload)

if response.status_code == 200:
    data = response.json()
    # Print only the first franchisees
    print(data[1])
else:
    print(f"Request failed with status code {response.status_code}")
# Assuming the JSON data is stored in text
json_data = json.loads(response.text)

# Convert the JSON data to a dataframe
df_inactive = pd.json_normalize(json_data)
# Collect the dataframes into a list that will be concatenated

###################### COACH DATA ACTIVE##################################

url = "https://api.smartstart.org.za/v1/Coach/Query"

payload = json.dumps({
  "Columns": [
    "FullName",
    "DateOfBirth",
    "AreaOfOperation",
    "Gender",
    "EthnicGroup",
    "WorkAddressProvince",
    "Franchisor",
    "Status"
  ],
  "Conditions": [
    {
      "Column": "Status",
      "Operator": "Equals",
      "Value": "Active"
    }
  ]
})
headers = {
  'Content-Type': 'application/json',
  'API-Key': '4369C387-DAB7-418A-A623-00B91753D0C3'
}

response = requests.request("GET", url, headers=headers, data=payload)

if response.status_code == 200:
    data = response.json()
    # Print only the first franchisees
    print(data[1])
else:
    print(f"Request failed with status code {response.status_code}")
# Assuming the JSON data is stored in text
json_data = json.loads(response.text)

# Convert the JSON data to a dataframe
df_coach = pd.json_normalize(json_data)

############################# INACTIVE COACHES ##########################

import requests
import json

url = "https://api.smartstart.org.za/v1/Coach/Query"

payload = json.dumps({
  "Columns": [
    "FullName",
    "DateOfBirth",
    "AreaOfOperation",
    "Gender",
    "EthnicGroup",
    "WorkAddressProvince",
    "Franchisor",
    "Status"
  ],
  "Conditions": [
    {
      "Column": "Status",
      "Operator": "Equals",
      "Value": "Inactive"
    }
  ]
})
headers = {
  'Content-Type': 'application/json',
  'API-Key': '4369C387-DAB7-418A-A623-00B91753D0C3'
}

response = requests.request("GET", url, headers=headers, data=payload)

if response.status_code == 200:
    data = response.json()
    # Print only the first franchisees
    print(data[1])
else:
    print(f"Request failed with status code {response.status_code}")

# Assuming the JSON data is stored in text
json_data = json.loads(response.text)

# Convert the JSON data to a dataframe
df_coach_inactive = pd.json_normalize(json_data)

###################################### ACTIVE FRANCHISOR ##################
import requests
import json

url = "https://api.smartstart.org.za/v1/Franchisor/Query"

payload = json.dumps({
  "Columns": [
    "Name"
  ],
  "Conditions": [
    {
      "Column": "Status",
      "Operator": "Equals",
      "Value": "Active"
    }
  ]
})
headers = {
  'Content-Type': 'application/json',
  'API-Key': '4369C387-DAB7-418A-A623-00B91753D0C3'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

# Assuming the JSON data is stored in text
json_data = json.loads(response.text)

# Convert the JSON data to a dataframe
df_franchisor = pd.json_normalize(json_data)

########################## CONCATENATE THE DATAFRAMES #################

# Collect the dataframes into a list that will be concatenated
frames_franchisees = [df_active, df_inactive]
frames_coach = [df_coach, df_coach_inactive]
# Create a concat the dataframes
df_franchisees = pd.concat(frames_franchisees)
df_coaches = pd.concat(frames_coach)

df1 = df_franchisees.copy()
df2 = df_coaches.copy()
df3 = df_franchisor.copy()

# merge the two DataFrames on 'guid' and 'franchisor.guid'
merged_df = pd.merge(df2, df3, left_on='Franchisor.Guid', right_on='Guid')
# Remove the columns 'Franchisor.Guid' and 'Guid_y'
merged_df = merged_df.drop(labels = ['Franchisor.Guid', 'Guid_y'], axis = 1)
merged_df.columns = ['Coach', 'DateOfBirth_Coach', 'AreaOfOperation_coach', 'Gender_coach', 'EthnicGroup_coach',
       'WorkAddressProvince_coach', 'Status_coach', 'Coach.Guid', 'Franchisor']
# merge the datasets
data = pd.merge(df1, merged_df, left_on='Coach.Guid', right_on='Coach.Guid')

data.to_csv('C:/Users/LazolaJavu/SmartStart/Rabelani Tshidavhu - Child Modelling update_2022/Child Modelling Project/Model Predictions/Time-Series-Forecasting/Data/raw/franchisee.csv')


# Import the packages
import pandas as pd
import numpy as np
import datetime
from datetime import date
# from fbprophet import Prophet
from functools import reduce
# from fbprophet.plot import plot_plotly, plot_components_plotly

start_date = datetime.date(2016, 1, 1)  # start date
end_date = datetime.date(2031, 12, 19)  # end date
num_days = (end_date - start_date).days + 1  # number of days between start and end dates

# create array of values
values = np.linspace(100, 100500, num_days)  # starting value of x and ending value of x_1
# create array of values
City_of_Johannesburg = np.linspace(332957, 332957, num_days)  # starting value of x and ending value of x_1
City_of_Cape_Town = np.linspace(169677, 169677, num_days)  # starting value of x and ending value of x_1
Polokwane = np.linspace(72052, 72052, num_days)  # starting value of x and ending value of x_1
Ekurhuleni = np.linspace(209777, 209777, num_days)  # starting value of x and ending value of x_1
City_of_Tshwane = np.linspace(158393, 158393, num_days)  # starting value of x and ending value of x_1
Bushbuckridge = np.linspace(40688, 40688, num_days)  # starting value of x and ending value of x_1
Ehlanzeni = np.linspace(116582, 116582, num_days)  # starting value of x and ending value of x_1
Bojanala = np.linspace(151168, 151168, num_days)  # starting value of x and ending value of x_1
Sedibeng = np.linspace(79595, 79595, num_days)  # starting value of x and ending value of x_1
Madibeng = np.linspace(54912, 54912, num_days)  # starting value of x and ending value of x_1
Collins_Chabane = np.linspace(50667, 50667, num_days)  # starting value of x and ending value of x_1
City_of_Mbombela = np.linspace(79542, 79542, num_days)  # starting value of x and ending value of x_1
Nyandeni = np.linspace(47504, 47504, num_days)  # starting value of x and ending value of x_1
Rustenburg = np.linspace(68991, 68991, num_days)  # starting value of x and ending value of x_1
Buffalo_City = np.linspace(72685, 72685, num_days)  # starting value of x and ending value of x_1
King_Sabata_Dalindyebo = np.linspace(59373, 59373, num_days)  # starting value of x and ending value of x_1
Nkomazi = np.linspace(53994, 53994, num_days)  # starting value of x and ending value of x_1
Emfuleni = np.linspace(62590, 62590, num_days)  # starting value of x and ending value of x_1
Nelson_Mandela_Bay = np.linspace(65905, 65905, num_days)  # starting value of x and ending value of x_1
Thembisile = np.linspace(50006, 50006, num_days)  # starting value of x and ending value of x_1
City_of_Matlosana = np.linspace(45887, 45887, num_days)  # starting value of x and ending value of x_1


# create array of dates
dates = [start_date + datetime.timedelta(days=i) for i in range(num_days)]

# create dataframe
data_muni_gap = pd.DataFrame({'date': dates, 'value': values, 'City of Johannesburg':City_of_Johannesburg,
                   'City of Cape Town':City_of_Cape_Town, 'Polokwane':Polokwane, 'Ekurhuleni':Ekurhuleni,
                   'City of Tshwane':City_of_Tshwane,'Bushbuckridge':Bushbuckridge,'Ehlanzeni':Ehlanzeni,'Bojanala':Bojanala,
                   'Sedibeng':Sedibeng,'Local Municipality of Madibeng':Madibeng,'Collins Chabane':Collins_Chabane,'City of Mbombela':City_of_Mbombela,
                   'Nyandeni':Nyandeni,'Rustenburg':Rustenburg,'Buffalo City':Buffalo_City,'King Sabata Dalindyebo':King_Sabata_Dalindyebo,
                   'Nkomazi':Nkomazi,'Emfuleni':Emfuleni,'Nelson Mandela Bay':Nelson_Mandela_Bay,'Thembisile':Thembisile, 'City of Matlosana':City_of_Matlosana})
# read_csv file:
data = pd.read_csv("C:/Users/LazolaJavu/SmartStart/Rabelani Tshidavhu - Child Modelling update_2022/Child Modelling Project/Model Predictions/Time-Series-Forecasting/Data/raw/children_data.csv")

data = data[['Guid', 'FullName', 'StartDate', 'InactiveDate', 'Status',
       'Franchisee.FullName', 'Franchisee.IdNumber', 'Franchisee.Province',
       'Franchisee.ProgrammeType', 'Franchisee.Guid']]

# convert the 'date' column to datetime
data['StartDate'] = pd.to_datetime(data['StartDate'], errors='coerce')

# convert the 'date' column to datetime
data['InactiveDate'] = pd.to_datetime(data['InactiveDate'], errors='coerce')

# Filter out any date after today
data = data[data['StartDate'] <= pd.to_datetime(date.today())]
# keep only dates after 2016.01.01
data = data[data['StartDate'] >= pd.to_datetime('2015-01-01')]

data_children = data.copy()

# read_csv file:
site_municipalities = pd.read_excel(r"C:/Users/LazolaJavu/SmartStart/Rabelani Tshidavhu - Child Modelling update_2022/Child Modelling Project/Model Predictions/Time-Series-Forecasting/Data/raw/Site Municipality.xlsx")

# read_csv file:
data_franchisee = pd.read_csv("C:/Users/LazolaJavu/SmartStart/Rabelani Tshidavhu - Child Modelling update_2022/Child Modelling Project/Model Predictions/Time-Series-Forecasting/Data/raw/franchisee.csv")

data_franchisee =data_franchisee[['Guid', 'FullName', 'IdNumber',
       'Gender', 'ProgrammeType', 'EthnicGroup', 'Province',
       'ReasonForLeaving', 'Principal', 'SiteAddress', 'Franchisor.Guid',
       'Coach.Guid', 'SiteAddress.Municipality',
       'Franchisor']]
# # Merge the excel file with the data we pulled from
merge_df = pd.merge(data_children, data_franchisee, left_on = 'Franchisee.IdNumber', right_on = 'IdNumber')
merge_df = pd.merge(merge_df, site_municipalities, left_on = 'Franchisee.IdNumber', right_on = 'ID Number')
# Data copy
data = merge_df.copy()
# select the franchisees that are active.
data_cpt_active = data[data['Status'] == 'Active']
# Use the province column to check the model performance by Province
data_cpt_muni = data_cpt_active[['StartDate','Site Municipality']]
# Now let us count the data of the site municipality
data_cpt_muni['Site Municipality'].value_counts().to_frame()

# Drop NaN values from the 'Site Municipality' column
data_cpt_active.dropna(subset=['Site Municipality'], inplace=True)

# Get unique values from the 'Site Municipality' column
unique_values = list(set(data_cpt_active['Site Municipality']))

print(unique_values)

municipality_list = unique_values

data_cpt_muni = data_cpt_muni.loc[data['Site Municipality'].isin(municipality_list)]
# A dummy variable is a binary variable that indicates whether a separate categorical variable takes on a specific value.
dummy = pd.get_dummies(data_cpt_muni['Site Municipality'])
# merge the datasets
data_cpt_muni = data_cpt_muni.merge(dummy, left_index=True, right_index=True)
# Change the column name
data_cpt_muni['id'] = data_cpt_muni['StartDate']
# Delete the column we don't need
del data_cpt_muni['StartDate']
# Reset the index
data_cpt_muni.set_index('id')
# Delete the column we don't need
del data_cpt_muni['Site Municipality']
# View the columns
municipality_list_2 = list(data_cpt_muni.columns)
# Create a copy of the data
df_grouped = data_cpt_muni.copy()
# Rearrange the columns from the dataframe
df_grouped = df_grouped[municipality_list_2]
df_grouped.reset_index()
# convert 'date' column to date format
df_grouped['id'] = pd.to_datetime(df_grouped['id'], errors='coerce')

# Convert start_date to datetime object
start_date = datetime.datetime.combine(datetime.date(2016, 1, 1), datetime.datetime.min.time())

end_date = datetime.datetime.now()

# Filter the DataFrame based on the date range
df_grouped = df_grouped[(df_grouped['id'] >= start_date) & (df_grouped['id'] <= end_date)]
# Define function to create time series
def create_time_series(data, column_name):
    data = data.sort_values(by='id')[['id', column_name]]
    data[column_name] = data[column_name].cumsum()
    data = data.rename(columns={'id': 'ds', column_name: 'y'})
    data = data.dropna().drop_duplicates(subset=['ds'])
    return data

# Apply function to create time series for selected cities
cities = municipality_list
df_grouped_basic = reduce(lambda left,right: pd.merge(left,right,on=['ds'], how='outer'), [create_time_series(data_cpt_muni, c) for c in cities])

# Rename the columns
df_grouped_basic.columns = ['ds'] + municipality_list


df_grouped_basic.to_csv("C:/Users/LazolaJavu/SmartStart/Rabelani Tshidavhu - Child Modelling update_2022/Child Modelling Project/Model Predictions/Time-Series-Forecasting/df_grouped_basic.csv")


import streamlit as st
import pandas as pd
import openpyxl
# import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from streamlit import components


import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from scipy.signal import savgol_filter
import base64
from io import BytesIO
import folium
from streamlit_folium import folium_static
import geopandas as gpd


# Libraries needed for the tutorial

import pandas as pd
import requests
import io

# Username of your GitHub account

username = 'lazola.javu@gmail.com'

# Personal Access Token (PAO) from your GitHub account

# token = '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'

token = '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'

########### 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 #################### Token doesn't expire

# Creates a re-usable session object with your creds in-built
github_session = requests.Session()
github_session.auth = (username, token)

url_4 = "https://raw.githubusercontent.com/LazolaJavu/Time-Series-Forecasting/main/Data/external/ECD_Data.csv?token=GHSAT0AAAAAACBIG46DYRXUHQIDWHOEL6B6ZEQEMQA"
ecd_census_data = github_session.get(url_4).content

# Reading the downloaded content and making it a pandas dataframe
ecd_census_data = pd.read_csv(io.StringIO(ecd_census_data.decode('utf-8')))
# Read the shape file
shape_file = gpd.read_file("C:/Users/LazolaJavu/SmartStart/Rabelani Tshidavhu - Child Modelling update_2022/Child Modelling Project/Model Predictions/Time-Series-Forecasting/Data/external/ne_10m_admin_1_states_provinces/ne_10m_admin_1_states_provinces.shp")
# Read the shape file
gdf = shape_file[shape_file['geonunit'] == 'South Africa']
# Read the children data
df = pd.read_csv('C:/Users/LazolaJavu/SmartStart/Rabelani Tshidavhu - Child Modelling update_2022/Child Modelling Project/Model Predictions/Time-Series-Forecasting/Data/raw/children_data.csv')
# Rename the column table
df['Province'] = df['Franchisee.Province']
# Group the data by province and count the values
province_counts = df['Province'].value_counts().reset_index()
province_counts.columns = ['Province', 'Counts']
merged_data = gdf.merge(province_counts, left_on='woe_name', right_on='Province', how='left')
# Copy the merged data
gdf = merged_data.copy()
# Save a csv file:
gdf.to_csv("C:/Users/LazolaJavu/SmartStart/Rabelani Tshidavhu - Child Modelling update_2022/Child Modelling Project/Model Predictions/Time-Series-Forecasting/Data/processed/gdf.csv")


# Import packages
import pandas as pd
from pandas_profiling import ProfileReport

import requests
import json
import pandas as pd

################################### Active FRANCHISEES ####################
url = "https://api.smartstart.org.za/v1/Franchisee/Query"

payload = json.dumps({
  "Columns": [
    "Guid",
    "FullName",
    "IdNumber",
    "PersonalNumber",
    "BirthDate",
    "CountryOfCitizenship",
    "Age",
    "InactivityComments",
    "MonthsSinceFranchisee",
    "IsSouthAfricanCitizen",
    "VerifiedByHomeAffairs",
    "AttendedChildProgress",
    "AttendedBusinessSkills",
    "IsClubLeader",
    "StartDate",
    "Status",
    "Gender",
    "ProgrammeType",
    "EthnicGroup",
    "Province",
    "ReasonForLeaving",
    "Franchisor",
    "Coach",
    "Principal"
  ],
  "Conditions": [
    {
      "Column": "Status",
      "Operator": "Equals",
      "Value": "Active"
    }
  ],
  "Related": [
    {
      "RelatedBy": "SiteAddress",
      "JoinType": "Outer",
      "Columns": [
        "Municipality",
        "Name",
        "PostalCode",
        "Ward",
        "Area",
        "StreetAddress",
        "SharedFullAddress",
        "Latitude",
        "Longitude",
        "SharedLatitude",
        "SharedLongitude"
      ]
    }
  ]
})
headers = {
  'Content-Type': 'application/json',
  'API-Key': '4369C387-DAB7-418A-A623-00B91753D0C3'
}

response = requests.request("GET", url, headers=headers, data=payload)

if response.status_code == 200:
    data = response.json()
    # Print only the first franchisees
    print(data[1])
else:
    print(f"Request failed with status code {response.status_code}")
# Assuming the JSON data is stored in text
json_data = json.loads(response.text)

# Convert the JSON data to a dataframe
df_active = pd.json_normalize(json_data)

################################### INACTIVE FRANCHISEES ####################

url = "https://api.smartstart.org.za/v1/Franchisee/Query"

payload = json.dumps({
  "Columns": [
    "Guid",
    "FullName",
    "IdNumber",
    "PersonalNumber",
    "BirthDate",
    "CountryOfCitizenship",
    "Age",
    "InactivityComments",
    "MonthsSinceFranchisee",
    "IsSouthAfricanCitizen",
    "VerifiedByHomeAffairs",
    "AttendedChildProgress",
    "AttendedBusinessSkills",
    "IsClubLeader",
    "StartDate",
    "Status",
    "Gender",
    "ProgrammeType",
    "EthnicGroup",
    "Province",
    "ReasonForLeaving",
    "Franchisor",
    "Coach",
    "Principal"
  ],
  "Conditions": [
    {
      "Column": "Status",
      "Operator": "Equals",
      "Value": "Inactive"
    }
  ],
  "Related": [
    {
      "RelatedBy": "SiteAddress",
      "JoinType": "Outer",
      "Columns": [
        "Municipality",
        "Name",
        "PostalCode",
        "Ward",
        "Area",
        "StreetAddress",
        "SharedFullAddress",
        "Latitude",
        "Longitude",
        "SharedLatitude",
        "SharedLongitude"
      ]
    }
  ]
})
headers = {
  'Content-Type': 'application/json',
  'API-Key': '4369C387-DAB7-418A-A623-00B91753D0C3'
}

response = requests.request("GET", url, headers=headers, data=payload)

if response.status_code == 200:
    data = response.json()
    # Print only the first franchisees
    print(data[1])
else:
    print(f"Request failed with status code {response.status_code}")
# Assuming the JSON data is stored in text
json_data = json.loads(response.text)

# Convert the JSON data to a dataframe
df_inactive = pd.json_normalize(json_data)
# Collect the dataframes into a list that will be concatenated

###################### COACH DATA ACTIVE##################################

url = "https://api.smartstart.org.za/v1/Coach/Query"

payload = json.dumps({
  "Columns": [
    "FullName",
    "DateOfBirth",
    "AreaOfOperation",
    "Gender",
    "EthnicGroup",
    "WorkAddressProvince",
    "Franchisor",
    "Status"
  ],
  "Conditions": [
    {
      "Column": "Status",
      "Operator": "Equals",
      "Value": "Active"
    }
  ]
})
headers = {
  'Content-Type': 'application/json',
  'API-Key': '4369C387-DAB7-418A-A623-00B91753D0C3'
}

response = requests.request("GET", url, headers=headers, data=payload)

if response.status_code == 200:
    data = response.json()
    # Print only the first franchisees
    print(data[1])
else:
    print(f"Request failed with status code {response.status_code}")
# Assuming the JSON data is stored in text
json_data = json.loads(response.text)

# Convert the JSON data to a dataframe
df_coach = pd.json_normalize(json_data)

############################# INACTIVE COACHES ##########################


url = "https://api.smartstart.org.za/v1/Coach/Query"

payload = json.dumps({
  "Columns": [
    "FullName",
    "DateOfBirth",
    "AreaOfOperation",
    "Gender",
    "EthnicGroup",
    "WorkAddressProvince",
    "Franchisor",
    "Status"
  ],
  "Conditions": [
    {
      "Column": "Status",
      "Operator": "Equals",
      "Value": "Inactive"
    }
  ]
})
headers = {
  'Content-Type': 'application/json',
  'API-Key': '4369C387-DAB7-418A-A623-00B91753D0C3'
}

response = requests.request("GET", url, headers=headers, data=payload)

if response.status_code == 200:
    data = response.json()
    # Print only the first franchisees
    print(data[1])
else:
    print(f"Request failed with status code {response.status_code}")

# Assuming the JSON data is stored in text
json_data = json.loads(response.text)

# Convert the JSON data to a dataframe
df_coach_inactive = pd.json_normalize(json_data)

###################################### ACTIVE FRANCHISOR ##################
import requests
import json

url = "https://api.smartstart.org.za/v1/Franchisor/Query"

payload = json.dumps({
  "Columns": [
    "Name"
  ],
  "Conditions": [
    {
      "Column": "Status",
      "Operator": "Equals",
      "Value": "Active"
    }
  ]
})
headers = {
  'Content-Type': 'application/json',
  'API-Key': '4369C387-DAB7-418A-A623-00B91753D0C3'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

# Assuming the JSON data is stored in text
json_data = json.loads(response.text)

# Convert the JSON data to a dataframe
df_franchisor = pd.json_normalize(json_data)

########################## CONCATENATE THE DATAFRAMES #################

# Collect the dataframes into a list that will be concatenated
frames_franchisees = [df_active, df_inactive]
frames_coach = [df_coach, df_coach_inactive]
# Create a concat the dataframes
df_franchisees = pd.concat(frames_franchisees)
df_coaches = pd.concat(frames_coach)

df1 = df_franchisees.copy()
df2 = df_coaches.copy()
df3 = df_franchisor.copy()

# merge the two DataFrames on 'guid' and 'franchisor.guid'
merged_df = pd.merge(df2, df3, left_on='Franchisor.Guid', right_on='Guid')
# Remove the columns 'Franchisor.Guid' and 'Guid_y'
merged_df = merged_df.drop(labels = ['Franchisor.Guid', 'Guid_y'], axis = 1)
merged_df.columns = ['Coach', 'DateOfBirth_Coach', 'AreaOfOperation_coach', 'Gender_coach', 'EthnicGroup_coach',
       'WorkAddressProvince_coach', 'Status_coach', 'Coach.Guid', 'Franchisor']
# merge the datasets
data = pd.merge(df1, merged_df, left_on='Coach.Guid', right_on='Coach.Guid')

print(data.shape)
# Create the Profile Report
profile = ProfileReport(data, title = "SmartStart Franchisees EDA")
# Save as an html file
profile.to_file("C:/Users/LazolaJavu/OneDrive - SmartStart/Desktop/Data-Science-Notes/data/franchisee_report.html")

###########################################################################################################################

################################### GET CHILDREN DATA #######################################
def get_franchisee_data(franchisor_value):

    url = "https://api.smartstart.org.za/v1/Child/Query/"

    payload = json.dumps({
      "Columns": ["Guid",
    "FullName",
    "FirstName",
    "Surname",
    "IdNumber",
    "AllergyType",
    "DisabilityType",
    "HealthConditions",
    "EmergencyContactNumber",
    "EmergencyContactFullName",
    "EmergencyContactFirstName",
    "EmergencyContactSurname",
    "AlternativePickupFirstName",
    "AlternativePickupSurname",
    "AlternativePickupContactNumber",
    "BirthDate",
    "StartDate",
    "HasAllergy",
    "HasDisability",
    "CaregiverPopiaConsent",
    "CaregiverPhotographyAndFilmingConsent",
    "IsSouthAfricanCitizen",
    "HasIdNumber",
    "Gender",
    "EthnicGroup",
    "HomeLanguage",
    "GrantType",
    "PlaygroupGroup",
    "InactiveReason",
    "Franchisee",
    "Caregiver",
    "Status"
      ],
      "Conditions": [
        {
          "Column": "Status",
          "Operator": "Equals",
          "Value": "Active"
        }
      ],
      "Related": [
        {
          "RelatedBy": "Franchisee",
          "Columns": [
            "FullName",
            "IdNumber",
            "Province",
            "ProgrammeType"
          ],
          "Conditions": [
            {
              "Column": "Franchisor",
              "Operator": "Equals",
              "Value": franchisor_value
            }
          ]
        }
      ]
    })
    headers = {
      'Content-Type': 'application/json',
      'API-Key': '4369C387-DAB7-418A-A623-00B91753D0C3'
    }

    response = requests.request("GET", url, headers=headers, data=payload)


    if response.status_code == 200:
        json_data = response.json()
        df = pd.json_normalize(json_data)
        return df
    else:
        print(f"Request failed with status code {response.status_code}")
        return None

## 1. KZN Franchisor
df_kzn = get_franchisee_data("5a6b40ec-1e4f-eb11-8345-00155d326100")
## 2. KZN Franchisor
df_KET = get_franchisee_data("3ed99252-d216-ec11-834c-00155d326100")
## 3. Lesedi_Solar
df_Lesedi_Solar = get_franchisee_data("e7b9933d-da35-ed11-8351-00155d326100")
## 4. Letsatsi Solar
df_Letsatsi_Solar = get_franchisee_data("e7b9933d-da35-ed11-8351-00155d326100")
## 5. PPTrust
df_PPTrust = get_franchisee_data("90b04590-6c96-ed11-8356-00155d326100")
## 6. ELRU-NW
df_ELRU_NW = get_franchisee_data("6289ad3f-e278-e611-80c7-0050568109d5")
## 6 GP Branch
df_GP_Branch  = get_franchisee_data("6a89ad3f-e278-e611-80c7-0050568109d5")
## 7 Khululeka
df_Khululeka  = get_franchisee_data("6c89ad3f-e278-e611-80c7-0050568109d5")
## 8 LETCEE
df_LETCEE  = get_franchisee_data("6e89ad3f-e278-e611-80c7-0050568109d5")
## 9 TREE
df_TREE  = get_franchisee_data("7089ad3f-e278-e611-80c7-0050568109d5")
## 10 Siyakholwa
df_Siyakholwa	=	get_franchisee_data('4b16de13-e386-e611-80ca-0050568109d5')
## 11 SAYM
df_SAYM	=	get_franchisee_data('474b1eed-e486-e611-80ca-0050568109d5')
## 12 Diaconia
df_Diaconia	=	get_franchisee_data('cb6f6d1a-e686-e611-80ca-0050568109d5')
## 13 LIMA
df_LIMA	=	get_franchisee_data('f3e19b66-e786-e611-80ca-0050568109d5')
## 14 ELRU
df_ELRU	=	get_franchisee_data('20b4261f-e886-e611-80ca-0050568109d5')
## 15 Lesedi_Educare_Association
df_Lesedi_Educare_Association	=	get_franchisee_data('7911a744-4584-e811-817d-0800274bb0e4')
## 16 3L_Development
df_3L_Development	=	get_franchisee_data('812aa76c-4584-e811-817d-0800274bb0e4')
## 17 df_Molteno
df_Molteno	=	get_franchisee_data('9093d385-4584-e811-817d-0800274bb0e4')
## 18 df_Penreach
df_Penreach	=	get_franchisee_data('0804f6ac-4584-e811-817d-0800274bb0e4')



def get_franchisee_data(franchisor_value):

    url = "https://api.smartstart.org.za/v1/Child/Query/"

    payload = json.dumps({
      "Columns": ["Guid",
    "FullName",
    "FirstName",
    "Surname",
    "IdNumber",
    "AllergyType",
    "DisabilityType",
    "HealthConditions",
    "EmergencyContactNumber",
    "EmergencyContactFullName",
    "EmergencyContactFirstName",
    "EmergencyContactSurname",
    "AlternativePickupFirstName",
    "AlternativePickupSurname",
    "AlternativePickupContactNumber",
    "BirthDate",
    "StartDate",
    "HasAllergy",
    "HasDisability",
    "CaregiverPopiaConsent",
    "CaregiverPhotographyAndFilmingConsent",
    "IsSouthAfricanCitizen",
    "HasIdNumber",
    "Gender",
    "EthnicGroup",
    "HomeLanguage",
    "GrantType",
    "PlaygroupGroup",
    "InactiveReason",
    "Franchisee",
    "Caregiver",
    "Status"
      ],
      "Conditions": [
        {
          "Column": "Status",
          "Operator": "Equals",
          "Value": "Inactive"
        }
      ],
      "Related": [
        {
          "RelatedBy": "Franchisee",
          "Columns": [
            "FullName",
            "IdNumber",
            "Province",
            "ProgrammeType"
          ],
          "Conditions": [
            {
              "Column": "Franchisor",
              "Operator": "Equals",
              "Value": franchisor_value
            }
          ]
        }
      ]
    })
    headers = {
      'Content-Type': 'application/json',
      'API-Key': '4369C387-DAB7-418A-A623-00B91753D0C3'
    }

    response = requests.request("GET", url, headers=headers, data=payload)


    if response.status_code == 200:
        json_data = response.json()
        df = pd.json_normalize(json_data)
        return df
    else:
        print(f"Request failed with status code {response.status_code}")
        return None

## 1. KZN Franchisor
df_kzn_inactive = get_franchisee_data("5a6b40ec-1e4f-eb11-8345-00155d326100")
## 2. KZN Franchisor
df_KET_inactive = get_franchisee_data("3ed99252-d216-ec11-834c-00155d326100")
## 3. Lesedi_Solar
df_Lesedi_Solar_inactive = get_franchisee_data("e7b9933d-da35-ed11-8351-00155d326100")
## 4. Letsatsi Solar
df_Letsatsi_Solar_inactive = get_franchisee_data("e7b9933d-da35-ed11-8351-00155d326100")
## 5. PPTrust
df_PPTrust_inactive = get_franchisee_data("90b04590-6c96-ed11-8356-00155d326100")
## 6. ELRU-NW
df_ELRU_NW_inactive = get_franchisee_data("6289ad3f-e278-e611-80c7-0050568109d5")
## 6 GP Branch
df_GP_Branch_inactive  = get_franchisee_data("6a89ad3f-e278-e611-80c7-0050568109d5")
## 7 Khululeka
df_Khululeka_inactive  = get_franchisee_data("6c89ad3f-e278-e611-80c7-0050568109d5")
## 8 LETCEE
df_LETCEE_inactive  = get_franchisee_data("6e89ad3f-e278-e611-80c7-0050568109d5")
## 9 TREE
df_TREE_inactive  = get_franchisee_data("7089ad3f-e278-e611-80c7-0050568109d5")
## 10 Siyakholwa
df_Siyakholwa_inactive	=	get_franchisee_data('4b16de13-e386-e611-80ca-0050568109d5')
## 11 SAYM
df_SAYM_inactive	=	get_franchisee_data('474b1eed-e486-e611-80ca-0050568109d5')
## 12 Diaconia
df_Diaconia_inactive	=	get_franchisee_data('cb6f6d1a-e686-e611-80ca-0050568109d5')
## 13 LIMA
df_LIMA_inactive	=	get_franchisee_data('f3e19b66-e786-e611-80ca-0050568109d5')
## 14 ELRU
df_ELRU_inactive	=	get_franchisee_data('20b4261f-e886-e611-80ca-0050568109d5')
## 15 Lesedi_Educare_Association
df_Lesedi_Educare_Association_inactive	=	get_franchisee_data('7911a744-4584-e811-817d-0800274bb0e4')
## 16 3L_Development
df_3L_Development_inactive	=	get_franchisee_data('812aa76c-4584-e811-817d-0800274bb0e4')
## 17 df_Molteno
df_Molteno_inactive	=	get_franchisee_data('9093d385-4584-e811-817d-0800274bb0e4')
## 18 df_Penreach
df_Penreach_inactive	=	get_franchisee_data('0804f6ac-4584-e811-817d-0800274bb0e4')

# Show the dataframes
frames = [df_kzn, df_KET, df_Lesedi_Solar, df_Letsatsi_Solar, df_PPTrust, df_ELRU_NW, df_GP_Branch, df_Khululeka, df_LETCEE, df_TREE, df_Siyakholwa, df_SAYM, df_Diaconia, df_LIMA, df_ELRU, df_Lesedi_Educare_Association, df_3L_Development, df_Molteno, df_Penreach, df_kzn_inactive, df_KET_inactive, df_Lesedi_Solar_inactive, df_Letsatsi_Solar_inactive, df_PPTrust_inactive, df_ELRU_NW_inactive, df_GP_Branch_inactive, df_Khululeka_inactive, df_TREE_inactive, df_Siyakholwa_inactive, df_SAYM_inactive, df_Diaconia_inactive, df_LIMA_inactive, df_ELRU_inactive, df_Lesedi_Educare_Association_inactive, df_3L_Development_inactive, df_Molteno_inactive, df_Penreach_inactive]
# Concatenate the dataframes
data = pd.concat(frames)

profile = ProfileReport(data, minimal=True)
profile.to_file(output_file="C:/Users/LazolaJavu/OneDrive - SmartStart/Desktop/Data-Science-Notes/data/Children_report_report.html")


# Import the packages
import pandas as pd
import datetime
from datetime import date
import pytz

# read_csv file:
data = pd.read_csv("C:/Users/LazolaJavu/SmartStart/Rabelani Tshidavhu - Child Modelling update_2022/Child Modelling Project\Model Predictions/Time-Series-Forecasting/Data/raw/children_data.csv")

# convert the 'date' column to datetime
data['Start Date'] = pd.to_datetime(data['StartDate'], errors='coerce')
del data['StartDate']

# convert the 'date' column to datetime
data['InactiveDate'] = pd.to_datetime(data['InactiveDate'], errors='coerce')

# Use the Modality column to check the model performance by Modality
data_mod = data[['Start Date','Franchisee.ProgrammeType']]
# A dummy variable is a binary variable that indicates whether a separate categorical variable takes on a specific value.
dummy = pd.get_dummies(data_mod['Franchisee.ProgrammeType'])
# A dummy variable is a binary variable that indicates whether a separate categorical variable takes on a specific value.
dummy = pd.get_dummies(data_mod['Franchisee.ProgrammeType'])
data_mod = data_mod.merge(dummy, left_index=True, right_index=True)
# Change the column name
data_mod['id'] = data_mod['Start Date']
# Delete the column we don't need
del data_mod['Start Date']
# Reset the index
data_mod.set_index('id')
# Delete the column we don't need
del data_mod['Franchisee.ProgrammeType']
# Rearrange the columns from the dataframe
data_mod_active = data_mod[['id', 'ECD Centre', 'Full Week (Daymothers)', 'Playgroup', 'SmartStart ECD']]
# Use the Modality column to check the model performance by Modality
data_mod = data[['InactiveDate','Franchisee.ProgrammeType']]
# A dummy variable is a binary variable that indicates whether a separate categorical variable takes on a specific value.
dummy = pd.get_dummies(data_mod['Franchisee.ProgrammeType'])
# A dummy variable is a binary variable that indicates whether a separate categorical variable takes on a specific value.
dummy = pd.get_dummies(data_mod['Franchisee.ProgrammeType'])
data_mod = data_mod.merge(dummy, left_index=True, right_index=True)
# Change the column name
data_mod['id'] = data_mod['InactiveDate']
# Delete the column we don't need
del data_mod['InactiveDate']
# Reset the index
data_mod.set_index('id')
# Delete the column we don't need
del data_mod['Franchisee.ProgrammeType']
# Rearrange the columns from the dataframe
data_mod_inactive = data_mod[['id', 'ECD Centre', 'Full Week (Daymothers)', 'Playgroup', 'SmartStart ECD']]
data_mod_inactive[['ECD Centre', 'Full Week (Daymothers)', 'Playgroup', 'SmartStart ECD']] *= -1

data_mod = pd.concat([data_mod_active, data_mod_inactive], axis=0)
data_mod = data_mod.sort_values(by='id')

# Filter out any date after today
data_mod = data_mod[data_mod['id'] <= pd.to_datetime(date.today())]
# keep only dates after 2016.01.01
data_mod = data_mod[data_mod['id'] >= pd.to_datetime('2015-01-01')]

# Create a function...
def create_time_series(data, column_name):
    data = data.sort_values(by='id')
    # There is an issue with the code dataframe above.
    # It shows the occurence per day, we want accumulated data.
    # The cumsum() function computes the values based on the previous one.
    data[column_name] = data[column_name].cumsum()
    # Selec the columns from the dataset
    data = data[['id', column_name]]
    # Assign the values for time for FBprophet
    data['ds'] = data['id']
    # Assign the value variable in FB Prophet
    data['y'] = data[column_name]
    # Select the needed varibales
    data = data[['ds', 'y']]
    # Drop rows with null values
    data = data.dropna(axis=0)
    data = data.drop_duplicates(subset=['ds'])
    return data

data_ecd = create_time_series(data_mod, 'ECD Centre')
data_daymother = create_time_series(data_mod, 'Full Week (Daymothers)')
data_playgroup = create_time_series(data_mod, 'Playgroup')
data_smartstart = create_time_series(data_mod, 'SmartStart ECD')

# Save as a dataframe into the base path
base_path = 'C:/Users/LazolaJavu/SmartStart/Rabelani Tshidavhu - Child Modelling update_2022/Child Modelling Project/Model Predictions/Time-Series-Forecasting/Data/interim'
# Saving the files as CSV
data_ecd.to_csv(base_path + '\data_ecd.csv')
data_daymother.to_csv(base_path + '/data_daymother.csv')
data_playgroup.to_csv(base_path + '/data_playgroup.csv')
data_smartstart.to_csv(base_path + '/data_smartstart.csv')

##################################################################### Franchisee #############################################################################################

# read_csv file:
data = pd.read_csv("C:/Users/LazolaJavu/SmartStart/Rabelani Tshidavhu - Child Modelling update_2022/Child Modelling Project\Model Predictions/Time-Series-Forecasting/Data/raw/franchisee.csv")

# convert the 'date' column to datetime
data['Start Date'] = pd.to_datetime(data['StartDate'], errors='coerce')
del data['StartDate']
# convert the 'date' column to datetime
data['InactiveDate'] = pd.to_datetime(data['InactiveDate'], errors='coerce')
# Use the Modality column to check the model performance by Modality
data_mod = data[['Start Date','ProgrammeType']]
# A dummy variable is a binary variable that indicates whether a separate categorical variable takes on a specific value.
dummy = pd.get_dummies(data_mod['ProgrammeType'])
# A dummy variable is a binary variable that indicates whether a separate categorical variable takes on a specific value.
dummy = pd.get_dummies(data_mod['ProgrammeType'])
data_mod = data_mod.merge(dummy, left_index=True, right_index=True)
# Change the column name
data_mod['id'] = data_mod['Start Date']
# Delete the column we don't need
del data_mod['Start Date']
# Reset the index
data_mod.set_index('id')
# Delete the column we don't need
del data_mod['ProgrammeType']
# Rearrange the columns from the dataframe
data_mod_active = data_mod[['id', 'ECD Centre', 'Full Week (Daymothers)', 'Playgroup', 'SmartStart ECD']]
# Use the Modality column to check the model performance by Modality
data_mod = data[['InactiveDate','ProgrammeType']]
# A dummy variable is a binary variable that indicates whether a separate categorical variable takes on a specific value.
dummy = pd.get_dummies(data_mod['ProgrammeType'])
# A dummy variable is a binary variable that indicates whether a separate categorical variable takes on a specific value.
dummy = pd.get_dummies(data_mod['ProgrammeType'])
data_mod = data_mod.merge(dummy, left_index=True, right_index=True)
# Change the column name
data_mod['id'] = data_mod['InactiveDate']
# Delete the column we don't need
del data_mod['InactiveDate']
# Reset the index
data_mod.set_index('id')
# Delete the column we don't need
del data_mod['ProgrammeType']
# Rearrange the columns from the dataframe
data_mod_inactive = data_mod[['id', 'ECD Centre', 'Full Week (Daymothers)', 'Playgroup', 'SmartStart ECD']]
data_mod_inactive[['ECD Centre', 'Full Week (Daymothers)', 'Playgroup', 'SmartStart ECD']] *= -1

data_mod = pd.concat([data_mod_active, data_mod_inactive], axis=0)
data_mod = data_mod.sort_values(by='id')

# Filter out any date after today
current_date = datetime.datetime.now(pytz.UTC).replace(hour=0, minute=0, second=0, microsecond=0)
data_mod = data_mod[data_mod['id'] <= current_date]
# keep only dates after 2016.01.01
data_mod = data_mod[data_mod['id'] >= pd.to_datetime('2015-01-01').tz_localize('UTC')]
data_mod['id'] = data_mod['id'].dt.strftime('%Y-%m-%d')
# Create a function...
def create_time_series(data, column_name):
    data = data.sort_values(by='id')
    # There is an issue with the code dataframe above.
    # It shows the occurence per day, we want accumulated data.
    # The cumsum() function computes the values based on the previous one.
    data[column_name] = data[column_name].cumsum()
    # Selec the columns from the dataset
    data = data[['id', column_name]]
    # Assign the values for time for FBprophet
    data['ds'] = data['id']
    # Assign the value variable in FB Prophet
    data['y'] = data[column_name]
    # Select the needed varibales
    data = data[['ds', 'y']]
    # Drop rows with null values
    data = data.dropna(axis=0)
    data = data.drop_duplicates(subset=['ds'])
    return data

data_ecd = create_time_series(data_mod, 'ECD Centre')
data_daymother = create_time_series(data_mod, 'Full Week (Daymothers)')
data_playgroup = create_time_series(data_mod, 'Playgroup')
data_smartstart = create_time_series(data_mod, 'SmartStart ECD')
# Save as a dataframe into the base path
base_path = 'C:/Users/LazolaJavu/SmartStart/Rabelani Tshidavhu - Child Modelling update_2022/Child Modelling Project/Model Predictions/Time-Series-Forecasting/Data/interim'
# Saving the files as CSV
data_ecd.to_csv(base_path + '\data_ecd_franchisees.csv')
data_daymother.to_csv(base_path + '/data_daymother_franchisees.csv')
data_playgroup.to_csv(base_path + '/data_playgroupdata_franchisees.csv')
data_smartstart.to_csv(base_path + '/data_smartstartdata_franchisees.csv')


# Import the packages
import pandas as pd
import datetime
from datetime import date
import pytz

# read_csv file:
data = pd.read_csv("C:/Users/LazolaJavu/SmartStart/Rabelani Tshidavhu - Child Modelling update_2022/Child Modelling Project\Model Predictions/Time-Series-Forecasting/Data/raw/children_data.csv")

# convert the 'date' column to datetime
data['StartDate'] = pd.to_datetime(data['StartDate'], errors='coerce')

# convert the 'date' column to datetime
data['InactiveDate'] = pd.to_datetime(data['InactiveDate'], errors='coerce')

# Filter out any date after today
data = data[data['StartDate'] <= pd.to_datetime(date.today())]
# keep only dates after 2016.01.01
data = data[data['StartDate'] >= pd.to_datetime('2015-01-01')]

# Create a new dataframe to evaluate the performance over time using
# Both active and inactive df
# Create a dataframe(s)
df_id = data[['InactiveDate', 'Franchisee.Province' ]]
df_sd = data[['StartDate', 'Franchisee.Province' ]]
# Get dummy variables for the two columns
dummy_sd = pd.get_dummies(df_sd['Franchisee.Province' ])
dummy_id = pd.get_dummies(df_id['Franchisee.Province' ])
# Merge the two dataframes
df_sd = df_sd.merge(dummy_sd, left_index=True, right_index=True)
df_id = df_id.merge(dummy_id, left_index=True, right_index=True)
# Change the column name
df_sd['id'] = df_sd['StartDate']
# Change the column name
df_id['id'] = df_id['InactiveDate']
# Drop the columns
df_sd = df_sd.drop(labels = ['StartDate', 'Franchisee.Province' ], axis =1)
df_id = df_id.drop(labels = ['InactiveDate', 'Franchisee.Province' ], axis=1)
# Drop the null values
df_id = df_id.dropna()
# Rearrange the columns
df_sd = df_sd[['id', 'Eastern Cape', 'Free State', 'Gauteng', 'KwaZulu-Natal', 'Limpopo',
       'Mpumalanga', 'North West', 'Northern Cape', 'Western Cape']]
df_id = df_id[['id', 'Eastern Cape', 'Free State', 'Gauteng', 'KwaZulu-Natal', 'Limpopo',
       'Mpumalanga', 'North West', 'Northern Cape', 'Western Cape']]
# Assign a negative on the inactive date
df_id[['Eastern Cape', 'Free State', 'Gauteng', 'KwaZulu-Natal', 'Limpopo',
       'Mpumalanga', 'North West', 'Northern Cape', 'Western Cape']] *= -1
# Concat the dataframes
frames = [df_sd, df_id]
df_prov = pd.concat(frames)
# Save the dataset
df_prov.to_csv('C:/Users/LazolaJavu/SmartStart/Rabelani Tshidavhu - Child Modelling update_2022/Child Modelling Project/Model Predictions/Time-Series-Forecasting/Data/interim/Provinces_SS.csv')

############################################################################## FRANCHISEES #################################################

# read_csv file:
data = pd.read_csv("C:/Users/LazolaJavu/SmartStart/Rabelani Tshidavhu - Child Modelling update_2022/Child Modelling Project\Model Predictions/Time-Series-Forecasting/Data/raw/franchisee.csv")
# convert the 'date' column to datetime
data['StartDate'] = pd.to_datetime(data['StartDate'], errors='coerce')
# convert the 'date' column to datetime
data['InactiveDate'] = pd.to_datetime(data['InactiveDate'], errors='coerce')
# Filter out any date after today
current_date = datetime.datetime.now(pytz.UTC).replace(hour=0, minute=0, second=0, microsecond=0)
data = data[data['StartDate'] <= current_date]
# keep only dates after 2016.01.01
data = data[data['StartDate'] >= pd.to_datetime('2015-01-01').tz_localize('UTC')]
data['StartDate'] = data['StartDate'].dt.strftime('%Y-%m-%d')
# Create a new dataframe to evaluate the performance over time using
# Both active and inactive df
# Create a dataframe(s)
df_id = data[['InactiveDate', 'Province' ]]
df_sd = data[['StartDate', 'Province' ]]
# Get dummy variables for the two columns
dummy_sd = pd.get_dummies(df_sd['Province' ])
dummy_id = pd.get_dummies(df_id['Province' ])
# Merge the two dataframes
df_sd = df_sd.merge(dummy_sd, left_index=True, right_index=True)
df_id = df_id.merge(dummy_id, left_index=True, right_index=True)
# Change the column name
df_sd['id'] = df_sd['StartDate']
# Change the column name
df_id['id'] = df_id['InactiveDate']
# Drop the columns
df_sd = df_sd.drop(labels = ['StartDate', 'Province' ], axis =1)
df_id = df_id.drop(labels = ['InactiveDate', 'Province' ], axis=1)
# Drop the null values
df_id = df_id.dropna()
# Rearrange the columns
df_sd = df_sd[['id', 'Eastern Cape', 'Free State', 'Gauteng', 'KwaZulu-Natal', 'Limpopo',
       'Mpumalanga', 'North West', 'Northern Cape', 'Western Cape']]
df_id = df_id[['id', 'Eastern Cape', 'Free State', 'Gauteng', 'KwaZulu-Natal', 'Limpopo',
       'Mpumalanga', 'North West', 'Northern Cape', 'Western Cape']]
# Assign a negative on the inactive date
df_id[['Eastern Cape', 'Free State', 'Gauteng', 'KwaZulu-Natal', 'Limpopo',
       'Mpumalanga', 'North West', 'Northern Cape', 'Western Cape']] *= -1
# Concat the dataframes
frames = [df_sd, df_id]
df_prov = pd.concat(frames)
# Save the dataset
df_prov.to_csv('C:/Users/LazolaJavu/SmartStart/Rabelani Tshidavhu - Child Modelling update_2022/Child Modelling Project/Model Predictions/Time-Series-Forecasting/Data/interim/Provinces_SS_franchisees.csv')


# Import the packages
import pandas as pd
import datetime
from datetime import date

########################################################################### CHILDREN DATA ##########################################################################

# read_csv file:
data = pd.read_csv("C:/Users/LazolaJavu/SmartStart/Rabelani Tshidavhu - Child Modelling update_2022/Child Modelling Project\Model Predictions/Time-Series-Forecasting/Data/raw/children_data.csv")

# Create a new dataframe to evaluate the performance over time using
# Both active and inactive df
df_startdate = data.groupby(['StartDate']).size().reset_index(name='counts')
# Dataframe with inactive franchisees
df_inactivedate = data.groupby(['InactiveDate']).size().reset_index(name='counts')
# Assign a negative variable inside a column
df_inactivedate['counts'] *= -1
# Add a column to the existing df
df_inactivedate['StartDate'] = df_inactivedate['InactiveDate']
# Delete inactive date
del df_inactivedate['InactiveDate']
# Change the way the dataframe looks like.
df_inactivedate = df_inactivedate[['StartDate', 'counts']]
# Add the two dataframes
df_dates = pd.concat([df_startdate, df_inactivedate], axis=0)
# Sort the values by the date of occurance
df_dates = df_dates.sort_values(by='StartDate')
# There is an issue with the code dataframe above.
# It shows the occurence per day, we want accumulated data.
# The cumsum() function computes the values based on the previous one.
df_dates['counts'] = df_dates['counts'].cumsum()
# Copy a dataframe
data = df_dates.copy()
# convert the 'date' column to datetime
data['Start Date'] = pd.to_datetime(data['StartDate'], errors='coerce')
del data['StartDate']
# Filter out any date after today
data = data[data['Start Date'] <= pd.to_datetime(date.today())]
# keep only dates after 2016.01.01
data = data[data['Start Date'] >= pd.to_datetime('2015-01-01')]
# Rearranged data
data = data[['Start Date', 'counts']]
# Save data as CSV
data.to_csv('C:/Users/LazolaJavu/SmartStart/Rabelani Tshidavhu - Child Modelling update_2022/Child Modelling Project/Model Predictions/Time-Series-Forecasting/Data/interim/Featured_children_data.csv')

################################################################# franchisees Data ##########################################################################################################

# read_csv file:
data = pd.read_csv("C:/Users/LazolaJavu/SmartStart/Rabelani Tshidavhu - Child Modelling update_2022/Child Modelling Project\Model Predictions/Time-Series-Forecasting/Data/raw/franchisee.csv")

# Create a new dataframe to evaluate the performance over time using
# Both active and inactive df
df_startdate = data.groupby(['StartDate']).size().reset_index(name='counts')
# Dataframe with inactive franchisees
df_inactivedate = data.groupby(['InactiveDate']).size().reset_index(name='counts')
# Assign a negative variable inside a column
df_inactivedate['counts'] *= -1
# Add a column to the existing df
df_inactivedate['StartDate'] = df_inactivedate['InactiveDate']
# Delete inactive date
del df_inactivedate['InactiveDate']
# Change the way the dataframe looks like.
df_inactivedate = df_inactivedate[['StartDate', 'counts']]
# Add the two dataframes
df_dates = pd.concat([df_startdate, df_inactivedate], axis=0)
# Sort the values by the date of occurance
df_dates = df_dates.sort_values(by='StartDate')
# There is an issue with the code dataframe above.
# It shows the occurence per day, we want accumulated data.
# The cumsum() function computes the values based on the previous one.
df_dates['counts'] = df_dates['counts'].cumsum()
# Convert the 'StartDate' column to datetime format
df_dates['StartDate'] = pd.to_datetime(df_dates['StartDate'], errors='coerce')

# Extract only the date portion from the 'StartDate' column
df_dates['StartDate'] = df_dates['StartDate'].dt.strftime('%Y-%m-%d')
# Copy a dataframe
data = df_dates.copy()
# convert the 'date' column to datetime
data['Start Date'] = pd.to_datetime(data['StartDate'], errors='coerce')
del data['StartDate']
# Filter out any date after today
data = data[data['Start Date'] <= pd.to_datetime(date.today())]
# keep only dates after 2016.01.01
data = data[data['Start Date'] >= pd.to_datetime('2015-01-01')]
# Rearranged data
data = data[['Start Date', 'counts']]
# Save data as CSV
data.to_csv('C:/Users/LazolaJavu/SmartStart/Rabelani Tshidavhu - Child Modelling update_2022/Child Modelling Project/Model Predictions/Time-Series-Forecasting/Data/interim/Featured_Franchisee_data.csv')
