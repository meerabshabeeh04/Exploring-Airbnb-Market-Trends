import numpy as np
import pandas as pd
airbnbcsv = pd.read_csv('airbnb_price.csv')  # Airbnb prices data from CSV file
airbnbexcel = pd.read_excel('airbnb_room_type.xlsx')  # Airbnb room types data from Excel file
airbnbtsv = pd.read_csv('airbnb_last_review.tsv', sep='\t')  # Airbnb last review dates from TSV file
print(airbnbcsv.head())  # Preview of the price data
print(airbnbexcel.head())  # Preview of the room type data
print(airbnbtsv.head())  # Preview of the last review data
# Merge the datasets on 'listing_id', which is the common column in all data
data = airbnbcsv.merge(airbnbexcel, on='listing_id')  # Merging price and room type data
data = data.merge(airbnbtsv, on='listing_id')  # Adding last review data to the merged dataframe
print(data)
# Convert the 'last_review' column to datetime format
data['last_review'] = pd.to_datetime(data['last_review'], infer_datetime_format=True)
# Find the earliest and most recent review dates
earliest = data['last_review'].min()  # The earliest review date
most_recent = data['last_review'].max()  # The most recent review date
print(earliest)
print(most_recent)
# Display the 'room_type' column
print(data['room_type'])
# Convert room types to lowercase for uniformity
data['room_type'] = data['room_type'].str.lower()
# Get the count of private rooms (second most common room type, index [1])
private_rooms = data['room_type'].value_counts()[1]
# Clean the 'price' column by removing 'dollars' text and converting to float
data['price'] = data['price'].str.replace('dollars', '').astype('float')
print(data['price'])
# Calculate the average price of listings
avg_listing_price = data['price'].mean()
print(avg_listing_price)
# Create a DataFrame with the review dates, number of private rooms, and average price
review_dates = pd.DataFrame({
    'first_reviewed': [earliest],  # Earliest review date
    'last_reviewed': [most_recent],  # Most recent review date
    'nb_private_rooms': [private_rooms],  # Number of private rooms
    'avg_price': [avg_listing_price.round(2)]  # Average listing price, rounded to 2 decimal places
})
print(review_dates)
