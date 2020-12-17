<?php
	if($_POST['act'] == 'MySQL检测'){
	  if(function_exists("mysql_close")==1){
	    $link=@mysql_connect($host.":".$port,$login,$password);
		if($link){
		  echo "<script> alert('连接到mysql数据库正常')</script>";
		}else{
		  echo "<script>alert('无法连接到mysql数据库')</script>";
		}
	  }else{
	    echo "<script>alert('服务器不支持mysql数据库！')</script>";
	  }
	}
?>