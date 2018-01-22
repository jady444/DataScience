# To know the data with count we will use table function.
# This will show the count of data which has 0 and 1
table(USDA$HighSodiumValue)

# To know the data which has both high sodium and high fat we will pass second variable in the above function.
# The data will be show in table
table(USDA$HighSodiumValue, USDA$HighFat)

# Tapply function
# It will group the Iron level data, group will be created by second argument which is HighProtein.
# Now third argument will mean the data of each group
tapply(USDA$Iron, USDA$HighProtein, mean, na.rm=TRUE)

tapply(USDA$VitaminC, USDA$HighCarbohydrate, max, na.rm=TRUE)

tapply(USDA$VitaminC, USDA$HighCarbohydrate, summary, na.rm=TRUE)
