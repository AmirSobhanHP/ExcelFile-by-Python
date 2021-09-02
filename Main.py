# install Required packages
# pip install openpyxl
# pip install pandas
import pandas
country = ["Iran","Germany","Italy","Russia"]
city = ["Tehran","Berlin","Rome","Moscow"]
continent = ["Asia","Europa","Europa","Eurasia"]
myDict={
    "country": country,
    "city": city,
    "continent": continent,
}
myDict_Data = pandas.DataFrame(myDict) # make data frame 
myDict_Data.to_excel(r"E:\My Projects\Python\ExcelFile-by-Python\file.xlsx",index=False) # convert data frame to excel file.int () enter location to create file.