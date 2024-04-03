import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
st.set_page_config(page_title="Video Processing Dashboard", page_icon=":chart_with_upwards_trend:", layout="wide")
# Load the dataset
@st.cache_data
def load_data():
    return pd.read_csv('video_processing_data.csv')

df = load_data()


# Set title and padding
st.title('Video Processing Dashboard')
st.markdown("---")
st.markdown('')

# Sidebar
st.sidebar.title('Filters')
resolution_filter = st.sidebar.multiselect('Filter by Resolution', df['Resolution'].unique(), df['Resolution'].unique())
frame_rate_filter = st.sidebar.slider('Filter by Frame Rate', int(df['Frame_Rate'].min()), int(df['Frame_Rate'].max()), (int(df['Frame_Rate'].min()), int(df['Frame_Rate'].max())))
duration_filter = st.sidebar.slider('Filter by Duration', int(df['Duration'].min()), int(df['Duration'].max()), (int(df['Duration'].min()), int(df['Duration'].max())))

# Apply filters
filtered_df = df[(df['Resolution'].isin(resolution_filter)) & (df['Frame_Rate'].between(*frame_rate_filter)) & (df['Duration'].between(*duration_filter))]

# Main content
st.subheader('Dataset Overview')
st.write(filtered_df)

# Visualization
st.subheader('Visualizations')

# Resolution pie chart
st.write('### Resolution Distribution')
fig_pie = px.pie(filtered_df, values='Duration', names='Resolution', title='Resolution Distribution')
st.plotly_chart(fig_pie)

# Frame Rate histogram
st.write('### Frame Rate Distribution')
fig_hist = px.histogram(filtered_df, x='Frame_Rate', nbins=20, title='Frame Rate Distribution')
st.plotly_chart(fig_hist)

# Duration vs File Size scatter plot
st.write('### Duration vs File Size')
fig_scatter = px.scatter(filtered_df, x='Duration', y='File_Size_MB', color='Resolution', title='Duration vs File Size')
st.plotly_chart(fig_scatter)

# 3D scatter plot with Resolution, Frame Rate, and Duration
st.write('### 3D Scatter Plot')
fig_3d = px.scatter_3d(filtered_df, x='Resolution', y='Frame_Rate', z='Duration', color='File_Size_MB', title='Resolution vs Frame Rate vs Duration')
st.plotly_chart(fig_3d)