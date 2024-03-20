import pandas as pd

df = pd.read_csv('route.csv')

count_routes = df.groupby(['user_type', 'from_station_name', 'from_station_latitude', 'from_station_longitude', 'to_station_name', 'to_station_latitude', 'to_station_longitude']).size().reset_index(name='count')

#print(count_routes)

#count_routes.to_csv('count_routes.csv', index=False)

# Count Subscribers

filtered_subscriber = count_routes[count_routes['user_type'] == 'Subscriber']

subscriber = filtered_subscriber.sort_values(by='count', ascending=False).head(15)

subscriber.to_csv('subscriber_routes.csv', index=False)


print("Ready by Subscriber")

# Count Customers

filtered_subscriber = count_routes[count_routes['user_type'] == 'Customer']

subscriber = filtered_subscriber.sort_values(by='count', ascending=False).head(15)

subscriber.to_csv('customers_routes.csv', index=False)


print("Ready by Customer")