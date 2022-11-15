<?php

    $fecha_prestamo = $_POST['fecha_prestamo'];
    $l_isbn = $_POST['l_isbn'];
    $n_ejemplar = $_POST['n_ejemplar'];
    $n_socio = $_POST['n_socio'];
    
    //conexion a mysql 
    $servidor = "localhost";
    $usuario = "root";
    $password = "";
    $baseDeDatos = "biblioteca";
    $conexion = mysqli_connect($servidor, $usuario, $password, $baseDeDatos);

    $sql = "insert into prestamo(fecha_prestamo, l_isbn, n_ejemplar, n_socio) values('$fecha_prestamo', '$l_isbn', $n_ejemplar, $n_socio);";
    
    mysqli_query($conexion, $sql);
    mysqli_close($conexion);
    header("location:../prestamo.html");
    
?>
