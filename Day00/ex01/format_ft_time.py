import time

time_now = time.time()
formatted_date = time.strftime("%b %d %Y", time.gmtime(time_now))
print(f"Secounds since Januray 1, \
1970: {time_now:,.4f} or {time_now:.2e} in scientific notation")
print(formatted_date)

# EXPECTED OUTPUT FOR COMPARISION DIFFRENT TIMES THO
# Seconds since January 1, 1970: 1,666,355,857.3622
# or 1.67e+09 in scientific notation$
# Aug 28 2023
