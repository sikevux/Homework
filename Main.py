#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# vim:fileencoding=utf8
# gflags is python 2.x only *sigh*

import OAuth
_service = OAuth.Authentication().auth()
_tasklists = _service.tasklists().list().execute()

class Main():
	def getTasklistId(self): 
		tasklists = _tasklists
		returning = False

		for tasklist in tasklists['items']:
			if tasklist['title'] == "Homework":
				returning = True
				return tasklist['id']
				break
		if returning is not True:
			tasklist = {
				'title': 'Homework',
			}

			result = _service.tasklists().insert(body=tasklist).execute()
			return result['id']

	def homework(self):
		tasks = _service.tasks().list(tasklist=self.getTasklistId()).execute()
		
		for task in tasks['items']:
			print task['title']

	def addTask(self, title, notes):
		task = {
			'title': title,
			'notes': notes,
		}
		result = _service.tasks().insert(tasklist=self.getTasklistId(), body=task).execute()
