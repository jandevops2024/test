#!/u01/app/oracle/middleware/wls12c_devops/oracle_common/common/bin/wlst.sh
import os, sys
readTemplate('/u01/app/oracle/middleware/wls12c_devops/wlserver/common/templates/wls/wls.jar')
cd('/Security/base_domain/User/weblogic')
cmo.setPassword('weblogic1')
cd('/Server/AdminServer')
setOption('ServerStartMode', 'prod')
cmo.setName('admin_devops')
cmo.setListenPort(7001)
cmo.setListenAddress('192.168.0.187')
writeDomain('/u01/app/oracle/middleware/wls12c_devops/user_projects/domains/devops_test')
closeTemplate()
print '>>>Domain created successfully>>>'
exit()
