## Data Analytics Project
## Title: Restaurant Business Analysis in Orange County (10 most populous cities)

Objective:
- One of our clients, a wealthy investor, would like to open a new restaurant in Orange County, and has narrowed the potential location down to 10 of the County’s most populous cities. 
- Our client wants to know the following: which city they can charge the highest price in, how long they should stay open to maximize customer ratings, and which type of cuisine they should serve based on the most popular customer ratings.
- To do that, we must figure out the most profitable location of the 10 cities selected; how long to keep the restaurant running for, and last but not least, what cuisine to specialize in to attract the most customers.

Business Questions:
1. <strong>Cities vs Price Point:</strong> <br>
Business question: Which city, of the chosen 10, has the highest price point for popular restaurants?

2.	<strong>Hours of Operation vs Customer Rating: </strong> <br>
Business question: How many hours of operation should you open your restaurant for?

3.	<strong>Cuisine vs Customer Rating</strong> <br>
Business question: What’s the most popular restaurant cuisine in these OC cities?

Implementation: 
- Used Python programming language, and Python Plotting Libary (Matplotlib). 
- Used Yelp! Fusion API. Set Environment <br>
```python
pip install yelpapi
```
Challenges: Due to the way the API is set up, only a maximum of 50 top searches will appear when a get requests is made. Because of this we limit the search radius to 5000 meters in order to cover each district as best as possible, and we used offset to maximize our results. 
``` python
url = "http://api.yelp.com/v3/businesses/search"
headers = {"Authorization":"Bearer %s" %api_key}
paramps = {"term":t,"location": city,"limit":50, "offset":50,"radius":5000}
results = requests.get(url,headers = headers,params = params).json()
```

## Discussion
- We recommend to our client that the best cuisine type to open based on popularity is Mediterranean. The hours of operation per week they should stay open to maximize the popularity of said ratings is 100 or less; and the city that offers the higherst price per rating is Anaheim.
- We can draw from our data set are that to maximize ratings, it is better to keep your restaurant open for less time. In addition, lower density of cuisine type could lead to higher average rating. Lastly, the most popular restaurants were on the cheaper sid of the yelp rating scale. 
