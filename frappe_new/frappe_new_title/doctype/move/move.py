# Copyright (c) 2025, imran and contributors
# For license information, please see license.txt
import frappe
from frappe.model.document import Document

class Move(Document):
    pass 

@frappe.whitelist()
def get_movies():
    # get_list data
    # movies = frappe.db.get_list("Move", fields=["movie_name", "rating"])
    # return movies 
    # get_all datas
    # movies = frappe.db.get_all("Move", fields=["movie_name", "rating"])
    # return movies 
    # get_single_data
    # movies = frappe.db.get_value("Move", "01s10ojcsn", "movie_name")
    # return movies
    # get_multiple data
    # movies = frappe.db.get_value('Move', 'Move-001', ['movie_name','genre','release_date','rating'])
    # return movies
    # as dict => get the directory names like ['movie_name':'vikram','genre':'action']=> without as dict=>['vikram','action']
    # movies = frappe.db.get_value('Move', 'Move-001', ['movie_name','genre','release_date','rating'], as_dict=True)
    # return movies
    # with filter
    # movies = frappe.db.get_value('Move',{'genre': 'Comedy'},['movie_name', 'genre', 'release_date', 'rating'], as_dict=True )
    # return movies
    # movies = frappe.db.get_single_value('Move','Move-001', fields=["movie_name", "rating"])
    # return movies
    # set the values in the particular fields single
    # movies = frappe.db.set_value('Move','Move-001','movie_name', 'Tourist Family')
    # return movies
    # set the values in the particular fields multiple
    # movies = frappe.db.set_value('Move', 'Move-001',{'movie_name':'Don', 'genre':'Comedy'})
    # return movies
    # values are updated by the modified timestamp don't update 
    # movies = frappe.db.set_value('Move', 'Move-001', {'movie_name':'Game Of Thrones', 'genre':'Fight'}, update_modified=False)
    # return movies
    # first check if there any records are in the move after then it will update
    # if frappe.db.exists('Move','Move-002'):
    #    movies = frappe.db.set_value('Move', 'Move-001', {'movie_name':'Don', 'genre':'Action'}, update_modified=False)
    #    return movies
    # else:
    #     frappe.msgprint('Record not found')
    # count the records in the db like doctype Move
    # movies = frappe.db.count('Move')
    # return movies
     # count the records in the db like doctype Move in genre filter
    # movies = frappe.db.count('Move', {'genre':'Action'})
    # return movies
    # first if the Move-002 delete the particular record
    # if frappe.db.exists('Move', 'Move-002'):
    #     movies = frappe.db.delete('Move','Move-002')
    #     return movies
    # else:
    #     frappe.msgprint("Record not found")
    # truncate the all records inside the move doctype
    # movies = frappe.db.truncate('Move')
    # return movies
    # commit is use to set the finally commited in the db
    # movies = frappe.db.set_value('Move', 'Move-001',{'movie_name':'Don', 'genre':'Comedy'})
    # # frappe.db.commit()
    # return movies
    # Savepoint - Transaction nadakum pothu, oru spot mark pannuvom nu ninaikkira mathiri.
    # “Indha varai work pannathu safe” nu sollurathu.
    # frappe.db.savepoint(save_point)
    # rollback - Sari illa da... panna changes-ai thirupi cancel pannu" nu sollurathu
    # frappe.db.rollback()
    # frappe.db.sql() -frappe.db.sql() is used to run raw SQL queries directly on the database inside Frappe.
    # movies = frappe.db.sql("SELECT movie_name, genre FROM `tabMove` WHERE genre='Fight'")
    # return movies
    # rename table in the sql
    # movies = frappe.rename_table("DocType", "Movies", "Move")
    # # rename table in the doctype
    # # movies = frappe.rename_doc("DocType", "Movies", "Move")
    # return movies

     movies = frappe.db.get_all("Move", fields=["movie_name", "genre", "release_date", "rating"])
     return movies

