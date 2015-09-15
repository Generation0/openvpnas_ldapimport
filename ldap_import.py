#/usr/bin/python3

import os
import json 
from getpass import getpass
from ldap3 import Server, Connection, SIMPLE, SYNC, ASYNC, SUBTREE, ALL

uri = input("LDAP Connection: ") 							
user = input("Username: ")	 	 							
password = getpass(prompt="Password: ", stream=None)		
ldap_group_path="OU=Users,OU=Company,DC=company ,DC=local"

group = input("Enter Group [All Users]:  ")
import_group = "OU="+group+","
ldap_path = import_group + " " + ldap_group_path

# define the Server and the Connection objects
s = Server(uri, get_info = ALL)  # define an unsecure LDAP server, requesting info on the server and the schema
c = Connection(s, auto_bind = True, user=user, password=password, check_names=True)

# search for User/Person objects (for help look for ldap-queries)
c.search(ldap_path,'(&(objectclass=user)(objectcategory=person))', SUBTREE, attributes = ['sAMAccountName'])
response = c.response_to_json()
result = c.result
parsed_json = json.loads(response)
print("importing", end=" ")
for entry in parsed_json['entries']:
	ma_name = entry['attributes']['sAMAccountName']
	print(".", end=" ")
	os.system("./sacli --user %s --key conn_group --value '%s' UserPropPut" %(ma_name, group))
print("\nimport finished")


