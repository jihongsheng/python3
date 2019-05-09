# -*- coding: UTF-8 -*-

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = "My first bicycle was a_input " + bicycles[0].title() + "."
print(message)
message = "My first bicycle was a_input %s." % (bicycles[0].title())
print(message)
