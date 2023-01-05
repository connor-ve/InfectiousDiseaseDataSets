import os
import requests 

def makeFile(path, content):
  for line in content:
    # print(line)
    with open(path, 'a') as f:
      f.write(line + '\n')
      f.close()

# check if file exists and delete it if it does 
months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
for _ in range(len(months)):
  try:
    os.remove(f'./Diseases2022Data/CovidData/month{months[_]}.csv')
  except:
    pass

for _ in range(len(months)):
  try:
    os.remove(f'./Diseases2023Data/CovidData/month{months[_]}.csv')
  except:
    pass

response = requests.get("https://github.com/nytimes/covid-19-data/raw/master/us-states.csv")
data2022 = [[],[],[],[],[],[],[],[],[],[],[],[]]
data2023 = [[],[],[],[],[],[],[],[],[],[],[],[]]
dailyData = response.text.splitlines()
definedHeaders = dailyData.pop(0).split(',')

for _ in range(len(data2022)):
  data2022[_].append(definedHeaders)
  data2023[_].append(definedHeaders)

def parseYear(date):
  year = date.split('-')[0]
  return int(year)

def parseMonth(date):
  month = date.split('-')[1]
  return int(month) - 1

for _ in range(len(dailyData)):
  dailyData[_] = dailyData[_].split(',')
  month = parseMonth(dailyData[_][0])

  if parseYear(dailyData[_][0]) == 2022:
    data2022[month].append(dailyData[_])
  elif parseYear(dailyData[_][0]) == 2023:
    data2023[month].append(dailyData[_])

# turn data2022 into a list of strings
for _ in range(len(data2022)):
  for x in range(len(data2022[_])):
    data2022[_][x] = ','.join(data2022[_][x])
  
# turn data2023 into a list of strings
for _ in range(len(data2023)): 
  for x in range(len(data2023[_])):
    data2023[_][x] = ','.join(data2023[_][x])

for _ in range(len(months)):
  makeFile(f'./Diseases2022Data/CovidData/month{months[_]}.csv', data2022[_])
  makeFile(f'./Diseases2023Data/CovidData/month{months[_]}.csv', data2023[_])



  