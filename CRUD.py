#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  CRUD.py
#       
#  Copyright 2013 Sergio Morlans <https://github.com/ikkipower/CRUD.git>
#       
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#       
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#       
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.

# CREATE DATABASE DBCrud;
# GRANT ALL ON DBCrud.* TO 'crud'@'localhost' IDENTIFIED BY 'cruduser';
# USE DBCrud;

from gi.repository import Gtk, GdkPixbuf, Gdk
from dbclass import Dbclass
import os, sys
import MySQLdb 

class CRUD_GUI:

    def __init__(self):

        self.builder = Gtk.Builder()
        self.builder.add_from_file("CRUD.glade")
        self.handlers = {"onDeleteWindow": Gtk.main_quit,
                         "onAboutDialog": self.onAboutDialog,
                         "onCloseAbout": self.onCloseAbout,
                         "onDBActionActivate": self.onDBActionActivate}
        
        dbobj = Dbclass('DBCrud','crud','cruduser')
        dbobj.connect()
        dbobj.create_table("ships")
        
        button1 = self.builder.get_object("addButton")
        #self.builder.get_object("label1").set_label("erase")
        #button1.set_label("Update")
        button1.set_sensitive(False)
        
        self.builder.connect_signals(self.handlers)
        self.window = self.builder.get_object("stwindow")
        self.window.show_all()
 
    def onDBActionActivate(self, menuitem):
		#box = self.builder.get_object("entry1")
		#box.set_text(menuitem.get_label())
		self.action = menuitem.get_label() 
		
    
    def destroy(self,window):
        Gtk.main_quit()
    
    def onAboutDialog(self, *args):
        self.about = self.builder.get_object("aboutdialog1")
        self.about.show_all()
    
    def onCloseAbout(self, *args):
        self.about = self.builder.get_object("aboutdialog1")
        self.about.hide()
  
    
def main():
    app = CRUD_GUI()
    Gtk.main()

if __name__ == "__main__":
    main()
