<?php

    $fecha_retorno = $_POST['fecha_retorno'];
    $l_isbn = $_POST['l_isbn'];

    //conexion a mysql 
    $servidor = "localhost";
    $usuario = "root";
    $password = "";
    $baseDeDatos = "biblioteca";
    $conexion = mysqli_connect($servidor, $usuario, $password, $baseDeDatos);

    $sql = "insert into retorno(fecha_retorno, l_isbn) values('$fecha_retorno', '$l_isbn');";
    
    mysqli_query($conexion, $sql);
    mysqli_close($conexion);
    header("location:../retorno.html");
    
?>
