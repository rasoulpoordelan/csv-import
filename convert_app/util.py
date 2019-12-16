
import datetime
def convert_string_to_timedelta(string1 : str) -> datetime.timedelta:
    days_v_hms = string1.split('days')
    hms = days_v_hms[1].split(':')
    dt = datetime.timedelta(days=int(days_v_hms[0]), hours=int(hms[0]), minutes=int(hms[1]), seconds=float(hms[2]))
    return dt