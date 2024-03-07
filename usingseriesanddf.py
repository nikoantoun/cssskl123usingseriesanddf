import pandas as pd
import numpy as np

#Task 1: Read in the data file and save its contents as a DataFrame object
fileName = 'flag.data'
#columns of data file
columns = [
    'name', 'landmass', 'zone', 'area', 'population', 'language', 'religion',
    'bars', 'stripes', 'colours', 'red', 'green', 'blue', 'gold', 'white', 'black',
    'orange', 'mainhue', 'circles', 'crosses', 'saltires', 'quarters', 'sunstars',
    'crescent', 'triangle', 'icon', 'animate', 'text', 'topleft', 'botright'
]
flags = pd.read_csv(fileName, header=None, names=columns) #read the file

#Task 2: Print out how many countries in the dataset are in North America.
numCountriesNorthAmerica = flags[flags['landmass'] == 1].shape[0] #North America = Landmass #1
print('Number in North America: ', numCountriesNorthAmerica) #print number of countries in North America

#Task 3: Print out how many countries are in each of the landmasses, using explicit loops
numLandmassLoops = {}
for i, row in flags.iterrows(): #traverse each index, checking the landmass of each country
    landmass = row['landmass']
    if landmass in numLandmassLoops: numLandmassLoops[landmass] += 1 #increment count
    else: numLandmassLoops[landmass] = 1 #sets to 1
#print, using a formatted way to output the counts
printLoopCountries = "\n".join([f"{landmass}   {count}" for landmass, count in sorted(numLandmassLoops.items())]) #format
print('Using explicit loops:\n', printLoopCountries) #print

#Task 3, without using explicit loops
numLandmassNoLoops = flags['landmass'].value_counts().to_dict() #use df value_counts() to track the count of each country in the col landmass, then convert to dictionary
#print, using the same formatted way
printCountriesNoLoops = flags['landmass'].value_counts().sort_index().to_string() #format
print('Without using explicit loops:\n', printCountriesNoLoops) #print

#Task 4 print total population in millions of countries that speaks each language
totalPopPerLang = flags.groupby('language')['population'].sum().sort_values(ascending=False) / 1000 #total population per language
printTotalPop = totalPopPerLang.apply(lambda x: f"{int(x * 1000)}") #formats total population per language
print(printTotalPop.to_string()) #print converted total population per language, using toString()

#Task 4, print total population in millions of countries UNDER 50 million that speaks each language
popLessThan50 = flags[flags['population'] < 50] #for countries with a population < 50m
totalPopPerLang50 = popLessThan50.groupby('language')['population'].sum().sort_values(ascending=False) / 1000 #same as totalPopPerLang, but with popLessThan50
printTotalPopPerLang50 = totalPopPerLang50.apply(lambda x: f"{int(x * 1000)}") #formats the under 50m var
print(printTotalPopPerLang50.to_string()) #print converted total population per language under 50m, using toString()

#Task 5: Create a merged DataFrame object that is the intersection of flags dataset and an employee dataset, then print (see print statement)
reps = {
    "Rep Name": ["Max", "Jill", "Fong", "Juanita", "Nya"],
    "Rep Language": [1, 2, 5, 5, 8]
}
dfReps = pd.DataFrame(reps) #create DataFrame of reps
mergeDfReps = pd.merge(flags, dfReps, left_on='language', right_on='Rep Language') #merge flags df with reps for the col language
totalReps = mergeDfReps.groupby('Rep Name').size().sum() #count total of representative-countries
print('Total representative-countries: ', totalReps) #print the total number of "representative-countries" your sales team covers based on language spoken.

#Task 6: print a table showing the total area of countries for each possible combination of landmass and language
areaOfCountriesTable = flags.pivot_table(values='area', index='landmass', columns='language', aggfunc='sum')
print(areaOfCountriesTable) #print

