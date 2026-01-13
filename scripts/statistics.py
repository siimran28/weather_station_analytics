def calculate_statistics(df):
    return {
        "mean_temperature": df["temperature_celsius"].mean(),
        "max_temperature": df["temperature_celsius"].max(),
        "min_temperature": df["temperature_celsius"].min(),
        "std_temperature": df["temperature_celsius"].std(),
        "mean_humidity": df["humidity"].mean()
    }
