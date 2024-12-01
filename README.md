# Idealista
Idealista Web Scraping & Data Analysis

Sraping the website
The project began with scraping the Idealista website. This was achieved with Selenium (for pagination purposes) and Beautiful Soup (to parse and extract the HTML).

There is a dicitonary, which goes along with the scraper, which includes all of the districts, municipalities or locations which are to be scraped. What is important here is to make sure no one link to be scraped includes more than 1.950 ads (30 ads per page * 65 pages). This is because even though a district, location or municipality may include more than 1.950 ads, Idealista will only show the ads up to around page 65.

Data Analysis
The data analysis began by cleaning and treating the data, and then exploring the housing market through different lenses.

Importantly, listings which were considered duplicates were eliminated. The criteria to eliminate was such that if the Listing_Area, Price, Location_1 and Floor were exactly the same, they would be eliminated. This is not a perfect solution, but rather a simpler one.
