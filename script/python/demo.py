from datetime import datetime, date, time

print 'hello python'
print 'hello world'
a = [1,2,3]
if a:
    print "something"
else:
    print "nothing"

b = []
if b:
    print "something"
else:
    print "nothing"

dt = datetime(2017, 02, 04, 16, 35, 00)
print dt.date()


for i in range(100):
    print i
