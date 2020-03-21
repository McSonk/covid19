from datetime import datetime, timedelta
from matplotlib import pyplot as plt
import matplotlib.dates as mdates

DATETIME_FORMAT = '%Y-%m-%d'
WINDOW_DAYS = 14

def plot_country_cases(df, country, ld_date=None):
    plt.figure(figsize=(15, 8))
    plt.title('Confirmed cases in %s' % country)
    plt.xlabel('Date')
    plt.ylabel('Number of cases')
    first_detected = df[country].where(lambda x: x > 0).dropna().index[0]
    print("First case for %s detected on %s" % (country, first_detected))
    plt.plot(df.loc[df.index > first_detected, country], label='Number of cases')
    if ld_date is not None:
        end_date = datetime.strptime(ld_date, DATETIME_FORMAT) + timedelta(days=WINDOW_DAYS)
        end_date_str = end_date.strftime(DATETIME_FORMAT)
        print("Lockdown started on %s" % (ld_date))
        plt.axvline(ld_date, linestyle='--', color='r', label='Lockdown started')
        plt.axvline(end_date_str, linestyle=':', color='r', label='14 days window')
        plt.legend()
    num_of_cases = df[country].dropna().iloc[-1]
    plt.xticks(rotation=80)
    print("Currently having %s confirmed cases" % f'{num_of_cases:,}')
    plt.show()


def plot_top5(df, from_date=None):
    top5 = df.iloc[-1].sort_values(ascending=False).head(5).index
    plt.figure(figsize=(15, 8))
    plt.title('Top 5 countries by confirmed cases')
    plt.xlabel('Date')
    plt.ylabel('Number of cases')
    if from_date is None:
        plt.plot(df.loc[:, top5])
    else:
        plt.plot(df.loc[df.index > from_date, top5])
    plt.legend(top5)
    plt.xticks(rotation=80)
    plt.show()