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

    # FIX weekday order
    order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    weekday_avg = df.groupby('weekday')['price'].mean().reindex(order)

    print("\nAverage cost by weekday:")
    print(weekday_avg)