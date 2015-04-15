import MySQLdb
import requests
import json

from requests.auth import HTTPBasicAuth
from attrdict import AttrDict
from datetime import datetime

from credentials import Credentials

# MySQL database credentials
host = Credentials.host
user = Credentials.user
passwd = Credentials.passwd
db = Credentials.db
table = Credentials.table_sonar

# Sonar instance data and credentials
sonar_url = Credentials.url_sonar
sonar_user = Credentials.user_sonar
sonar_passwd = Credentials.passwd_sonar
sonar_project_key = Credentials.project_key_sonar
sonar_metrics = [
    'lines',
    'ncloc',
    'classes',
    'files',
    'packages',
    'functions',
    'accessors',
    'statements',
    'public_api',
    'complexity',
    'class_complexity',
    'function_complexity',
    'file_complexity',
    'comment_lines',
    'comment_lines_density',
    'public_documented_api_density',
    'public_undocumented_api',
    'tests',
    'test_execution_time',
    'test_errors',
    'skipped_tests',
    'test_failures',
    'test_success_density',
    'coverage',
    'lines_to_cover',
    'uncovered_lines',
    'line_coverage',
    'conditions_to_cover',
    'uncovered_conditions',
    'branch_coverage',
    'duplicated_lines',
    'duplicated_blocks',
    'duplicated_files',
    'duplicated_lines_density',
    'weighted_violations',
    'violations_density',
    'violations',
    'blocker_violations',
    'critical_violations',
    'major_violations',
    'minor_violations',
    'info_violations'
]

# Establish a MySQL connection
database = MySQLdb.connect(host, user, passwd, db)

# Get the cursor, which is used to traverse the database, line by line
cursor = database.cursor()

# Mysql - Create the INSERT INTO sql query
format_strings = ','.join(['%s'] * (len(sonar_metrics) + 6))
query = """INSERT INTO """ + table + """ (
  `timestamp`,
  `key`,
  `name`,
  `datestamp`,
  `lang`,
  `version`,
  `lines`,
  `ncloc`,
  `classes`,
  `files`,
  `packages`,
  `functions`,
  `accessors`,
  `statements`,
  `public_api`,
  `complexity`,
  `class_complexity`,
  `function_complexity`,
  `file_complexity`,
  `comment_lines`,
  `comment_lines_density`,
  `public_documented_api_density`,
  `public_undocumented_api`,
  `tests`,
  `test_execution_time`,
  `test_errors`,
  `skipped_tests`,
  `test_failures`,
  `test_success_density`,
  `coverage`,
  `lines_to_cover`,
  `uncovered_lines`,
  `line_coverage`,
  `conditions_to_cover`,
  `uncovered_conditions`,
  `branch_coverage`,
  `duplicated_lines`,
  `duplicated_blocks`,
  `duplicated_files`,
  `duplicated_lines_density`,
  `weighted_violations`,
  `violations_density`,
  `violations`,
  `blocker_violations`,
  `critical_violations`,
  `major_violations`,
  `minor_violations`,
  `info_violations`
) VALUES (""" + format_strings + """)"""

# Query for SonarQube
sonarquery = sonar_url + '/api/resources?resource=' + \
    sonar_project_key + '&' + 'metrics=' + ','.join(sonar_metrics)

# Request to Jira API
# r = requests.get(sonarquery, auth=HTTPBasicAuth(sonar_user, sonar_passwd))

# HTTPBasicAuth is faling,this is another way
r = requests.get(sonarquery, headers=Credentials.header_auth_sonar)

# Convert the response to JSON
r.headers['content-type']
r.encoding
sonar_json = r.json()

datestamp = str(datetime.today())

# Parse the resporse with all the proejcts queried
for project in sonar_json:

    # inproves JSON attributes accesibility
    project = AttrDict(project)

    # Assigns values  to compose the MySQL Query

    # Project details
    projectdata = (
        datestamp,
        project.key,
        project.name,
        project.date,
        project.lang,
        project.version
    )

    # Metric List form Sonar metric list to store values
    metriclist = list(sonar_metrics)

    # Parse the metrics
    for metric in project.msr:
        if metric.key in sonar_metrics:
            metriclist[sonar_metrics.index(metric.key)] = metric.val

    # Metric List converted form list to tuple
    metricvalues = tuple(metriclist)

    # Concatenates all the  items
    values = projectdata + metricvalues

    # Execute the MySQL Query
    cursor.execute(query, values)

    # ### Closing MySQL stuff ###

    # Close the cursor
    cursor.close()

    # Commit the transaction
    database.commit()

    # Close the database connection
    database.close()

    print (datestamp
           + ' Operation finished, updated metrics SonarQube '
           + project.name + ' Project.')
