from scripts.data_loader import load_weather_data
from scripts.data_cleaning import clean_weather_data, select_required_columns
from scripts.statistics import calculate_statistics
from scripts.visualization import plot_temperature

df = load_weather_data("data/GlobalWeatherRepository.csv")
# print(df.head())
df = clean_weather_data(df)
df = select_required_columns(df)

stats = calculate_statistics(df)
print(stats)
# print(df.head())

plot_temperature(df)
