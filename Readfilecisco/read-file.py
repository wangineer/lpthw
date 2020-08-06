#This file reads line by line and applies attribute to it.


#To run
#python read-file.py

file = open('dev-01-info', 'r')

name = file.readline().strip()
ip_address = file.readline().strip()
os_type = file.readline().strip()
username = file.readline().strip()
password = file.readline().strip()

print('device name: ',name)
print ('ip address:  ',ip_address)
print ('os type:     ',os_type)
print ('username:    ',username)
print ('password:    ',password)


#This might work for python version 2.something
#print'device name: ',name
#print 'ip address:  ',ip_address
#print 'os type:     ',os_type
#print 'username:    ',username
#print 'password:    ',password



print ('--- Device into nicely formatted')
print ('Name   IP addr    OS    Username    Password')
print ('----   ----   -----   ----   -----')
print ('{0:8} {1:15} {2:8} [3:10} {4:10}'.format(name, ip_address, os_type, usernamer, password))