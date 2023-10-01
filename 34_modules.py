# time code 3:06:15
# module

import assets.modulesMessages as messages
messages.hello()
messages.bye()


# other way to call functions
from assets.modulesMessages import hello, bye
hello()
bye()

help('modules') # get all modules built in