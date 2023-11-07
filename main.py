import csv

import pandas as pd

import plotly_express as px

df1 = pd.read_csv("scraped-data.csv")
# print(df1["mass"])

data1 = []

df1["mass"] = df1["mass"]*0.102763
df1["radius"] = df1["radius"]*0.000954588

# print(df1["mass"])

# print(df1.describe())
# print(df1.info())
# print(df1.dtypes)

df1.to_csv("final_data.csv")

df1["gravity"] = 6.6*10**-11 * df1["mass"]/df1["radius"]**2
# print(df1)
df1.to_csv("final_data_with_gravity.csv")

solar_chart_mass_radius_graph = px.scatter(x=df1["mass"],y=df1["radius"])
solar_chart_mass_radius_graph.show()

solar_chart_mass_radius_list = []
solar_chart_mass_radius_list.append(df1["mass"])
solar_chart_mass_radius_list.append(df1["radius"])
df1["distance"] = df1["distance"].sort_values()
print(df1["distance"])
suitable_stars = []
star_dist = []
for i in df1["distance"]:
    if i <= 100:
        suitable_stars.append(True)
    else:
        suitable_stars.append(False)

suitable_stars_new_data = pd.Series(suitable_stars)
new_data = df1[suitable_stars_new_data]
print(new_data)
suitable_stars_1 = []

for i in df1["distance"]:
    if 150 < i and i < 350:
        suitable_stars_1.append(True)
    else:
        suitable_stars_1.append(False)

suitable_stars_new_data_1 = pd.Series(suitable_stars_1)
new_data_1 = df1[suitable_stars_new_data_1]

print(new_data_1)
new_data_1.reset_index(inplace = True)
new_data_1.to_csv("filter_data.csv")
