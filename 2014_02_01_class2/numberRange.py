days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
months_in_year = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

for month in months_in_year:
   print "\n" + month + "\n"
   
   for week in range(1,5):
      print "Week {0}".format(week)


      for day in days_of_week[2:4]:
         print day

   

 
