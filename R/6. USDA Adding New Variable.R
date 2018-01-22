# To check the 1st value of sodium is greater than average value of Sodium
USDA$Sodium[1] > mean(USDA$Sodium, na.rm = TRUE)

USDA$Sodium[50] > mean(USDA$Sodium, na.rm = TRUE)

# Now to check for every data, this will check of lot of data and will not display properly
USDA$Sodium > mean(USDA$Sodium, na.rm = TRUE)

# So to overcome above situation we can assign the value to new dataset
HighSodiumValue = USDA$Sodium > mean(USDA$Sodium, na.rm = TRUE)

str(HighSodiumValue)

# The data above is in TRUE and FALSE, but we want that to be numeric 0 and 1.
# So we will use the numeric function to do so
HighSodiumValue = as.numeric(USDA$Sodium > mean(USDA$Sodium, na.rm = TRUE))

str(HighSodiumValue)

# Now we want to add the data to our dataset of USDA so we will use the below function
# It will create the new column of HighSodiumValue to our dataset of USDA
USDA$HighSodiumValue = as.numeric(USDA$Sodium > mean(USDA$Sodium, na.rm = TRUE))

str(USDA)

# Now lets add the same thing for HighProtein, HighFat, HighCarbohydrate
USDA$HighProtein = as.numeric(USDA$Protein > mean(USDA$Protein, na.rm = TRUE))
USDA$HighFat = as.numeric(USDA$TotalFat > mean(USDA$TotalFat, na.rm = TRUE))
USDA$HighCarbohydrate = as.numeric(USDA$Carbohydrate > mean(USDA$Carbohydrate, na.rm = TRUE))

str(USDA)
