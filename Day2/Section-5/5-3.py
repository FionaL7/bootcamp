from datetime import datetime, timedelta
import calendar
# 1. Current Time
now = datetime.now()
print("Current DateTime:", now)

# 2. Add 7 Days
future = now + timedelta(days=7)
print("7 Days Later:", future)

# 3. Format as "YYYY-MM-DD"
print("Formatted Date:", now.strftime("%Y-%m-%d"))

# 4. Parse "2024-01-01" into a datetime
parsed_date = datetime.strptime("2024-01-01", "%Y-%m-%d")
print("Parsed Date:", parsed_date)

# 5. Get Weekday Name
weekday_name = calendar.day_name[now.weekday()]
print("Today is:", weekday_name)

# 6. Date Comparison
date1 = datetime(2024, 1, 1)
date2 = datetime(2025, 5, 6)

if date1 < date2:
    print("Earlier date is:", date1)
else:
    print("Earlier date is:", date2)


# 7. Print Calendar of May 2025
print(calendar.month(2025, 5))

# 8. Round to Top of the Hour
rounded = now.replace(minute=0, second=0, microsecond=0)
print("Rounded Hour:", rounded)
