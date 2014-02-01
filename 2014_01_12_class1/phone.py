phone = "7038616379"
print "My number is {0}".format(phone)
print "Local: {0}-{1}".format(phone[3:6],phone[6:])
print "Domestic: ({0}){1}-{2}".format(phone[0:3],phone[3:6],phone[6:])
print "International: +1-{0}-{1}-{2}".format(phone[0:3],phone[3:6],phone[6:])