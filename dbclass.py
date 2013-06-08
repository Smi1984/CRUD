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
         self.mycon = MySQLdb.connect(host='localhost', user='crud',passwd='cruduser', db='DBCrud')
         # Creamos el cursor, pero especificando que sea de la subclase DictCursor
         
         self.micursor = self.mycon.cursor(MySQLdb.cursors.DictCursor);
   
         
      
      def insData(self,clase,crew,longi,anch,alt):
         nid = self.idgenerator() + 1
         
         query = "INSERT INTO ships (id, Clase, Crew, Longi, Anch, Alt) VALUES ("+str(nid)+",\""+clase+"\","+str(crew)+","+str(longi)+","+str(anch)+","+str(alt)+");"
         
         self.micursor.execute(query)
         self.mycon.commit() 

      def updateData(self,idold,clase,crew,longi,anch,alt):
         
         query = "UPDATE ships SET Clase = \""+clase+"\", Crew ="+str(crew)+", Longi ="+str(longi)+", Anch="+str(anch)+", Alt="+str(alt)+" WHERE id ="+str(idold)+";"
                 
         self.micursor.execute(query)
         self.mycon.commit() 
      
      def delData(self,cId,cname):
         
         query = "DELETE FROM ships WHERE Id = "+cId+" AND Clase =\""+cname+"\";"
         self.micursor.execute(query)
         self.mycon.commit() 
      
      def showData(self, delid,cname):
        
         query= "SELECT * FROM ships WHERE Id = "+delid+" AND Clase =\""+cname+"\";" 
         self.micursor.execute(query)   
         self.mycon.commit()   
         registro = self.micursor.fetchone()

         # Imprimimos el registro resultante
             
         return registro
         
      def listDataClase(self):

         query= "SELECT Id,Clase FROM ships WHERE 1;" 
         self.micursor.execute(query)
         self.mycon.commit()      
         registro = self.micursor.fetchall()      
         return registro
      
      def disconnect():
         self.micursor.close()
         self.mycon.commit() 

      def idgenerator(self):
         query= "SELECT Max(Id) FROM ships WHERE 1 ORDER BY Id;" 
         self.micursor.execute(query)
         self.mycon.commit()      
         registro = self.micursor.fetchone() 
         return registro['Max(Id)']
      
      
