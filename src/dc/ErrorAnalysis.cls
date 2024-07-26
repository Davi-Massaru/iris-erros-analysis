Class dc.ErrorAnalysis Extends %Persistent
{

Property namespace As %String;

Property error As %String;

Property timeHour As %String;

Property process As %String;

Property errorID As %String;

Index ErrorKeyIDX On errorID [ Unique ];

Property errorMessage As %VarString;

Property displayPID As %String;

Property username As %String;

Property codeLine As %String;

Property byDate As %String;

Property errorDetailColumn1 As %Stream.GlobalCharacter;

Property errorDetailColumn2 As %Stream.GlobalCharacter;

Property errorDetailColumn3 As %Stream.GlobalCharacter;

Property errorDetailColumn4 As %Stream.GlobalCharacter;

Storage Default
{
<Data name="ErrorAnalysisDefaultData">
<Value name="1">
<Value>%%CLASSNAME</Value>
</Value>
<Value name="2">
<Value>namespace</Value>
</Value>
<Value name="3">
<Value>error</Value>
</Value>
<Value name="4">
<Value>timeHour</Value>
</Value>
<Value name="5">
<Value>process</Value>
</Value>
<Value name="6">
<Value>errorID</Value>
</Value>
<Value name="7">
<Value>errorMessage</Value>
</Value>
<Value name="8">
<Value>displayPID</Value>
</Value>
<Value name="9">
<Value>username</Value>
</Value>
<Value name="10">
<Value>codeLine</Value>
</Value>
<Value name="11">
<Value>byDate</Value>
</Value>
<Value name="12">
<Value>errorDetailColumn1</Value>
</Value>
<Value name="13">
<Value>errorDetailColumn2</Value>
</Value>
<Value name="14">
<Value>errorDetailColumn3</Value>
</Value>
<Value name="15">
<Value>errorDetailColumn4</Value>
</Value>
</Data>
<DataLocation>^dc.ErrorAnalysisD</DataLocation>
<DefaultData>ErrorAnalysisDefaultData</DefaultData>
<IdLocation>^dc.ErrorAnalysisD</IdLocation>
<IndexLocation>^dc.ErrorAnalysisI</IndexLocation>
<StreamLocation>^dc.ErrorAnalysisS</StreamLocation>
<Type>%Storage.Persistent</Type>
}

}
