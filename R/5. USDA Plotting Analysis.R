# Reading the USDA file in data frame USDA
USDA <-  read.csv("USDA.csv")

# Show all columns of data frame USDA
str(USDA)

summary(USDA)

USDA$Sodium

# Below function shows the index which has maximun value of Sodium in it
which.max(USDA$Sodium)

# Below function displays all the columns of the data frame
names(USDA)

USDA$Description[265]

# Creating subset of USDA as HighSodium which has more than 10000 Sodium in it
HighSodium <- subset(USDA, Sodium>=10000)

nrow(HighSodium)  # Displays no of rows in dataset
str(HighSodium)
summary(HighSodium)

HighSodium$Description

# To find the Product index whose name is Caviar using macth function in Description column
match("CAVIAR", USDA$Description)

USDA$Sodium[4154]

# To short the above 2 steps we can use below code
USDA$Sodium[match("CAVIAR", USDA$Description)]

summary(USDA$Sodium)
sd(USDA$Sodium, na.rm = TRUE)

# To plot the graph of data we use plot function. In this first argument will be for X axis and second argument will be for Y axis
plot(USDA$Protein, USDA$TotalFat)

# Here we added more arguments for naming the X & Y axis.
# Also added main argument to name the graph with color of graph to be red
plot(USDA$Protein, USDA$TotalFat, xlab="Protein", ylab="Fat", main="Protein vs Fat", col="Red")

# Now we will see the histogram graph
# Note: In histogram we can use only 1 axis as other will be for bars
hist(USDA$VitaminC, xlab = "Vitamin C (mg)", main = "Histogram of Vitamin C Levels")

# To distribute the graph in many proper graphs we add limit to X axis
hist(USDA$VitaminC, xlab = "Vitamin C (mg)", main = "Histogram of Vitamin C Levels", xlim=c(0,100))

# To distribute the graph in many proper graphs we add limit to X axis and now break them into 1mg to see the data
hist(USDA$VitaminC, xlab = "Vitamin C (mg)", main = "Histogram of Vitamin C Levels", xlim=c(0,100), breaks = 2000)

# Now we will see the box plot of the data and it is also for 1 variable means one column
boxplot(USDA$Sugar, main="Boxplot of Sugra Levels")

boxplot(USDA$Sugar, main="Boxplot of Sugra Levels", ylab="Sugar (g)")
