# MY FIRST ATTEMPT
# import calendar
#
# year_one = 2017
# year_two = 2020
#
# month_one = 5
# month_two = 11
#
# date_one = 9
# date_two = 27
###############################################################################
# MY SECOND ATTEMPT AFTER VIEWING THE SOLUTION
from datetime import date

first_date = date(2020, 3, 5)
second_date = date(2020, 9, 27)

num_of_days = second_date - first_date
print(num_of_days.days)