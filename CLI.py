#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# vim:fileencoding=utf8
# gflags is python 2.x only *sigh*

from Main import Main
import sys

class BasicCLI():
	"""Class for creating and handling the very basic CLI"""
	def __init__(self):
		print "Sikevux's awesome homework thingey stuff\n"
		self.interface()
		pass

	def interface(self):
		self.luser_input = raw_input("-> ")
		if self.luser_input == "t":
			Main().homework()
		elif self.luser_input.startswith("add "):
			self.interface_add()
		elif self.luser_input == "exit":
			sys.exit()
		else:
			print "Your input was:", self.luser_input
                self.interface()
	def interface_add(self):
		task_add_input = self.luser_input[4:]
		task_add_data = task_add_input.split("::")
		task_add_notes = ""
		task_add_title = task_add_data[0]
		if len(task_add_data) >= 2:
			task_add_notes = task_add_data[1]

		Main().addTask(task_add_title, task_add_notes)
