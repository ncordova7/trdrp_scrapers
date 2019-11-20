# trdrp_scrapers
tools used to help with Health and Space Lab research 
Suleiman Karkoutli - Submission 3 

I wrote the Yelp API scraper script which hits the Yelp API and retries information on different dispensaries.
After retrieving the Yelp Data it then retrieves all of the reviews for each respective dispensary.  
These reviews can then be used to mine sentiment.  The Yelp script can also be used to retrieve information on community centers which will be beneifical for our analysis. 
Elmer and I also diagrammed and created our data ingestion pipeline. We currently have the API and Database connection sections completed

Planning to do next:
-I am planning on populating our tables to our SQL Server Database with the Weedmaps + Yelp information and maintaining data integrity checks.
- After our data is on the server this will be used to preproccess our review data and create sentiment visualizations through Tableau.
-Over see Tableau visualizations and serve as the point of contact for any Tableau troubleshooting. 


