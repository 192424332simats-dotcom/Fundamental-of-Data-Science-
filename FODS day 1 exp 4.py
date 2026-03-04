import pandas as pd
property_data = pd.read_csv('C:/Users/bella/OneDrive/Documents/housing1.csv')
average_price_by_location = property_data.groupby('location')['listing_price'].mean()
properties_more_than_four_bedrooms = property_data[property_data['number_of_bedrooms'] > 4]
num_properties_more_than_four_bedrooms = len(properties_more_than_four_bedrooms)
property_with_largest_area = property_data.loc[property_data['area_in_square_feet'].idxmax()]
print("1. Average Listing Price by Location:")
print(average_price_by_location)
print("\n2. Number of Properties with More Than Four Bedrooms:", num_properties_more_than_four_bedrooms)
print("\n3. Property with the Largest Area:")
print(property_with_largest_area)

