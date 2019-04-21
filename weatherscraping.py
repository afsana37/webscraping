import requests
from bs4 import BeautifulSoup
import pandas as pd
page = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
# print(page.content)
soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.prettify())
seven_day = soup.find(id="seven-day-forecast")
# print(seven_day.prettify())
forecast_items = seven_day.find_all(class_="tombstone-container")
# for item in forecast_items:
# 	print("This is an item\n")
# 	print(item.prettify())
# 	print("\n")


tonight = forecast_items[0]
# print(tonight.prettify())
period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()

# print(period)
# print(short_desc)
# print(temp)

img = tonight.find("img")
desc = img['title']

# print(desc)

period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]

# print(periods)


short_descs = seven_day.select(".tombstone-container .short-desc")
short = [sd.get_text() for sd in short_descs]
temps =  seven_day.select(".tombstone-container .temp")
tem = [tm.get_text() for tm in temps]
descs = seven_day.select(".tombstone-container img")
des = [ds['title'] for ds in descs]
# print(short)
# print(tem)
# print(des)

weather = pd.DataFrame({
        "period": periods,
         "short_desc": short,
         "temp": tem,
         "desc":des
    })

# print(weather)

temp_nums = weather["temp"].str.extract("(?P<temp_num>\d+)", expand=False)
weather["temp_num"] = temp_nums.astype('int')
# print(temp_nums)

# print(weather["temp_num"].mean())

is_night = weather["temp"].str.contains("Low")
weather["is_night"] = is_night

print(is_night)