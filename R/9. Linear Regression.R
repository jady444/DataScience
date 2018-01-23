# In this we will use linear regression to perdict the quality of wine

wine = read.csv("wine.csv")
str(wine)
summary(wine)

#----------------------------------------
model1 = lm(Price ~ AGST, data=wine)
summary(model1)

model1$residuals

SSE= sum(model1$residuals^2)
SSE

#----------------------------------------
model2 = lm(Price ~ AGST + HarvestRain, data=wine)
summary(model2)

model2$residuals

SSE= sum(model2$residuals^2)
SSE

#----------------------------------------
model3 = lm(Price ~ AGST + HarvestRain + WinterRain + Age + FrancePop, data=wine)
summary(model3)

model3$residuals

SSE= sum(model3$residuals^2)
SSE
