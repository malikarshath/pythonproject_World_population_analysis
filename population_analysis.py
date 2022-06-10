import time

print("Data analysis of world population.\n")

time.sleep(1)

def data():
    global scan_file
    global all_year
    scan_file = {}
    file = open("Programming Exercise Data - World Population Data.csv", "r")
    for row in file:
        scan_file[row.strip().split(',')[0]] = row.strip().split(',')[1:]
    print('All data from csv file has been read into dictionary.\n')

    all_year = list(scan_file.items())[0][1]

def statistics():
    global scan_file
    global all_year
    while True:
        year = input(f"Select a year to find the statistics {all_year[0]}-{all_year[-1]}: ")
        if year not in all_year:
            print("Sorry that is not a valid year")
            continue
        else:
            break
    index = all_year.index(year)

    list_of_population = [float(value[index]) for value in scan_file.values()][1:]

    maximum_population, minimum_population = max(list_of_population), min(list_of_population)

    country_with_max_index = list_of_population.index(maximum_population)
    country_with_min_index = list_of_population.index(minimum_population)

    country_with_max = list(scan_file.keys())[1:][country_with_max_index]
    country_with_min = list(scan_file.keys())[1:][country_with_min_index]

    print(
        f"In {year} countries with minimum and maximum population were: [{country_with_max}:{int(maximum_population)}] and [{country_with_min}:{int(minimum_population) }] respectively!\n")


def growth_percentage():
    global scan_file
    global all_year
    growth_percent = {}
    for value in list(scan_file.keys())[1:]:
        growth_percent[value] = 100 * ((float(scan_file[value][-1]) - float(scan_file[value][0]))) / float(scan_file[value][0])

    list_of_gp = [value for value in growth_percent.values()]
    max_gp,min_gp=max(list_of_gp),min(list_of_gp)
    max_gp_country_index =list_of_gp.index(max_gp)
    min_gp_country_index =list_of_gp.index(min_gp)
    max_gp_country = list(growth_percent.keys())[max_gp_country_index]
    min_gp_country = list(growth_percent.keys())[min_gp_country_index]

    print(f'From 1960 to 2020 the countries with maximum and minimum growth percentages were: [{max_gp_country}:{round(max_gp,1)}%] and [{min_gp_country}:{round(min_gp,1)}%] respectively!\n')
def period_growth_percentage():
    global scan_file
    global all_year
    while True:
        starting_year = input("Enter starting year: ")
        ending_year = input("Enter ending year: ")
        starting_index, ending_index = all_year.index(starting_year), all_year.index(ending_year)
        if starting_index < ending_index:
            gp = {}
            for value in list(scan_file.keys())[1:]:
                gp[value] = 100 * (
                    (float(scan_file[value][ending_index]) - float(scan_file[value][starting_index]))) / float(
                    scan_file[value][starting_index])
            list_of_gp = [float(value) for value in gp.values()]
            max_gp, min_gp = max(list_of_gp), min(list_of_gp)
            max_gp_country_index = list_of_gp.index(max_gp)
            min_gp_country_index = list_of_gp.index(min_gp)
            max_gp_country = list(gp.keys())[max_gp_country_index]
            min_gp_country = list(gp.keys())[min_gp_country_index]
            print(f'From {starting_year} to {ending_year} the countries with maximum and minimum growth percentages were: [{max_gp_country}:{round(max_gp,1)}%] and [{min_gp_country}:{round(min_gp,1)}%] respectively!\n')
            break
        else:
            print("starting year has to be less then ending year")
            continue

def future_growth():
    global scan_file
    global all_year
    while True:
        country_forecast = input("Enter the country to visualize data: ").title()
        Year_forecast = int(input("Enter number of years to find future growth rate: "))

        if country_forecast in scan_file.keys():
            growth_percentage = 100 * ((float(scan_file[country_forecast][-1]) -float(scan_file[country_forecast][(-1-Year_forecast)]))/float(scan_file[country_forecast][(-1-Year_forecast)]))
            estimation = float(scan_file[country_forecast][-1]) + (
                        (float(scan_file[country_forecast][-1]) / 100) * round(growth_percentage, 1))
            print(
                f"For {country_forecast} population will go from {int(scan_file[country_forecast][-1])} to {int(estimation)} in year {int(all_year[-1]) + Year_forecast}")
            break
        else:
            print("Sorry that is not a valid country.")
            continue

try:
    data()
    time.sleep(1)
    statistics()
    time.sleep(1)
    growth_percentage()
    time.sleep(1)
    period_growth_percentage()
    time.sleep(1)
    future_growth()

except:
    print("File not found")
