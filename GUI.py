#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# vim:fileencoding=utf8
# gflags is python 2.x only *sigh*
from Main import Main
import urwid
urwid.set_encoding("UTF-8")
welcome_message = urwid.Edit("Sikevux's awesome homework thingey stuff\n-> ")
def interface_add(self):
	task_add_input = self.luser_input[4:]
	task_add_data = task_add_input.split("::")
	task_add_notes = ""
	task_add_title = task_add_data[0]
	if len(task_add_data) >= 2:
		task_add_notes = task_add_data[1]
		Main().addTask(task_add_title, task_add_notes)

def interface_show(task_show_input):
#	return task_show_input
	return Main().showTask(task_show_input)

def interface_list():
	tasks = Main().listTasks()
	return_value = ""
	for task in tasks['items']:
		return_value += task['title']+"\n"
	return_value = return_value[:-1]
	return return_value

def new_command():
	return urwid.Edit(("-> "))

def new_action(luser_input):
	if luser_input == "exit":
		raise urwid.ExitMainLoop()
	elif luser_input.startswith("add "):
		interface_add()
	elif luser_input.startswith("show "):
		return urwid.Text((interface_show(luser_input[5:])))
	elif luser_input == "list":
		return urwid.Text((interface_list()))
	return urwid.Text((luser_input))

content = urwid.SimpleListWalker([welcome_message])
listbox = urwid.ListBox(content)

def handle_input(input):
	if input != 'enter':
		return
	global focus_widget, position
	focus_widget, position = listbox.get_focus()
	if not hasattr(focus_widget, 'edit_text'):
		return
#	content = [ new_action(focus_widget.edit_text)]
	content[position+1:position+2] = [ new_action(focus_widget.edit_text)]
	if not content[position+2:position+3]:
		content.append(new_command())
	listbox.set_focus(position+2)

main_loop = urwid.MainLoop(listbox, unhandled_input=handle_input)
main_loop.run()
