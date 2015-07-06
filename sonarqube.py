"""SonarQube dumper version 1.0."""

import jsonservice

from attrdict import AttrDict
from datetime import datetime

from credentials import Credentials
from dbase import Dbase

# MySQL database table
table = Credentials.table_sonar

# Sonar instance data and credentials
sonar_url = Credentials.url_sonar
sonar_project_key = Credentials.project_key_sonar

# Sonar Metrics to be checked
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

# Database initialization
db = Dbase()
db.open()

# Mysql - Create the INSERT INTO sql query
format_strings = ','.join(['%s'] * (len(sonar_metrics) + 6))
query = """INSERT INTO """ + table + """ (
  `timestamp`,
  `key`,
  `name`,
  `datestamp`,
  `lang`,
  `version`,`""" \
  + '`,`'.join(sonar_metrics) + """`
) VALUES (""" + format_strings + """)"""

# Compose Query for SonarQube
sonarquery = sonar_url + \
    '/api/resources?resource=' + \
    sonar_project_key + \
    '&metrics=' + ','.join(sonar_metrics)

# Retrieve the sonarqube Json file
sonar_json = jsonservice.get_json(sonarquery, Credentials.header_auth_sonar)

# Saves Date stamp for this dump
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
        'UQASAR',  # project.name, this has been harcoded to avoid problems
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
    db.query(query, values)

    # Close the database connection
    db.close()

    print (datestamp
           + ' Operation finished, updated metrics SonarQube '
           + project.name + ' Project.')
