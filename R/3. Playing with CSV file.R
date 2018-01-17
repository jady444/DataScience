Under15
# Above command gives error as it is column of WHO data set.
# So to access it we use below command. And shows data of Under15 column

WHO$Under15

mean(WHO$Under15)   # for getting mean of the column
sd(WHO$Under15)     # for getting standard deviation of the column
summary(WHO$Under15)  # for getting summary of the column

which.min(WHO$Under15)  # to get the minimun data of the column
WHO$Country[86]         # to get the county name which has minimun data of the column

which.max(WHO$Under15)  # to get the maximum data of the column
WHO$Country[124]        # to get the county name which has maximumdata of the column

# Have scatter plot of the data 
plot(WHO$GNI, WHO$FertilityRate)  # X axis has GNI and Y axis has FertilityRate


# To have data only for GNI above 10000 and FertilityRate above 2.5, we will create subset for it
Outliners <- subset(WHO, GNI > 10000 & FertilityRate > 2.5)
plot(Outliners$GNI, Outliners$FertilityRate)

# To check how many rows are there we will use nrows function
nrow(Outliners)

# To get data of selected columns we use vector of column names
Outliners[c("Country","GNI","FertilityRate")]
