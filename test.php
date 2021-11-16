<?php

$mysqli = mysqli_connect("localhost", "root", "", "aman");
if ($mysqli){
    echo "" . mysqli_connect_error();
}

$user = "fadhly";
$pasword = "1' OR '1'='1 ";

$user = $mysqli->real_escape_string($user);
$pasword = $mysqli->real_escape_string($pasword);

$sql = "SELECT * FROM user WHERE user='$user' AND pasword='$pasword'";

    die($sql);
if ($result = $mysqli->query($sql)){
    print_r($result->fetch_object());
}