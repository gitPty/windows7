net use * /d /y
net use  \\10.148.55.32 "Precious.life99*" /user:"administrator"



md \\10.148.55.32\d$\ADBackup\DPBG\DPBG-DC10\DC%DATE:~0,4%%DATE:~5,2%%DATE:~8,2% 


::%DATE:~0,4%%DATE:~5,2%%DATE:~8,2%
ECHO Y|wbadmin start systemstatebackup -backuptarget:\\10.148.55.32\d$\ADBackup\DPBG\DPBG-DC10\DC%DATE:~0,4%%DATE:~5,2%%DATE:~8,2%
net use * /d /y

