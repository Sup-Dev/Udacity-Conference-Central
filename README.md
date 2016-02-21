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

The Session is linked to the Conference with the help of the conference key as Conference is an ancestor of the Session, hence a conference is always associate with the session. Also, I have separated the date and time fields so as to easily handle it.
 
For the Speaker I have created a separate model with contains the name, biography and an extra profile field if the speaker choose to be an attendee. Also, note that I have added a speaker field in Session so as to associate a speaker with it.
 
Session field entities:
* highlights - All the topics that are highlights for the session.
* speaker - Name of the speaker.
* duration - Total running time for the conference.
* type_of_session - The category of the session it comes in - ex: workshops, walkthrough, demos etc
* start_date - The date when the session is being held
* start_time - The time when the session starts

Session endpoints:
* createSession - creates a new session.
* getConferenceSessions - gets all sessions that have a conference as their ancestor
* getConferenceSessionsByType - gets all the session based on the type specified
* getSessionsBySpeaker - gets all session that a speaker is taking

Speaker field entities:
* displayName - the name of the speaker
* profileKey - user key linked to this speaker
* biography - small bio data of the speaker

Speaker endpoints:
* addSpeaker - create a new speaker


## Task 3 
### Additional Queries

For the first query I have added an end point to fetch all those conferences which are only partially filled.
 
In the next query I have added an end point to fetch all the speakers present.

Query endpoints:
* getPartialConferences - fetches all conferences whose data is only filled partially
* getSpeakers - get a list of all speakers

### Query Problem

The query problem was that in case of non-workshop and before 7pm we had to compare in two different fields. It is as specified in the app engine document, "inequality filters are limited to at most one property".

To get around this issue, I simply split the problem into two stages. First, I get the items that are not workshops and has conference as it's ancestor by using **ndb.AND** query. Then, I loop through all items received and check the *start_time* attribute of the item and check if the *hour* property is less than the number of **hours** received from the url for time related comparisons.

I have given the solution to the problem in the endpoint **getConferenceBefore**.

## Task 4 
## Featured Speaker

Added a task queue to check for speaker and added it to memcache.
