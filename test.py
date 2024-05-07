import requests
from bs4 import BeautifulSoup
import pandas as pd

# The base URL
base_url = "https://www.daad.de/en/studying-in-germany/universities/all-degree-programmes/?hec-subjectGroup=1-226&hec-degreeType=37&hec-teachingLanguage=2&hec-admissionTerm=sw,w&hec-studyType=v,i&hec-p="

# Send a GET request to the first page to get the total number of pages
response = requests.get(base_url + "1")
soup = BeautifulSoup(response.text, 'html.parser')
div = soup.find('div', {'class': 'o-nav__item u-size-20 u-display-flex u-items-center ml-8'})
text = div.text
number = int(text.split()[1])

# A list to store the data
data = []

# Iterate over all pages
# for page in range(1, number):
#     # Update the URL to include the current page number
#     url = base_url + str(page)

#     # Send a GET request to the URL
#     response = requests.get(url)

#     # Parse the HTML with BeautifulSoup
#     soup = BeautifulSoup(response.text, 'html.parser')

#     # Extract the required information
#     list = soup.find_all('li', {'class': 'qa-db-result-item'})
    
#     for n in range(len(list)):
#         university_name = list[n].find_all('span', {'class': 'js-dynamic-content u-display-block u-font-regular u-size-18 mb-8'})[0].text
#         course_name = list[n].find('span', {'class': 'js-dynamic-content u-display-block u-font-light u-size-24 mb-24 u-size-32@lg'}).text
#         degree = list[n].find_all('div', {'class': 'js-dynamic-content s-result-item'})[0].text
#         duration = list[n].find_all('div', {'class': 'js-dynamic-content s-result-item'})[1].text
#         location = list[n].find_all('div', {'class': 'js-dynamic-content s-result-item'})[2].text
#         study_type = list[n].find_all('div', {'class': 'js-dynamic-content s-result-item'})[3].text
#         deadlines = list[n].find_all('div', {'class': 'js-dynamic-content s-result-item'})[4].text.split('\n')
#         if deadlines[0] == 'DeadlinesNo information':
#             deadlines = ""
#         link = list[n].find('a')['href']

#         # Add the data to the list
#         data.append({
#             'University Name': university_name,
#             'Course Name': course_name,
#             'Location': location,
#             'Deadlines': deadlines,
#             # =HYPERLINK("https://www.daad.de+Link+", "Link")
#             'Link': '=HYPERLINK("https://www.daad.de' + link + '", "Link")'
#         })
link = '/en/studying-in-germany/universities/all-degree-programmes/detail/srh-university-of-applied-sciences-heidelberg-applied-computer-science-w40883/?hec-subjectGroup=1-226&hec-degreeType=37&hec-teachingLanguage=2&hec-admissionTerm=sw,w&hec-studyType=v,i&hec-p=1'
link1 = link[:len(link)//2]
link2 = link[len(link)//2:]

data.append({
            'University Name': 'university_name',
            'Course Name': 'course_name',
            'Location': 'location',
            'Deadlines': 'deadlines',
            # =HYPERLINK("https://www.daad.de+Link+", "Link")
            'Link': '=HYPERLINK("https://www.daad.de' + link1 + link2 + '", "Link")',
            'raw_link': 'https://www.daad.de' + link 
        })

# Create a DataFrame from the list of dictionaries
df = pd.DataFrame(data)

# Export the DataFrame to an Excel file in the specified directory
df.to_excel('C:\\Users\\SFI19\\Documents\\Git\\Daad\\test.xlsx', index=False)