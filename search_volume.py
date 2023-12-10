from pytrends.request import TrendReq
from time import sleep

def company_score(name):
    try:
        pytrends = TrendReq(hl='en-US', tz=360)
        kw_list = [name]
        pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='', gprop='')
        df = pytrends.interest_over_time()
        # print(str(name) + " " + str(df[name].sum()))
        return df[name].sum()
    except Exception as e:
        # print(f"Error fetching data for {name}: {e}")
        return 0
