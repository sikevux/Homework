#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# vim:fileencoding=utf8
# gflags is python 2.x only *sigh*

import gflags
import httplib2

from apiclient.discovery import build
from oauth2client.file import Storage
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.tools import run

class Authentication():
	"""Class to handle the Authentication"""

	def auth(self):
		FLAGS = gflags.FLAGS
		FLOW = OAuth2WebServerFlow(
				client_id='',
				client_secret='',
				scope='https://www.googleapis.com/auth/tasks',
				user_agent='Homework/0.0.1')

		storage = Storage('tasks.dat')
		credentials = storage.get()

		if credentials is None or credentials.invalid == True:
				credentials = run(FLOW, storage)

		http = httplib2.Http()
		http = credentials.authorize(http)

		service = build(serviceName='tasks', version='v1', http=http,
				developerKey='')
		return service
