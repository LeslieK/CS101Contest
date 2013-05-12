# Leslie B. Klein
# leslieklein@comcast.net
# Udacity CS101 Contest

# inputs: your food intake
# outputs: your percent RDI for many nutrients, including sugar
# food database: USDA National Nutrient Database for Standard Reference, Release 24
# DRI (Daily Recommended Intake) Tables: USDA National Agricultural Library
# foodIndex - a dictionary that stores food database ('ABBREV.txt')
# nutrientIndex - a dictionary that stores DRI for each nutrient in the foodIndex
# RDI (Recommended Daily Intake) values are read from 'RDI.csv' file

# The program supports reading in the RDI of multiple countries. (each stored in a separate text file)
# nutrientIndex is a dictionary organized like this:
# nutrientIndex[nutrient][country] is a list: [[rdivalues_country_1], [rdivalues_country2]]
# Would be interesting to compare graphs for the same food using n different sets of RDI values
# Since I do not know how to plot more than 1 set of data, I am running with 'US' only.


# col: nutrient
# [nutrient, weightUnit]
colHeadings = []
colHeadings.append(['Water', 6])
colHeadings.append(['Energ_Kcal', 7])
colHeadings.append(['Protein', 6])
colHeadings.append(['Lipid_Tot', 6])
colHeadings.append(['Ash', 6])
colHeadings.append(['Carbohydrt', 6])
colHeadings.append(['Fiber_TD', 6])
colHeadings.append(['Sugar_Tot', 6])
colHeadings.append(['Calcium', 3])
colHeadings.append(['Iron', 3])
colHeadings.append(['Magnesium', 3])
colHeadings.append(['Phosphorus', 3])
colHeadings.append(['Potassium', 3])
colHeadings.append(['Sodium', 3])
colHeadings.append(['Zinc', 3])
colHeadings.append(['Copper', 3])
colHeadings.append(['Manganese', 3])
colHeadings.append(['Selenium', 4])
colHeadings.append(['Vit_C', 3])
colHeadings.append(['Thiamin', 3])
colHeadings.append(['Riboflavin', 3])
colHeadings.append(['Niacin', 3])
colHeadings.append(['Panto_acid', 3])
colHeadings.append(['Vit_B6', 3])
colHeadings.append(['Folate_Tot', 4])
colHeadings.append(['Folic_acid', 4])
colHeadings.append(['Food_Folate', 4])
colHeadings.append(['Folate_DFE', 4])
colHeadings.append(['Choline_Tot', 3])
colHeadings.append(['Vit_B12', 4])
colHeadings.append(['Vit_A_IU', 5])
colHeadings.append(['Vit_A_RAE', 4])
colHeadings.append(['Retinol', 4])
colHeadings.append(['Alpha_Carot', 4])
colHeadings.append(['Beta_Carot', 4])
colHeadings.append(['Beta_Crypt', 4])
colHeadings.append(['Lycopene', 4])
colHeadings.append(['Lut+Zea', 4])
colHeadings.append(['Vit_E', 3])
colHeadings.append(['Vit_D_ug', 4])
colHeadings.append(['Vit_D_IU', 5])
colHeadings.append(['Vit_K', 4])
colHeadings.append(['FA_Sat', 6])
colHeadings.append(['FA_Mono', 6])
colHeadings.append(['FA_Poly', 6])
colHeadings.append(['Cholestrl', 3])
colHeadings.append(['GmWt_1',8])
colHeadings.append(['GmWt_Desc1', 8])
colHeadings.append(['GmWt_2', 8])
colHeadings.append(['GmWt_Desc2', 8])
colHeadings.append(['Refuse_Pct', 8])


# nutrients
nutrientNames = []
for i in range(len(colHeadings)-5):
    nutrientNames.append(colHeadings[i])


units = []
units.append('L')
units.append('g/kg')
units.append('g/1000kcal')
units.append('mg')
units.append('ug')
units.append('IU')
units.append('g')
units.append('kcal')
units.append('')    # '' means units are not applicable

def split_string(source, splitlist):

    split_pos = []  # list of the positions of the separation characters
    tokens = []

    # store delimiter positions
    for i in range(len(splitlist)):
        separator = splitlist[i]
        start = 0
        while start < len(source):
             end = source.find(separator, start)
             if end == -1:
                 break
             else:
                split_pos.append(end)
                start = end + 1
    split_pos.sort()

    # build token list
    start = 0

    for j in range(len(split_pos)):
        end = split_pos[j]
        if start == end:
            tokens.append('~~')
        else:
            tokens.append(source[start:end])
        start = end + 1
    tokens.append(source[start:])

    #remove \n
    tokens[-1] = tokens[-1][:-1]
    return tokens

# txt Food Index
# data source: US Dept of Agriculture
# Agriculture Research Service
# USDA National Nutrient Database for Standard Reference, Release 24
# ABBREVIATED database (flat file: ABBREV.txt) (2 MB)
foodIndex = {}
fhand = open('ABBREV.txt')
for line in fhand:
    tokens = split_string(line, ['^'])
    ndb = tokens[0][1:6]
    foodIndex[ndb] = []
    foodIndex[ndb].append(tokens[1][1:-1])
    token_list = []
    for i in range(2, len(tokens)):
        if tokens[i] != '':
            if tokens[i][0] != '~':
                token_list.append(float(tokens[i]))
            else:
                token_list.append(tokens[i][1:-1])
    foodIndex[ndb].append(token_list)
fhand.close()
'''
# text file: RDI Values per nutrient
# source: http://www.iom.edu/Activities/Nutrition/SummaryDRIs/~/media/Files/Activity%20Files/Nutrition/DRIs/5_Summary%20Table%20Tables%201-4.pdf
# USDA National Agricultural Library
# Dietary Reference Intakes: Recommended Intakes for Individuals
# pp. 2, 4, 5

# Note: nutrientIndex is structured to store multiple sets of RDI values for each nutrient
# Would be interesting to generate a plot for each countries values
# Need to learn about plotting in python
#
'''

'''
# RDIValue = [[unit], ['19-30','19-30'], ['31-50','31-50'], ['51-70','51-70'] ,['>70', '>70']]
# ageGroup[0] is male
# ageGroup[1] is female
'''

##CountryRDIFiles = ['RDIUS.txt', 'RDIUK.txt', 'RDIAUSNZ.txt']
##countries = ['US', 'UK', 'AUS']

CountryRDIFiles = ['RDIUS.txt']
countries = ['US']

# initialize nutrientIndex dictionary
nutrientIndex = {}
for i in range(len(nutrientNames)):
    nutrientIndex[nutrientNames[i][0]] = []
    for j in range(len(countries)):
        nutrientIndex[nutrientNames[i][0]].append([])
        
countryCnt = 0   
for RDIfile in CountryRDIFiles:
    rhand = open(RDIfile)
    for line in rhand:
        tokens = split_string(line, [','])
        nutrient = tokens[0][1:-1]
        unit = tokens[1]
        rdiValues = [int(unit)]
        nutrientIndex[nutrient][countryCnt].append(rdiValues)
        for i in range(2,10,2):
            rdiValues = [float(tokens[i]), float(tokens[i+1])]
            nutrientIndex[nutrient][countryCnt].append(rdiValues)
    countryCnt += 1
    rhand.close()

def getNutrientNumber(nutrientNames, nutrient):
    for i in range(len(nutrientNames)):
        if nutrient == nutrientNames[i][0]:
            return i
    else:
        return -1

def calcNutrientsConsumed(foodIndex, totalFood):
    '''
    foodIndex - index of food items
    totalFood - list of food: [[descr, ndb, wtInGrams], ..., ]
    '''
    totalNutrientsConsumed = []
    # set every elem to 0.
    for i in range(len(nutrientNames)):
        totalNutrientsConsumed.append(0.)
    for food in totalFood:
        foodNutrientsConsumed = []
        ndb = food[1]
        wtInGrams = food[2]
        nutrientList = foodIndex[ndb][1][:-5]
        for i in range(len(nutrientList)):
            if nutrientList[i] == '':
                 nutrientList[i] = 0
            per100Grams = nutrientList[i]
            unitsConsumed = per100Grams / 100. * wtInGrams # each nutrient has its own unit; converted to mg to calc rdi
            foodNutrientsConsumed.append(unitsConsumed)
        totalNutrientsConsumed = sum_nutrients(totalNutrientsConsumed, foodNutrientsConsumed)
    return totalNutrientsConsumed
       
def sum_nutrients(list1, list2):
    if len(list1) != len(list2):
        return 'list1 and list2 must be same size.'
    else:
        sumList = []
        for i in range(len(list1)):
            sumList.append(list1[i] + list2[i])
    return sumList
    
def calcPercentRDI(nutrientIndex, nutrientNames, nutrientsConsumed, age, gender, bodyWeightKg): 
    '''
    inputs:
    nutrientIndex - index of nutrients
    nutrientNames - list of nutrient names
    nutrientsConsumed - list of nutrients consumed
    age - a number
    gender - a string; 'female' or 'male'
    weight - in kg

    returns:
    percentRDI - a list (nutrient consumed)/(nutrient rdi), for each nutrient; [percent, percent, percent, ..., ]
    '''

    # initialize percentRDI
    percentRDI = {}
    for country in countries:
        percentRDI[country] = []
    
    if age >= 19 and age <=30:
        ageGroup = 1
    elif age > 30 and age <= 50:
        ageGroup = 2
    elif age > 50 and age <= 70:
        ageGroup = 3
    elif age > 70:
        ageGroup = 4
    else:
        print 'age must be at least 19'
        print 'assuming age is 19 - 30'
        ageGroup = 1
    if gender == 'female':
        x = 1
    else:
        x = 0

    for i in range(len(countries)):
        for elem in nutrientNames:
            number = getNutrientNumber(nutrientNames, elem[0])
            nutrient_in_mg = convert_to_mg(nutrientsConsumed[number], elem[1], 1.)
            if nutrientIndex[elem[0]][i] != []:               
                rdiUnit = nutrientIndex[elem[0]][i][0][0]
                rdi = float(nutrientIndex[elem[0]][i][ageGroup][x]) 
                rdi_in_mg = convert_to_mg(rdi, rdiUnit, bodyWeightKg)
                percent = nutrient_in_mg/rdi_in_mg * 100
                percentRDI[countries[i]].append(percent)
            else:
                percentRDI[countries[i]].append('No RDI.')
    return percentRDI

def convert_to_mg(quantity, unit, bodyWeightKg):
    if unit == 0:
        return quantity * 1000000.       # 1 L water = 1 kg; 1 kg = 1000000 mg
    elif unit == 1:
        return quantity * bodyWeightKg * 1000 # 1 g = 1000 mg 
    elif unit == 2:
        return quantity * 1000
    elif unit == 3:        
        return quantity            # in mg
    elif unit == 4:
        return quantity/1000.      # 1 mg = 1000 ug
    elif unit == 5:
        return quantity            # IU; do not convert IU
    elif unit == 6:
        return quantity * 1000     # 1 g = 1000 mg   
    
def calc_total_sugar(nutrientNames, nutrientsConsumed):
    number = getNutrientNumber(nutrientNames, 'Sugar_Tot')
    return nutrientsConsumed[number]
        
def print_percent_RDI(percentRDI, nutrientNames):
    for country in countries:
        for i in range(len(percentRDI[country])):
            if percentRDI[country][i] != 'No RDI.':
                print nutrientNames[i][0] + ': ' + str(percentRDI[country][i])

def getDataToPlot(nutrientNames, percentRDI):
    x_list = {}
    y_list = {}
    for country in countries:
        x_list[country] = []
        y_list[country] = []
    
    for country in countries:
        for i in range(len(percentRDI[country])):
            if percentRDI[country][i] != 'No RDI.':
                y_list[country].append(percentRDI[country][i])
                x_list[country].append(nutrientNames[i][0])
    return x_list, y_list
    
def plotData(nutrientNames, percentRDI):
    # need to make this work for len(countries) > 1
    # This code was based on a tutorial here:
    # http://scienceoss.com/bar-plot-with-custom-axis-labels/
    # Boy, was I lucky to find it!!!
    
    '''
    x_list - nutrientsConsumed
    y_list - percent_of_rdi values

    '''
    #from matplotlib import pyplot 
    from matplotlib import pylab as p
    fig = p.figure()
    ax = fig.add_subplot(1, 1, 1)

    
    x_list, y_list = getDataToPlot(nutrientNames, percentRDI)

    # as written, only works for 1 country
    for country in countries:
        # number of bars
        N = len(x_list[country])
        # bar height
        height = y_list[country]

        # x-axis
        ind = range(N) # x locations
        
        # plot data
        ax.bar(ind, height, align='center')

        # set labels
        ax.set_xlabel('Nutrients Consumed')
        ax.set_xticks(ind)
        xlabels = x_list[country]
        ax.set_xticklabels(xlabels)
        fig.autofmt_xdate()

        # create a y-label
        ax.set_ylabel('Percent RDI')

        p.show()

## Go Shopping!!!!   
## Use this procedure to get a subset of food from the US gov data base (ABBREV.txt)
## Then manually cut and paste to make a list of food for a meal.
## Append to each foodList [ food, ndb# ] a wtInGrams => [ food, ndb#, wtInGrams ]

def searchForFoodItem(item):
    '''
    item - a string identifying a food item; for ex, 'CEREAL'
    '''
    ITEM = item.upper()
    count = 0
    foodList = []
    for ndb in foodIndex:
        descr = foodIndex[ndb][0]
        res = descr.find(ITEM)
        if res != -1:
            count = count + 1
            foodList.append([descr[:40], ndb])
    print str(count) + ' items found matching ' + item
    return foodList

## test case: CHEESE,GRUYERE, 50g
##nutrientsConsumed = calcNutrientsConsumed(foodIndex, [['CHEESE,GRUYERE', '01023', 50.]])
##percentRDI = calcPercentRDI(nutrientIndex, nutrientNames, nutrientsConsumed, age=20, gender='female', bodyWeightKg=55)
##print_percent_RDI(percentRDI, nutrientNames)
'''
Results from www.fitday.com (my results):
Protein: 32 (41) (bodyWeightKg = 55)
Carbs: 0 (0.1)
Fiber: 0 (0)
Calcium: 42 (50)
Iron: 1 (0.5)
Magnesium: 6 (5.1)
Phosphorus: 43 (43.2)
Zinc: 24 (24.4)
Cooper: 2 (1.8)
Manganese: 0 (0.5)
Selenium: 13 (13.2)
Vit C: 0 (0)
Thiamin: 3 (2.7)
Riboflavin: 13 (12.6)
Niacin: 0 (0.4)
Panto Acid: 6 (5.6)
Vit B-6: 3 (3.1)
Vit B-12: 33 (33.3)
Vit A: 19 (19.4)
Vit E: 1 (0.9)
Vit D: 0 (2)
'''
# Define meals
# Hungry? Change this value accordingly.
wtInGrams = 75.
breakfast1 = [ ['CEREALS RTE,QUAKER,TSTD OATMEAL SUPREME ', '08545', 1.2*wtInGrams], \
              ['MILK,WHL,3.25% MILKFAT,WO/ ADDED VIT A &', '01211', 2*wtInGrams], \
              ['BANANAS,RAW', '09040', .5*wtInGrams], \
              ['ALMONDS,DRY RSTD,WO/SALT', '12063', .2*wtInGrams] ]

lunch1 = [ ['TOMATOES,RED,RIPE,RAW,YEAR RND AVERAGE', '11529', wtInGrams], \
          ['LETTUCE,COS OR ROMAINE,RAW', '11251', .5*wtInGrams], \
          ['OLIVES,RIPE,CND (SMALL-EXTRA LRG)', '09193', wtInGrams], \
          ['CHEESE,FETA', '01019', 1.2*wtInGrams], \
          ['AVOCADOS,RAW,ALL COMM VAR', '09037', wtInGrams], \
          ['VINEGAR,BALSAMIC', '02069', .5*wtInGrams] ]

dinner1 = [ ['SALMON,ATLANTIC,FARMED,CKD,DRY HEAT', '15237', 4*wtInGrams],\
            ['COLLARDS,CKD,BLD,DRND,WO/SALT', '11162', 2*wtInGrams],\
            ['SWEET POTATO,CKD,BLD,WO/ SKN,W/ SALT', '11876', wtInGrams],\
            ['CABBAGE,RED,CKD,BLD,DRND,W/SALT', '11752', wtInGrams] ]

drinks1 = [ ['COFFEE,INST,REG,PDR,HALF THE CAFFEINE', '14203', 4*wtInGrams],\
            ['TEA,RTD,LIPTON BRISK ICED TEA,W/ LEMON F', '14476', 2*wtInGrams] ]

breakfast2 = [ ["MCDONALD'S,SCRMBLD EGGS", '21320',2*wtInGrams ],\
               ["MCDONALD'S,BISCUIT,LRG SIZE", '21460', wtInGrams],\
               ['COFFEE,INST,REG,PDR,HALF THE CAFFEINE', '14203', 2*wtInGrams] ]

lunch2 = [ ["MCDONALD'S,CAESAR SALAD W/ GRILLED CHICK", '21370', 2*wtInGrams],\
           ['CARBONATED BEV,COLA,CONTAINS CAFFEINE', '14400', 2*wtInGrams],\
           ["MCDONALD'S,MCFLURRY W/ OREO COOKIES", '21339', wtInGrams] ]

dinner2 = [ ["MCDONALD'S,DOUBLE CHEESEBURGER", '21344', 2*wtInGrams],\
            ["MCDONALD'S,FRENCH FR", '21238', 2*wtInGrams], \
            ['CARBONATED BEV,COLA,CONTAINS CAFFEINE', '14400', 2*wtInGrams] ]

def mealPlan(list_of_meals):
    totalFood = []
    for elem in list_of_meals:
        totalFood = totalFood + elem
    return totalFood

# UNCOMMENT 1 of the meal plans

## Healthful Plan
totalFood1 = mealPlan([breakfast1, lunch1, dinner1, drinks1])
consumed = calcNutrientsConsumed(foodIndex, totalFood1)

#### McDonald's Food Plan
##totalFood2 = mealPlan([breakfast2, lunch2, dinner2])
##consumed = calcNutrientsConsumed(foodIndex, totalFood2)

def analyzeFood():
    bodyWeight = raw_input('Enter your bodyWeight in Kg (default = 55): ')
    if (not (bodyWeight not in range(30, 200))) or (bodyWeight == ''):
        bodyWeightKg = 55.
    print 'bodyWeight set to ', bodyWeightKg

    gender = raw_input("Enter your gender (male or female; default = female): ")
    if (gender != 'male' and gender != 'female'):
        gender = 'female'
    print 'gender set to ', gender

    age = raw_input("Enter your age (default = 20): ")
    if (not(age.isdigit()) or (int(age) not in range(19, 120))):
        age = 20
    print 'age set to ', age
    print

    percentRDI = calcPercentRDI(nutrientIndex, nutrientNames, consumed, age=20, gender='female', bodyWeightKg=55.)              
    print 'Total Calories Consumed (kcal): ', consumed[1]
    print 'Total Protein Consumed (g): ', consumed[2]
    print 'Total Fat Consumed (g): ', consumed[3]
    print 'Saturated Fat Consumed (g): ', consumed[42]
    print 'Total Sodium Consumed (mg): ', consumed[13]
    print 'Total Carbohydrates Consumed (g): ', consumed[5]
    print 'Total Sugar Consumed (g) : ', consumed[7]
    print 'New Sugar recommendations:'
    print 'adult men - 36 g/day'
    print 'adult women - 20 g/day'
    print 'children - 12 g/day)'
    print 'Plotting RDI vs nutrients...'
    plotData(nutrientNames, percentRDI)
