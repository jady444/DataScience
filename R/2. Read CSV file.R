# Below command shows the location of acting working directory
getwd()

# Below command sets the location of working directory
setwd("E:/DB/R")

# Now from that directory we read the CSV file and assigning data to some variable

WHO <- read.csv("WHO.csv")
# WHO

# Below command will show the structure of the data frame by function str
str(WHO)

# Summary function will give the total summary of data set
summary(WHO)

# To take subset of data use subset function as shown below
WHO_Europe <- subset(WHO, Region == "Europe")

str(WHO_Europe)
summary(WHO_Europe)

# To write the data from dataset to CSV file
write.csv(WHO_Europe, "WHO_Europe.csv")

# To get the list of data set in R
ls()

# To remove the data set in R
rm(WHO_Europe)
