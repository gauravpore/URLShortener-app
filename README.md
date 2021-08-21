# 🔹URLShortener
## 🔸Overview:
### 📌Click [here](https://drive.google.com/file/d/1NkTVstCDgjh42h6_RkSA0aYnZOIQudFL/view?usp=sharing) to watch the demo of the project.

URL shortening is a technique on the World Wide Web in which a Uniform Resource Locator (URL) may be made substantially shorter and still direct to the required page. This is achieved by using a redirect which links to the web page that has a long URL.
This repository contains all the required source files for the Django application and shortening algorithm used.

## 🔸**Concepts:**
- URL shortening
- API service
- Back-end Development

## 🔸**Tools & Technologies:**
- Python 3
- [Django](https://www.djangoproject.com/start/)
- HTML
- Sqlite3
- Git Bash
- PyCharm
- Anaconda Environment

## 🔸**Algorithm used:**
- Python Script : [`algorithm.py`](https://github.com/gauravpore/URLShortener-app/blob/final/algorithm.py)
```python
  - Python dictionary is used to store (key: original url, value: numeric id).
  - When a  new url is given as input, a new id (latest id + 1) is generated, which will always be unique.
  - Base62 encoding is implemented to encode the original url into a unique id, as base62 supports 56800 times more url than base10.
  - Base10 = 10 * 10 * 10 * 10 * 10 * 10
	- Base62: 62 * 62 * 62 * 62 * 62 * 62
	- Characters used : [0-9] [a-z] [A-Z]
  ```

- Time Complexity:  ``O( n*log_62(id) )``
|| Adding one item to the dictionary takes O(1), so if there are n items, it’ll take ``O(n)`` time.
|| Converting base10 to base62 takes ``O(log_62(id))``.|| Hence time complexity is ``O(n*log_62(id)``
- Space Complexity: ``O(n)``

### 🔸**Scalability:**
The implemented algorithm can encode `1000000000` , i.e billion of urls and generate their corresponding unique shortened id.

## 🔹Working & Features:
```
- The objective of the application is to generate a shortened url, from the original url provided by the user.
- The application uses the django backend for handling requests, and uses sqlite database to store the urls, with timestamp.
- Forms and basic Html is used to enable user-friendly frontend UI, so that users can interact with the application.
- The application generates a unique short url from the original url, so that users can use the converted url to land on the desired original url.
```

>🔸Installation Guide:
- To install django:
```
pip install django
```
- To run the application on local Port 8000:
```py manage.py runserver```

- Refer [this](https://docs.djangoproject.com/en/3.2/) to know more about important commands.

## 🔹Test-Driven Development:
Here are some tests that I have identified that we can implement in order to develop and test our application using TDD, which ensures more bug-free application features.
```
1. The short URL must always be smaller than the original URL.
2. If user gives short url, we must able to recover the original URL
3. The home page must consist of a form to enter the long URL (input url for conversion).
4. Submitting URL must show the shortened url
5. Clicking on the short url must redirect to the original (long) url.
```

## 🔹Deployment Guide:
The django app can be further deployed on the heroku platform, which provides free-web hosting for python apps.
Refer [this](https://devcenter.heroku.com/articles/getting-started-with-python) to deploy the URLShortener application.

## 🔹References:
- [Django Documentation](https://docs.djangoproject.com/en/3.2/)
- [MD5 Encyption algorithm](https://en.wikipedia.org/wiki/MD5)
- [Anaconda Environment](https://www.anaconda.com/)
- [Heroku deployment](https://devcenter.heroku.com/categories/deployment)


## 🔸Screenshot of UI:
![alt tag](https://github.com/gauravpore/URLShortener-app/blob/final/snip.png "Chrome Extension")



