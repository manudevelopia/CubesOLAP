import MySQLdb
import requests

from requests.auth import HTTPBasicAuth
from attrdict import AttrDict
from datetime import date

from credentials import Credentials

# MySQL database credentials
host = Credentials.host
user = Credentials.user
passwd = Credentials.passwd
db = Credentials.db
table = Credentials.table_jira

# Jira instance data and credentials
jira_url = Credentials.url_jira
jira_user = Credentials.user_jira
jira_passwd = Credentials.passwd_jira
jira_metrics = [
    'Issuekey',
    'Project',
    'Summary',
    'Type',
    'Status',
    'Priority',
    'Resolution',
    'Assignee',
    'Reporter',
    'Creator',
    'Created',
    'Last_Viewed',
    'Updated',
    'Resolved',
    'Affects_Versions',
    'Fix_Versions',
    'Components',
    'Due_Date',
    'Votes',
    'Watchers',
    'Images',
    'Original_Estimate',
    'Remaining_Estimate',
    'Time_Spent',
    'Work_Ratio',
    'SubTasks',
    'Linked_Issues',
    'Environment',
    'Description',
    'Security_Level',
    'Progress',
    'SUM_Progress',
    'SUM_Time_Spent',
    'SUM_Remaining_Estimate',
    'SUM_Original_Estimate',
    'Labels',
    'Business_Value',
    'Epic_Colour',
    'Epic_Link',
    'Epic_Name',
    'Epic_Status',
    'EpicTheme',
    'Flagged',
    'Raised_During',
    'Rank',
    'Sprint',
    'Story',
    'Story_Points',
    'Team',
    'Test_Sessions',
    'Testing_Status',
    'CHART_Date_of_First_Response'
]


# Functions #

# Set a sigle valule
def set_value(element, collection):
    if collection is None:
        return None
    elif element in collection:
        return collection[element]
    else:
        return None


# Set several values followed by coma
def set_array(element, obj, coll):
    if coll is None:
        return None
    else:
        val = ""
        for compo in coll[obj]:
            val += compo[element]
    return val.replace('.', ',')


# set values from a list comma separated
def set_values_list(list):
    return ','.join(list)


# format dates removing unneeded info
def format_dates(date):
    if date is not None:
        return date[0:10]
    else:
        return ''

# Establish a MySQL connection
database = MySQLdb.connect(host, user, passwd, db)

# Get the cursor, which is used to traverse the database, line by line
cursor = database.cursor()

# Mysql - Create the INSERT INTO sql query - 52 Columns
format_strings = ','.join(['%s'] * (len(jira_metrics)))
query = """INSERT INTO """ + table + """ (
    `Issuekey`,
    `Project`,
    `Summary`,
    `Type`,
    `Status`,
    `Priority`,
    `Resolution`,
    `Assignee`,
    `Reporter`,
    `Creator`,
    `Created`,
    `Last_Viewed`,
    `Updated`,
    `Resolved`,
    `Affects_Versions`,
    `Fix_Versions`,
    `Components`,
    `Due_Date`,
    `Votes`,
    `Watchers`,
    `Images`,
    `Original_Estimate`,
    `Remaining_Estimate`,
    `Time_Spent`,
    `Work_Ratio`,
    `SubTasks`,
    `Linked_Issues`,
    `Environment`,
    `Description`,
    `Security_Level`,
    `Progress`,
    `SUM_Progress`,
    `SUM_Time_Spent`,
    `SUM_Remaining_Estimate`,
    `SUM_Original_Estimate`,
    `Labels`,
    `Business_Value`,
    `Epic_Colour`,
    `Epic_Link`,
    `Epic_Name`,
    `Epic_Status`,
    `EpicTheme`,
    `Flagged`,
    `Raised_During`,
    `Rank`,
    `Sprint`,
    `Story`,
    `Story_Points`,
    `Team`,
    `Test_Sessions`,
    `Testing_Status`,
    `CHART_Date_of_First_Response`
) VALUES (""" + format_strings + """)"""


# Request to Jira API
r = requests.get(jira_url, auth=HTTPBasicAuth(jira_user, jira_passwd))

# Check if the statuscode is 200 = ok! and truncates the table
if(r.status_code == 200):
    cursor.execute("TRUNCATE TABLE " + table)
    print "TRUNCATE TABLE " + table

r.headers['content-type']
r.encoding

# Convert the response to JSON
json_issue = r.json()

# Improves the JSON objects values accesibility
issue = AttrDict(json_issue)

# Print as a trace
for element in issue.issues:
    # Issue basic information
    Issuekey = element.key
    Project = element.fields.project.name
    Summary = element.fields.summary
    Type = element.fields.issuetype.name
    Status = element.fields.status.name
    Priority = element.fields.priority.name
    Resolution = set_value('name', element.fields.resolution)

    # team, users information
    Assignee = set_value('displayName', element.fields.assignee)
    Reporter = element.fields.reporter.displayName
    Creator = element.fields.creator.displayName

    # Dates information
    Created = format_dates(element.fields.created)
    Last_Viewed = format_dates(element.fields.lastViewed)
    Updated = format_dates(element.fields.updated)
    Resolved = format_dates(element.fields.resolutiondate)
    Due_Date = format_dates(element.fields.duedate)

    Affects_Versions = set_array('name', 'versions', element.fields)
    Fix_Versions = set_array('name', 'fixVersions', element.fields)
    Components = set_array('name', 'components', element.fields)

    Votes = element.fields.votes.votes
    Watchers = element.fields.watches.watchCount
    Images = ""

    # Workload
    Original_Estimate = element.fields.timeoriginalestimate
    Remaining_Estimate = element.fields.timeestimate
    Time_Spent = element.fields.timespent

    Work_Ratio = element.fields.workratio
    SubTasks = ""  # element.fields.subtasks # [] that needs to be parsed
    Linked_Issues = ""  # element.fields.issuelinks # []
    Environment = element.fields.environment
    Description = ''  # element.fields.description) Errors char u'\u2013'
    Security_Level = ""
    Progress = ""
    SUM_Progress = ""
    SUM_Time_Spent = element.fields.timespent
    SUM_Remaining_Estimate = element.fields.aggregatetimespent
    SUM_Original_Estimate = element.fields.aggregatetimeoriginalestimate
    Labels = set_values_list(element.fields.labels)
    Business_Value = set_value('customfield_10005', element.fields)
    Epic_Colour = ""
    Epic_Link = element.fields.customfield_10008
    Epic_Name = ""
    Epic_Status = ""
    EpicTheme = ""
    Flagged = ""
    Raised_During = ""
    Rank = element.fields.customfield_10300
    Sprint = ""  # element.fields.customfield_10007 # []
    Story = element.fields.customfield_10200
    Story_Points = set_value('customfield_10004', element.fields)
    Team = ""
    Test_Sessions = ""
    Testing_Status = element.fields.customfield_10021
    CHART_Date_of_First_Response = element.fields.customfield_10001

    values = (
        Issuekey,
        Project,
        Summary,
        Type,
        Status,
        Priority,
        Resolution,
        Assignee,
        Reporter,
        Creator,
        Created,
        Last_Viewed,
        Updated,
        Resolved,
        Affects_Versions,
        Fix_Versions,
        Components,
        Due_Date,
        Votes,
        Watchers,
        Images,
        Original_Estimate,
        Remaining_Estimate,
        Time_Spent,
        Work_Ratio,
        SubTasks,
        Linked_Issues,
        Environment,
        Description,
        Security_Level,
        Progress,
        SUM_Progress,
        SUM_Time_Spent,
        SUM_Remaining_Estimate,
        SUM_Original_Estimate,
        Labels,
        Business_Value,
        Epic_Colour,
        Epic_Link,
        Epic_Name,
        Epic_Status,
        EpicTheme,
        Flagged,
        Raised_During,
        Rank,
        Sprint,
        Story,
        Story_Points,
        Team,
        Test_Sessions,
        Testing_Status,
        CHART_Date_of_First_Response
    )
    # Execute the Query
    cursor.execute(query, values)


# Closing MySQL stuff

# Close the cursor
cursor.close()

# Commit the transaction
database.commit()

# Close the database connection
database.close()

print "Operation finished updated " + str(issue.total) + " issues from JIRA. " + str(date.today())
