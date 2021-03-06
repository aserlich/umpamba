import csv
import sys
import sqlite3

'''
This little piece of code will port a csv exports from mongoexport and input it into a sqlite3 database
could be abstracted to work generically, must use python 3+ for UTF reasons. 
'''

conn = sqlite3.connect("db.sqlite3")

c = conn.cursor()

# try:
#     c.execute('drop table saNews')
# except:
#     pass

# c.execute('create table saNews (_id text, author text ,downloaded_at text,id text,meta_description text, owner text,publication text,published text,sub_type text,summary text,text text,title text,url text);')

csv.field_size_limit(sys.maxsize)

with open("saNewsDb.csv", "r") as f:
    csvReader = csv.reader(f)
    n = 0
    for row in csvReader:
        if n != 0:
            blarg = row[0:3]
            blarg += row[4:13]
            for i in range(0,12):
                if blarg[i] is None:
                    blarg[i] = ''
            try:
                c.execute('INSERT INTO newscoder_story ' \
                          '(_id, author, downloaded_at, ' \
                          'meta_description, owner, publication, ' \
                          'published, sub_type, summary, text, title, url)' \
                          ' VALUES (?,?,?,?,?,?,?,?,?,?,?,?)', blarg)
            except sqlite3.IntegrityError as e:
                print(blarg)
                print(e)
                      
        n += 1

conn.commit()
