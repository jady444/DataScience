# To see histogram chart of any column data using below fuction
hist(WHO$CellularSubscribers)

# To see box plot of any column data with respect to specific column
# using below fuction
boxplot(WHO$LifeExpectancy ~ WHO$Region)

# Below function with arguments will show the data with lables for X,Y axis and Main name for the chart
boxplot(WHO$LifeExpectancy ~ WHO$Region, xlab="", ylab="Life Expectancy", main="Life Expectancy by Region")

# This will show the data in table as we have seen in summary function
table(WHO$Region)

# This will show the mean Region wise of population Over60 column
tapply(WHO$Over60, WHO$Region, mean)

# Below function is to find the minimun of Literacy rate region wise and shows NA
# NA is displayed as we dont have all the data in LiteracyRate column
tapply(WHO$LiteracyRate, WHO$Region, min)

# To over come the above issue we use same command with argument in it
# This na.rm will neglect the data who is NA
tapply(WHO$LiteracyRate, WHO$Region, min, na.rm=TRUE)

# Assignment
tapply(WHO$ChildMortality, WHO$Region, mean)
