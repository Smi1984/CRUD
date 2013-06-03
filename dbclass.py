#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       dbclass.py       
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

from math import sqrt
import MySQLdb 

class Dbclass:

      def __init__ (self,dbname,dbuser,dbpasswd):
		  self.dbname = dbname
		  self.dbuser = dbuser
		  self.dbpasswd = dbpasswd
          

      def connect(self):
         Conexion = MySQLdb.connect(host='localhost', user='crud',passwd='cruduser', db='DBCrud')
         # Creamos el cursor, pero especificando que sea de la subclase DictCursor
         
         self.micursor = Conexion.cursor(MySQLdb.cursors.DictCursor);
         
      def insData(self,clase,crew,longi,anch,alt,fname): 
         query = "INSERT INTO ships(id,Clase,Crew,Longi, Anch, Alt, Fname)VALUES(3,\"sss\",33,33,33,33,\"fff\");"
         self.micursor.execute(query)
      
      def disconnect():
         self.micursor.close();
