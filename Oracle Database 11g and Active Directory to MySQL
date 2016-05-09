#To connect to the database and retrieve the Addresses.
    $StrConnection="Driver={Oracle in OraClient11g_home1};Dbq=;Uid=;Pwd=;"
    $StrSQLStatement="SELECT ADDRESS.ADDRESS_NAME, ADDRESS.ADDRESS_LINE1, ADDRESS.ADDRESS_LINE2, ADDRESS.ADDRESS_LINE3, ADDRESS.ADDRESS_LINE4, ADDRESS.ADDRESS_LINE5, COUNTRY.COUNTRY, ADDRESS.POST_CODE, ADDRESS.FAX_NO FROM ADDRESS LEFT OUTER JOIN COUNTRY on ADDRESS.ADDRESS_LINE6 = COUNTRY.COUNTRY_ID WHERE ADDRESS.ADDRESS_LINE1 <> 'null' AND ADDRESS.DOWNLOAD = 1;"
    $objODBCCommand = New-Object System.Data.Odbc.OdbcCommand
    $objODBCCommand.CommandText = $StrSQLStatement
    $objODBCCommand.Connection = $StrConnection
    $objODBCDataAdapter = New-Object System.Data.Odbc.OdbcDataAdapter
    $objODBCDataAdapter.SelectCommand = $objODBCCommand
    $objAddressesDataset = New-Object System.Data.DataSet
    $objODBCDataAdapter.Fill($objAddressesDataSet)

#The measure command below is to used to measure the time it takes to insert the addresses into the Addesses table on MySQL.
#measure-command{}


#Addresses table.
#To load the MySql.Data.MySqlClient Namespace, to use the MySQL Connector
    [void][system.reflection.Assembly]::LoadWithPartialName("MySql.Data")
#To open the Connection to the database on MySql.
    $strMySqlConnectionString ="server=;database=;Persist Security Info=false;user id=;pwd=;"
    $objMySqlConnection = New-Object MySql.Data.MySqlClient.MySqlConnection($strMySQLConnectionString)
    $objMySqlConnection.Open()

    $objMySqlCommand = New-Object MySql.Data.MySqlClient.MySqlCommand
    $objMySqlCommand.Connection = $objMySqlConnection
#To truncate the Addresses table.
    $objMySqlCommand.CommandText = "TRUNCATE TABLE Addresses;"
    $objMySqlCommand.ExecuteNonQuery()
    $objMySqlCommand.CommandText = "INSERT INTO Addresses(AddressName,AddressLine1,AddressLine2,AddressLine3,AddressLine4,AddressLine5,Country,Postcode,FaxNo)VALUES(@$objAddressesDataSet.ADDRESS_NAME,@$objAddressesDataSet.ADDRESS_LINE1,@$objAddressesDataSet.ADDRESS_LINE2,@$objAddressesDataSet.ADDRESS_LINE3,@$objAddressesDataSet.ADDRESS_LINE4,@$objAddressesDataSet.ADDRESS_LINE5,@$objAddressesDataSet.COUNTRY,@$objAddressesDataSet.POST_CODE,@$objAddressesDataSet.FAX_NO);" 
    $objMySqlCommand.prepare()
#To add the  addresses MySQLCommand Parameters with a blank value.
    $objMySqlCommand.parameters.addwithvalue("@$objAddressesDataSet.ADDRESS_NAME",[string]::Empty)
    $objMySqlCommand.parameters.addwithvalue("@$objAddressesDataSet.ADDRESS_LINE1",[string]::Empty)
    $objMySqlCommand.parameters.addwithvalue("@$objAddressesDataSet.ADDRESS_LINE2",[string]::Empty)
    $objMySqlCommand.parameters.addwithvalue("@$objAddressesDataSet.ADDRESS_LINE3",[string]::Empty)
    $objMySqlCommand.parameters.addwithvalue("@$objAddressesDataSet.ADDRESS_LINE4",[string]::Empty)
    $objMySqlCommand.parameters.addwithvalue("@$objAddressesDataSet.ADDRESS_LINE5",[string]::Empty)
    $objMySqlCommand.parameters.addwithvalue("@$objAddressesDataSet.COUNTRY",[string]::Empty)
    $objMySqlCommand.parameters.addwithvalue("@$objAddressesDataSet.POST_CODE",[string]::Empty)
    $objMySqlCommand.parameters.addwithvalue("@$objAddressesDataSet.FAX_NO",[string]::Empty)
#To add the  addresses MySQLCommand values from the addresses Dataset, for each field, for each record.
    foreach ($objAddress in $objAddressesDataSet.tables.rows) 
    { 
    $objMySqlCommand.Parameters["@$objAddressesDataSet.ADDRESS_NAME"].Value = $objAddress.ADDRESS_NAME
    $objMySqlCommand.Parameters["@$objAddressesDataSet.ADDRESS_LINE1"].Value = $objAddress.ADDRESS_LINE1
    $objMySqlCommand.Parameters["@$objAddressesDataSet.ADDRESS_LINE2"].Value = $objAddress.ADDRESS_LINE2
    $objMySqlCommand.Parameters["@$objAddressesDataSet.ADDRESS_LINE3"].Value = $objAddress.ADDRESS_LINE3
    $objMySqlCommand.Parameters["@$objAddressesDataSet.ADDRESS_LINE4"].Value = $objAddress.ADDRESS_LINE4
    $objMySqlCommand.Parameters["@$objAddressesDataSet.ADDRESS_LINE5"].Value = $objAddress.ADDRESS_LINE5
    $objMySqlCommand.Parameters["@$objAddressesDataSet.COUNTRY"].Value = $objAddress.COUNTRY
    $objMySqlCommand.Parameters["@$objAddressesDataSet.POST_CODE"].Value = $objAddress.POST_CODE
    $objMySqlCommand.Parameters["@$objAddressesDataSet.FAX_NO"].Value = $objAddress.FAX_NO
    $objMySqlCommand.ExecuteNonQuery()
#To show each field of the  address, when it is being inserted from $objAddressesDataSet into the Addresses table on MySQL, and the length of characters in each field. It is to be used for debugging.
    if([string]::IsNullOrEmpty($objAddress.ADDRESS_NAME))
    {write-host There is no Address Name for this record.
    write-host}
    else
    {write-host $objAddress.ADDRESS_NAME
    write-host Which is $objAddress.ADDRESS_NAME.length characters long.
    write-host}
    if([string]::IsNullOrEmpty($objAddress.ADDRESS_LINE1))
    {write-host There is no Address Line 1 for this record.
    write-host}
    else
    {write-host $objAddress.ADDRESS_LINE1
    write-host Which is $objAddress.ADDRESS_LINE1.length characters long.
    write-host}
    if([string]::IsNullOrEmpty($objAddress.ADDRESS_LINE2))
    {write-host There is no Address Line 2 for this record.
    write-host}
    else
    {write-host $objAddress.ADDRESS_LINE2
    write-host Which is $objAddress.ADDRESS_LINE2.length characters long.
    write-host}
    if([string]::IsNullOrEmpty($objAddress.ADDRESS_LINE3))
    {write-host There is no Address Line 3 for this record.
    write-host}
    else
    {write-host $objAddress.ADDRESS_LINE3
    write-host Which is $objAddress.ADDRESS_LINE3.length characters long.
    write-host}
    if([string]::IsNullOrEmpty($objAddress.ADDRESS_LINE4))
    {write-host There is no Address Line 4 for this record.
    write-host}
    else
    {write-host $objAddress.ADDRESS_LINE4
    write-host Which is $objAddress.ADDRESS_LINE4.length characters long.
    write-host}
    if([string]::IsNullOrEmpty($objAddress.ADDRESS_LINE5))
    {write-host There is no Address Line 5 for this record.
    write-host}
    else
    {write-host $objAddress.ADDRESS_LINE5
    write-host Which is $objAddress.ADDRESS_LINE5.length characters long.
    write-host}
    if([string]::IsNullOrEmpty($objAddress.COUNTRY))
    {write-host There is no Country for this record.
    write-host}
    else
    {write-host $objAddress.COUNTRY
    write-host Which is $objAddress.COUNTRY.length characters long.
    write-host}
    if([string]::IsNullOrEmpty($objAddress.POST_CODE))
    {write-host There is no Postcode for this record.
    write-host}
    else
    {write-host $objAddress.POST_CODE
    write-host Which is $objAddress.POST_CODE.length characters long.
    write-host}
    if([string]::IsNullOrEmpty($objAddress.FAX_NO))
    {write-host There is no Fax No for this record.
    write-host}
    else
    {write-host $objAddress.FAX_NO
    write-host Which is $objAddress.FAX_NO.length characters long.
    write-host}
    }
    write-host There are $objAddressesDataSet.tables.rows.Count Records.
    write-host

    $objMySqlCommand.parameters.clear()
    #$objMySqlConnection.open()
#Staff table.
#To truncate the Staff table.
    $objMySqlCommand.CommandText = "TRUNCATE TABLE Staff;"
    $objMySqlCommand.ExecuteNonQuery()
#To retrieve the staff on Active Directory, which are First name and the LDAP property for this is givenName, Last name and the LDAP property for this is Surname, and Custom attribute 1 and the LDAP property for this is extensionattribute1
    $strStaff = Get-ADUser -Filter {((department -like "*") -or (department -eq "") -or (department -eq "")) -and (company -eq "")} -searchbase "OU=,DC=,DC=,DC=" -property givenName,Surname,extensionattribute1|select givenname,surname,extensionattribute1
    $objMySqlCommand.CommandText = "INSERT INTO Staff(FirstName,LastName,Initials)VALUES(@strEachStaff.givenName,@strEachStaff.Surname,@strEachStaff.extensionattribute1);" 
    $objMySqlCommand.prepare()
#To add the staff MySQLCommand parameters with a blank value.    
    $objMySqlCommand.parameters.addwithvalue("@strEachStaff.givenName",[string]::Empty)
    $objMySqlCommand.parameters.addwithvalue("@strEachStaff.Surname",[string]::Empty)
    $objMySqlCommand.parameters.addwithvalue("@strEachStaff.extensionattribute1",[string]::Empty)
#To add the  staff MySQLCommand values from $strStaff, for each field, for each record.    
    foreach($strEachStaff in $strStaff)
    { 
    $objMySqlCommand.Parameters["@strEachStaff.givenName"].Value = $strEachStaff.givenName
    $objMySqlCommand.Parameters["@strEachStaff.Surname"].Value = $strEachStaff.Surname
    $objMySqlCommand.Parameters["@strEachStaff.extensionattribute1"].Value = $strEachStaff.extensionattribute1
    $objMySqlCommand.ExecuteNonQuery()
#To show each staff when it is being inserted from the $strStaff into the Staff table on MySQL, and the length of characters in each field. It is to be used for debugging.    
    write-host $strEachStaff.givenName
    write-host
    write-host $strEachStaff.Surname
    write-host
    write-host $strEachStaff.extensionattribute1
    write-host
    }
    write-host There are $strStaff.count staff.
    write-host
    $objMySqlConnection.close()
