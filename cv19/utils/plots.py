from matplotlib import pyplot as plt
from pandas import DataFrame

from cv19.utils.date import add_days, elapsed_time
from cv19.utils.manipulation import first_case_date

WINDOW_DAYS = 14


def __generic__plot__(df: DataFrame, country: str, ld_date: str, language: str, changes: DataFrame, labels):
    if language == 'es':
        labels['date_label'] = 'Fecha'
        labels['cases_label'] = 'Acumulado de casos'
        labels['first_det_label'] = 'Primer caso en %s detectado el %s. Han pasado %s días desde entonces'
        labels['lock_started_label'] = 'Cuarentena iniciada en %s'
        labels['lock_label'] = 'Inició la cuarentena'
        labels['window_label'] = "Ventana de 14 días"
        labels['current_num_label'] = 'Actualmente hay %s casos confirmados'
    else:
        labels['date_label'] = 'Date'
        labels['cases_label'] = 'Cumulative cases'
        labels['first_det_label'] = "First case for %s detected on %s. %s days have passed since then"
        labels['lock_started_label'] = "Lockdown started on %s"
        labels['lock_label'] = 'Lockdown started'
        labels['window_label'] = '14 days window'
        labels['current_num_label'] = "Currently having %s confirmed cases"

    first_detected = first_case_date(df, country)
    elapsed_days = elapsed_time(first_detected)
    aux = df.loc[df.index >= first_detected, country]
    aux.index = aux.index.format()

    plt.figure(figsize=(15, 8))
    plt.xlabel(labels['date_label'])
    print(labels['first_det_label'] % (country, first_detected, elapsed_days))
    aux.plot(label=labels['cases_label'])
    if changes is not None:
        max_cases = changes[country].max()
        print(labels['max_number_label'] % f'{max_cases:,}')
        aux_c = changes.loc[changes.index >= first_detected, country]
        aux_c.index = aux_c.index.format()
        aux_c.plot(kind='bar', label=labels['cases_per_day_lab'])
        plt.axhline(max_cases, linestyle='-.', color='b', label=(labels['max_label'] % max_cases))
        plt.legend()
    if ld_date is not None:
        print(labels['lock_started_label'] % (ld_date))
        ld_pos = aux[aux.index < ld_date].size
        plt.axvline(ld_pos, linestyle=':', color='r', label=labels['lock_started_label'])
        plt.axvline(ld_pos + WINDOW_DAYS, linestyle=':', color='r', label=labels['window_label'])
        plt.legend()

    num_of_cases = df[country].dropna().iloc[-1]
    print(labels['current_num_label'] % f'{num_of_cases:,}')
    return first_detected

def plot_country_cases(df: DataFrame, country: str, ld_date=None, language='en', changes=None):
    labels = dict()
    if language == 'es':
        labels['new_cases_label'] = 'Casos confirmados en %s'
        labels['y_label'] = 'Número de casos'
        labels['n_cases_label'] = 'Número de casos'
        labels['cases_per_day_lab'] = 'Nuevos casos reportados'
        labels['max_number_label'] = 'Máximo número de nuevos casos: %s'
        labels['max_label'] = 'Techo de nuevos casos en %s'
    else:
        labels['new_cases_label'] = 'Confirmed cases in %s'
        labels['y_label'] = 'Number of cases'
        labels['n_cases_label'] = 'Number of cases'
        labels['cases_per_day_lab'] = 'New cases reported'
        labels['max_number_label'] = 'Max number of new cases: %s'
        labels['max_label'] = 'Peak of new cases on %s'
    
    __generic__plot__(df, country, ld_date, language, changes, labels)
    plt.title(labels['new_cases_label'] % country)
    plt.ylabel(labels['y_label'])
    plt.show()

def plot_country_deaths(df, country, ld_date=None, language='en', changes=None):
    labels = dict()
    if language == 'es':
        labels['new_cases_label'] = 'Muertes confirmadas en %s'
        labels['y_label'] = 'Número de muertes'
        labels['n_cases_label'] = 'Número de muertes'
        labels['cases_per_day_lab'] = 'Muertes al día reportadas'
        labels['max_number_label'] = 'Máximo número de muertes reportadas: %s'
        labels['max_label'] = 'Techo de muertes diarias en %s'
    else:
        labels['new_cases_label'] = 'Confirmed deaths in %s'
        labels['y_label'] = 'Number of deaths'
        labels['n_cases_label'] = 'Number of deaths'
        labels['cases_per_day_lab'] = 'Daily deaths reported'
        labels['max_number_label'] = 'Highest number of daily deaths: %s'
        labels['max_label'] = 'Peak of daily deaths on %s'
    first_case_date = __generic__plot__(df, country, ld_date, language, changes, labels=labels)
    plt.title(labels['new_cases_label'] % country)
    plt.ylabel(labels['y_label'])
    plt.show()


def plot_top5(df, from_date=None):
    top5 = df.drop("the world", 1).iloc[-1].sort_values(ascending=False).head(5).index
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
