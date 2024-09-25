import pandas as pd
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import seaborn as sns
from fontTools.misc.plistlib import Data

url = 'https://www.hko.gov.hk/en/cis/awsYearlyExtract.htm?stn=HKA'
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table')
headers = [header.get_text() for header in table.find_all('th')]
rows =[]
for row in table.find_all('tr')[1:]:
    cells = row.find_all('td')
    rows.append([cell.get_text() for cell in cells])
    df = pd.DataFrame(rows, columns=headers)
    df['year'] =pd.to_numeric(df['year'], errors='coerce')
    df['Mean Temperature(°C)']=pd.to_numeric(df['Mean Temperature (°C)'], errors='coerce')
    plt.figure(figsize=(10,6))
    sns.lineplot(data=df, x='Year', y='Mean Temperature (°C)')
    plt.title('Mean Temperature Over Years')
    plt.xlabel('Year')
    plt.ylabel('Mean Temperature (°C)')
    plt.show()
else:
    print(f"Failed to retrieve the web page. Status code: {response.status_code}")

