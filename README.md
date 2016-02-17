App Engine application for the Udacity training course.

## Products
- [App Engine][1]

## Language
- [Python][2]

## APIs
- [Google Cloud Endpoints][3]

## Setup Instructions
1. Update the value of `application` in `app.yaml` to the app ID you
   have registered in the App Engine admin console and would like to use to host
   your instance of this sample.
1. Update the values at the top of `settings.py` to
   reflect the respective client IDs you have registered in the
   [Developer Console][4].
1. Update the value of CLIENT_ID in `static/js/app.js` to the Web client ID
1. (Optional) Mark the configuration files as unchanged as follows:
   `$ git update-index --assume-unchanged app.yaml settings.py static/js/app.js`
1. Run the app with the devserver using `dev_appserver.py DIR`, and ensure it's running by visiting your local server's address (by default [localhost:8080][5].)
1. (Optional) Generate your client library(ies) with [the endpoints tool][6].
1. Deploy your application.


[1]: https://developers.google.com/appengine
[2]: http://python.org
[3]: https://developers.google.com/appengine/docs/python/endpoints/
[4]: https://console.developers.google.com/
[5]: https://localhost:8080/
[6]: https://developers.google.com/appengine/docs/python/endpoints/endpoints_tool

## Task 1 
### Session and Speaker implementation

The Session is linked to the Conference with the help of the conference key, hence a conference is always associate with the session. Also, I have separated the date and time fields so as to easily handle it.
 
For the Speaker I have created a separate model with contains the name, biography and an extra profile field if the speaker choose to be an attendee. Also, note that I have added a speaker field in Session so as to associate a speaker with it. 

## Task 3 
### Additional Queries

For the first query I have added an end point to fetch all those conferences which are only partially filled.
 
In the next query I have added an end point to fetch all the speakers present.

### Query Problem

The query problem was that in case of non-workshop and before 7pm we had to compare in two different fields.

To get around this issue, I simply split the problem into two stages. First, I get the items that are not workshops. Then, I checked through the *start_time* attribute for time related comparisons.

## Task 4 
## Featured Speaker

Added a task queue to check for speaker and added it to memcache.
