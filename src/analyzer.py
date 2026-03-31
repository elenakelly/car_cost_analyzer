def analyze(df):
    print("\n===== ANALYSIS =====")

    print(f"Total spent: €{df['price'].sum():.2f}")
    print(f"Average trip: €{df['price'].mean():.2f}")

    print("\nMost expensive trip:")
    print(df.loc[df['price'].idxmax()])

    print("\nMonthly spending:")
    print(df.groupby('month')['price'].sum())

    print("\nAverage cost per km:")
    print(df['price_per_km'].mean())

    print("\nMost expensive weekday:")
    print(df.groupby('weekday')['price'].mean().sort_values(ascending=False))