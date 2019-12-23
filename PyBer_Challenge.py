#%%
%matplotlib inline

# %%
# Dependencies
import matplotlib.pyplot as plt 
import matplotlib as mpl 
import pandas as pd 
import numpy as np 
import os


# %%
# Load files
city_data_to_load = os.path.join("Resources", "city_data.csv" )
ride_data_to_load = os.path.join("Resources", "ride_data.csv")

# %%
# Read data files and store them in DataFrames
city_data_df = pd.read_csv(city_data_to_load)
ride_data_df = pd.read_csv(ride_data_to_load)

# %%
# Combine the data into a single dataset
pyber_challenge_df = pd.merge(ride_data_df, city_data_df, how="left", on=["city", "city"])

# Display the DataFrame
pyber_challenge_df.head()

# %%
# Total Rides by city type
total_rides = pyber_challenge_df.groupby(["type"]).count()["ride_id"]
total_rides

# %%
# Total Drivers by city type
total_drivers = city_data_df.groupby(["type"]).sum()["driver_count"]
total_drivers

# %%
# Total Fares
total_fares = pyber_challenge_df.groupby(["type"]).sum()["fare"]
total_fares

# %%
# Avg Fare per Ride
avg_fare_per_ride = total_fares / total_rides
avg_fare_per_ride


# %%
# Avg Fare per Driver
avg_fare_per_driver = total_fares / total_drivers
avg_fare_per_driver

# %%
# Creating a summary DataFrame using lists of values with keys
pyber_summary_df = pd.DataFrame({"Total Rides": total_rides, 
    "Total Drivers": total_drivers,
    "Total Fares": total_fares,
    "Average Fare per Ride": avg_fare_per_ride,
    "Average Fare per Driver": avg_fare_per_driver})
pyber_summary_df

# %%
# Formatting summary DataFrame columns
pyber_summary_df.index.name = None
pyber_summary_df["Total Rides"] = pyber_summary_df["Total Rides"].map("{:,}".format)
pyber_summary_df["Total Drivers"] = pyber_summary_df["Total Drivers"].map("{:,}".format)
pyber_summary_df["Total Fares"] = pyber_summary_df["Total Fares"].map("${:,.2f}".format)
pyber_summary_df["Average Fare per Ride"] = pyber_summary_df["Average Fare per Ride"].map("${:,.2f}".format)
pyber_summary_df["Average Fare per Driver"] = pyber_summary_df["Average Fare per Driver"].map("${:,.2f}".format)

pyber_summary_df

# %%
# Rename DataFrame columns
pyber_challenge_df.rename(columns = {'city':'City', 'date':'Date', 'fare':'Fare', 'ride_id':'Ride Id', 'driver_count': 'No. Drivers', 'type':'City Type'}, inplace = True)
pyber_challenge_df

# %%
# Set index to Date column
date_index = pyber_challenge_df.set_index(["Date"])
pyber_challenge_dateindex_df = pd.DataFrame(date_index)
pyber_challenge_dateindex_df

# %%
# Create a fare DataFrame using copy()
fares_df = pyber_challenge_df[['Date', 'City Type', 'Fare']].copy()
fares_df

# %%
# Check Fares_df info
fares_df.info()

# %%
# Convert date index from object to datetime
fares_df["Date"] = pd.to_datetime(fares_df["Date"])
fares_df.info()

# %%
# Create new df on total fares by type and by date
fares_by_type_date = fares_df.groupby(["City Type", "Date"]).sum()["Fare"]
fares_by_type_date_df = pd.DataFrame(fares_by_type_date)

fares_by_type_date_df.head()

# %%
# Create a pivot table df
fares_pivot_df = fares_df.pivot(index='Date', columns='City Type', values='Fare')

fares_pivot_df
# %%
# Create a new df from pivot within date criteria
fares_pivot_sub_df = fares_pivot_df.loc['2019-01-01': '2019-04-28']

fares_pivot_sub_df


# %%
# Resample fares_pivot_sub_df into weekly sum
fares_pivot_sub_wk_df = fares_pivot_sub_df.resample('W', how='sum')

fares_pivot_sub_wk_df.head()

# %%
# Generate graph

plt.style.use('fivethirtyeight')
plt.figure()
plt.rcParams["figure.figsize"]=(15,5)
fares_pivot_sub_wk_df.plot()
plt.xlabel('Month', fontsize="14")
plt.ylabel('Fare ($USD)', fontsize="14")
plt.xticks(fontsize="12")
plt.yticks(fontsize="12")
plt.title('Total Fare by City Type', fontsize="16")
lgnd = plt.legend(fontsize="10", mode="Expanded", loc="best", title="City Type")
lgnd.get_title().set_fontsize(10)

plt.savefig("Analysis/Fig8.png")

plt.show()



# %%
