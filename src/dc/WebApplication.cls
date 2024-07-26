Class dc.WebApplication Extends %CSP.REST [ System = 3 ]
{

Parameter CHARSET = "utf-8";

Parameter CONVERTINPUTSTREAM = 1;

Parameter CONTENTTYPE = "application/json";

Parameter Version = "1.0.0";

Parameter HandleCorsRequest = 1;

Parameter PAGESIZE As INTEGER = 20;

ClassMethod DivideBy0Objectscript() [ Language = objectscript ]
{
    // FIND ERROR
    //import iris
    //try:
    //    print(1/0)
    //except Exception as e:
    //    iris.routine('BACK^%ETN')
    Try {
        Do ##class(dc.WebApplication).DivideBy0Python()
        //w (1/0)
    }
    Catch ex {
        Do ex.Log()
    }
    return $$$OK
}

ClassMethod badDOB() [ Language = objectscript ]
{
    Try {
      SET badDOB=##class(%Exception.General).%New("<BAD DOB>","999",,"Birth date is in the future")
      THROW badDOB
    }
    Catch ex {
        Do ex.Log()
    }
    return $$$OK
}

/// Description
ClassMethod DivideBy0Python() [ Language = python ]
{
    print(1/0)
}

XData UrlMap [ XMLNamespace = "http://www.intersystems.com/urlmap" ]
{
<Routes>
    <Route Url="/DivideBy0Objectscript" Method="GET" Call="DivideBy0Objectscript"/>
    <Route Url="/badDOB" Method="GET" Call="badDOB"/>
</Routes>
}

}
