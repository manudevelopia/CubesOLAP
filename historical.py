import MySQLdb
import requests
import json
import datetime

from requests.auth import HTTPBasicAuth
from attrdict import AttrDict
from datetime import date

# Local database credentials
#host = "localhost"
#user = "root"
#passwd = "root"

#  Remote database credentials
host =      "mysql.server"
user =      "uqasar"
passwd =    "UqasarAdmin2012"

# Common MySQL credentials
db = 'uqasar$cubes'
table = 'historic'

# Sonar instance data and credentials
cubes_url = 'http://uqasar.pythonanywhere.com/cube/'
cubes_user = 'none'
cubes_passwd = 'none'
cubes_project = 'jira'
cubes_metrics = 'facts'

# Other vars
date = datetime.datetime.now()

# Establish a MySQL connection
database = MySQLdb.connect(host, user, passwd, db)

# Get the cursor, which is used to traverse the database, line by line
cursor = database.cursor()

# Mysql - Create the INSERT INTO sql query
query = """INSERT INTO """ + table + """ (
  `facts`,
  `timestamp`
) VALUES ( %s, %s)"""

# Query for SonarQube
cubesquery = cubes_url + cubes_project + '/'+cubes_metrics

# Request to Jira API
r = requests.get(cubesquery, auth=HTTPBasicAuth(cubes_user, cubes_passwd))

#
if(r.status_code != 200) :
    print '[' + str(date) + '] Cubes facts has NOT been stored'
    quit()

# Convert the response to JSON
r.headers['content-type']
r.encoding
cubes_json = str(r.json())

values = (cubes_json, date)

# Execute the MySQL Query
cursor.execute(query, values)

### Closing MySQL stuff ###

# Close the cursor
cursor.close()

# Commit the transaction
database.commit()

# Close the database connection
database.close()

# Prints the trace to get Logged by system
print '[' + str(date) + '] Cubes facts has been stored'
