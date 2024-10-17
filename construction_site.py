import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
#ssc
# Sample Data
data = {
    'Project': ['Site A', 'Site B', 'Site C', 'Site D'],
    'Cost': [200000, 150000, 300000, 250000],
    'Workforce': [50, 40, 60, 55],
    'Status': ['Ongoing', 'Completed', 'Ongoing', 'Completed']
}

df = pd.DataFrame(data)

# Streamlit App Configuration
st.title('Construction Site System Analysis')
st.sidebar.title('Options')

# Pie chart for Project Cost Distribution
st.sidebar.subheader('Pie Chart: Cost Distribution')
if st.sidebar.checkbox('Show Pie Chart'):
    fig_pie, ax_pie = plt.subplots()
    ax_pie.pie(df['Cost'], labels=df['Project'], autopct='%1.1f%%', startangle=90)
    ax_pie.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig_pie)

# Bar Chart for Workforce Allocation
st.sidebar.subheader('Bar Chart: Workforce Allocation')
if st.sidebar.checkbox('Show Bar Chart'):
    fig_bar = px.bar(df, x='Project', y='Workforce', title='Workforce Allocation')
    st.plotly_chart(fig_bar)

# Display Data in Table format
st.sidebar.subheader('Display Table Data')
if st.sidebar.checkbox('Show Data Table'):
    st.write(df)

# Show a status filter
status_filter = st.sidebar.multiselect(
    'Filter by Project Status', options=df['Status'].unique(), default=df['Status'].unique()
)
filtered_df = df[df['Status'].isin(status_filter)]

# Filtered Project Data
st.subheader('Filtered Project Data')
st.dataframe(filtered_df)

# Add further functionality (e.g., project cost prediction)
st.sidebar.subheader('Cost Prediction Analysis')
cost_input = st.sidebar.number_input('Enter predicted cost for analysis (in INR)', min_value=10000, max_value=1000000, value=50000)
st.write(f'Your predicted cost input: ₹{cost_input:,}')

# Further analysis based on prediction can go here
# ...

