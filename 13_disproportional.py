#! /usr/bin/env python
# -*- coding: utf-8 -*-

# http://www.pythonchallenge.com/pc/return/disproportional.html

import xmlrpclib

Server=xmlrpclib.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
print Server.system.listMethods()
print Server.system.methodHelp('phone')
print Server.phone('Bert')

#http://www.pythonchallenge.com/pc/return/italy.html