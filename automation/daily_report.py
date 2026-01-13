from scripts.data_loader import load_weather_data
from scripts.data_cleaning import clean_weather_data, select_required_columns
from scripts.statistics import calculate_statistics

def generate_report():
    df = load_weather_data("data/GlobalWeatherRepository.csv")
    df = clean_weather_data(df)
    df = select_required_columns(df)

    stats = calculate_statistics(df)

    with open("daily_report.txt", "w") as f:
        for key, value in stats.items():
            f.write(f"{key}: {value}\n")

if __name__ == "__main__":
    generate_report()
