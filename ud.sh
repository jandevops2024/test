#!/bin/bash
IFS=','
Location=/u01/app/oracle/apps
application=$deploy
echo $application
for i in $application
do
if  [ "$i" = "benefits" ]
then
/u01/app/oracle/devops/jenkins/scripts/test/ud.py weblogic welcome1 t3://192.168.0.187:7001 $i $Location/$i.war payroll_1 
elif [ "$i" = "messaging" ]
then
/u01/app/oracle/devops/jenkins/scripts/test/ud.py weblogic welcome1 t3://192.168.0.187:7001 $i $Location/$i.war payroll_1
elif [ "$i" = "contacts" ]
then
/u01/app/oracle/devops/jenkins/scripts/test/ud.py weblogic welcome1 t3://192.168.0.187:7001 $i $Location/$i.war payroll_1
elif [ "$i" = "timeoff" ]
then
/u01/app/oracle/devops/jenkins/scripts/test/ud.py weblogic welcome1 t3://192.168.0.187:7001 $i $Location/$i.war payroll_1
else
echo "Invalid !.. selection"
fi
done
