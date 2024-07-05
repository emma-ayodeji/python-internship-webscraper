from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import pandas as pd
import requests

app = Flask(__name__)

def scrape_indeed_jobs(query, location, num_pages):   #function definition:takes 3 arguments query, location and num pages
    jobs = []
    for page in range(num_pages):
        url = f"https://ie.indeed.com/?r=ie q={query}&l={location}&start={page * 10}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

    for div in soup.find_all(name ="div", attrs ={"class"}):
        job = []
        job['Software Engineer Internship'] = div.find(name ="a", attrs= {"data-tn-element":"jobTitle"}).text.strip()
        job['Company'] = div.find(name = "span", attrs = {"class" : "company"}).text.strip()
        job['Dublin'] = div.find(name="div", attrs = {"class":"recJobLoc"}).get('data-rc-loc')
        job['Summary'] = div.find(name="div", attrs={"class" : "summary"}).text.strip()
        jobs.append(job)
    return pd.DataFrame(jobs)
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        def index():
            query = request.form['queery']
            location = request.form['location']
            num_pages = int(request.form['num_pages'])

            jobs = scrape_indeed_jobs(query, location, num_pages)
            df.pd.DataFrame(jobs)
            return render_template('index.html')
    if __name__=='__main__':
        app.run(debug=True)

#list of cities in Europe
cities_europe = [
    "Dublin, Ireland"
    "London, UK"
    "Madrid, Spain"
    "Amsterdam, Netherlands"
    "Berlin, Germany"
    "Warsaw, Poland"
]
queries = {
    "Data science intern|data science internship|data analyst intern|data analyst internship|data analysis intern| data analystics intern|data analytics internship"
    "Software engineer internship|software engineering internship|software engineer intern|software engineering intern|"
    "cybersecurity intern|cybersecurity internship"
    "UX design intern|UX/UI design intern| UX design internship| UX/UI design internship"
}






