import pandas as pd
'''Where the CSV are stored'''
DIR_NAME = 'data/'
'''Filename of the confirmed cases CSV. This file is obtained from data
held by the John Hopkings University'''
CONF_FILE_NAME = 'confirmed.csv'

'''Filename of the confirmed deaths CSV. This file is obtained from data
held by the John Hopkings University'''
DEATH_FILE_NAME = 'deaths.csv'

'''Where the result CSV will be stored'''
CONF_TARGET_FILE = 'conf_per_day.csv'

'''Where the result CSV will be stored'''
DEATH_TARGET_FILE = 'deaths_per_day.csv'

'''Columns not to be used for further analysis
Province/State: The state within the country where the reports comes from
Lat/Long: The latitude and longitude of the reports
'''
UNUSED_COLS = ['Province/State', 'Lat', 'Long']


'''The country column has an ugly name. This constants references to it'''
ORIGINAL_COUNTRY_COL_NAME = 'Country/Region'

'''A more short and beautiful column name for the country'''
COUNTRY_COL_NAME = 'Country'


def parse_file(file_name, target):
    #Dictionary to make the replacement of the column names
    COLS_REPLACE = {ORIGINAL_COUNTRY_COL_NAME: COUNTRY_COL_NAME}
    #Read the CSV.
    print('Reading file "%s%s"...' % (DIR_NAME, file_name))
    data = pd.read_csv('%s%s' % (DIR_NAME, file_name))
    print("done!")
    data.drop(UNUSED_COLS, 1, inplace=True)
    data.rename(columns=COLS_REPLACE, inplace=True)
    #Group by country (to summarize the data from the provinces/states)
    print("Making group by operations...")
    group = data.groupby('Country').sum()
    # In the original file the rows represents the countries and the columns
    # represents the dates. It's more useful the other way around
    by_date = group.transpose()
    print("done!")
    #Rename index col, and make pandas interprete it as a datetime object
    by_date.index.names = ['Date']
    by_date.index = pd.to_datetime(by_date.index)
    print("Writing to file '%s%s'" % (DIR_NAME, target))
    by_date.to_csv('%s%s' % (DIR_NAME, target))
    print("Done! Have a nice day!")

if __name__ == "__main__":
    parse_file(CONF_FILE_NAME, CONF_TARGET_FILE)
    print("***********************")
    parse_file(DEATH_FILE_NAME, DEATH_TARGET_FILE)