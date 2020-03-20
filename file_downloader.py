from urllib.request import urlretrieve

CONFIRMED_URL = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv'
DIR_PATH = 'data/'
CONFIRMED_FILENAME = 'confirmed.csv'

if __name__ == "__main__":
    print("Downloading data from url %s" % CONFIRMED_URL)
    print("Target location: %s%s" % (DIR_PATH, CONFIRMED_FILENAME))
    urlretrieve(CONFIRMED_URL, '%s%s' % (DIR_PATH, CONFIRMED_FILENAME))
    print("Done!")