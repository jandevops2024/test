JAVA_HOME=/u01/app/oracle/middleware/java
export JAVA_HOME
PATH=$JAVA_HOME/bin:$PATH
export PATH
java -Xmx1024m -jar /u01/app/oracle/software/software/fmw_12.2.1.2.0_wls.jar -silent -responseFile /u01/app/oracle/software/software/response.rsp -invPtrLoc /u01/app/oracle/software/oraInst.loc

if [ $? -eq 0 ]
then
echo "Weblogic installation is successful"
else
echo "fix the errors to move successfully"
fi

