# Overview
Import Groups from LDAP into your OpenVPN Access Server

# Quicksetup

**At first you need to change the Path to your Group in ldap_import.py and check the Path to the Openvpn Access Server Script Folder**

Then copy the script into the script folder of openvpnas and launch the script in a virtual environment
```
virtualenv -p python3 py3env
cd py3env
source bin/activate
cd ..
pip install ldap3
python ldap_import
```

