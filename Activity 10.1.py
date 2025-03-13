#-------------------------------------------------------------------------------
# Name:        Activity 10.1
# Purpose:     To investigate how the behaviour of the t statistic of a sample
#              compares with the behaviour of the z statistic of the population.
#
# Author:      Safwan
#
# Created:     12/03/2025
# Copyright:   (c) Safwan 2025
# Licence:     No liscence
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

#Import numpy and matplotlib's plotting tools.
import numpy as np
import matplotlib.pyplot as plt

#Create a function which takes a sample of said size from a normally distributed
#population that has a specified mean and standard deviation.
def selectSample(mean, stDev, sIze):

    #Select a sample of said size from a population of said mean and standard deviation.
    #Convert to string because matplotlib gives a messy list that we need to clean a bit.
    sample = str(np.random.normal(loc=mean, scale=stDev, size=sIze))

    #Convert the brackets into spaces to get rid of them and make the upcoming splitting easier.
    sample = sample.translate(str.maketrans({"[":" ", "]":" "}))

    #Split by _ to remove them.
    sample = sample.split(" ")

    #Remove empty strings leaving only strings containing numbers.
    while "" in sample:
        sample.remove("")

    #Convert strings into floating numbers.
    for i in sample:
        sample[sample.index(i)] = float(i)

    #Return the sample of values.
    return sample

#Create a class to store each sample, as well as related statistics.
class Sample:

    #A sample has a certain size and comes from a population with a certain mean
    #and standard deviation, so those are the arguments for the __init__ function.
    def __init__(self,popMean,popStdev,sampleSize):

        #Select values from a population with given traits using selectSample.
        self.Values = selectSample(popMean,popStdev,sampleSize)

        #Compute the sample mean.
        self.Mean = np.mean(self.Values)

        #Compute the sample standard deviation. ddof=1 because the denominator is
        #n-1, and ddof is how much n is subtracted by.
        self.Stdev = np.std(self.Values, ddof=1, mean=self.Mean)

        #Compute the Z statistic.
        self.Zstatistic = (self.Mean-popMean)*np.sqrt(sampleSize)/popStdev

        #Compute the T statistic.
        self.Tstatistic = ((self.Mean-popMean)/self.Stdev)*np.sqrt(sampleSize)

#Create a list to store the samples.
samples = []

#Pick 200 samples of 5 observations from a population with mean of 100 and standard
#deviation of 10.
for i in range(200):
    samples.append(Sample(100,10,5))

#Save the Z statistics and T statistics.
allZstatistics = []
allTstatistics = []
for i in samples:
    allZstatistics.append(i.Zstatistic)
    allTstatistics.append(i.Tstatistic)

#The activity requires that the histograms use the same scale. To encompass both
#histograms in their entirety, the maximum and minimum of BOTH lists combined is
#computed, giving the same range for BOTH histograms.
histMaxX = max(allZstatistics+allTstatistics)
histMinX = min(allZstatistics+allTstatistics)

#Find the highest bar for both histograms, denoted by YZ and YT.
YZ, bins, patches = plt.hist(allZstatistics)
YT, bins, patches = plt.hist(allTstatistics)

#Find the maximum of YZ and YT.
histMaxY = max(max(YZ),max(YT))

#Close this histogram since it is unnecessary.
plt.close()

#Make a histogram for the Z statistics.
plt.figure("Z statistic histogram")

#Set the figure's Y bounds and give a margin of about 10% of the highest bar.
plt.ylim(0,histMaxY*1.20)

#Make a histogram from all the Z statistics and set the range from the minimum
#to the maximum of BOTH Z and T statistics.
plt.hist(allZstatistics, range = (histMinX,histMaxX))

#Make a histogram for the Z statistics.
plt.figure("T statistic histogram")

#Set the figure's Y bounds and give a margin of about 10% of the highest bar.
plt.ylim(0,histMaxY*1.20)

#Make a histogram from all the T statistics and set the range from the minimum
#to the maximum of BOTH Z and T statistics.
plt.hist(allTstatistics, range = (histMinX,histMaxX))

#Show the plot!
plt.show()
