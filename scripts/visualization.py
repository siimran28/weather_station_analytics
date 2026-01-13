import matplotlib.pyplot as plt

def plot_temperature(df):
    # Resample to daily average
    daily_df = df.set_index("last_updated")["temperature_celsius"].resample("D").mean()

    plt.figure(figsize=(10, 5))
    plt.plot(daily_df.index, daily_df.values)
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.title("Daily Average Temperature Trend")
    plt.tight_layout()
    plt.show()
