import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#Importing the COVID 19 dataset from John Hopkins University

corona_dataset_csv = pd.read_csv("Datasets/covid19_Confirmed_dataset.csv")
corona_dataset_csv.head()

#checking shape of dataframe

corona_dataset_csv.shape

#deleting columns that aren't needed

corona_dataset_csv.drop(["Lat","Long"],axis=1,inplace=True)
corona_dataset_csv.head(10)

#aggregating the rows by the country

corona_dataset_aggregated = corona_dataset_csv.groupby("Country/Region").sum()
corona_dataset_aggregated.head(10)

#visualizing data related to multiple countries

corona_dataset_aggregated.loc["China"].plot()
corona_dataset_aggregated.loc["Italy"].plot()
corona_dataset_aggregated.loc["Spain"].plot()
plt.legend()

#finding good measure represented as a number, describing spread of virus in a country

corona_dataset_aggregated.loc["China"].plot()
corona_dataset_aggregated.loc["China"][:3].plot()

#calculating the first derivative of the curve

corona_dataset_aggregated.loc["China"].diff().plot()

#finding the max infection rate for multiple countries

corona_dataset_aggregated.loc["China"].diff().plot()
corona_dataset_aggregated.loc["Spain"].diff().plot()
corona_dataset_aggregated.loc["Italy"].diff().plot()

#finding max infection rates for all countries

countries = list(corona_dataset_aggregated.index)
max_infection_rates = []
for c in countries :
        max_infection_rates.append(corona_dataset_aggregated.loc[c].diff().max())
corona_dataset_aggregated["max_infection_rate"] = max_infection_rates

corona_dataset_aggregated.head()

#creating a new dataframe with only needed columns

corona_data = pd.DataFrame(corona_dataset_aggregated["max_infection_rate"])
corona_data.head()

#importing the dataset

happiness_report_csv("Datasets/worldwide_happiness_report.csv")
happiness_report_csv.head()

#dropping the columns not needed

useless_cols = ["Overall rank", "Score", "Generosity", "Perceptions of corruption"]
happiness_report_csv.drop(useless_cols,axis=1,inplace=True)
happiness_report_csv.head()

#changing the index of dataframe

happiness_report_csv.set_index("Country or region",inplace=True)
happiness_report_csv.head()

#merging the two datasets

data = corona_data.join(happiness_report_csv,how="inner")
data.head()

#correlation matrix

data.corr()

#visualizing results and plotting graphs

#plotting GDP per capita vs max infection rate

x = data["GDP per capita"]
y = data["max_infection_rate"]
sns.scatterplot(x,np.log(y))

sns.regplot(x,nplog(y))

#plotting social support vs max infection rate

x = data["Social support"]
y = data["max_infection_rate"]
sns.scatterplot(x,np.log(y))

sns.regplot(x,nplog(y))

#plotting healthy life expectancy vs max infection rate

x = data["Healthy life expectancy"]
y = data["max_infection_rate"]
sns.scatterplot(x,np.log(y))

sns.regplot(x,nplog(y))

#plotting freedom to make life choices vs max infection rate

x = data["Freedom to make life choices"]
y = data["max_infection_rate"]
sns.scatterplot(x,np.log(y))

sns.regplot(x,nplog(y))

#results indicate a positive correlation between life factors and COVID infection rates
