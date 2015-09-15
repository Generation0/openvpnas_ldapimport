# Overview
Import Groups from LDAP into your OpenVPN Access Server

# Quicksetup

**At first you need to change the Path to your Group in ldap_import.py**

Then copy the script into the script folder of openvpnas and launch the script in a virtual environment
```
cp ldap_import.py /usr/local/openvpn_as/scripts
cd py3env
source bin/activate
cd /usr/local/openvpn_as/scripts
python ldap_import
```

