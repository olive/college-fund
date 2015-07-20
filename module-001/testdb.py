#!/usr/bin/python

import MySQLdb



tables = [
"""
drop table if exists Ratings;
""",
"""
drop table if exists Notes;
""",
"""
drop table if exists Users;
""",
"""

create table if not exists Users (
	ID MEDIUMINT NOT NULL AUTO_INCREMENT,
	Name varchar(30) NOT NULL,
	DateCreated DATETIME NOT NULL,
	PRIMARY KEY (ID)
);
""",
"""
create table if not exists Notes (
	ID MEDIUMINT NOT NULL AUTO_INCREMENT,
	UserID MEDIUMINT NOT NULL,
	DatePosted DATETIME NOT NULL,
	Inactive TINYINT(1) NOT NULL,
	DateInactivated DATETIME NOT NULL,
	PRIMARY KEY (ID)
);
""",
"""
create table if not exists Ratings (
	ID MEDIUMINT NOT NULL AUTO_INCREMENT,
	Rating MEDIUMINT NOT NULL,
	NoteID MEDIUMINT NOT NULL,
	UserID MEDIUMINT NOT NULL,
	DateRated DATETIME NOT NULL,
	FOREIGN KEY (NoteID)
		REFERENCES Notes(ID)
		ON DELETE CASCADE,
	FOREIGN KEY (UserID)
		REFERENCES Users(ID)
		ON DELETE CASCADE,
	PRIMARY KEY (ID)
);
"""]


# Open database connection
db = MySQLdb.connect("localhost","root","","APPDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

for table in tables:
	cursor.execute(table)
	print("working")

cursor.execute("insert into Users (Name, DateCreated) values ('TestUser', NOW())")
cursor.execute("select * from Users")
data = cursor.fetchone()
print("Data = %s" % str(data))
cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
cursor.execute("truncate table Ratings")
cursor.execute("truncate table Notes")
cursor.execute("truncate table Users")
cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")
# disconnect from server
db.close()
