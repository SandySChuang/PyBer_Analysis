#%%
%matplotlib inline

# %%
# Dependencies
import matplotlib.pyplot as plt 
import pandas as pd 
import os


# %%
# Load files
city_data_to_load = os.path.join("Resources", "city_data.csv" )
ride_data_to_load = os.path.join("Resources", "ride_data.csv")

# %%
# Read city data file and store it in DataFrame
city_data_df = pd.read_csv(city_data_to_load)
city_data_df.head(10)

# %%
# Read ride data file and store it in DataFrame
ride_data_df = pd.read_csv(ride_data_to_load)
ride_data_df.head(10)

# %%
# Get the columns and rows that are not null
city_data_df.count()

# %%
# Get the columns and the rows that are not null
city_data_df.isnull().sum()

# %%
# Get the data types of each column
city_data_df.dtypes

# %%
# Get the unique values for the type of city
city_data_df["type"].unique()

# %%
# Get the number of data points from the Urban cities
sum(city_data_df["type"]=="Urban")

# %%
# Get the number of data points from the Suburban cities
sum(city_data_df["type"]=="Suburban")

# %%
# Get the number of data points from the Rural cities
sum(city_data_df["type"]=="Rural")

# %%
# Get columns and rows for ride data
ride_data_df.count()

# %%
# Get the columns and rows that are not null
ride_data_df.isnull().sum()

# %%
# Get the data types of each column
ride_data_df.dtypes

# %%
# Combine the data into a single dataset
pyber_data_df = pd.merge(ride_data_df, city_data_df, how="left", on=["city", "city"])

# Display the DataFrame
pyber_data_df.head()

# %%
# Create the Urban city DataFrame
urban_cities_df = pyber_data_df[pyber_data_df["type"] =="Urban"]
urban_cities_df.head()

# %%
# Create the Suburban and Rural DataFrames
suburban_cities_df = pyber_data_df[pyber_data_df["type"] =="Suburban"]
rural_cities_df = pyber_data_df[pyber_data_df["type"] =="Rural"]

# %%
rural_cities_df.head(10)

# %%
# Get the number or rides for urban cities
urban_ride_count = urban_cities_df.groupby(["city"]).count()["ride_id"]
urban_ride_count.head()

# %%
# Get the number or rides for Suburban and Rural cities
suburban_ride_count = suburban_cities_df.groupby(["city"]).count()["ride_id"]
rural_ride_count = rural_cities_df.groupby(["city"]).count()["ride_id"]

# %%
# Get average fare for each city in the urban cities
urban_avg_fare = urban_cities_df.groupby(["city"]).mean()["fare"]
urban_avg_fare.head()

# %%
# Get average fare for each city in the suburban and rural cities
suburban_avg_fare = suburban_cities_df.groupby(["city"]).mean()["fare"]
rural_avg_fare = rural_cities_df.groupby(["city"]).mean()["fare"]

# %%
# Get the average number of drivers for each urban city
urban_driver_count = urban_cities_df.groupby(["city"]).mean()["driver_count"]
urban_driver_count.head()

# %%
# Get the average number of drivers for each suburban and urban cities
suburban_driver_count = suburban_cities_df.groupby(["city"]).mean()["driver_count"]
rural_driver_count = rural_cities_df.groupby(["city"]).mean()["driver_count"]

# %%
# Build the scatter plots for urban cities
plt.scatter(urban_ride_count, 
    urban_avg_fare, 
    s=10*urban_driver_count, c="coral",
    edgecolor="black", linewidths=1,
    alpha=0.8, label="Urban")
plt.title("PyBer Ride-Sharing Data (2019)")
plt.ylabel("Average Fare ($)")
plt.xlabel("Total Number of Rides (Per City)")
plt.grid(True)
plt.legend()

# %%
# Build the scatter plots for Suburban cities
plt.scatter(suburban_ride_count, 
    suburban_avg_fare, 
    s=10*suburban_driver_count, c="skyblue",
    edgecolor="black", linewidths=1,
    alpha=0.8, label="Suburban")
plt.title("PyBer Ride-Sharing Data (2019)")
plt.ylabel("Average Fare ($)")
plt.xlabel("Total Number of Rides (Per City)")
plt.grid(True)
plt.legend()

# %%
# Build the scatter plots for rural cities
plt.scatter(rural_ride_count, 
    rural_avg_fare, 
    s=10*rural_driver_count, c="gold",
    edgecolor="black", linewidths=1,
    alpha=0.8, label="Rural")
plt.title("PyBer Ride-Sharing Data (2019)")
plt.ylabel("Average Fare ($)")
plt.xlabel("Total Number of Rides (Per City)")
plt.grid(True)
plt.legend()

# %%
# Build the scatter charts for each city type
plt.subplots(figsize=(10, 6))
plt.scatter(urban_ride_count, 
    urban_avg_fare, 
    s=10*urban_driver_count, c="coral",
    edgecolor="black", linewidths=1,
    alpha=0.8, label="Urban")

plt.scatter(suburban_ride_count, 
    suburban_avg_fare, 
    s=10*suburban_driver_count, c="skyblue",
    edgecolor="black", linewidths=1,
    alpha=0.8, label="Suburban")

plt.scatter(rural_ride_count, 
    rural_avg_fare, 
    s=10*rural_driver_count, c="gold",
    edgecolor="black", linewidths=1,
    alpha=0.8, label="Rural")

# Incorporate the other graph properties
plt.title("PyBer Ride-Sharing Data (2019)", fontsize=20)
plt.ylabel("Average Fare ($)", fontsize=12)
plt.xlabel("Total Number of Rides (Per City)", fontsize=12)
plt.grid(True)

# declare a legend variable to add customized features
lgnd = plt.legend(fontsize="12", mode="Expanded",
        scatterpoints=1, loc="best", title="City Types")
lgnd.legendHandles[0]._sizes = [75]
lgnd.legendHandles[1]._sizes = [75]
lgnd.legendHandles[2]._sizes = [75]
lgnd.get_title().set_fontsize(12)

# Incorporate a text label about circle size.
plt.text(42, 35, "Note:\nCircle size correlates\nwith driver count per city.", fontsize="12")

# Save the figure.
plt.savefig("Analysis/Fig1.png")

plt.show()
# %%
# Get summary statistics for Urban
urban_cities_df.describe()

# %%
# Get summary statistics for Suburban
suburban_cities_df.describe()

# %%
# Get summary statistics for Rural
rural_cities_df.describe()


# %%
# Get summary statistics on urban ride count
urban_ride_count.describe()

# %%
# Get summary statistics on suburban ride count
suburban_ride_count.describe()

# %%
# Get summary statistics on rural ride count
rural_ride_count.describe()

# %%
# Calculate the mean of the ride count for each city type.
round(urban_ride_count.mean(),2), round(suburban_ride_count.mean(),2), round(rural_ride_count.mean(),2)

# %%
# Calculate the median of the ride count for each city type.
round(urban_ride_count.median()), round(suburban_ride_count.median()), round(rural_ride_count.median())


# %%
# Calculate the mode of the ride count for Urban cities
urban_ride_count.mode()


# %%
# Calculate the mode of the ride count for suburban cities
suburban_ride_count.mode()

# %%
# Import NumPy and the stats module from SciPy
import numpy as np 
import scipy.stats as sts 


# %%
# Calculate the measures of central tendency for the ride count for the urban cities
mean_urban_ride_count = np.mean(urban_ride_count)
print(f"The mean for the ride counts for urban trips is {mean_urban_ride_count: .2f}.")

median_urban_ride_count = np.median(urban_ride_count)
print(f"The median for the ride counts for urban trips is {median_urban_ride_count}.")

mode_urban_ride_count = sts.mode(urban_ride_count)
print(f"The mode for the ride counts for urban trips is {mode_urban_ride_count}.")


# %%
# Calculate the measures of central tendency for the ride count for the suburban cities
mean_suburban_ride_count = np.mean(suburban_ride_count)
print(f"The mean for the ride counts for suburban trips is {mean_suburban_ride_count: .2f}.")

median_suburban_ride_count = np.median(suburban_ride_count)
print(f"The median for the ride counts for suburban trips is {median_suburban_ride_count}.")

mode_suburban_ride_count = sts.mode(suburban_ride_count)
print(f"The mode for the ride counts for suburban trips is {mode_suburban_ride_count}.")

# %%
# Calculate the measures of central tendency for the ride count for the rural cities
mean_rural_ride_count = np.mean(rural_ride_count)
print(f"The mean for the ride counts for rural trips is {mean_rural_ride_count: .2f}.")

median_rural_ride_count = np.median(rural_ride_count)
print(f"The median for the ride counts for rural trips is {median_rural_ride_count}.")

mode_rural_ride_count = sts.mode(rural_ride_count)
print(f"The mode for the ride counts for rural trips is {mode_rural_ride_count}.")

# %%
# Get the fares for the urban cities
urban_fares = urban_cities_df["fare"]
urban_fares.head()

# %%
# Calculate the measures of central tendency for the average fare for the urban cities
mean_urban_fares = np.mean(urban_fares)
print(f"The mean fare price for urban trips is ${mean_urban_fares:.2f}.")

median_urban_fares = np.median(urban_fares)
print(f"The median fare price for urban trips is ${median_urban_fares}.")

mode_urban_fares = sts.mode(urban_fares)
print(f"The mode fare price for urban trips is {mode_urban_fares}.")

# %%
# Get the fares for the suburban and rural cities
suburban_fares = suburban_cities_df["fare"]
rural_fares = rural_cities_df["fare"]

# %%
# Calculate the measures of central tendency for the average fare for the suburban and rural cities
mean_suburban_fares = np.mean(suburban_fares)
print(f"The mean fare price for suburban trips is ${mean_suburban_fares:.2f}.")

median_suburban_fares = np.median(suburban_fares)
print(f"The median fare price for suburban trips is ${median_suburban_fares}.")

mode_suburban_fares = sts.mode(suburban_fares)
print(f"The mode fare price for suburban trips is {mode_suburban_fares}.")

mean_rural_fares = np.mean(rural_fares)
print(f"The mean fare price for rural trips is ${mean_rural_fares:.2f}.")

median_rural_fares = np.median(rural_fares)
print(f"The median fare price for rural trips is ${median_rural_fares}.")

mode_rural_fares = sts.mode(rural_fares)
print(f"The mode fare price for rural trips is {mode_rural_fares}.")

# %%
# Get the driver count for the all city types
urban_drivers = urban_cities_df["driver_count"]
suburban_drivers = suburban_cities_df["driver_count"]
rural_drivers = rural_cities_df["driver_count"]

# %%
# Calculate the measures of central tendency for the driver counts for all city types
mean_urban_drivers = np.mean(urban_drivers)
print(f"The mean driver count for urban trips is {mean_urban_drivers:.1f}.")

median_urban_drivers = np.median(urban_drivers)
print(f"The median driver count for urban trips is {median_urban_drivers}.")

mode_urban_drivers = sts.mode(urban_drivers)
print(f"The mode driver count for urban trips is {mode_urban_drivers}.")

mean_suburban_drivers = np.mean(suburban_drivers)
print(f"The mean driver count for suburban trips is {mean_suburban_drivers:.1f}.")

median_suburban_drivers = np.median(suburban_drivers)
print(f"The median driver count for suburban trips is {median_suburban_drivers}.")

mode_suburban_drivers = sts.mode(suburban_drivers)
print(f"The mode driver count for suburban trips is {mode_suburban_drivers}.")

mean_rural_drivers = np.mean(rural_drivers)
print(f"The mean driver count for rural trips is {mean_rural_drivers:.1f}.")

median_rural_drivers = np.median(rural_drivers)
print(f"The median driver count for rural trips is {median_rural_drivers}.")

mode_rural_drivers = sts.mode(rural_drivers)
print(f"The mode driver count for rural trips is {mode_rural_drivers}.")

# %%
# Create a box-and-whisker plot for the urban cities ride count.
x_labels = ["Urban"]
fig, ax = plt.subplots()
ax.boxplot(urban_ride_count, labels=x_labels)
# Add the title, y-axis label and grid.
ax.set_title('Ride Count Data (2019)')
ax.set_ylabel('Number of Rides')
ax.set_yticks(np.arange(10, 41, step=2.0))
ax.grid()
plt.show()

# %%
# Create a box-and-whisker plot for the suburban cities ride count.
x_labels = ["Suburban"]
fig, ax = plt.subplots()
ax.boxplot(suburban_ride_count, labels=x_labels)
# Add the title, y-axis label and grid.
ax.set_title('Ride Count Data (2019)')
ax.set_ylabel('Number of Rides')
ax.set_yticks(np.arange(0, 30, step=2.0))
ax.grid()
plt.show()

# %%
# Create a box-and-whisker plot for the rural cities ride count.
x_labels = ["Rural"]
fig, ax = plt.subplots()
ax.boxplot(rural_ride_count, labels=x_labels)
# Add the title, y-axis label and grid.
ax.set_title('Ride Count Data (2019)')
ax.set_ylabel('Number of Rides')
ax.set_yticks(np.arange(0, 30, step=2.0))
ax.grid()
plt.show()

# %%
# Create a box-and-whisker plot for the all city types ride count.
x_labels = ["Urban","Suburban","Rural"]
ride_count_data = [urban_ride_count, suburban_ride_count, rural_ride_count]
fig, ax = plt.subplots(figsize=(10,6))
ax.boxplot(ride_count_data, labels=x_labels)
# Add the title, y-axis label and grid.
ax.set_title('Ride Count Data (2019)')
ax.set_xlabel("City Types")
ax.set_ylabel('Number of Rides')
ax.set_yticks(np.arange(0, 45, step=3.0))
ax.grid()

# Save the figure
plt.savefig("Analysis/Fig2.png")
plt.show()

# %%
# Get the city that matches 39
urban_city_outlier = urban_ride_count[urban_ride_count==39].index[0]
print(f"{urban_city_outlier} has the highest rider count.")

# %%
# Create a box-and-whisker plot for the all city types fares.
x_labels = ["Urban","Suburban","Rural"]
fares_data = [urban_fares, suburban_fares, rural_fares]
fig, ax = plt.subplots(figsize=(10,6))
ax.boxplot(fares_data, labels=x_labels)
# Add the title, y-axis label and grid.
ax.set_title('Ride Fare Data (2019)')
ax.set_xlabel("City Types")
ax.set_ylabel('Fare($USD)')
ax.set_yticks(np.arange(0, 60, step=5.0))
ax.grid()

# Save the figure
plt.savefig("Analysis/Fig3.png")
plt.show()

# %%
# Create a box-and-whisker plot for the all city types driver counts.
x_labels = ["Urban","Suburban","Rural"]
drivers_data = [urban_drivers, suburban_drivers, rural_drivers]
fig, ax = plt.subplots(figsize=(10,6))
ax.boxplot(drivers_data, labels=x_labels)
# Add the title, y-axis label and grid.
ax.set_title('Ride Count Data (2019)')
ax.set_xlabel("City Types")
ax.set_ylabel('Number of Drivers')
ax.set_yticks(np.arange(0, 80, step=5.0))
ax.grid()

# Save the figure
plt.savefig("Analysis/Fig4.png")
plt.show()

# %%
# Get the sum of the fares for each city type.
sum_fares_by_type = pyber_data_df.groupby(["type"]).sum()["fare"]
sum_fares_by_type

# %%
# Get the sum of all the fares.
total_fares = pyber_data_df["fare"].sum()
total_fares

# %%
# Calculate the percentage of fare for each city type.
type_percents = 100 * sum_fares_by_type / total_fares
type_percents

# %%
# import mpl to change pie configuration using rcParams.
import matplotlib as mpl 
# Build the percentage of fares by city type pie chart.
plt.subplots(figsize=(10,6))
plt.pie(type_percents, 
    labels=["Rural", "Suburban", "Urban"],
    colors=["gold", "lightskyblue", "lightcoral"],
    explode=[0,0,0.1],
    autopct='%1.1f%%',
    shadow=True, startangle=150)
plt.title("% of Total Fares by City Type")
# Change the default font size
mpl.rcParams['font.size'] = 14
plt.savefig("Analysis/Fig5.png")
plt.show()

# %%
# Calculate Ride Percent by City Type
ride_percents = 100 * pyber_data_df.groupby(["type"]).count()["ride_id"] / pyber_data_df["ride_id"].count()
ride_percents

# %%
# Build the percentage of rides by city type pie chart.
plt.subplots(figsize=(10,6))
plt.pie(ride_percents, 
    labels=["Rural", "Suburban", "Urban"],
    colors=["gold", "lightskyblue", "lightcoral"],
    explode=[0,0,0.1],
    autopct='%1.1f%%',
    shadow=True, startangle=150)
plt.title("% of Total Rides by City Type")
# Change the default font size
mpl.rcParams['font.size'] = 14
plt.savefig("Analysis/Fig6.png")
plt.show()

# %%
# Calculate Driver Percent by City Type
driver_percents = 100 * pyber_data_df.groupby(["type"]).sum()["driver_count"] / pyber_data_df["driver_count"].sum()
driver_percents

# %%
# Build the percentage of driver by city type pie chart.
plt.subplots(figsize=(10,6))
plt.pie(driver_percents, 
    labels=["Rural", "Suburban", "Urban"],
    colors=["gold", "lightskyblue", "lightcoral"],
    explode=[0,0,0.1],
    autopct='%1.1f%%',
    shadow=True, startangle=150)
plt.title("% of Total Drivers by City Type")
# Change the default font size
mpl.rcParams['font.size'] = 14
plt.savefig("Analysis/Fig7.png")
plt.show()

# %%
