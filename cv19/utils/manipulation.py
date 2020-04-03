from datetime import datetime

from pandas import DataFrame, Series


def calc_changes(df: DataFrame) -> DataFrame:
    data = df - df.shift()
    data.fillna(0, inplace=True)
    return data

def first_case_date(df: DataFrame, country: str) -> datetime:
    return df[country].where(lambda x: x > 0).dropna().index[0]

def first_n_cases(df: DataFrame, country: str, n: int, first_date=None):
    if first_date is None:
        first_date = first_case_date(df, country)
    return df.loc[df.index >= first_date, country].head(n).reset_index(drop=True), first_date

def build_first_n_df(df: DataFrame, countries: list, n: int, target: DataFrame, first_dates=None):
    dates = dict()
    for country in countries:
        if first_dates is None:
            target[country], date = first_n_cases(df, country, n)
            dates[country] = date
        else:
            target[country], date = first_n_cases(df, country, n, first_dates[country])
    return dates

def which_countries_before(df: DataFrame, search_country: str):
    aux = df.drop('the world', axis=1)
    infected_countries = []
    for i in range(0, len(aux)):
        c = aux.iloc[i]
        c = c[c > 0]
        lote = c.index
        for country in lote:
            if country == search_country:
                return infected_countries
            if country not in infected_countries:
                infected_countries.append(country)
    return None
