import urllib.request as urllib2

key_path = 'key_march2018.txt'
y = open(key_path, 'r')
token = y.read()
# need to add the subfolder folder.  I'm thinking, if exists do this, else go to this subfolder
print(token)
git_url = "https://raw.githubusercontent.com/avvo/data-monitoring/master/metrics/acv.metric"
print (git_url)
request = urllib2.Request(git_url)

request.add_header('Authorization', 'token %s' % token)
# goes to git raw file and downloads it
response = urllib2.urlopen(request)
print(response.read())


#### This works to read a file from Git folder
