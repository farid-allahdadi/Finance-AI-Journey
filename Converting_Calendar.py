import jdatetime

def shamsi_to_miladi(shamsi_date):
    year, month, day = map(int, shamsi_date.split("/"))
    jalali_date = jdatetime.date(year, month, day)
    return jalali_date.togregorian().strftime("%Y-%m-%d")

# تست تابع
print(shamsi_to_miladi("1404/05/08"))