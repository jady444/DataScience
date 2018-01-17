Country <- c("Brazil","China","India","Switzerland","USA")
LifeExpectancy <- c(74,76,65,83,79)

# To add both the variable Country & LifeExpectancy data.frame

CountryData <- data.frame(Country, LifeExpectancy)
CountryData

# The above example shows to add two variables 

# To add extra column to data we can use below function

CountryData$Population <- c(100000,122000,1300056,987645,123456)
CountryData

# To add new rows of data we need to have other 3 vectors for all the 
# columns we use rbind

Country <- c("Australia","Greece")
LifeExpectancy <- c(82,80)
Population <- c(23050,11125)

NewCountryData <- data.frame(Country, LifeExpectancy, Population)
NewCountryData

AllCountry <- rbind(CountryData, NewCountryData)
AllCountry