import os
import pandas as pd

# Define the folder containing the CSV files
data_folder = "temperature_data"

# Dictionary to store average temperatures for each file
file_averages = {}

# Dictionary to store the temperature ranges for each station
station_ranges = {}

# Dictionary to store the average temperatures for each station
station_averages = {}

# Iterate over each CSV file in the folder
for filename in os.listdir(data_folder):
    if filename.endswith(".csv"):
        file_path = os.path.join(data_folder, filename)

        # Read the CSV file
        df = pd.read_csv(file_path)

        # Extract temperature data for January to December (assumes columns 5 to 16)
        temperature_data = df.iloc[:, 4:16]

        # Calculate the average temperature for the file
        file_average = temperature_data.values.flatten()
        valid_data = pd.Series(file_average).dropna()  # Exclude missing values
        overall_average = valid_data.mean() if not valid_data.empty else None

        # Store the average temperature for the file
        file_averages[filename] = overall_average

        # Calculate the temperature range and average for each station
        for index, row in df.iterrows():
            station_name = row["STATION_NAME"]
            monthly_temps = row.iloc[4:16]
            valid_temps = monthly_temps.dropna()
            if not valid_temps.empty:
                # Calculate temperature range
                temp_range = valid_temps.max() - valid_temps.min()
                if station_name in station_ranges:
                    station_ranges[station_name] = max(station_ranges[station_name], temp_range)
                else:
                    station_ranges[station_name] = temp_range

                # Calculate average temperature
                station_avg = valid_temps.mean()
                if station_name in station_averages:
                    station_averages[station_name].append(station_avg)
                else:
                    station_averages[station_name] = [station_avg]

# Find the station(s) with the largest temperature range
max_range = max(station_ranges.values())
largest_range_stations = [station for station, temp_range in station_ranges.items() if temp_range == max_range]

# Find the warmest and coolest station(s)
station_avg_overall = {station: sum(avgs) / len(avgs) for station, avgs in station_averages.items()}
warmest_avg = max(station_avg_overall.values())
coolest_avg = min(station_avg_overall.values())
warmest_stations = [station for station, avg in station_avg_overall.items() if avg == warmest_avg]
coolest_stations = [station for station, avg in station_avg_overall.items() if avg == coolest_avg]

# Save average temperatures for each file
average_output_file = "average_temp.txt"
with open(average_output_file, "w") as f:
    f.write("Average Temperatures for Each File\n")
    f.write("File\tAverage Temperature\n")
    for filename, avg_temp in file_averages.items():
        f.write(f"{filename}\t{avg_temp:.2f}\n" if avg_temp is not None else f"{filename}\tNo Data\n")

# Save station(s) with the largest temperature range
range_output_file = "largest_temp_range_station.txt"
with open(range_output_file, "w") as f:
    f.write("Station(s) with Largest Temperature Range\n")
    f.write(f"Largest Range: {max_range:.2f}\n")
    f.write("Stations:\n")
    for station in largest_range_stations:
        f.write(f"{station}\n")

# Save warmest and coolest stations
warmest_coolest_output_file = "warmest_and_coolest_station.txt"
with open(warmest_coolest_output_file, "w") as f:
    f.write("Warmest and Coolest Stations\n")
    f.write(f"Warmest Average: {warmest_avg:.2f}\n")
    f.write("Warmest Stations:\n")
    for station in warmest_stations:
        f.write(f"{station}\n")
    f.write(f"\nCoolest Average: {coolest_avg:.2f}\n")
    f.write("Coolest Stations:\n")
    for station in coolest_stations:
        f.write(f"{station}\n")

print(f"Average temperatures for each file have been saved to {average_output_file}.")
print(f"Stations with the largest temperature range have been saved to {range_output_file}.")
print(f"Warmest and coolest stations have been saved to {warmest_coolest_output_file}.")
