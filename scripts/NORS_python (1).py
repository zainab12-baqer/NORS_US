%ls *.csv

df_nors=pd.read_csv('NORS_20250224.csv')

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_nors.info()

df_nors.head()

df_nors.isnull().sum()

rows,col = df_nors.shape

(df_nors.isnull().sum()/rows)*100

df_nors.describe()

df_nors.shape

df_nors.duplicated().sum()

df_filtered_years = df_nors[df_nors.Year >= 1998]
df_filtered_years

df_filtered_years.corr(numeric_only=True)

plt.figure(figsize=(12, 6))
sns.heatmap(df_filtered_years.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

df_filtered_years['Month'].unique()

df_filtered_years['Year'].unique()

df_year= df_filtered_years.groupby(['Year']).size().reset_index(name='Outbreak_Count')
df_year=df_year.sort_values(by='Outbreak_Count',ascending=False).head(10)
df_year

df_year.info()

df_year= df_filtered_years.groupby(['Year']).size().reset_index(name='Outbreak_Count')
plt.figure(figsize=(12, 6))
plt.plot(df_year['Year'], df_year['Outbreak_Count'],color='Brown')
plt.xlabel('Year')
plt.ylabel('Outbreak Count')
plt.title('Number of Outbreaks by Year')
plt.grid(axis='y', color='gray', linestyle='--', linewidth=0.3)

df_month= df_filtered_years.groupby(['Month']).size().reset_index(name='Outbreak_Count')
plt.figure(figsize=(12, 6))
plt.bar(df_month['Month'], df_month['Outbreak_Count'],color='brown')
plt.xlabel('Month')
plt.ylabel('Outbreak Count')
plt.title('Number of Outbreaks by Month')
plt.grid(axis='y', color='gray', linestyle='--', linewidth=0.3)

df_month

df_year_p=df_filtered_years.groupby(['Year','Primary Mode'])
df_year_p.count()

df_state_cases=df_filtered_years.groupby(['State']).size().reset_index(name='Highest number of Outbreak')
df_sort_state=df_state_cases.sort_values(by='Highest number of Outbreak',ascending=False).head(10)
plt.figure(figsize=(12, 6))
plt.bar(df_sort_state['State'], df_sort_state['Highest number of Outbreak'])
plt.xlabel('State')
plt.ylabel('Highest number of Outbreak')
plt.title('Highest number of Outbreak by State')
plt.grid(axis='y', color='gray', linestyle='--', linewidth=0.3)

df_sort_state

import folium
df_state_map = df_filtered_years.groupby(['State']).size().reset_index(name='Highest number of Outbreak')
df_state_map=us_state_map=folium.Map(location=[39.8283,-98.5795],zoom_start=4)
highest_number_of_outbreaks = [[ 27.6648, -81.5158],'Florida',
                              [38.6275278, -92.5665786],'Ohi',
                              [39.9526, -75.1652],'Califonia',
                              [40.7128, -74.0060],'pennsylvania',
                              [31.9686, -99.9018],'texas',
                              [38.9072, -77.0369],'washington',
                              [43.7001, -84.4278],'michigan',
                              [40.7128, -74.0060],'new york',
                              [44.9778, -93.2650],'minnesota',
                              [40.1833, -88.2500],'illinois']
for i in range(0, len(highest_number_of_outbreaks), 2):
    coordinates = highest_number_of_outbreaks[i]
    state_name = highest_number_of_outbreaks[i + 1]
    folium.Marker(
        location=coordinates,
        popup=folium.Popup(state_name, show=True),
        tooltip=state_name,
        icon=folium.Icon(icon="info-sign", color="green")
    ).add_to(us_state_map)
us_state_map

df_primary.replace('Environmental contamination other than food/water' ,'Environmental',inplace=True)

df_primary=df_filtered_years.groupby(['Primary Mode']).size().reset_index(name='Most Common Mode Of Transmission')
df_sort_primary=df_sort_primary.sort_values(by='Most Common Mode Of Transmission',ascending=False)
df_sort_primary.replace('Environmental contamination other than food/water' ,'Environmental',inplace=True)
plt.figure(figsize=(13, 6))
plt.barh(df_sort_primary['Primary Mode'],df_sort_primary['Most Common Mode Of Transmission'])
plt.xlabel('Most Common Mode Of Transmission')
plt.ylabel('Primary Mode')
plt.title('Most Common Mode Of Transmission')
plt.grid(axis='y', color='gray', linestyle='--', linewidth=0.3)

df_sort_primary

df_mode=df_filtered_years.groupby(['Etiology','Year'])

df_filtered_years.replace('Norovirus Genogroup II' ,'Norovirus',inplace=True)
df_filtered_years.replace('Norovirus unknown' ,'Norovirus',inplace=True)
df_filtered_years.replace('Norovirus Genogroup I' ,'Norovirus',inplace=True)

df_mode.sort_values(by='Most Common Causes')

Bahrain_data = df[(df['Entity'] == 'Bahrain')]
Qatar_data = df[(df['Entity'] == 'Qatar')]
plt.figure(figsize=(10, 6))
plt.plot(Bahrain_data['Year'],Bahrain_data['it_net_user_zs'],color = 'green',label='Bahrain')
plt.plot(Qatar_data ['Year'],Qatar_data['it_net_user_zs'],color='blue',label='Qatar')
plt.xlabel('Year')
plt.ylabel('% of Population')
plt.grid(axis='y', color='gray', linestyle='--', linewidth=0.3)
plt.legend()

df_mode=df_filtered_years.groupby(['Etiology'])
df_filtered_years['Etiology'].value_counts().head(3).plot(kind='line', figsize=(12, 6))
plt.xlabel('Count')
plt.ylabel('Etiology')
plt.title('Top 10 Most Common Causes')
plt.grid(axis='y', color='gray', linestyle='--', linewidth=0.3)

df_mode=df_filtered_years.groupby(['Etiology','Year']).size().reset_index(name='Most Common Causes') 
Norovirus_data = df_mode[(df_mode['Etiology'] == 'Norovirus')]  
Salmonella_enterica_data = df_mode[(df_mode['Etiology'] == 'Salmonella enterica')]
Escherichia_Shiga_data = df_mode[(df_mode['Etiology'] == 'Escherichia coli, Shiga toxin-producing')]
plt.figure(figsize=(12, 6))
plt.plot(Norovirus_data['Year'], Norovirus_data['Most Common Causes'], color='green', label='Norovirus')
plt.plot(Salmonella_enterica_data['Year'], Salmonella_enterica_data['Most Common Causes'], color='blue', label='Salmonella enterica')
plt.plot(Escherichia_Shiga_data['Year'], Escherichia_Shiga_data['Most Common Causes'], color='red', label='Escherichia coli, Shiga toxin-producing')
plt.xlabel('Year')
plt.ylabel('Etiology')
plt.grid(axis='y', color='gray', linestyle='--', linewidth=0.3)
plt.legend()

df_relationship=df_filtered_years.groupby(['Hospitalizations','Deaths','Year']).size().reset_index(name='Relationship')
df_relationship

df_relationship=df_filtered_years.groupby(['Hospitalizations','Deaths','Year']).size().reset_index(name='Relationship')
plt.figure(figsize=(10, 6))
plt.bar(df_relationship['Year'],df_relationship['Hospitalizations'],color = 'green',label='Hospitalizations')
plt.bar(df_relationship ['Year'],df_relationship['Deaths'],color='blue',label='Deaths')
plt.xlabel('Year')
plt.ylabel('the number of cases')
plt.grid(axis='y', color='grey', linestyle='--', linewidth=0.3)
plt.legend()

df_relationship=df_filtered_years.groupby(['Hospitalizations','Deaths','Year']).size().reset_index(name='Relationship')
df_relationship.corr(numeric_only=True)
plt.figure(figsize=(12, 6))
sns.heatmap(df_relationship.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()


df_food=df_filtered_years.groupby(['Primary Mode','Food Vehicle','Setting']).size().reset_index(name='FOOD')
df_food.value_counts()
Food_data = df_food[(df_food['Primary Mode'] == 'Food')]
#Food_data['Setting'].unique()
df_food

restaurant = ['Restaurant: Other','Restaurant: Sit-down dining','Restaurant: Fast-food (drive up service or pay at counter)','Restaurant: Buffet',
              'Restaurant: Sit-down dining; Restaurant: Other','Restaurant: Fast-food (drive up service or pay at counter); Restaurant: Sit-down dining',
              'Restaurant: Sit-down dining; Restaurant: Fast-food (drive up service or pay at counter)',
              'Restaurant: Sit-down dining; Office/indoor workplace; Restaurant: Other']

private_residence = ['Private home/residence','Residence - Single-family home','Private home/residence; Residence - Single-family home',
                     'Private home/residence; Other','Private home/residence; Religious facility','Residence - Multi-unit housing']

healthcare_facility = ['Hospital','Long-term care/nursing home/assisted living facility','Hospital; Long-term care/nursing home/assisted living facility',
                       'Hospital; Private home/residence','Long-term care/nursing home/assisted living facility; Private home/residence']

school_daycare = ['School/college/university','Child daycare/preschool','School/college/university; Private home/residence',
                  'Child daycare/preschool; Private home/residence','School/college/university; Caterer']

religious_facility = ['Religious facility','Religious facility; Private home/residence','Religious facility; Caterer']

event_space = ['Banquet Facility (food prepared and served on-site)','Festival/fair','Event space',
               'Banquet Facility (food prepared and served on-site); Festival/fair']

retail_grocery = ['Grocery store/bakery/deli/convenience store','Grocery store/bakery/deli/convenience store; Private home/residence',
                  'Grocery store/bakery/deli/convenience store; Restaurant: Other','Grocery store/bakery/deli/convenience store; Restaurant: Sit-down dining']

caterer = ['Caterer','Caterer; Private home/residence',
           'Caterer; Restaurant: Sit-down dining','Caterer; Grocery store/bakery/deli/convenience store']

public_space = ['Park/outdoor area','Festival/fair','Camp']

other = ['Other','Other; Private home/residence','Other; Festival/fair',
         'Correctional/detention facility','Office/indoor workplace',
         'Ship/boat','Farm/dairy/agricultural setting']

def categorize_setting(setting):
  if setting in restaurant:
    return 'Restaurant'
  elif setting in private_residence:
    return 'Private Residence'
  elif setting in healthcare_facility:
    return 'Healthcare Facility'
  elif setting in school_daycare:
    return 'School/Daycare'
  elif setting in religious_facility:
    return 'Religious Facility'
  elif setting in event_space:
    return 'Event Space'
  elif setting in retail_grocery:
    return 'Retail/Grocery'
  elif setting in caterer:
    return 'Caterer'
  elif setting in public_space:
    return 'Public Space'
  elif setting in other:
    return 'Other'
  else:
    return 'Unknown'

df_food['Setting_Category'] = df_food['Setting'].apply(categorize_setting)

df_food

df_food['Food Vehicle'].unique()

df_food['Setting_Category'].value_counts().plot(kind='barh', figsize=(12, 6))
plt.xlabel('Number of Food Vehicles')
plt.ylabel('Setting Category')
plt.title('Highest Number of Food Vehicles by Setting Category')
plt.grid(axis='y', color='gray', linestyle='--', linewidth=0.3)
plt.show()

plt.figure(figsize=(12, 6))
df_food['Food Vehicle'].value_counts().head(10).plot(kind='barh')
plt.xlabel('Food Vehicle')
plt.ylabel('Highest number of Food Vehicle')
plt.title('Highest number of Food Vehicle')
plt.grid(axis='y', color='gray', linestyle='--', linewidth=0.3)

df_animal=df_filtered_years.groupby(['Primary Mode','Animal Type','Setting']).size().reset_index(name='Most Associated With Animal')
df_animal.value_counts()
animal_data = df_animal[(df_animal['Primary Mode'] == 'Animal contact')]
animal_data

animal_data['Setting'].unique()

festival_fair = ['Festival/Fair', 'Event space; Fairground; Petting zoo; Farm/dairy/agricultural setting; Zoo or animal exhibit',
    'Festival/Fair; Private home/residence','Petting zoo; Festival/Fair']

animal_related = ['Petting zoo','Animal shelter or sanctuary','Private home/residence; Animal shelter or sanctuary',
    'Farm/dairy/agricultural setting','Farm/dairy/agricultural setting; Petting zoo',
    'Farm/dairy/agricultural setting; Veterinary clinic','Veterinary clinic',
    'Veterinary clinic; Private home/residence','Zoo or animal exhibit',
    'Zoo or animal exhibit; Farm/dairy/agricultural setting','Veterinary clinic; Farm/dairy/agricultural setting']

private_residence = ['Private home/residence','Private home/residence; Animal shelter or sanctuary',
    'Residence - Single-family home','Private home/residence; Petting zoo',
    'Private home/residence; Festival/Fair; Other','Private home/residence; Farm/dairy/agricultural setting',
    'Private home/residence; Agricultural feed store','Residence - Multi-unit housing',
    'Residence - Single-family home; Residence - Multi-unit housing']

educational = ['School/college/university','School/college/university; Farm/dairy/agricultural setting',
    'Child daycare/preschool','Child daycare/preschool; Private home/residence',
    'School/college/university; Child daycare/preschool; Private home/residence']

agricultural = ['Agricultural feed store','Agricultural feed store; Farm/dairy/agricultural setting; Private home/residence',
    'Agricultural feed store; Private home/residence','Farm/dairy/agricultural setting; Residence - Single-family home',
    'Residence - Single-family home; Farm/dairy/agricultural setting; Agricultural feed store']

healthcare = ['Hospital']

correctional = ['Correctional/detention facility','Private home/residence; Correctional/detention facility','Other; Correctional/detention facility']

parks_outdoor = ['Park/outdoor area; Farm/dairy/agricultural setting','Residence - Multi-unit housing; Park/outdoor area; Residence - Single-family home; Other; Fairground']


def categorize_setting(setting):
  if setting in festival_fair:
    return 'Festival/Fair'
  elif setting in animal_related:
    return 'Animal Related'
  elif setting in private_residence:
    return 'Private Residence'
  elif setting in educational:
    return 'Educational'
  elif setting in agricultural:
    return 'Agricultural'
  elif setting in healthcare:
    return 'Healthcare'
  elif setting in correctional:
    return 'Correctional'
  elif setting in parks_outdoor:
    return 'Parks/Outdoor'
  else:
    return 'Unknown'

df_animal['Setting_Category'] = df_animal['Setting'].apply(categorize_setting)

df_anima

df_animal['Setting_Category'].value_counts().plot(kind='barh', figsize=(12, 6))
plt.xlabel('Number of Animal Types')
plt.ylabel('Setting Category')
plt.title('Most Associated Animal Types by Setting Category')
plt.grid(axis='y', color='gray', linestyle='--', linewidth=0.3)

df_animal['Animal Type'].unique()

df_animal.replace('Dog or puppy' ,'Dog / puppy',inplace=True)
df_animal.replace('Cat or kitten' ,'Cat / kitten',inplace=True)

df_animal['Animal Type'].value_counts().head(10).plot(kind='barh', figsize=(12, 6))
plt.xlabel('Number of Animal Types')
plt.ylabel('Animal Type')
plt.title('Most Associated Animal Types')
plt.grid(axis='y', color='gray', linestyle='--', linewidth=0.3)



