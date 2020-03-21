
def calc_changes(df):
    data = df - df.shift()
    data.fillna(0, inplace=True)
    return data