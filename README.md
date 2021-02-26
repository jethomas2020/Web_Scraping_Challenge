# Web_Scraping_Challenge

# Mission to Mars

![Alt text](/relative/path/to/Images/mission_to_mars.jpg?raw=true "Mission to Mars")

----------------------
# Background

In this assignment, you will build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. The following outlines what you need to do.

------------
# Step 1 - Scraping Data

Completed the initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

    - Created a Jupyter Notebook file called mission_to_mars.ipynb and used this to complete 
    all of the scraping and analysis tasks. 
    
    - The following outlines what was scraped.

**NASA Mars News**

    - Scraped the NASA Mars News Site and collected the latest News Title and Paragraph Text. 
    - Assigned the text to variables that you can reference later.

**Example:**
news_title = "Testing Proves Its Worth With Successful Mars Parachute Deployment"

news_p = "The giant canopy that helped land Perseverance on Mars was tested here on Earth at NASA’s Wallops Flight Facility in Virginia."

**JPL Mars Space Images - Featured Image**

    Visited the url for the NASA JPL (Jet Propulsion Laboratory)- CIT Featured Space Image. 
    ['https://www.jpl.nasa.gov']

    Used splinter to navigate the site and find the image url for the current Featured Mars Image and 
        assign the url string to a variable called featured_image_url.
        ['https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars']
            - used image url for full size .jpg image
            - completed url string for this image.

**Example:**
featured_image_url = 'https://d2pn8kiwq2w21t.cloudfront.net/images/jpegPIA24425.2e16d0ba.fill-400x400-c50.jpg'


**Mars Planet Facts**

    Visited the Mars Facts webpage ['https://space-facts.com/mars/'] and used Pandas to scrape the table 
        containing facts about the planet including Diameter, Mass, etc.

    Used Pandas to convert the data to a HTML table string.

**Mars Hemispheres**

    Visited the USGS Astrogeology site ['https://astrogeology.usgs.gov'] to obtain high 
    resolution images for each of Mar's Hemispheres.

   Clicked on each of the links to the Hemispheres in order to find the image url to the full resolution image.
    [hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars']

    Saved both the image url string for the full resolution Hemisphere image, and the Hemisphere 
        title containing the Hemisphere name. 
    Used a Python dictionary to store the data using the keys img_url and title.

    Appended the dictionary with the image url string and the Hemisphere title to a list. 
    This list contains one dictionary for each Hemisphere.

**Example:**
hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "..."},
    {"title": "Cerberus Hemisphere", "img_url": "..."},
    {"title": "Schiaparelli Hemisphere", "img_url": "..."},
    {"title": "Syrtis Major Hemisphere", "img_url": "..."},


-----------------------------------
# Step 2 - MongoDB and Flask Application

Used MongoDB with Flask templating to create a new HTML page that displays all of the information 
that was scraped from the URLs above.

    Started by converting the Jupyter notebook into a Python script called scrape_mars.py with a function 
    called scrape that will execute all of the scraping code from above and return one Python dictionary 
    containing all of the scraped data.

    Next, created a route called /scrape that will import the scrape_mars.py script and call your 
        scrape function.
        Stored the return value in Mongo as a Python dictionary.

    Created a root route / that will query your Mongo database and pass the mars data into an HTML template 
        to display the data.

    Create a template HTML file called index.html that will take the mars data dictionary and display all 
        of the data in the appropriate HTML elements. Use the following as a guide for what the final product 
        should look like, but feel free to create your own design.
    
    
    ADD IMAGES -\\
    
    Step 3 - Submission





To submit your work to BootCampSpot, create a new GitHub repository and upload the following:

    The Jupyter Notebook containing the scraping code used.

    Screenshots of your final application.

    Submit the link to your new repository to BootCampSpot.

    Ensure your repository has regular commits (i.e. 20+ commits) and a thorough README.md file

NOTE:

    Used Splinter to navigate the sites when needed and BeautifulSoup to help find and parse out the necessary data.

    Used Pymongo for CRUD applications for the database. For this homework, we simply overwrote the existing document 
    each time the /scrape url is visited and new data is obtained.

    Used Bootstrap to structure your HTML template.
