from matplotlib import pyplot as plt
from pandas import DataFrame
from cv19.utils.date import elapsed_time, add_days

WINDOW_DAYS = 14


def __generic__plot__(df: DataFrame, country: str, ld_date: str, display_label: str, language: str, changes: DataFrame):
    if language == 'es':
        date_label = 'Fecha'
        cases_label = 'Número de casos'
        first_det_label = 'Primer caso en %s detectado el %s. Han pasado %s días desde entonces'
        lock_started_label = 'Cuarentena iniciada en %s'
        lock_label = 'Inició la cuarentena'
        window_label = "Ventana de 14 días"
        current_num_label = 'Actualmente hay %s casos confirmados'
    else:
        date_label = 'Date'
        cases_label = 'Number of cases'
        first_det_label = "First case for %s detected on %s. %s days have passed since then"
        lock_started_label = "Lockdown started on %s"
        lock_label = 'Lockdown started'
        window_label = '14 days window'
        current_num_label = "Currently having %s confirmed cases"

    first_detected = df[country].where(lambda x: x > 0).dropna().index[0]
    elapsed_days = elapsed_time(first_detected)
    aux = df.loc[df.index >= first_detected, country]
    aux.index = aux.index.format()

    
    plt.figure(figsize=(15, 8))
    plt.xlabel(date_label)
    print(first_det_label % (country, first_detected, elapsed_days))
    aux.plot(label=cases_label)
    if ld_date is not None:
        end_date_str = add_days(ld_date, WINDOW_DAYS)
        print(lock_started_label % (ld_date))
        plt.axvline(ld_date, linestyle='--', color='r', label=lock_label)
        plt.axvline(end_date_str, linestyle=':', color='r', label=window_label)
        plt.legend()
    if changes is not None:
        max_cases = changes[country].max()
        #print(max_number_label % f'{max_cases:,}')
        aux_c = changes.loc[changes.index >= first_detected, country]
        aux_c.index = aux_c.index.format()
        aux_c.plot(kind='bar')
        #changes[country].iloc[changes.index >= first_case_date].plot.bar(label=cases_per_day_lab)
        #df.loc[df.index >= first_detected, country].plot(ax = ax)
        #plt.axhline(max_cases, linestyle='-.', color='b', label=(max_label % max_cases))
        plt.legend()

    num_of_cases = df[country].dropna().iloc[-1]
    print(current_num_label % f'{num_of_cases:,}')
    return first_detected

def plot_country_cases(df: DataFrame, country: str, ld_date=None, language='en', changes=None):
    if language == 'es':
        new_cases_label = 'Casos confirmados en %s'
        y_label = 'Número de casos'
        n_cases_label = 'Número de casos'
        cases_per_day_lab = 'Nuevos casos reportados'
        max_number_label = 'Máximo número de nuevos casos: %s'
        max_label = 'Techo de nuevos casos en %s'
    else:
        new_cases_label = 'Confirmed cases in %s'
        y_label = 'Number of cases'
        n_cases_label = 'Number of cases'
        cases_per_day_lab = 'New cases reported'
        max_number_label = 'Max number of new cases: %s'
        max_label = 'Peak of new cases on %s'
    __generic__plot__(df, country, ld_date, n_cases_label, language, changes)
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


def plot_country_deaths(df, country, ld_date=None, language='en', changes=None):
    if language == 'es':
        new_cases_label = 'Muertes confirmadas en %s'
        y_label = 'Número de muertes'
        n_cases_label = 'Número de muertes'
        cases_per_day_lab = 'Muertes al día reportadas'
        max_number_label = 'Máximo número de muertes reportadas: %s'
        max_label = 'Techo de muertes diarias en %s'
    else:
        new_cases_label = 'Confirmed deaths in %s'
        y_label = 'Number of deaths'
        n_cases_label = 'Number of deaths'
        cases_per_day_lab = 'Daily deaths reported'
        max_number_label = 'Highest number of daily deaths: %s'
        max_label = 'Peak of daily deaths on %s'
    first_case_date = __generic__plot__(df, country, ld_date, n_cases_label, language)
    if changes is not None:
        max_cases = changes[country].max()
        print(max_number_label % f'{max_cases:,}')
        changes[country].iloc[changes.index >= first_case_date].plot.bar(label=cases_per_day_lab)
        plt.axhline(max_cases, linestyle='-.', color='b', label=(max_label % max_cases))
        plt.axhline(0, linestyle=':', color='black')
        plt.legend()
    plt.title(new_cases_label % country)
    plt.ylabel(y_label)
    plt.show()

def plot_death_changes(df, country, ld_date=None, language='en'):
    if language == 'es':
        new_cases_label = 'Muertes en %s'
        y_label = 'Número de muertes reportadas'
        n_cases_label = 'Muertes reportadas'
        max_number_label = 'Máximo número de muertes reportadas: %s'
        max_label = 'Techo en %s'
    else:
        new_cases_label = 'Confirmed deaths in %s'
        y_label = 'Number of deaths'
        n_cases_label = 'New deaths'
        max_number_label = 'Max number of deaths: %s'
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
