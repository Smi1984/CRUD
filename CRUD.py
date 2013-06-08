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
import types

class CRUD_GUI:

    def __init__(self):

        self.builder = Gtk.Builder()
        self.builder.add_from_file("CRUD.glade")
        self.handlers = {"onDeleteWindow": Gtk.main_quit,
                         "onButtonPressed": self.onButtonPressed,
                         "onAboutDialog": self.onAboutDialog,
                         "onCombochanged": self.onCombochanged,
                         "onCloseAbout": self.onCloseAbout,
                         "onDBActionActivate": self.onDBActionActivate}
       
        
        
        
        #inicializar la base de datos, conectandola
        self.dbobj = Dbclass('DBCrud','crud','cruduser')
        self.dbobj.connect()
        
        #combobox

        
        self.viselcomb = self.builder.get_object("combobox1")
        self.viselcomb.set_sensitive(False) #solo activo en los menus eliminar y visualizar
        
        
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
		if self.opt == 2: # eliminar
		   #desactivar botón hasta que se seleccione otro dato
		   self.button1.set_sensitive(False)
		   #update combobox
		   self.fillCombobox() 
		   self.clearTextbox()
		   print "eliminar"
		   self.status_bar.push(0, "Datos eliminados")
		elif self.opt == 1: # insertar
		   print "insertar"
		   getclase=self.lclase.get_text()
		   getcrew=self.lcrew.get_text()
		   getlong=self.llong.get_text()
		   getanch=self.lanch.get_text()
		   getalt=self.lalt.get_text()

		   if getanch == "" or getlong == "" or getcrew == "" or getalt == "" or getclase == "":
			   self.status_bar.push(0, "Error: Algunos de los datos están en blanco")
		   else:
			   try:
				   
				   
				   getintcrew = int(getcrew)
				   getintlong = int(getlong)
				   getintcrew = int(getcrew)
				   getintalt =int(getalt)
				   getintanch = int(getanch)
				   self.dbobj.insData(getclase,getcrew,getlong,getanch,getalt)
				   self.status_bar.push(0, "Datos insertados")
				   self.clearTextbox()			
			   except:
				   self.status_bar.push(0, "Error: Algunos de los datos no són del tipo correcto")
			   else:
				   self.dbobj.insData(getclase,getcrew,getlong,getanch,getalt)
				   self.status_bar.push(0, "Datos insertados")
				   self.clearTextbox()			
	  	   
		elif self.opt == 4: #update 
		   print "update"
		   self.status_bar.push(0, "Datos actualizados")
        

    
    def onDBActionActivate(self, menuitem):
		
        self.status_bar.push(0, menuitem.get_label())
		#Sacando información en la barra de estado
        self.action = menuitem.get_label()
        self.clearTextbox()
        if self.action == "Insertar":
           self.insertarData()    
        elif self.action == "Eliminar":
           self.eliminarData()			
        elif self.action == "Actualizar":
           self.actualizarData()          
        else:
           self.visualizarData()
		   
    def insertarData(self):
        self.opt = 1
        self.button1.set_label("Insertar")
        self.viselcomb.set_sensitive(False)
        self.button1.set_sensitive(True)
        self.fillCombobox() 
       

    def eliminarData(self):
        self.opt = 2
        self.button1.set_label("Eliminar")
        self.viselcomb.set_sensitive(True)
        self.button1.set_sensitive(True)
        self.fillCombobox()

    def visualizarData(self):
        self.opt = 3
        self.button1.set_sensitive(False)  
        reg = self.dbobj.showData()
        self.fillTextbox(reg)
        

    
    def clearTextbox(self):
		self.lclase.set_text("")
		self.lcrew.set_text("")
		self.llong.set_text("")
		self.lanch.set_text("")
		self.lalt.set_text("")
		self.imgshp.set_from_file(self.get_image("Portada"))
    
    def fillTextbox(self, datalist):
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
	
    def onCombochanged(self,box):
		#Visualizar primero los datos antes de eliminar
        reg = self.dbobj.showData()
        self.fillTextbox(reg)    
        tree_iter = box.get_active_iter()
        if tree_iter != None:
			if self.opt == 2: # eliminar
			  model = box.get_model()
			  clase = model[tree_iter][0]
			  self.dbobj.delData(clase)
			  print "eliminar" + clase
			elif self.opt == 1: # insertar
			  print "insertar"
			elif self.opt == 4: #update 
			  print "update"
		
  
    def get_image(self, name):
		
		images ={'Akira': 'src/Akira.jpg',
				 'Portada': 'src/star_trek_portada.png',}
  
		if images.has_key(name):
			return images[name]
		else:
		    return images['Portada']    
        
    def actualizarData(self):
        self.opt = 4
        self.button1.set_label("Actualizar")
        self.button1.set_sensitive(True) 
        #primer valor el id del campo a actualizar
        #los otros campos son los nuevos datos
        self.dbobj.updateData(99,"llll",11,21,12,2)
    
    def fillCombobox(self):
        store = Gtk.ListStore(str)
        lista = self.dbobj.listDataClase()
        store.clear()
        self.viselcomb.clear()
        #llenamos el combobox
        for cmp in lista:
            store.append([cmp["Clase"]])

        self.viselcomb.set_model(store)
        cell = Gtk.CellRendererText()
        self.viselcomb.pack_start(cell, True)
        self.viselcomb.add_attribute(cell, 'text', 0)
    
        
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
