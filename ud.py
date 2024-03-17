#!/u01/app/oracle/middleware/wls12c_devops/oracle_common/common/bin/wlst.sh
def wlDeployUndeploy(username, password, adminURL, appName, location, targets):
    try:
        #connect to admin server
        connect(username, password, adminURL)
        #start edit operation
        edit()
        startEdit()

        #stop application
        stopApplication(appName)

        #start undeploying application to "AdminServer" server
        progress = undeploy(appName, timeout=60000)
        progress.printStatus()
        save()
        activate(20000,block="true")
        #start deploying application to ""AdminServer" server
        progress = deploy(appName,location,targets)
        progress.printStatus()
        #print 'Done deploying application' +appname

    except Exception, e:
         print ex.toString()

user=sys.argv[1]
password=sys.argv[2]
url=sys.argv[3]
app=sys.argv[4]
locate=sys.argv[5]
target=sys.argv[6]
wlDeployUndeploy(user,password,url,app,locate,target)
