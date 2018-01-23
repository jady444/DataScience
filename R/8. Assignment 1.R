# -----------------Problem 1------------------------------------
# Loading the data from CSV file to poll variable
poll <- read.csv("AnonymityPoll.csv")

summary(poll)
str(poll)

summary(poll$Smartphone)
table(poll$Smartphone)

table(poll$State, poll$Region)

# Other way is to create the subset of data whose region is Midwest

MidwestInterviewees = subset(poll, Region=="Midwest")
str(MidwestInterviewees)

table(MidwestInterviewees$State)
# -----------------Problem 2------------------------------------
str(poll)

table(poll$Internet.Use, poll$Smartphone)

summary(poll$Internet.Use)
summary(poll$Smartphone)

limited = subset(poll, poll$Internet.Use==1 | poll$Smartphone==1)
str(limited)

# -----------------Problem 3------------------------------------
summary(limited)

mean(limited$Info.On.Internet)
table(limited$Info.On.Internet)

str(limited)
table(limited$Worry.About.Info)

summary(limited$Worry.About.Info)

summary(limited$Anonymity.Possible)

summary(limited$Tried.Masking.Identity)

summary(limited$Privacy.Laws.Effective)

# -----------------Problem 4------------------------------------

hist(limited$Age)

plot(limited$Age, limited$Info.On.Internet)
max(table(limited$Age, limited$Info.On.Internet))

# By running the command jitter multiple times, we can see that the jitter function randomly adds or subtracts a small value from each number, and two runs will yield different results.
jitter(c(1, 2, 3))


plot(jitter(limited$Age), jitter(limited$Info.On.Internet))

tapply(limited$Info.On.Internet, limited$Smartphone, mean, na.rm=TRUE)

tapply(limited$Tried.Masking.Identity, limited$Smartphone, mean, na.rm=TRUE)

