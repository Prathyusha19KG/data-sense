
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Restaurant Cuisine Insights", layout="centered")

st.title("Top 10 Restaurant Cuisines")
st.write("This dashboard presents the most popular cuisine types based on restaurant counts from a real-world dataset.")

# Data for top 10 cuisines
cuisine_data = {
    'Cuisine': [
        'North Indian', 'Chinese', 'Fast Food', 'Mughlai', 'Italian',
        'Bakery', 'Continental', 'Cafe', 'Desserts', 'South Indian'
    ],
    'Restaurants': [3960, 2735, 1986, 995, 764, 745, 736, 703, 653, 636]
}

cuisine_df = pd.DataFrame(cuisine_data)

# Plot
st.subheader("Top 10 Cuisines by Number of Restaurants")
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='Restaurants', y='Cuisine', data=cuisine_df, palette='viridis', ax=ax)
ax.set_title('Top 10 Cuisines')
st.pyplot(fig)

# Key Insight
st.markdown("### Key Insight")
st.markdown("""
North Indian and Chinese cuisines dominate the restaurant landscape, together making up over 6,600 establishments.
This indicates a strong consumer preference for traditional and familiar food options.
""")
