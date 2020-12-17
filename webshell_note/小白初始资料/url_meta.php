<html>
<head>
<title></title>

<?php
header("content-type:text/html;charset=utf-8");
if(isset($_REQUEST['url']))
{
	$url=$_REQUEST['url'];
}else{
	$url="url_meta.php";
}

?>
<meta http-equiv="Refresh" content="5; url=<?php echo $url?>" />
</head>
<body>
</body>
</html>
