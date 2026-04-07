import pandas as pd


def clean_data(data):
    import pandas as pd

    df = pd.DataFrame(data)

    df['date'] = pd.to_datetime(df['date'], dayfirst=True)

    # REMOVE zero-distance trips (important fix)
    df = df[df['distance_km'] > 0]

    df['month'] = df['date'].dt.to_period('M')
    df['weekday'] = df['date'].dt.day_name()

    df['price_per_km'] = df['price'] / df['distance_km']

    return df