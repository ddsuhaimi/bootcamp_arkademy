<html>
<?php require_once 'connections.php'; ?>
<!DOCTYPE html>
<html>
<head>
    <!-- Latest compiled and minified CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css" integrity="sha384-HSMxcRTRxnN+Bdg0JdbxYKrThecOKuH5zCYotlSAcp1+c8xmyTe9GYg1l9a69psu" crossorigin="anonymous">

    <!-- Optional theme -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap-theme.min.css" integrity="sha384-6pzBo3FDv/PJ8r2KRkGHifhEocL+1X2rVCTTkUfGk7/0pbek5mMa1upzvWbrUbOZ" crossorigin="anonymous">

    <!-- Latest compiled and minified JavaScript -->
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js" integrity="sha384-aJ21OjlMXNL5UyIl/XNwTMqvzeRMZH2w8c5cRVpzpU8Y5bApTppSuUkhZXN0VxHd" crossorigin="anonymous"></script>

    <!-- Custom styles for this template -->
    <link href="starter-template.css" rel="stylesheet">

    <!-- Just for debugging purposes. Don't actually copy these 2 lines! -->
    <!--[if lt IE 9]><script src="../../assets/js/ie8-responsive-file-warning.js"></script><![endif]-->
    <script src="../../assets/js/ie-emulation-modes-warning.js"></script>
    <title>Dedi - Arkademi Bootcamp TEST</title>


</head>
<body><br>
   <h3 align="center"> View untuk Relasi Table</h3>
   <h3 align="center"></h3>
   <br>
   <div class="container">
      <div class="row"></div>
      <div class="col-lg-12">
       <a href="create.php"><button type="button">Add</button></a>
       <table class="table table-bordered" border="1" cellspacing="0" cellpadding="0">
        <thead>
            <tr>
                <th>Name</th>
                <th>Work</th>
                <th>Salary</th>
                <th>Salary_ID</th>
                <th>Action</th>
            </tr>
        </thead>
        <tbody>
           <?php
           $sql = "SELECT name.id, name.name, work.name AS workk, kategori.salary AS salary FROM name JOIN work ON name.id=work.id JOIN kategori ON name.id_salary=kategori.id";
           $result = $connect->query($sql);

           if($result->num_rows > 0) {
            while($row = $result->fetch_assoc()) {
                echo "<tr>
                <td>".$row['name']."</td>
                <td>".$row['workk']."</td>
                <td>".$row['salary']."</td>
                <td>
                <a href='edit.php?id=".$row['name.id']."'><button type='button'>Edit</button></a>
                <a href='delete.php?id=".$row['name.id']."'><button type='button'>Remove</button></a>
                </td>
                </tr>";
            }
        } else {
            echo "<tr><td colspan='5'><center>No Data Avaliable</center></td></tr>";
        }
        ?>
    </tbody>
</table>
</div>


</div>

</body>
</html>