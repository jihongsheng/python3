# -*- coding: UTF-8 -*-

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)
message = "My first bicycle was a %s." % (bicycles[0].title())
print(message)
