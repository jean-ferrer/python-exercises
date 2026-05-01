# 2026-04-19

import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    
    weather = weather.sort_values(by='recordDate')

    weather['temp_anterior'] = weather['temperature'].shift(1)

    weather['diff_dias'] = weather['recordDate'].diff().dt.days

    result = weather[(weather['temp_anterior'] < weather['temperature']) & (weather['diff_dias'] == 1)]

    return result[['id']]