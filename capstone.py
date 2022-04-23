import pandas as pd
import matplotlib.pyplot as plt

def yearwisePrice(df):
    dfnew = df[["Year","price"]]
    groupeddfnew = dfnew.groupby("Year")
    mediandfnew = groupeddfnew.median().reset_index()
    plt.plot(mediandfnew["Year"],mediandfnew["price"], color='red', marker='o')
    plt.title('London House Prices Over The Years')
    plt.xlabel('Year')
    plt.ylabel('Price In Pounds')
    plt.grid(True)
    plt.show()

def districtwisePrice(df):
    df = df[["Year","district","price"]]
    dfnew = df[df["Year"] > "2015"]
    dfnew = dfnew[["district","price"]]
    groupeddfnew = dfnew.groupby("district")
    mediandfnew = groupeddfnew.median().reset_index()
    meandfnewleastfive = mediandfnew.sort_values(by = "price")
    cheapestdistricts = meandfnewleastfive.head().reset_index()
    lscheapest5districts = cheapestdistricts["district"].unique()
    plt.barh(mediandfnew["district"], mediandfnew["price"])
    plt.title('House Prices In Different Districts')
    plt.xlabel('Price in Fractions of Millions of Pounds')
    plt.show()
    return lscheapest5districts

def districtYearWise(df,lscheapest5districts):
    dfnew = df[["Year","price","district"]]
    for item in lscheapest5districts:
        districtdf = dfnew[dfnew["district"] == item]
        groupeddfnew = districtdf.groupby("Year")
        mediandfnew = groupeddfnew.median().reset_index()
        plt.plot(mediandfnew["Year"],mediandfnew["price"], label=item, marker='o')
        plt.title('House Prices In Top 5 Affordable Districts')
    plt.xlabel('Year')
    plt.ylabel('Price In Pounds')
    plt.grid(True)
    plt.legend()
    plt.show()

def toplocations(df):
    dfnew1 = df[["Year","district","price","area","distance_to_station"]]
    dfnew2 = dfnew1[dfnew1["Year"] == "2021"]
    dfnewarea = dfnew2[dfnew2["area"] > 150]
    dfnewarealom = dfnewarea[dfnewarea["distance_to_station"] < 2]
    dfnewarealompl4 = dfnewarealom[dfnewarealom["price"] < 1000000].reset_index()
    return dfnewarealompl4


df = pd.read_csv("https://raw.githubusercontent.com/thakuraman2195/pythontest/main/London_House_Prices_data.csv")
df["Year"] = df["date"].str[:4]
yearwisePrice(df)
lscheapest5districts = districtwisePrice(df)
dfcheapest5districts = df[df["district"].isin(lscheapest5districts)]
districtYearWise(df,lscheapest5districts)
locations = toplocations(dfcheapest5districts)
print(locations)
print("Here are your Top 2 properties. Python Was Fun! Thank you!")