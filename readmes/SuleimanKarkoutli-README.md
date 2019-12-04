# trdrp_scrapers
tools used to help with Health and Space Lab research 
Suleiman Karkoutli - Final Submission 

Final Product: Yelp API Scraper
I wrote the Yelp API scraper script which hits the Yelp API and retrives a list of all of the local business types. For instance, the script takes in a list of business types (dispensaries, community centers, parks, etc) which is provided through the YAML file. It then iterates through each business type and retrieves information on all of the local businesses. For example, when the script is iterating through the dispensaries keyword it pulls all of the dispensaires in the specified region (in this case South Los Angeles)
After retrieving the Yelp data for our business types it then retrieves all of the reviews for each respective business.  
These reviews can then be used to mine sentiment.  The sentiment analysis was not implemented in this sprint, but the data ingestion is in place for such an analysis.

Other Contributions:
-Provided json to pandas dataframe parsing logic (used in all of our scrapers)
-I diagrammed and created our data ingestion pipeline.  
-Aided Karl with the database schema design
-Handled known API errors for the Yelp API (the API is buggy at times and it is a known error on their side) so that the script continues to run efficiently
-Consulted on potentional visualization methods

Features not implemented:
-Sentiment Analysis of reviews for various business types was not implemented due to time constraints and level of effort
-Not all data integrity checks were implmented on the SQL Server Side
-Tableau visualizations were not created (due to sentiment analysis being put on hold )


