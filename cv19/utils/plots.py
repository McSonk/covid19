from datetime import datetime, timedelta
from matplotlib import pyplot as plt
import matplotlib.dates as mdates

DATETIME_FORMAT = '%Y-%m-%d'
WINDOW_DAYS = 14

def __generic__plot__(df, country, ld_date, display_label, language):
    if language == 'es':
        date_label = 'Fecha'
        cases_label = 'Número de casos'
        first_det_label = 'Primer caso en %s detectado el %s'
        lock_started_label = 'Cuarentena iniciada en %s'
        lock_label = 'Inició la cuarentena'
        window_label = "Ventana de 14 días"
        current_num_label = 'Actualmente hay %s casos confirmados'
    else:
        date_label = 'Date'
        cases_label = 'Number of cases'
        first_det_label = "First case for %s detected on %s"
        lock_started_label = "Lockdown started on %s"
        lock_label = 'Lockdown started'
        window_label = '14 days window'
        current_num_label = "Currently having %s confirmed cases"

    plt.figure(figsize=(15, 8))
    plt.xlabel(date_label)
    first_detected = df[country].where(lambda x: x > 0).dropna().index[0]
    plt.plot(df.loc[df.index > first_detected, country], label=cases_label)
    print(first_det_label % (country, first_detected))
    if ld_date is not None:
        end_date = datetime.strptime(ld_date, DATETIME_FORMAT) + timedelta(days=WINDOW_DAYS)
        end_date_str = end_date.strftime(DATETIME_FORMAT)
        print(lock_started_label % (ld_date))
        plt.axvline(ld_date, linestyle='--', color='r', label=lock_label)
        plt.axvline(end_date_str, linestyle=':', color='r', label=window_label)
        plt.legend()
    num_of_cases = df[country].dropna().iloc[-1]
    plt.xticks(rotation=80)
    print(current_num_label % f'{num_of_cases:,}')

def plot_country_cases(df, country, ld_date=None, language='en'):
    if language == 'es':
        new_cases_label = 'Casos confirmados en %s'
        y_label = 'Número de nuevos casos'
        n_cases_label = 'Número de casos'
    else:
        new_cases_label = 'Confirmed cases in %s'
        y_label = 'Number of cases'
        n_cases_label = 'Number of cases'
    __generic__plot__(df, country, ld_date, n_cases_label, language)
    plt.title(new_cases_label % country)
    plt.ylabel(y_label)
    plt.show()

def plot_country_changes(df, country, ld_date=None, language='en'):
    if language == 'es':
        new_cases_label = 'Nuevos casos en %s'
        y_label = 'Número de nuevos casos'
        n_cases_label = 'Nuevos casos'
        max_number_label = 'Máximo número de nuevos casos: %s'
        max_label = 'Techo en %s'
    else:
        new_cases_label = 'Confirmed new cases in %s'
        y_label = 'Number of new cases'
        n_cases_label = 'New cases'
        max_number_label = 'Max number of new cases: %s'
        max_label = 'Peak on %s'
    __generic__plot__(df, country, ld_date, n_cases_label, language)
    max_cases = df[country].max()
    print(max_number_label % max_cases)
    plt.axhline(max_cases, linestyle='-.', color='b', label=(max_label % max_cases))
    plt.axhline(0, linestyle=':', color='black')
    plt.title(new_cases_label % country)
    plt.ylabel(y_label)
    plt.legend()
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