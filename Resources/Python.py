import pandas as pd
import numpy

columns = ["City_ID	City","Cloudiness","Country	Date","Humidity","Lat","Lng","Max Temp","Wind Speed"
]
cities_df = pd.read_csv('cities.csv', names=columns)


# Use the .to_html() to get your table in html
cities_df.to_html("Data.htm") 
