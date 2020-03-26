from urllib.request import urlretrieve

CONFIRMED_URL = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
DEATHS_URL = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
DIR_PATH = 'data/'
CONFIRMED_FILENAME = 'confirmed.csv'
DEATHS_FILENAME= 'deaths.csv'

def download_confirmed():
    print("Downloading data from url %s" % CONFIRMED_URL)
    print("Target location: %s%s" % (DIR_PATH, CONFIRMED_FILENAME))
    urlretrieve(CONFIRMED_URL, '%s%s' % (DIR_PATH, CONFIRMED_FILENAME))
    print("Done!")

def download_deaths():
    print("Downloading data from url %s" % DEATHS_URL)
    print("Target location: %s%s" % (DIR_PATH, DEATHS_FILENAME))
    urlretrieve(DEATHS_URL, '%s%s' % (DIR_PATH, DEATHS_FILENAME))
    print("Done!")

if __name__ == "__main__":
    download_confirmed()
    print("********************")
    download_deaths()