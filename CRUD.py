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
                         "onButtonPressed": self.onButtonPressed,
                         "onAboutDialog": self.onAboutDialog,
                         "onCloseAbout": self.onCloseAbout,
                         "onDBActionActivate": self.onDBActionActivate}
       
        
        
        
        #inicializar la base de datos, conectandola
        self.dbobj = Dbclass('DBCrud','crud','cruduser')
        self.dbobj.connect()
        
        #combobox
        
        self.viselcomb = self.builder.get_object("combobox1")
        
        #cogemos la barra de estado
        self.status_bar = self.builder.get_object("statusbar1")
        self.status_bar.push(0, "Conectado a la base de datos")
        
        #solamente nos interesa para añadir el nombre del 
        #fichero que usaremos para cargar la foto. Se necesita que la 
        #imagen este en el directorio src
        
        self.lclase = self.builder.get_object("lclase")
        self.lcrew = self.builder.get_object("lcrew")
        self.llong = self.builder.get_object("llong")
        self.lanch = self.builder.get_object("lanch")
        self.lalt = self.builder.get_object("lalt")
        
        
        self.imgshp = self.builder.get_object("imgships")
        
        
        #boton 1 inicialmente desactivado
        self.button1 = self.builder.get_object("addButton")
        self.button1.set_sensitive(False)
        
        self.builder.connect_signals(self.handlers)
        self.window = self.builder.get_object("stwindow")
        self.window.show_all()

    def onButtonPressed(self,button):
        self.status_bar.push(0, "Ejecutando insertar data")
        
        
		
    
    def onDBActionActivate(self, menuitem):
		
        self.status_bar.push(0, menuitem.get_label())
		#Sacando información en la barra de estado
        self.action = menuitem.get_label()
        
        if self.action == "Insertar":
           self.insertarData()
           
        elif self.action == "Eliminar":
           self.eliminarData()
			
        elif self.action == "Actualizar":
           self.actualizarData()
           
        else:
           self.visualizarData()
		   
    def insertarData(self):
        self.button1.set_label("Insertar")
        self.button1.set_sensitive(True)
        self.dbobj.insData("Akira",88,77,66,55)
         

    def eliminarData(self):
        self.button1.set_label("Eliminar")
        self.button1.set_sensitive(True)
        self.dbobj.delData("kkkk")

    def visualizarData(self):
        self.button1.set_sensitive(False)  
        reg = self.dbobj.showData()
        
        self.filltextbox(reg)

    
    def filltextbox(self, datalist):
		cmplist = ["id", "Clase", "Crew", "Longi", "Anch", "Alt"]                
		for cmp in datalist:
			
			if cmp == "Clase":
				self.lclase.set_text(datalist[cmplist[1]])
				
			elif cmp == "Crew":
				self.lcrew.set_text(str(datalist[cmplist[2]]))
			elif cmp == "Longi": 
				self.llong.set_text(str(datalist[cmplist[3]]))
			elif cmp == "Anch":
				self.lanch.set_text(str(datalist[cmplist[4]]))
 			elif cmp == "Alt":
				self.lalt.set_text(str(datalist[cmplist[5]]))
			
		self.imgshp.set_from_file(self.get_image(datalist[cmplist[1]]))
		    
  
    def get_image(self, name):
		
		images ={'Akira': 'src/Akira.jpg',
				 'Portada': 'src/star_trek_portada.png',}
  
		if images.has_key(name):
			return images[name]
		else:
		    return images['Portada']    
        
    def actualizarData(self):
        self.button1.set_label("Actualizar")
        self.button1.set_sensitive(True) 
        #primer valor el id del campo a actualizar
        #los otros campos son los nuevos datos
        self.dbobj.updateData(99,"llll",11,21,12,2)
        
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
