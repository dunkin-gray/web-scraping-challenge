# web-scraping-challenge

Mission to Mars | Web Scraping Challenge
For this challenge, I created a web application that scrapes data on Mars from four different websites; Mars news site, Mars space images site, Mars facts site and Mars hemisphere's site. To complete my intial scraping and analysis, I used Jupyter Notebook, Beautiful Soup, Pandas and Splinter. I then used MongoDB and Flask to create an HTML page displaying all of the information scraped. In the application, the user has the ability to scrape data from each of these sites using the 'Scrape New Data' button at the top of the page.

Mission_to_Mars

mission_to_mars.ipynd | My jupyter noteboook file with my intial analysis.
Mission_to_Mars/Flask_App

scrape_mars.py | Returns a Python dictionary containing all of the scraped data from my Jupyter Notebook.
app.py | Routes all of the data from my scrape_mars.py file and passes the data into an HTML template.
templates/index.html | Displays the Mars data dictionary in a webpage format.
Mission_to_Mars/Images

MissionToMars.png | A screenshot of my final application.
MissionToMars
