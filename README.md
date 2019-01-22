# Mission to Mars

Web Scraping NASA Mars News, NASA Mars Space Image, NASA Twitter and U.S Geological survey sites have been scrapped to collect latest news and images. Scrapping was used as the data is frequently changing and users can request for a new scrape as well.

NASA Mars News: NASA publishes articles and latest developments related to Mars exploration. This scrape collects the title and a brief synopsis of the article.
NASA Mars Space Image: This site publishes selected images of Mars as featured images. The scrape was to pull the latest image.
NASA Twitter: NASA twitter feed contains Mars weather information. We scrape NASA’s twitter feed to identify the latest weather post. Any non-weather posts are ignored.
U.S Geological Survey: Scrape was to collect the recent pictures of the hemispheres of Mars.

![mission_to_mars](Images/mission_to_mars.jpg)

```python
# Example:
featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA16225_hires.jpg'
```

### Mars Weather

* Visit the Mars Weather twitter account [here](https://twitter.com/marswxreport?lang=en) and scrape the latest Mars weather tweet from the page. Save the tweet text for the weather report as a variable called `mars_weather`.

```python
# Example
mars_weather = 'Sol 1801 (Aug 30, 2017), Sunny, high -21C/-5F, low -80C/-112F, pressure at 8.82 hPa, daylight 06:09-17:55'
```

```python
# Example:
hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "..."},
    {"title": "Cerberus Hemisphere", "img_url": "..."},
    {"title": "Schiaparelli Hemisphere", "img_url": "..."},
    {"title": "Syrtis Major Hemisphere", "img_url": "..."},
]
```

- - -


![final_app_part1.png](Images/final_app_part1.png)
![final_app_part2.png](Images/final_app_part2.png)

- - -

