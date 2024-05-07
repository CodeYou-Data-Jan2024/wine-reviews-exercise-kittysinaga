import pandas as pd

# read the file in the data folder 
file_path1="C:/Users/kitty/wine-reviews-exercise-kittysinaga/data/winemag-data-130k-v2.csv.zip"
df=pd.read_csv(file_path1)

# create a data frame by country and sum of reviews (taster name)
summary1=df.groupby("country").taster_name.value_counts()

# create a series by country and average points
summary2=df.groupby("country").points.mean()

# specify only 1 decimal point
pd.set_option("display.precision",1)

# combine both series, with 1st column being country
summary=pd.merge(summary1,summary2,on="country")

# write the data frame onto a csv file
file_path2="C:/Users/kitty/wine-reviews-exercise-kittysinaga/data/reviews-per-country.csv"
summary.to_csv(file_path2,index=False)
