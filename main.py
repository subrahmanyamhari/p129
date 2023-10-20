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
star_dist.append(df1[3])
suitable_stars.append(df1)
print(suitable_stars)
for i,value in enumerate(star_dist):
    if value != "NaN":
        if int(value) > 100:
            suitable_stars.pop(i)

for i,value in enumerate(suitable_stars[6]):
    if 150 < int(value) and int(value) < 350:
        pass
    else:
        suitable_stars.pop(i)

print(suitable_stars)
suitable_star = pd.DataFrame(suitable_stars)
suitable_star.to_csv("filter_data.csv")