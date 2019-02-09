#!/usr/bin/env python
#
# AccessDump.py
# A simple script to dump the contents of a Microsoft Access Database.
# It depends upon the mdbtools suite:
#   http://sourceforge.net/projects/mdbtools/

# original py script
# http://mazamascience.com/WorkingWithData/?p=168
# source
import sys, subprocess # python v 2.4
import os.path
from colour import bcolors

if(len(sys.argv) != 2):
  sys.exit(sys.argv[0] + " takes one argument.")

DATABASE = sys.argv[1]

if(not DATABASE.endswith(".mdb")):
  sys.exit("Argument file must be in .mdb")

if(not os.path.isfile(DATABASE) ):
  sys.exit(
    bcolors.FAIL + sys.argv[1] + " does not exist." +
    bcolors.FAIL)

# Get the list of table names with "mdb-tables"
table_names = subprocess.Popen(["mdb-tables", "-1", DATABASE],
                               stdout=subprocess.PIPE).communicate()[0]
tables = table_names.split('\n')

# Dump each table as a CSV file using "mdb-export",
# converting " " in table names to "_" for the CSV filenames.
for table in tables:
    if table != '':
        filename = table.replace(" ","_") + ".csv"
        file = open(filename, 'w')
        print("Dumping " + table)
        contents = subprocess.Popen(["mdb-export", DATABASE, table],
                                    stdout=subprocess.PIPE).communicate()[0]
        file.write(contents)
        file.close()
