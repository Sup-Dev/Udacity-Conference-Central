#!/usr/bin/env python

"""
main.py -- Udacity conference server-side Python App Engine
    HTTP controller handlers for memcache & task queue access

$Id$

created by wesc on 2014 may 24

"""

__author__ = 'wesc+api@google.com (Wesley Chun)'

import webapp2
from google.appengine.api import app_identity
from google.appengine.api import mail
from conference import ConferenceApi

from google.appengine.api import memcache
from google.appengine.ext import ndb
from models import Session

from conference import MEMCACHE_SPEAKER_KEY


class SetAnnouncementHandler(webapp2.RequestHandler):
    def get(self):
        """Set Announcement in Memcache."""
        ConferenceApi._cacheAnnouncement()
        self.response.set_status(204)


class SendConfirmationEmailHandler(webapp2.RequestHandler):
    def post(self):
        """Send email confirming Conference creation."""
        mail.send_mail(
            'noreply@%s.appspotmail.com' % (
                app_identity.get_application_id()),     # from
            self.request.get('email'),                  # to
            'You created a new Conference!',            # subj
            'Hi, you have created a following '         # body
            'conference:\r\n\r\n%s' % self.request.get(
                'conferenceInfo')
        )


# Task 4
class CheckFeaturedSpeakerHandler(webapp2.RequestHandler):
    def post(self):
        """Set featured speaker."""
        query = Session.query().filter(Session.speaker_key == self.request.get('speaker_key'))

        if query.count() > 1:
            speaker = self.request.get('speaker')
            message = speaker + " is our featured speaker"
            memcache.set(MEMCACHE_SPEAKER_KEY, message)

app = webapp2.WSGIApplication([
    ('/crons/set_announcement', SetAnnouncementHandler),
    ('/tasks/send_confirmation_email', SendConfirmationEmailHandler),
    ('/tasks/check_featured_speaker', CheckFeaturedSpeakerHandler),
], debug=True)
