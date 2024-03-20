import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

# Load the data from the Excel file
file_path = 'data_bike_filtered.xlsx'
df = pd.read_excel(file_path)


plt.figure(figsize=(15, 8))

# Subplot 1: User Type Distribution
plt.subplot(2, 3, 1)
user_counts = df['usertype'].value_counts()
plt.pie(user_counts, labels=user_counts.index, autopct='%1.1f%%', startangle=90, colors=['lightblue', 'lightcoral'])
plt.title('User Type Distribution')

# Subplot 2: User Gender Distribution
plt.subplot(2, 3, 2)
user_gender = df['gender'].value_counts()
plt.pie(user_gender, labels=user_gender.index, autopct='%1.1f%%', startangle=90, colors=['lightblue', 'lightcoral'])
plt.title('User Gender Distribution')

# Subplot 3: Birth Year Distribution 
plt.subplot(2, 3, 3)
subscriber_birth_years = df[df['usertype'] == 'Subscriber']['birthyear'].value_counts().head(10)
subscriber_birth_years = subscriber_birth_years.sort_index()
plt.plot(subscriber_birth_years.index, subscriber_birth_years.values, marker='o', color='blue', label='Top 10 Subscriber Birth Years')
plt.fill_between(subscriber_birth_years.index, subscriber_birth_years.values, color='blue', alpha=0.2)
plt.xlabel('Birth Year')
plt.ylabel('Count')
plt.title('Top 10 Subscriber Birth Years')

# Subplot 4: Categorical Scatter Plot for Top Ten Ages of Subscribers
plt.subplot(2, 3, 4)
total_subscribers = len(df[df['usertype'] == 'Subscriber'])
top_ten_age_counts = df[df['usertype'] == 'Subscriber']['age'].value_counts().head(10)
sns.barplot(x=top_ten_age_counts.index, y=top_ten_age_counts.values, color='skyblue')
plt.ylabel('Percentage')
plt.xlabel('Age')
plt.title('Top Ten Subscriber Ages (Percentage)')


df['duration_seconds'] = pd.to_timedelta(df['duration'].astype(str).str.replace('[^0-9:]', '', regex=True)).dt.total_seconds()
top_ten_durations = df['duration_seconds'].value_counts().head(15).index
df_top_ten = df[df['duration_seconds'].isin(top_ten_durations)]

top_durations_df = pd.DataFrame({
    'Duration': df_top_ten['duration_seconds'],
    'Subscriber': df_top_ten[df_top_ten['usertype'] == 'Subscriber']['duration_seconds'].value_counts().reindex(top_ten_durations, fill_value=0),
    'Customer': df_top_ten[df_top_ten['usertype'] == 'Customer']['duration_seconds'].value_counts().reindex(top_ten_durations, fill_value=0)
})

# Subplot 5: Bar Chart for Top Ten Durations
plt.subplot(2, 3, 5)
bar_width = 20
plt.bar(top_durations_df['Duration'], top_durations_df['Subscriber'], width=bar_width, label='Subscriber', color='skyblue')
plt.bar(top_durations_df['Duration'] + bar_width, top_durations_df['Customer'], width=bar_width, label='Customer', color='blue')
plt.xlabel('Duration (seconds)')
plt.ylabel('Count')
plt.title('Top Ten Durations for Customers and Subscribers')
plt.legend()


plt.tight_layout()
plt.show()
