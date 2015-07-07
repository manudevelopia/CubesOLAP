"""SonarQube dumper version 1.0."""

import jsonservice

from attrdict import AttrDict
from datetime import datetime

from credentials import Credentials
from dbase import Dbase

# Timestamp to grab all metric values with the same date on evey dump
datestamp = None

# MySQL database table
table = Credentials.table_sonar

# Sonar instance data and credentials
sonar_url = Credentials.url_sonar + '/api/resources?resource='
sonar_project_key = Credentials.project_key_sonar

# Sonar Metrics to be checked in SonarQube
# undesired metrics can be commented
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


def get_components(project_key):
    """Get Json of the project from the Sonarqube."""
    query = sonar_url + project_key + '&depth=-1'
    return jsonservice.get_json(query, Credentials.header_auth_sonar)


def get_metric_values(key):
    """Get Metric values to be persisted in MySQL."""
    # Compose Query for SonarQube
    query = sonar_url + \
        key + '&metrics=' + ','.join(sonar_metrics)

    # Retrieve the sonarqube Json file
    sonar_json = jsonservice.get_json(query, Credentials.header_auth_sonar)

    # Parse the resporse to retrieve the metric values
    for project in sonar_json:
        # inproves JSON attributes accesibility
        project = AttrDict(project)

        # Project details
        projectdata = (
            datestamp,
            project.key,
            'UQASAR',  # project.name, this has been harcoded to avoid problems
            project.date,
            project.lang,
            'Version 1'  # .project.version
        )

        # Metric List to store values with 0 to store Sonar metric list
        # maybe list should contain 'None' instead 0.
        metriclist = list(0 for i in xrange(len(sonar_metrics)))

        # Parse the metrics
        for metric in project.msr:
            if metric.key in sonar_metrics:
                metriclist[sonar_metrics.index(metric.key)] = metric.val

        # Metric List converted form list to tuple
        metricvalues = tuple(metriclist)

        # Concatenates all the  items
        return projectdata + metricvalues


def main():
    """SonarQube script data dumper."""
    global datestamp

    # Generate Timestamp for this dump
    datestamp = str(datetime.today())

    # Database initialization
    db = Dbase()
    db.open()

    # Get Project Sonar Components
    components = get_components(sonar_project_key)
    for component in components:
        c = AttrDict(component)
        # Get the values for the key
        values = get_metric_values(c.key)
        # Execute the MySQL Query
        db.query(query, values)

    # Close the database connection
    db.close()

    # Print a Happy ending
    print (datestamp + ' Operation finished, metrics updated.')


if __name__ == "__main__":
    main()
