import pandas as pd
import plotly.express as px

# Sample data
df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr"],
    "Revenue": [120, 150, 170, 140]
})

# Create chart
fig = px.bar(
    df,
    x="Month",
    y="Revenue",
    title="Monthly Revenue"
)

# Show chart
fig.show()