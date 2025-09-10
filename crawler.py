import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"


#https://realpython.github.io/fake-jobs/
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="ResultsContainer")
# print(results.prettify())

#To find all the job postings
job_cards = results.find_all("div", class_="card-content")
# print(job_elements[0])


#Adding .text after each element to get only the text
#.strip() removes any extra whitespace


# for job_card in job_cards:
#     title_element = job_card.find("h2", class_="title")
#     company_element = job_card.find("h3", class_="company")
#     location_element = job_card.find("p", class_="location")
#     print(title_element.text.strip())
#     print(company_element.text.strip())
#     print(location_element.text.strip())
#     print()


python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
    )
#to get information of each job we must navigate to the great-grandparent element

python_jobs_info = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

# for job_card in python_jobs_info:
#     title_element = job_card.find("h2", class_="title")
#     company_element = job_card.find("h3", class_="company")
#     location_element = job_card.find("p", class_="location")
#     print(title_element.text.strip())
#     print(company_element.text.strip())
#     print(location_element.text.strip())
#     print()

#getting urls of buttons 

# for job_card in python_jobs_info:
#     links = job_card.find_all("a")
#     for link in links:
#         link_url = link["href"]
#         print(f"Apply here: {link_url}\n")

#we only want apply button url so we can do this by indexing

for job_card in python_jobs_info:
    title_element = job_card.find("h2", class_="title")
    company_element = job_card.find("h3", class_="company")
    location_element = job_card.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())

    link = job_card.find_all("a")[1]["href"]
    print(f"Apply here: {link}\n")

