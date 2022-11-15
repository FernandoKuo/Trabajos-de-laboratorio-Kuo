<?php

    $isbn = $_POST['isbn'];
    $titulo = $_POST['titulo'];
    $autor = $_POST['autor'];
    $genero = $_POST['genero'];
    $e_cant = $_POST['e_cant'];
    
    //conexion a mysql 
    $servidor = "localhost";
    $usuario = "root";
    $password = "";
    $baseDeDatos = "biblioteca";
    $conexion = mysqli_connect($servidor, $usuario, $password, $baseDeDatos);

    $sql = "insert into libro(isbn, titulo, autor, genero, e_cant) values('$isbn', '$titulo', '$autor', '$genero', $e_cant);";
    mysqli_query($conexion, $sql);

    for ($i = 1; $i <= $e_cant; $i++) {
        $sql = "insert into ejemplar(cant, l_isbn) values($i, '$isbn');";
        mysqli_query($conexion, $sql);
    }

    mysqli_close($conexion);
    header("location:../libros.html");
    
    
?>
