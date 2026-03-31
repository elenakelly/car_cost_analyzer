import pandas as pd

def clean_data(data):
    df = pd.DataFrame(data)

    df['date'] = pd.to_datetime(df['date'], dayfirst=True)
    
    df['month'] = df['date'].dt.to_period('M')
    df['weekday'] = df['date'].dt.day_name()

    # New useful metrics
    df['price_per_km'] = df['price'] / df['distance_km']

    return df