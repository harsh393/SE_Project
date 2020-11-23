<?php
 
 session_start();

$con=mysqli_connect('localhost','root','');

mysqli_select_db($con,'regdb');
$name=$_POST['user'];
$pass=$_POST['password'];
$email=$_POST['email'];

$s="select * from user where name='$name'";
$result=mysqli_query($con,$s);
$num=mysqli_num_rows($result);
if($num==1)
{
	echo "username already taken";
	header('location:login.php');
}
else
{
	$reg="insert into user(name,password,email) values('$name','$pass','$email')";
	mysqli_query($con,$reg);
	echo "Registration successful";
	header('location:http://127.0.0.1:5000/');
}
?>