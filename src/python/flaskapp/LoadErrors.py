import iris

def load_namespaces_with_errors(): 
    namespaces_with_errors = []

    rset = iris.cls("%ResultSet")._New()
    rset.ClassName="SYS.ApplicationError"
    rset.QueryName="NamespaceList"
    rset.Execute()
    
    while rset._Next():
        print(rset.Get("Namespace"))
        namespaces_with_errors.append(rset.Get("Namespace"))

    return namespaces_with_errors

def load_dates():
    dates_with_erros = []

    namespaces_with_errors = load_namespaces_with_errors()
    for namespace in namespaces_with_errors:

        rset = iris.cls("%ResultSet")._New()
        rset.ClassName="SYS.ApplicationError"
        rset.QueryName="DateList"
        rset.Execute(namespace)

        namespace_errors = {"namespace": namespace, "dates": []}
        while rset._Next():
            namespace_errors["dates"].append(rset.Get("Date"))

        dates_with_erros.append(namespace_errors)

    return dates_with_erros

def load_erros():
    error_list = []

    dates_with_erros = load_dates()
    for namespace_errors in dates_with_erros:
        for date in namespace_errors["dates"]:
            rset = iris.cls("%ResultSet")._New()
            rset.ClassName="SYS.ApplicationError"
            rset.QueryName="ErrorList"
            rset.Execute(namespace_errors["namespace"],date)
            while rset._Next():
                error_dict = {
                    "date": date,
                    "namespace": namespace_errors["namespace"],
                    "error": rset.Get("Error #"),
                    "time": rset.Get("Time"),
                    "process": rset.Get("Process"),
                    "error_ID": f"{namespace_errors['namespace']}:{date}:{rset.Get('Error #')}:{rset.Get('Time')}:{rset.Get('Process')}",
                    "error_message": rset.Get("Error message"),
                    "displayPID": rset.Get("DisplayPID"),
                    "username": rset.Get("Username"),
                    "code_line": rset.Get("Code line"),
                }
                error_list.append(error_dict)

    return error_list

def load_error_detail(error):

    current_namespace = iris.cls("%SYSTEM.SYS").NameSpace()

    iris.cls("dc.Utils").SetNameSpace("%SYS")
    rset = iris.cls("%ResultSet")._New()
    rset.ClassName="SYS.ApplicationError"
    rset.QueryName="ErrorDetail"
    rset.Execute(error["namespace"],error["date"], error["error"], 1)

    iris.cls("dc.Utils").SetNameSpace(current_namespace)

    if rset._Next():
        return {
            "Column1" : (rset.Get("Column1")),
            "Column2" : (rset.Get("Column2")),
            "Column3" : (rset.Get("Column3")),
            "Column4" : (rset.Get("Column4"))
        }
    return {
            "Column1" : "",
            "Column2" : "",
            "Column3" : "",
            "Column4" : ""
        }
def charge():
    current_namespace = iris.cls("%SYSTEM.SYS").NameSpace()
    iris.cls("dc.Utils").SetNameSpace("%SYS")
    errors = load_erros()
    iris.cls("dc.Utils").SetNameSpace(current_namespace)
    for error in errors:
        error_detail = load_error_detail(error)

        ErrorAnalysis = iris.cls("dc.ErrorAnalysis")._New()
        ErrorAnalysis.namespace = error["namespace"]
        ErrorAnalysis.error = error["error"]
        ErrorAnalysis.timeHour = error["time"]
        ErrorAnalysis.process = error["process"]
        ErrorAnalysis.errorID = error["error_ID"]
        ErrorAnalysis.errorMessage = error["error_message"]
        ErrorAnalysis.displayPID = error["displayPID"]
        ErrorAnalysis.username = error["username"]
        ErrorAnalysis.codeLine = error["code_line"]
        ErrorAnalysis.byDate = error["date"]
        ErrorAnalysis.errorDetailColumn1 = error_detail["Column1"]
        ErrorAnalysis.errorDetailColumn2 = error_detail["Column2"]
        ErrorAnalysis.errorDetailColumn3 = error_detail["Column3"]
        ErrorAnalysis.errorDetailColumn4 = error_detail["Column4"]
        ErrorAnalysis._Save()

    iris.cls("dc.Utils").SetNameSpace(current_namespace)

