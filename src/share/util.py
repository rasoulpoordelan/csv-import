import datetime


def paginate(total, page, size, pagenation_size):
    total_page = total // size
    start = 0
    end = 0
    if total_page <= pagenation_size:
        start, end = 1, total_page
    elif total_page > pagenation_size:
        if page == 1:
            start, end = 1, pagenation_size
        elif page + pagenation_size > total_page:
            start, end = page - (pagenation_size - (total_page - page)), total_page
        else:
            start, end = page, page + pagenation_size
    return {
        "pages": [(i, size) for i in range(start, end + 1)],
        "page": page,
        "size": size,
        "has_next": True if page < total_page else False,
        "has_previous": True if page != 1 else False,
    }


def convert_string_to_timedelta(string1: str) -> datetime.timedelta:
    days_v_hms = string1.split("days")
    hms = days_v_hms[1].split(":")
    dt = datetime.timedelta(
        days=int(days_v_hms[0]),
        hours=int(hms[0]),
        minutes=int(hms[1]),
        seconds=float(hms[2]),
    )
    return dt
