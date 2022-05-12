<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Data</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <style>
        body{ font: 14px sans-serif; text-align: center; }
        div.scroll {
            margin:4px, 4px;
            padding:4px;
            background-color: white;
            width: 950px;
            height: 500px;
            overflow-x: hidden;
            overflow-y: auto;
            text-align:justify;
        }
    </style>
</head>
<body>
<h1>Search</h1>
<p>
    <center>
<div class="scroll"><?php
    //// Initialize the session
    //session_start();
    //
    //// Check if the user is logged in, if not then redirect him to login page
    //if(!isset($_SESSION["loggedin"]) || $_SESSION["loggedin"] !== true){
    //    header("location: login.php");
    //    exit;
    //}
    echo "<br>", "<br>", "<br>";


    $row = 1;
    if (($handle = fopen("cern.csv", "r")) !== FALSE) {
        while (($data = fgetcsv($handle, 1000, ",")) !== FALSE) {
            $num = count($data);
            echo "<p> $num fields in line $row: <br /></p>\n";
            $row++;
            for ($c=0; $c < $num; $c++) {
                echo $data[$c] . "<br />\n";
            }
        }
        fclose($handle);
    }
    //?>
</div>
</center>
<br>
<br>
    <a href="data.php" class="btn btn-danger ml-3">Back</a>
</p>
</body>
</html>
