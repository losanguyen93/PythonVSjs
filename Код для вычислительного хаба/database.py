#!/usr/bin/python
# -*- coding: utf-8
import MySQLdb
import string
import datetime


def  input_dataperson(lname, data_name, bucket_name):
	# соединяемся с базой данных
	db = MySQLdb.connect(host="eu-cdbr-sl-lhr-01.cleardb.net", user="bd51db6b9db508", passwd="1561ab78", db="ibmx_29e62892a53c4f3", charset='utf8')
	# формируем курсор
	cursor = db.cursor()
	# запрос к БД
	# выполняем запрос
	print "input_dataperson"
	lname = "\'" + lname + "\'"
	sql = "SELECT PersonID FROM persons WHERE Mail LIKE " + lname
	cursor.execute(sql)
	db.commit()
	data =  cursor.fetchall()
	if len(data) != 0:
		now = datetime.datetime.now()
		date_now = now.strftime("%Y-%m-%d %H:%M")
		cursor.execute("INSERT INTO dataofperson (Person_ID ,data_name, bucket_name, data_of_file) VALUES (%s, %s, %s, %s);", (str(data[0][0]), data_name, bucket_name, date_now))
		db.commit()
	cursor.close()
	db.close()

def get_bucket_name(lname):
	# соединяемся с базой данных
	db = MySQLdb.connect(host="eu-cdbr-sl-lhr-01.cleardb.net", user="bd51db6b9db508", passwd="1561ab78", db="ibmx_29e62892a53c4f3", charset='utf8')
	# формируем курсор
	cursor = db.cursor()
	# запрос к БД
	# выполняем запрос
	data = []
	data2 = []
	print "get_bucket_name"
	lname = "\'" + lname + "\'"
	sql = "SELECT PersonID FROM ibmx_29e62892a53c4f3.persons WHERE persons.Mail LIKE " + lname
	cursor.execute(sql)
	db.commit()
	data =  cursor.fetchall()
	if len(data) != 0: 
			cursor.execute("SELECT bucket_name FROM dataofperson WHERE Person_ID LIKE (%s);",(str(data[0][0])))
			db.commit()
			data2 =  cursor.fetchall()
			if len(data2) != 0:
				return data2[0][0]

	
	print "data2 = ", data2
	return data2
	cursor.close()
	db.close()


def get_data_file(lname):
	# соединяемся с базой данных
	db = MySQLdb.connect(host="eu-cdbr-sl-lhr-01.cleardb.net", user="bd51db6b9db508", passwd="1561ab78", db="ibmx_29e62892a53c4f3", charset='utf8')
	# формируем курсор
	cursor = db.cursor()
	# запрос к БД
	# выполняем запрос
	data = []
	data2 = []
	lname = "\'" + lname + "\'"
	sql = "SELECT PersonID FROM ibmx_29e62892a53c4f3.persons WHERE persons.Mail LIKE " + lname
	cursor.execute(sql)
	db.commit()
	data =  cursor.fetchall()
	print "get data file = ", data[0][0]
	if len(data) != 0:
			# print "get_data_profile = ", data
			cursor.execute("SELECT data_name, data_of_file FROM persons INNER JOIN dataofperson WHERE PersonID = (%s) AND Person_ID = (%s);",(str(data[0][0]), str(data[0][0])))
			db.commit()
			data2 =  cursor.fetchall()
			print "get data2 file = ", data2
			if len(data2) != 0:
				return data2
	return data2
	cursor.close()
	db.close()


def get_profile(lname):
	# соединяемся с базой данных
	db = MySQLdb.connect(host="eu-cdbr-sl-lhr-01.cleardb.net", user="bd51db6b9db508", passwd="1561ab78", db="ibmx_29e62892a53c4f3", charset='utf8')
	# формируем курсор
	cursor = db.cursor()
	# запрос к БД
	# выполняем запрос
	data = []
	lname = "\'" + lname + "\'"
	sql = "SELECT PersonID, LastName, FirstName, Address, Mail FROM ibmx_29e62892a53c4f3.persons WHERE persons.Mail LIKE " + lname
	cursor.execute(sql)
	db.commit()
	data =  cursor.fetchall()
	return data
	cursor.close()
	db.close()


def get_bucket_name(lname):
	# соединяемся с базой данных
	db = MySQLdb.connect(host="eu-cdbr-sl-lhr-01.cleardb.net", user="bd51db6b9db508", passwd="1561ab78", db="ibmx_29e62892a53c4f3", charset='utf8')
	# формируем курсор
	cursor = db.cursor()
	# запрос к БД
	# выполняем запрос
	data = []
	data2 = []
	lname = "\'" + lname + "\'"
	sql = "SELECT PersonID FROM ibmx_29e62892a53c4f3.persons WHERE persons.Mail LIKE " + lname
	cursor.execute(sql)
	db.commit()
	data =  cursor.fetchall()
	if len(data) != 0:
		cursor.execute("SELECT bucket_name FROM dataofperson WHERE Person_ID = (%s);",(str(data[0][0])))
		db.commit()
		data2 =  cursor.fetchall()
		return data2[0][0]
	return data
	cursor.close()
	db.close()