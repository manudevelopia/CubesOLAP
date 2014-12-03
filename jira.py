import MySQLdb
import requests
from requests.auth import HTTPBasicAuth
from attrdict import AttrDict
from datetime import date


# host =      "localhost"
# user =      "root"
# passwd =    "root"

host =      "mysql.server"
user =      "uqasar"
passwd =    "UqasarAdmin2012"

db =        "uqasar$cubes"
table =     "jira"

# Establish a MySQL connection
database = MySQLdb.connect(host, user, passwd, db)

# Get the cursor, which is used to traverse the database, line by line
cursor = database.cursor()

# Mysql - Create the INSERT INTO sql query - 52 Columns
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
) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

# Request to Jira API
r = requests.get('https://uqasar.atlassian.net/rest/api/2/search?jql=&maxResults=-1',
                 auth=HTTPBasicAuth('uqasaradmin', 'UqasarAdmin2012'))

# Check if the statuscode is 200 = ok! and truncates the table
if(r.status_code == 200) :
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
    Issuekey = element.key
    Project = element.fields.project.name
    Summary = element.fields.summary
    Type = element.fields.issuetype.name
    Status = element.fields.status.statusCategory.name
    Priority = element.fields.priority.name

    if(element.fields.resolution is None ):
        Resolution = ""
    else:
        Resolution = element.fields.resolution.name

    if(element.fields.assignee.displayName is None):
        Assignee = ""
    else :
        Assignee = element.fields.assignee.displayName

    Reporter = element.fields.reporter.displayName
    Creator = element.fields.creator.displayName
    Created = element.fields.created
    Last_Viewed = element.fields.lastViewed
    Updated = element.fields.updated
    Resolved = element.fields.resolutiondate
    Affects_Versions = "" #element.fields.versions # [] that needs to be parsed
    Fix_Versions =  "" #element.fields.fixVersions # [] that needs to be parsed
    Components = "" #element.fields.components # [] that needs to be parsed
    Due_Date = element.fields.duedate
    Votes = element.fields.votes.votes
    Watchers = element.fields.watches.watchCount
    Images = ""
    Original_Estimate = element.fields.timeoriginalestimate
    Remaining_Estimate = element.fields.aggregatetimeestimate
    Time_Spent = element.fields.timespent
    Work_Ratio = element.fields.workratio
    SubTasks = "" # element.fields.subtasks # [] that needs to be parsed
    Linked_Issues = "" # element.fields.issuelinks # [] that needs to be parsed
    Environment = element.fields.environment
    Description = "" ## element.fields.description # Fails because the Latin1-utf-8 issue
    Security_Level = ""
    Progress = ""
    SUM_Progress = ""
    SUM_Time_Spent = element.fields.timespent
    SUM_Remaining_Estimate = element.fields.aggregatetimespent
    SUM_Original_Estimate = element.fields.aggregatetimeoriginalestimate
    Labels = "" # element.fields.labels # [] that needs to be parsed
    Business_Value = ""
    Epic_Colour = ""
    Epic_Link = element.fields.customfield_10008
    Epic_Name = ""
    Epic_Status = ""
    EpicTheme = ""
    Flagged = ""
    Raised_During = ""
    Rank = element.fields.customfield_10300
    Sprint = "" # element.fields.customfield_10007 # [] that needs to be parsed
    Story = element.fields.customfield_10200
    Story_Points = ""
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

    cursor.execute(query, values)
    #print (values)


### Closing MySQL stuff

# Close the cursor
cursor.close()

# Commit the transaction
database.commit()

# Close the database connection
database.close()

print "Operation finished updated " + str(issue.total) + " issues from JIRA. " + str(date.today())
