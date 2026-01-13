

def clean_weather_data(df):
    # print("Rows before cleaning:", len(df))
    # Sort data by time (important for time-series)
    df.sort_values("last_updated", inplace=True)

    # Remove duplicate sensor readings
    df.drop_duplicates(inplace=True)

    # Forward fill missing sensor values
    df.ffill(inplace=True)

    # Validate temperature range (Celsius)
    df = df[
        (df["temperature_celsius"] > -40) &
        (df["temperature_celsius"] < 60)
    ]

    # Validate wind speed (km/h)
    df = df[df["wind_kph"] < 150]
    # print("Rows before cleaning:", len(df))

    return df



def select_required_columns(df):
    """
    Select only relevant weather station sensor columns
    """
    required_columns = [
        "last_updated",
        "temperature_celsius",
        "humidity",
        "pressure_mb",
        "wind_kph"
    ]
    return df[required_columns]
