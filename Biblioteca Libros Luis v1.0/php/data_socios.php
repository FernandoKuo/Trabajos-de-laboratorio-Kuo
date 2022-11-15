<?php

    $nombre = $_POST['nombre'];
    $dni = $_POST['dni'];
    $direccion = $_POST['direccion'];
    $telefono = $_POST['telefono'];
    $mail = $_POST['mail'];
    
    //conexion a mysql 
    $servidor = "localhost";
    $usuario = "root";
    $password = "";
    $baseDeDatos = "biblioteca";
    $conexion = mysqli_connect($servidor, $usuario, $password, $baseDeDatos);

    $sql = "insert into socio(nombre, telefono, direccion, dni, mail) values('$nombre', '$telefono', '$direccion', $dni, '$mail');";
    
    mysqli_query($conexion, $sql);
    mysqli_close($conexion);
    header("location:../socios.html");
    
?>
