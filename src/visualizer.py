import plotly.express as px



def plot_monthly(df):
    import plotly.express as px

    monthly = df.groupby('month')['price'].sum().reset_index()

    # FIX: convert Period → string
    monthly['month'] = monthly['month'].astype(str)

    fig = px.bar(
        monthly,
        x='month',
        y='price',
        title='Monthly Car Rental Spending'
    )

    fig.show()