echo off
title VPN Connectivity Test

rem Runs the VPN Connectivity Test and will attempt to find TTL in the result, if it has found TTL then the VPN Connectivity Test has been successfull.

:RunVPNConnectivityTest
rem If cls is not used below before the VPN Connectivity Test starts then for example where the VPN Connectivity Test starts U:\Shaqil\Scripts>echo off will be displayed.
cls
echo Welcome to the VPN Connectivity Test
echo.
set /p IPAddress="Enter the IP address to test with, and then press enter: "
echo.
echo The VPN Connectivity Test is running, please wait . . .
echo.
ping %IPAddress% | find "TTL=" >nul
rem echo %errorlevel%
if errorlevel 1 goto VPNConnectivityTestFailed
echo The VPN Connectivity Test has been Successfull.
echo.
pause
exit

rem If the VPN Connectivity Test has failed, then the following message below will be displayed below. Afterwards the user will be asked if they want to run the VPN Connectivity Test again, if the user enters anything other than y or n then a message will be displayed with what they have entered, and will be asked again.

:VPNConnectivityTestFailed
echo The VPN Connectivity Test has failed, no response from the server. Please Check your VPN connection and try again.
echo.
rem echo %errorlevel%

:RunVPNConnectivityTestagain
set /p RunVPNConnectivityTestagain="Would you like to run the VPN Connectivity Test again? Press Y for Yes or N for No and then press enter "
echo.
if %RunVPNConnectivityTestagain% NEQ y (
if %RunVPNConnectivityTestagain% NEQ n (
echo You have entered %RunVPNConnectivityTestagain%
echo.
goto RunVPNConnectivityTestagain
)
)
if %RunVPNConnectivityTestagain%==y goto RunVPNConnectivityTest
if %RunVPNConnectivityTestagain%==n goto Exit

:Exit
pause
