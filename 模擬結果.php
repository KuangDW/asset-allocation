<?php 
ini_set('max_execution_time', '0'); 

if(file_exists('error6.txt')){ 
  unlink('error6.txt');//將檔案刪除
}
if(file_exists('error7.txt')){ 
  unlink('error7.txt');//將檔案刪除
}
if(file_exists('error8.txt')){ 
  unlink('error8.txt');//將檔案刪除
}
if(file_exists('error9.txt')){ 
  unlink('error9.txt');//將檔案刪除
}
if(file_exists('error10.txt')){ 
  unlink('error10.txt');//將檔案刪除
}


?>
<!DOCTYPE html>
<html lang="en">

<head>

  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="">
  <meta name="author" content="">

  <title>DA DA 智能理財</title>

  <!-- Custom fonts for this theme -->
  <link href="vendor/fontawesome-free/css/all.min.css" rel="stylesheet" type="text/css">
  <link href="https://fonts.googleapis.com/css?family=Montserrat:400,700" rel="stylesheet" type="text/css">
  <link href="https://fonts.googleapis.com/css?family=Lato:400,700,400italic,700italic" rel="stylesheet" type="text/css">

  <!-- Theme CSS -->
  <link href="css/freelancer.min.css" rel="stylesheet">
          <!-- ================= Favicon ================== -->
        <!-- Standard -->
        <link rel="shortcut icon" href="http://placehold.it/64.png/000/fff">
        <!-- Retina iPad Touch Icon-->
        <link rel="apple-touch-icon" sizes="144x144" href="http://placehold.it/144.png/000/fff">
        <!-- Retina iPhone Touch Icon-->
        <link rel="apple-touch-icon" sizes="114x114" href="http://placehold.it/114.png/000/fff">
        <!-- Standard iPad Touch Icon-->
        <link rel="apple-touch-icon" sizes="72x72" href="http://placehold.it/72.png/000/fff">
        <!-- Standard iPhone Touch Icon-->
        <link rel="apple-touch-icon" sizes="57x57" href="http://placehold.it/57.png/000/fff">

        <!-- <link href="assets/css/lib/helper.css" rel="stylesheet"> -->
        <!-- <link href="assets/css/style.css" rel="stylesheet"> -->
    <!-- <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="description" content="">
    <meta name="generator" content="GitBook 3.2.2">
    <meta name="author" content="chartjs">
    <meta content="text/html; charset=utf-8" http-equiv="Content-Type">
    <link rel="stylesheet" href="https://www.chartjs.org/docs/latest/gitbook/style.css">             
    <link rel="stylesheet" href="https://www.chartjs.org/docs/latest/gitbook/gitbook-plugin-search-plus/search.css">        
    <link rel="stylesheet" href="https://www.chartjs.org/docs/latest/gitbook/gitbook-plugin-highlight/website.css">           
    <link rel="stylesheet" href="https://www.chartjs.org/docs/latest/gitbook/gitbook-plugin-fontsettings/website.css">        
    <link rel="stylesheet" href="https://www.chartjs.org/docs/latest/style.css"> -->
      
    <meta name="HandheldFriendly" content="true"/>
    <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black">
    <link rel="apple-touch-icon-precomposed" sizes="152x152" href="https://www.chartjs.org/docs/latest/gitbook/images/apple-touch-icon-precomposed-152.png">
    <link rel="shortcut icon" href="https://www.chartjs.org/docs/latest/gitbook/images/favicon.ico" type="image/x-icon">  
    <link rel="next" href="https://www.chartjs.org/docs/latest/charts/polar.html" />      
    <link rel="prev" href="https://www.chartjs.org/docs/latest/charts/radar.html" />
    <link rel="stylesheet" href="https://www.chartjs.org/docs/latest/gitbook/gitbook-plugin-chartjs/style.css">
    <script src="https://www.chartjs.org/docs/latest/gitbook/gitbook-plugin-chartjs/Chart.bundle.js"></script>
    <script src="https://www.chartjs.org/docs/latest/gitbook/gitbook-plugin-chartjs/chartjs-plugin-deferred.js"></script>
    

</head>

<body id="page-top">
<?php

$_SESSION["age"] = $_POST["age"];
$_SESSION["retireAge"] = $_POST["retireAge"];
$_SESSION["expectAge"] = $_POST["expectAge"];
$_SESSION["expenses"] = $_POST["expenses"];
$_SESSION["risk"] = $_POST["risk"];
$_SESSION["in_per_year"] = $_POST["in_per_year"];
$_SESSION["want_calc"] = $_POST["want_calc"];
$_SESSION["want_see"] = $_POST["want_see"];//ymdnum

$servername = "localhost";
$username = "root";
$password = "esfortest";
$dbname = "etf";
// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
// $sql = "SELECT id , port, distance  FROM test_table  WHERE id='1234'";
$a = $_POST["age"];
$b = $_POST["retireAge"];
$c = $_POST["expectAge"];
$d = $_POST["expenses"];
$f = $_POST["in_per_year"];
$e = $_POST["risk"];
$g = $_POST["want_calc"];
$h = $_POST["want_see"];
$sqlyourname = $_POST["yourname"];
$sqlpassword = $_POST["password"];

// $sql = "INSERT INTO user_data (`age`, `retireAge`, `expectAge`, `expenses`, `want_calc`, `want_see`,`name`,`id`) VALUES ($a,$b,$c,$d,$g,$h,$sqlyourname,$sqlpassword)";
$sql = "INSERT INTO user_datat (name,id,age,retireAge,expectAge,expenses,want_calc,want_see)VALUES ('$sqlyourname','$sqlpassword','$a','$b','$c','$d','$g','$h' )";
$resultyy = $conn->query($sql);
$sqlr = "INSERT INTO user_datatr (name,id,age,retireAge,expectAge,expenses,want_calc,want_see)VALUES ('$sqlyourname','$sqlpassword','$a','$b','$c','$d','$g','$h' )";
$resultyyr = $conn->query($sqlr);
$conn->close();
$y_in_money = $_POST["in_per_year"]*10000;
// $y_in_money = 60000;

//投入年份數
$years = $_SESSION["retireAge"] - $_SESSION["age"]+1;
$yyyy = $years-1;

//需要的退休金金額
 $need_pension = $_POST["expenses"] * ($_SESSION["expectAge"] - $_SESSION["retireAge"]) * 12 * 10000 * pow(1+1.72/100,$years-1);//需要準備的退休金
//$need_pension = $_POST["expenses"] * ($_SESSION["expectAge"] - $_SESSION["retireAge"]) * 12 * 10000 ;//需要準備的退休金
$need_pension = ceil($need_pension);

$first_input = $_SESSION["risk"];
$want_see_far = $_SESSION["want_calc"];

unset($out);
$var = 6;
$var1 = 12;
$mode = 3;
//選股 C:/Users/User/Anaconda3/python.exe
// exec("C:/Users/Alia/AppData/Local/Programs/Python/Python37/python.exe testsig1.py 2>error.txt {$yyyy} {$need_pension} {$y_in_money}",$out,$ret);
// exec("C:/Users/Alia/AppData/Local/Programs/Python/Python37/python.exe new_choose5.py 2>error.txt {$yyyy} {$need_pension} {$y_in_money} {$mode}",$out,$ret);
exec("C:/Python38-32/python.exe choose_try.py 2>error.txt {$yyyy} {$need_pension} {$y_in_money} {$mode} {$first_input} {$want_see_far} {$sqlyourname} {$sqlpassword}",$out,$ret);
// exec("C:/Users/User/Anaconda3/python.exe new_choose5.py 2>error.txt {$yyyy} {$need_pension} {$y_in_money}",$out,$ret);

// $_SESSION["ymd"] = $_POST["ymd"];


$servername = "localhost";
$username = "root";
$password = "esfortest";
$dbname = "etf";
$usertable = 'user_datat';
// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
mysqli_query($conn,"SET NAMES 'utf8'");
$sql = "SELECT * FROM $usertable where name = '".$sqlyourname ."'";
// $sql = "SELECT * FROM $usertable where name = '".$var[$i] ."'";
// $sql = "SELECT * FROM $usertable where (name = $yourname and id = $password )";
// $sql = "SELECT * FROM $usertable where (name = 'max')"
// echo $sql;
$result = mysqli_query($conn,$sql);
$row = mysqli_fetch_array($result);
$var=explode(" ",$row[4]);//選股結果
// $var = $row[4];
$n = count($var);//選出幾個
$weight = explode(" ",$row[5]);
$reward = $row[8];
$std_dev = $row[15];
$expect = $row[8];
$first_input = $row[9];
$y_in_money = $row[10];
$years = $row[17] - $row[16]+1;
$yyyy = $years-1;
$need_pension = $row[19]  * ($row[18] - $row[17]) * 12 * 10000 * pow(1+1.72/100,$years-1);//需要準備的退休金
//$need_pension = $_POST["expenses"] * ($_SESSION["expectAge"] - $_SESSION["retireAge"]) * 12 * 10000 ;//需要準備的退休金
$need_pension = ceil($need_pension);

?>
        
<?php
unset($out);
exec("C:/Python38-32/python.exe functions/再平衡_risk_年_try.py 2>error6.txt {$sqlyourname} {$sqlpassword}",$out,$ret);
// exec("C:/Users/Alia/AppData/Local/Programs/Python/Python37/python.exe 無再平衡_risk2.py 2>error.txt {$yyyy} {$need_pension} {$y_in_money} {$mode} {$first_input} {$want_see_far}",$out,$ret);
$date_arr = implode(",",explode(" ",$out[0]));
$total_money_y = implode(",",explode(" ",$out[1]));
for ( $i=0 ; $i<$n ; $i++ ){
    $ratio_y[$i] = implode(",",explode(" ",$out[$i+2]));
}
$sharpe_y = implode(",",explode(" ",$out[$n+2]));
$std_y = implode(",",explode(" ",$out[$n+3]));
$mdd_y = implode(",",explode(" ",$out[$n+4]));
$risk_y = explode(" ",$out[$n+5]);
$new_y = implode(",",explode(" ",$out[$n+6]));


unset($out);
exec("C:/Python38-32/python.exe functions/再平衡_risk_日_try.py 2>error8.txt {$sqlyourname} {$sqlpassword}",$out,$ret);
$total_money_d = implode(",",explode(" ",$out[1]));
for ( $i=0 ; $i<$n ; $i++ ){
    $ratio_d[$i] = implode(",",explode(" ",$out[$i+2]));
}
$sharpe_d = implode(",",explode(" ",$out[$n+2]));
$std_d = implode(",",explode(" ",$out[$n+3]));
$mdd_d = implode(",",explode(" ",$out[$n+4]));
$risk_d = explode(" ",$out[$n+5]);
$new_d = implode(",",explode(" ",$out[$n+6]));



unset($out);
exec("C:/Python38-32/python.exe functions/無再平衡_risk2_try.py 2>error9.txt {$sqlyourname} {$sqlpassword}",$out,$ret);
$total_money_n = implode(",",explode(" ",$out[1]));
for ( $i=0 ; $i<$n ; $i++ ){
    $ratio_n[$i] = implode(",",explode(" ",$out[$i+2]));
}
$sharpe_n = implode(",",explode(" ",$out[$n+2]));
$std_n = implode(",",explode(" ",$out[$n+3]));
$mdd_n = implode(",",explode(" ",$out[$n+4]));
$risk_n = explode(" ",$out[$n+5]);
$new_n = implode(",",explode(" ",$out[$n+6]));



unset($out);
exec("C:/Python38-32/python.exe functions/再平衡_risk_月_try.py 2>error7.txt {$sqlyourname} {$sqlpassword}",$out,$ret);
// $date_arr = implode(",",explode(" ",$out[0]));
$date_arr = implode(",",explode(" ",$out[0]));
$total_money_m = implode(",",explode(" ",$out[1]));
for ( $i=0 ; $i<$n ; $i++ ){
    $ratio_m[$i] = implode(",",explode(" ",$out[$i+2]));
}
$sharpe_m = implode(",",explode(" ",$out[$n+2]));
$std_m = implode(",",explode(" ",$out[$n+3]));
$mdd_m = implode(",",explode(" ",$out[$n+4]));
$risk_m = explode(" ",$out[$n+5]);
$new_m = implode(",",explode(" ",$out[$n+6]));








unset($out);
exec("C:/Python38-32/python.exe functions/db_flush.py 2>error10.txt {$sqlyourname} {$sqlpassword}",$out,$ret);
$flame_1 = $out[0];
$flame_2 = $out[1];
$flame_4 = $risk_m[0];
$flame_3 = $risk_m[count($risk_m)-1];



$servername = "localhost";
$username = "root";
$password = "esfortest";
$dbname = "etf";
$usertable="detail";

// $conn->close();

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
$ccc=1;
for ($i=0;$i<count($weight)-1;$i++){

  $weight[$i] = round($weight[$i],5);
  $ccc=$ccc-$weight[$i];
}
$weight[count($weight)-1]=$ccc;


// $count_percent_stock = 0;
// $stock = array(0=>0);
// $stock_name = array(0=>0);
// $count_stock = 0;
// $stock_percent = array(0=>0);
// for ( $i=0 ; $i<$n ; $i++ ){
//     // $sql = "select * from `性質表` where name = '"+$var[$i] +"'";
//     $sql = "SELECT * FROM $usertable where name = '".$var[$i] ."'";
//     // echo $sql;
//     $result = mysqli_query($conn,$sql);
//     $row = mysqli_fetch_array($result);
//     if($row[3]=='股票型'){
//         // $weight[$i] = round($weight[$i],5);
//         $wght = $weight[$i]*100;
//         $count_percent_stock += $wght;
//         $stock[$count_stock] = $row[0];
//         $stock_percent[$count_stock] = $wght;
//         $stock_name[$count_stock++] = $row[1];
//         //echo ("$row[0] \t\t $row[1] <div style='float:right;'> $wght %</div><br>");
//     }

// }


// $count_percent_bond = 0;
// $bond = array(0=>0);
// $bond_name = array(0=>0);
// $count_bond = 0;
// $bond_percent = array(0=>0);
// for ( $i=0 ; $i<$n ; $i++ ){
//     $sql = "SELECT * FROM $usertable where name = '".$var[$i] ."'";
//     // echo $sql;
//     $result = mysqli_query($conn,$sql);
//     $row = mysqli_fetch_array($result);
//     //if($row[3]=='債券型'){
//     if(preg_match("/債券/",$row[3] )){
//         // $weight[$i] = round($weight[$i],5);
//         $wght = $weight[$i]*100;
//         //echo ("$row[0] \t\t $row[1] <div style='float:right;'> $wght %</div><br>");
//         $count_percent_bond += $wght;
//         $bond[$count_bond] = $row[0];
//         $bond_percent[$count_bond] = $wght;
//         $bond_name[$count_bond++] = $row[1];
        
//     }
    
// }


$count_percent_stockstock = 0;
$stockstock = array(0=>0);
$stockstock_name = array(0=>0);
$count_stockstock = 0;
$stockstock_percent = array(0=>0);
for ( $i=0 ; $i<$n ; $i++ ){
    mysqli_query($conn,"SET NAMES 'utf8'");
    // $sql = "select * from 性質表 where name = '"+$var[$i] +"'";
    $sql = "SELECT * FROM $usertable where name = '".$var[$i] ."'";
    // echo $sql;
    $result = mysqli_query($conn,$sql);
    $row = mysqli_fetch_array($result);
    if($row[14]=='STOCK'){
    // if(preg_match("/股/",$row[3] ) and ($row[14]=='ETF') ){
        // $weight[$i] = round($weight[$i],5);
        $wght = $weight[$i]*100;
        $count_percent_stockstock += $wght;
        $stockstock[$count_stockstock] = $row[0];
        $stockstock_percent[$count_stockstock] = $wght;
        $stockstock_name[$count_stockstock++] = $row[1];
        //echo ("$row[0] \t\t $row[1] <div style='float:right;'> $wght %</div><br>");
    }

}

$count_percent_stock = 0;
$stock = array(0=>0);
$stock_name = array(0=>0);
$count_stock = 0;
$stock_percent = array(0=>0);
for ( $i=0 ; $i<$n ; $i++ ){
    mysqli_query($conn,"SET NAMES 'utf8'");
    // $sql = "select * from 性質表 where name = '"+$var[$i] +"'";
    $sql = "SELECT * FROM $usertable where name = '".$var[$i] ."'";
    // echo $sql;
    $result = mysqli_query($conn,$sql);
    $row = mysqli_fetch_array($result);
    // if($row[3]=='股票型'){
    if(preg_match("/股/",$row[3] ) and ($row[14]=='ETF') ){
        // $weight[$i] = round($weight[$i],5);
        $wght = $weight[$i]*100;
        $count_percent_stock += $wght;
        $stock[$count_stock] = $row[0];
        $stock_percent[$count_stock] = $wght;
        $stock_name[$count_stock++] = $row[1];
        //echo ("$row[0] \t\t $row[1] <div style='float:right;'> $wght %</div><br>");
    }

}


$count_percent_bond = 0;
$bond = array(0=>0);
$bond_name = array(0=>0);
$count_bond = 0;
$bond_percent = array(0=>0);
for ( $i=0 ; $i<$n ; $i++ ){
    mysqli_query($conn,"SET NAMES 'utf8'");
    $sql = "SELECT * FROM $usertable where name = '".$var[$i] ."'";
    // echo $sql;
    $result = mysqli_query($conn,$sql);
    $row = mysqli_fetch_array($result);
    //if($row[3]=='債券型'){
    if(preg_match("/債/",$row[3] )and ($row[14]=='ETF') ){
        // $weight[$i] = round($weight[$i],5);
        $wght = $weight[$i]*100;
        //echo ("$row[0] \t\t $row[1] <div style='float:right;'> $wght %</div><br>");
        $count_percent_bond += $wght;
        $bond[$count_bond] = $row[0];
        $bond_percent[$count_bond] = $wght;
        $bond_name[$count_bond++] = $row[1];
        
    }
    
}

$count_percent_other = 0;
$other = array(0=>0);
$other_name = array(0=>0);
$count_other = 0;
$other_percent = array(0=>0);
for ( $i=0 ; $i<$n ; $i++ ){
    mysqli_query($conn,"SET NAMES 'utf8'");
    $sql = "SELECT * FROM $usertable where name = '".$var[$i] ."'";
    // echo $sql;
    $result = mysqli_query($conn,$sql);
    $row = mysqli_fetch_array($result);
    //if($row[3]=='債券型'){
    if(!(preg_match("/債/",$row[3] )) and !(preg_match("/股/",$row[3] )) and ($row[14]=='ETF')){
        // $weight[$i] = round($weight[$i],5);
        $wght = $weight[$i]*100;
        //echo ("$row[0] \t\t $row[1] <div style='float:right;'> $wght %</div><br>");
        $count_percent_other += $wght;
        $other[$count_other] = $row[0];
        $other_percent[$count_other] = $wght;
        $other_name[$count_other++] = $row[1];
        
    }
    
}

?>

  <!-- Navigation -->
  <nav class="navbar navbar-expand-lg text-uppercase fixed-top" id="mainNav" style = "background: 	#2E8B57;">
    <div class="container">
      <a class="navbar-brand js-scroll-trigger" href="http://localhost/asset-allocation-pages/start-pages/start.php">DA DA 智能理財</a>
      <button class="navbar-toggler navbar-toggler-right text-uppercase font-weight-bold bg-primary text-white rounded" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
        Menu
        <i class="fas fa-bars"></i>
      </button>
      <div class="collapse navbar-collapse" id="navbarResponsive">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item mx-0 mx-lg-1">
            <a class="nav-link py-3 px-0 px-lg-3 rounded js-scroll-trigger" href="#portfolio">金流呈現</a>
          </li>
          <li class="nav-item mx-0 mx-lg-1">
            <a class="nav-link py-3 px-0 px-lg-3 rounded js-scroll-trigger" href="#about">投資組合</a>
          </li>
          <li class="nav-item mx-0 mx-lg-1">
            <a class="nav-link py-3 px-0 px-lg-3 rounded js-scroll-trigger" href="#contact">資產比例</a>
          </li>
          <li class="nav-item mx-0 mx-lg-1">
            <a class="nav-link py-3 px-0 px-lg-3 rounded js-scroll-trigger" href="#aboutm">風險評估</a>
          </li>
          
        </ul>
      </div>
    </div>
  </nav>

  <!-- Masthead -->
  <header class="masthead text-white text-center" style = "background: #FFBF00;">
    <div class="container d-flex align-items-center flex-column">

      <!-- Masthead Avatar Image -->
      <img class="masthead-avatar mb-5" src="img/bee_3.png" alt="">

      <!-- Masthead Heading -->
      <h2 class="masthead-heading text-uppercase mb-0">大數據系統演算法</h2><br>
      <h2 class="masthead-heading text-uppercase mb-0">幫你模擬投資表現</h2>

      <!-- Icon Divider -->
      <div class="divider-custom divider-light">
        <div class="divider-custom-line"></div>
        <div class="divider-custom-icon">
          <i class="fas fa-star"></i>
        </div>
        <div class="divider-custom-line"></div>
      </div>

      <!-- Masthead Subheading -->
      <p class="masthead-subheading font-weight-light mb-0">看完結果不再害怕理財!</p>

    </div>
  </header>
  <br><br>
  <div class="row">

            <!-- Earnings (Monthly) Card Example -->
            <div class="col-xl-3 col-md-6 mb-4">
              <div class="card border-left-primary shadow h-100 py-2">
                <div class="card-body">
                  <div class="row no-gutters align-items-center">
                    <div class="col mr-2">
                      <div class="text-xs font-weight-bold text-primary text-uppercase mb-1">投入資金</div>
                      <div class="h5 mb-0 font-weight-bold text-gray-800">$<?php echo number_format($flame_1); ?></div>
                    </div>
                    <div class="col-auto">
                      <i class="fas fa-calendar fa-2x text-gray-300"></i>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Earnings (Monthly) Card Example -->
            <div class="col-xl-3 col-md-6 mb-4">
              <div class="card border-left-success shadow h-100 py-2">
                <div class="card-body">
                  <div class="row no-gutters align-items-center">
                    <div class="col mr-2">
                      <div class="text-xs font-weight-bold text-success text-uppercase mb-1">現在資金</div>
                      <div class="h5 mb-0 font-weight-bold text-gray-800">$<?php echo number_format($flame_2);?></div>
                    </div>
                    <div class="col-auto">
                      <i class="fas fa-dollar-sign fa-2x text-gray-300"></i>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Earnings (Monthly) Card Example -->
            <div class="col-xl-3 col-md-6 mb-4">
              <div class="card border-left-success shadow h-100 py-2">
                <div class="card-body">
                  <div class="row no-gutters align-items-center">
                    <div class="col mr-2">
                      <div class="text-xs font-weight-bold text-success text-uppercase mb-1">資產變化標準差</div>
                      <div class="h5 mb-0 font-weight-bold text-gray-800"><?php echo ($flame_3);?></div>
                    </div>
                    <div class="col-auto">
                      <i class="fas fa-dollar-sign fa-2x text-gray-300"></i>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Pending Requests Card Example -->
            <div class="col-xl-3 col-md-6 mb-4">
              <div class="card border-left-warning shadow h-100 py-2">
                <div class="card-body">
                  <div class="row no-gutters align-items-center">
                    <div class="col mr-2">
                      <div class="text-xs font-weight-bold text-warning text-uppercase mb-1">投入至今年化標準差</div>
                      <div class="h5 mb-0 font-weight-bold text-gray-800"><?php echo ($flame_4);?>%</div>
                    </div>
                    <div class="col-auto">
                      <i class="fas fa-comments fa-2x text-gray-300"></i>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

  <!-- Portfolio Section -->
  <section class="page-section portfolio" id="portfolio">
    <div class="container">

      <!-- Portfolio Section Heading -->
      <h2 class="page-section-heading text-center text-uppercase text-secondary mb-0">金流呈現</h2>

      <!-- Icon Divider -->
      <div class="divider-custom">
        <div class="divider-custom-line"></div>
        <div class="divider-custom-icon">
          <i class="fas fa-star"></i>
        </div>
        <div class="divider-custom-line"></div>
      </div>

      <div class="row">
                            <!-- column -->
                            <div class="col-lg-1">
                            </div>
                            <div class="col-lg-10">
                                <div class="card">
                                    <div class="card-body">
                                        <h4 class="card-title">模擬金流呈現<?php //print_r($risk_y); ?></h4>
                                        <div><h6>依據您所輸入的參數為您選擇了最適合您的投資組合;投資期間經過 <?php echo($years-1); ?> 年後,您的投組價值會達到<?php echo($flame_2); ?>元。</h6></div>
                                        <p><div class="chartjs-wrapper"><canvas id="chartjs-0" class="chartjs" width="undefined" height="undefined"></canvas>
                                            <script>new Chart(document.getElementById("chartjs-0"),
                                            {"type":"line",
                                            "data":{"labels":<?php echo "[ $date_arr ]"; ?>,
                                            "datasets":[{"label":"每年再平衡","data": <?php echo "[ $total_money_y ]"; ?>,"fill":false,"borderColor":"rgb(75, 192, 192)","lineTension":0.1},
                                                        {"label":"每月再平衡","data": <?php echo "[ $total_money_m ]"; ?>,"fill":false,"borderColor":"rgb(255, 0, 0)","lineTension":0.1},
                                                        {"label":"價值再平衡","data": <?php echo "[ $total_money_d ]"; ?>,"fill":false,"borderColor":"rgb(0, 255, 0)","lineTension":0.1},
                                                        {"label":"無再平衡","data":   <?php echo "[ $total_money_n ]"; ?>,"fill":false,"borderColor":"rgb(0, 0, 255)","lineTension":0.1}]},
                                                        "options":{}});
                                            </script>
                                        </div></p>
                                    </div>
                                </div>
                            </div>
                            <div class="col-lg-1">
                            </div>
  </section>

  <!-- About Section -->
  <section class="page-section mb-0" id="about" style = "background: #FFBF00;">
    <div class="container">

      <!-- About Section Heading -->
      <h2 class="page-section-heading text-center text-uppercase ">投資組合</h2>

      <!-- Icon Divider -->
      <div class="divider-custom divider-light">
        <div class="divider-custom-line"></div>
        <div class="divider-custom-icon">
          <i class="fas fa-star"></i>
        </div>
        <div class="divider-custom-line"></div>
      </div>

      <div class="row">
                            <div class="col-lg-1">
                            </div>
                            <div class="col-lg-3">
                                <div class="card text-center" height="100%">
                                    
                                    <!-- <div class="m-t-10">
                                        <p>Customer Feedback</p>
                                        <h5>385749</h5>
                                    </div> -->
                                    <!-- <div class="widget-card-circle pr m-t-20 m-b-20" id="info-circle-card"> -->
                                      
                                        <!-- <div id="pieChartdiv" style="width: 100%; height: 395px">
                                            <div class="chartjs-wrapper"><canvas id="chartjs-4" class="chartjs" width="100%" height="130px"></canvas>
                                            <script>new Chart(document.getElementById("chartjs-4"),
                                            {"type":"doughnut","data":{"labels":["股票型","債券型"],
                                            "datasets":[{"label":"My First Dataset","data":[<?php print_r($count_percent_stock);?>,<?php print_r($count_percent_bond);?>],
                                            "backgroundColor":["rgb(255, 99, 132)","rgb(54, 162, 235)"]}]}});</script></div>
                                        </div> -->
                                        <div id="pieChartdiv" style="width: 100%; height: 395px">
                                            <div class="chartjs-wrapper"><canvas id="chartjs-4" class="chartjs" width="100%" height="130px"></canvas>
                                            <script>new Chart(document.getElementById("chartjs-4"),
                                            {"type":"doughnut","data":{"labels":["ETF股票型","ETF債券型","ETF其他型"],
                                            "datasets":[{"label":"My First Dataset","data":[<?php print_r($count_percent_stockstock);?>,<?php print_r($count_percent_stock);?>,<?php print_r($count_percent_bond);?>,<?php print_r($count_percent_other);?>],
                                            "backgroundColor":["rgb(255, 99, 132)","rgb(54, 162, 235),","rgb(255, 222, 132)","rgb(158, 99, 132)"]}]}});</script></div>
                                        </div>
                                        <!-- <i class="ti-control-shuffle pa"></i> -->
                                    <!-- </div> -->
                                    <!-- <div>
                                    <ul class="widget-line-list m-b-15">
                                        <li class="border-right">年化報酬率 <br><span > <?php print_r($reward);?></span></li>
                                        <li>年化標準差 <br><span ><?php print_r($std_dev*100);?>%</span></span></li>
                                        
                                    </ul>
                                    </div> -->

                                    <br>
                                    <p class="lead">年化報酬率<?php print_r($reward);?></p>
                                    <br>
                                    <p class="lead">年化標準差<?php print_r($std_dev*100);?>%</p>
                                    <br>
                                    
                                </div>
                                <!-- <div class="card nestable-cart">
                                    <div class="card-title">
                                        <h4>USA</h4>
                                        <div class="card-title-right-icon">
                                            <ul>

                                            </ul>
                                        </div>
                                    </div>
                                    <div class="Vector-map-js">
                                        <div id="vmap13" class="vmap"></div>
                                    </div>
                                </div> -->
                                <!-- /# card -->
                            </div>
                            <!-- /# column -->
                            <div class="col-lg-7">
                                <div class="card">
                                    <div class="card-title">
                                        <h3>選股結果 <br/></h3>
                                    </div>
                                    <p> </p>
                                    <div class="card-body">
                                        <div class="table-responsive">
                                        <!-- <h4>股票  <?php print_r($count_percent_stockstock); ?> %</h4>
                                            <table class="table">
                                                <thead>
                                                    <tr>
                                                        <th colspan="2">ETF</th>
                                                        <th>比例</th>
                                                        
                                                    </tr>
                                                </thead>
                                                <tbody>
                                                    <tr>
                                                        <?php
                                                            $count_percent = 0;
                                                            for ( $i=0 ; $i<$count_stockstock ; $i++ ){
                                                                // echo ("$stock[$i] \t\t $stock_name[$i] <div style='float:right;'> $stock_percent[$i] %</div><br>");
                                                                echo("<tr> <td>$stockstock[$i]</td> <td> $stockstock_name[$i]</td> <td>$stockstock_percent[$i]%</td> </tr>");
                                                            }
                                                        ?>
                                                        <td><span>VTI</span></td>
                                                        <td><span>Vanguard整體股市ETF</span></td>
                                                        <td><span>25%</span></td> -->
                                                        
                                                    </tr>
                                                    
                                                </tbody>
                                            </table>
                                            <h4>ETF股票型  <?php print_r($count_percent_stock); ?> %</h4>
                                            <table class="table">
                                                <thead>
                                                    <tr>
                                                        <th colspan="2">ETF</th>
                                                        <th>比例</th>
                                                        
                                                    </tr>
                                                </thead>
                                                <tbody>
                                                    <tr>
                                                        <?php
                                                            $count_percent = 0;
                                                            for ( $i=0 ; $i<$count_stock ; $i++ ){
                                                                // echo ("$stock[$i] \t\t $stock_name[$i] <div style='float:right;'> $stock_percent[$i] %</div><br>");
                                                                echo("<tr> <td>$stock[$i]</td> <td> $stock_name[$i]</td> <td>$stock_percent[$i]%</td> </tr>");
                                                            }
                                                        ?>
                                                        <!-- <td><span>VTI</span></td>
                                                        <td><span>Vanguard整體股市ETF</span></td>
                                                        <td><span>25%</span></td> -->
                                                        
                                                    </tr>
                                                    
                                                </tbody>
                                            </table>
                                            <h4>ETF債券型  <?php print_r($count_percent_bond); ?> %</h4>
                                            <table class="table">
                                                <thead>
                                                    <tr>
                                                        <th colspan="2">ETF</th>
                                                        <th>比例</th>
                                                        
                                                    </tr>
                                                </thead>
                                                <tbody>
                                                    <tr>
                                                        <?php
                                                            // $count_percent = 0;
                                                            for ( $i=0 ; $i<$count_bond ; $i++ ){
                                                                // echo ("$stock[$i] \t\t $stock_name[$i] <div style='float:right;'> $stock_percent[$i] %</div><br>");
                                                                echo("<tr> <td>$bond[$i]</td> <td> $bond_name[$i]</td> <td>$bond_percent[$i]%</td> </tr>");
                                                            }
                                                        ?>
                                                        <!-- <td><span>VTI</span></td>
                                                        <td><span>Vanguard整體股市ETF</span></td>
                                                        <td><span>25%</span></td> -->
                                                        
                                                    </tr>
                                                    
                                                </tbody>
                                            </table>
                                            <h4>ETF其他型  <?php print_r($count_percent_other); ?> %</h4>
                                            <table class="table">
                                                <thead>
                                                    <tr>
                                                        <th colspan="2">ETF</th>
                                                        <th>比例</th>
                                                        
                                                    </tr>
                                                </thead>
                                                <tbody>
                                                    <tr>
                                                        <?php
                                                            // $count_percent = 0;
                                                            for ( $i=0 ; $i<$count_other ; $i++ ){
                                                                // echo ("$stock[$i] \t\t $stock_name[$i] <div style='float:right;'> $stock_percent[$i] %</div><br>");
                                                                echo("<tr> <td>$other[$i]</td> <td> $other_name[$i]</td> <td>$other_percent[$i]%</td> </tr>");
                                                            }
                                                        ?>
                                                        <!-- <td><span>VTI</span></td>
                                                        <td><span>Vanguard整體股市ETF</span></td>
                                                        <td><span>25%</span></td> -->
                                                        
                                                    </tr>
                                                    
                                                </tbody>
                                            </table>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <div class="col-lg-1">
                            </div>
                            <div class="col-lg-1">
                            </div>
                            
                        </div>
  </section>


  <!-- About Section -->
  


  <!-- Contact Section -->
  <section class="page-section" id="contact">
    <div class="container">

      <!-- Contact Section Heading -->
      <h2 class="page-section-heading text-center text-uppercase text-secondary mb-0">資產比例</h2>

      <!-- Icon Divider -->
      <div class="divider-custom">
        <div class="divider-custom-line"></div>
        <div class="divider-custom-icon">
          <i class="fas fa-star"></i>
        </div>
        <div class="divider-custom-line"></div>
      </div>

      <!-- Contact Section Form -->
      <div class="row">
                            <div class="col-lg-1">
                            </div>
                            <div class="col-lg-10">
                                <div class="card alert">
                                    <div class="card-title">
                                        <h4>每年再平衡</h4>
                                    </div>
                                
                                    <!-- <div><h6>過去<?php  echo( (string)$_SESSION['want_see'] . (string)$_SESSION['ymd']); ?>的歷史回測結果，
                                    共投入了<?php echo($final_in_money)?>元，資產終值為<?php echo($final_money)?>元，
                                    總報酬率是 <?php echo(round($rrr,3)."%");?>。
                                    </h6></div> -->
                                    <div class="chartjs-wrapper"><canvas id="chartjs-1" class="chartjs" width="undefined" height="undefined"></canvas>
                                        <script>new Chart(document.getElementById("chartjs-1"),
                                            {"type":"line",
                                            "data":{"labels":<?php echo "[ $date_arr ]"; ?>,
                                            
                                            "datasets":[
                                                <?php
                                                $R_R = array(0=>0);
                                                $G_G = array(0=>0);
                                                $B_B = array(0=>0);

                                                $R_R[1] = 255;$R_R[2] = 0;$R_R[3] = 0;$R_R[4] = 255;$R_R[5] = 0;$R_R[6] = 255;$R_R[7] = 255;$R_R[8] = 255;$R_R[9] = 0;$R_R[10] = 47;$R_R[11] = 123;$R_R[12] = 255;$R_R[13] = 255;$R_R[14] = 255;$R_R[15] = 128;$R_R[16] = 139;$R_R[17] = 128;$R_R[18] = 220;$R_R[19] = 255;
                                                $G_G[1] = 0;$G_G[2] = 255;$G_G[3] = 0;$G_G[4] = 255;$G_G[5] = 255;$G_G[6] = 0;$G_G[7] = 69;$G_G[8] = 165;$G_G[9] = 100;$G_G[10] = 79;$G_G[11] = 104;$G_G[12] = 255;$G_G[13] = 255;$G_G[14] = 255;$G_G[15] = 128;$G_G[16] = 69;$G_G[17] = 0;$G_G[18] = 20;$G_G[19] = 140;
                                                $B_B[1] = 0;$B_B[2] = 0;$B_B[3] = 255;$B_B[4] = 0;$B_B[5] = 255;$B_B[6] = 255;$B_B[7] = 0;$B_B[8] = 0;$B_B[9] = 0;$B_B[10] = 79;$B_B[11] = 238;$B_B[12] = 255;$B_B[13] = 255;$B_B[14] = 255;$B_B[15] = 128;$B_B[16] = 19;$B_B[17] = 128;$B_B[18] = 60;$B_B[19] = 0;


                                                // echo ("{'label':'".$var[$i]."','data': [".$ratio_y[$i]."],'fill':false,'borderColor':'rgb(255, 0, 0)','lineTension':0.1}," );
                                                for ($i=0;$i<$n;$i++){
                                                    echo ("{'label':'".$var[$i]."','data': [".$ratio_y[$i]."],'fill':false,'borderColor':'rgb(".(string)($R_R[$i]).",".(string)($G_G[$i]).", " .(string)($B_B[$i]).")','lineTension':0.1}" );
                                                if ($i!=$n-1){
                                                    echo (',');
                                                  }
                                                }
                                                ?>

                                               
                                                ]},"options":{}});
                 
                                        </script>
                                    </div>
                                    
                                    
                                </div>
                                <!-- /# card -->
                            </div>
                            <div class="col-lg-1">
                            </div>
            </div>

            <div class="row">
                            <div class="col-lg-1">
                            </div>
                            <div class="col-lg-10">
                                <div class="card alert">
                                    <div class="card-title">
                                        <h4>每月再平衡</h4>
                                    </div>
                                    <!-- <div><h6>過去<?php  echo( (string)$_SESSION['want_see'] . (string)$_SESSION['ymd']); ?>的歷史回測結果，
                                    共投入了<?php echo($final_in_money)?>元，資產終值為<?php echo($final_money)?>元，
                                    總報酬率是 <?php echo(round($rrr,3)."%");?>。
                                    </h6></div> -->
                                    <div class="chartjs-wrapper"><canvas id="chartjs-2" class="chartjs" width="undefined" height="undefined"></canvas>
                                        <script>new Chart(document.getElementById("chartjs-2"),
                                            {"type":"line",
                                            "data":{"labels":<?php echo "[ $date_arr ]"; ?>,
                                            
                                            "datasets":[
                                                <?php
                                                $R_R = array(0=>0);
                                                $G_G = array(0=>0);
                                                $B_B = array(0=>0);

                                                $R_R[1] = 255;$R_R[2] = 0;$R_R[3] = 0;$R_R[4] = 255;$R_R[5] = 0;$R_R[6] = 255;$R_R[7] = 255;$R_R[8] = 255;$R_R[9] = 0;$R_R[10] = 47;$R_R[11] = 123;$R_R[12] = 255;$R_R[13] = 255;$R_R[14] = 255;$R_R[15] = 128;$R_R[16] = 139;$R_R[17] = 128;$R_R[18] = 220;$R_R[19] = 255;
                                                $G_G[1] = 0;$G_G[2] = 255;$G_G[3] = 0;$G_G[4] = 255;$G_G[5] = 255;$G_G[6] = 0;$G_G[7] = 69;$G_G[8] = 165;$G_G[9] = 100;$G_G[10] = 79;$G_G[11] = 104;$G_G[12] = 255;$G_G[13] = 255;$G_G[14] = 255;$G_G[15] = 128;$G_G[16] = 69;$G_G[17] = 0;$G_G[18] = 20;$G_G[19] = 140;
                                                $B_B[1] = 0;$B_B[2] = 0;$B_B[3] = 255;$B_B[4] = 0;$B_B[5] = 255;$B_B[6] = 255;$B_B[7] = 0;$B_B[8] = 0;$B_B[9] = 0;$B_B[10] = 79;$B_B[11] = 238;$B_B[12] = 255;$B_B[13] = 255;$B_B[14] = 255;$B_B[15] = 128;$B_B[16] = 19;$B_B[17] = 128;$B_B[18] = 60;$B_B[19] = 0;
                                                // echo ("{'label':'".$var[$i]."','data': [".$ratio_y[$i]."],'fill':false,'borderColor':'rgb(255, 0, 0)','lineTension':0.1}," );
                                                for ($i=0;$i<$n;$i++){
                                                    echo ("{'label':'".$var[$i]."','data': [".$ratio_m[$i]."],'fill':false,'borderColor':'rgb(".(string)($R_R[$i]).",".(string)($G_G[$i]).", " .(string)($B_B[$i]).")','lineTension':0.1}" );
                                                if ($i!=$n-1){
                                                    echo (',');
                                                  }
                                                }
                                                ?>
                                                ]},"options":{}});
                                        </script>
                                    </div>
                                    
                                    
                                </div>
                                <!-- /# card -->
                            </div>
                            <div class="col-lg-1">
                            </div>
            </div>
            <div class="row">
                            <div class="col-lg-1">
                            </div>
                            <div class="col-lg-10">
                                <div class="card alert">
                                    <div class="card-title">
                                        <h4>價值再平衡</h4>
                                    </div>
                                    <!-- <div><h6>過去<?php  echo( (string)$_SESSION['want_see'] . (string)$_SESSION['ymd']); ?>的歷史回測結果，
                                    共投入了<?php echo($final_in_money)?>元，資產終值為<?php echo($final_money)?>元，
                                    總報酬率是 <?php echo(round($rrr,3)."%");?>。
                                    </h6></div> -->
                                    <div class="chartjs-wrapper"><canvas id="chartjs-3" class="chartjs" width="undefined" height="undefined"></canvas>
                                        <script>new Chart(document.getElementById("chartjs-3"),
                                            {"type":"line",
                                            "data":{"labels":<?php echo "[ $date_arr ]"; ?>,
                                            
                                            "datasets":[
                                                <?php
                                                // echo ("{'label':'".$var[$i]."','data': [".$ratio_y[$i]."],'fill':false,'borderColor':'rgb(255, 0, 0)','lineTension':0.1}," );
                                                for ($i=0;$i<$n;$i++){
                                                    echo ("{'label':'".$var[$i]."','data': [".$ratio_d[$i]."],'fill':false,'borderColor':'rgb(".(string)($R_R[$i]).",".(string)($G_G[$i]).", " .(string)($B_B[$i]).")','lineTension':0.1}" );
                                                if ($i!=$n-1){
                                                    echo (',');
                                                  }
                                                }
                                                ?>
                                                ]},"options":{}});
                                        </script>
                                    </div>
                                    
                                    
                                </div>
                                <!-- /# card -->
                            </div>
                            <div class="col-lg-1">
                            </div>
            </div>
            <div class="row">
                            <div class="col-lg-1">
                            </div>
                            <div class="col-lg-10">
                                <div class="card alert">
                                    <div class="card-title">
                                        <h4>無再平衡</h4>
                                    </div>
                                    
                                    <div class="chartjs-wrapper"><canvas id="chartjs-5" class="chartjs" width="undefined" height="undefined"></canvas>
                                        <script>new Chart(document.getElementById("chartjs-5"),
                                            {"type":"line",
                                            "data":{"labels":<?php echo "[ $date_arr ]"; ?>,
                                            
                                            "datasets":[
                                                <?php
                                                // echo ("{'label':'".$var[$i]."','data': [".$ratio_y[$i]."],'fill':false,'borderColor':'rgb(255, 0, 0)','lineTension':0.1}," );
                                                for ($i=0;$i<$n;$i++){
                                                    echo ("{'label':'".$var[$i]."','data': [".$ratio_n[$i]."],'fill':false,'borderColor':'rgb(".(string)($R_R[$i]).",".(string)($G_G[$i]).", " .(string)($B_B[$i]).")','lineTension':0.1}" );
                                                if ($i!=$n-1){
                                                    echo (',');
                                                  }
                                                }
                                                ?>
                                                ]},"options":{}});
                                        </script>
                                    </div>
                                </div>
                                <!-- /# card -->
                            </div>
                            <div class="col-lg-1">
                            </div>
                            </div>
            

  </section>
  </section>
  <section class="page-section mb-0" id="aboutm" style = "background: #FFBF00;">
    <div class="container">

      <!-- About Section Heading -->
      <h2 class="page-section-heading text-center text-uppercase ">風險評估</h2>

      <!-- Icon Divider -->
      <div class="divider-custom divider-light">
        <div class="divider-custom-line"></div>
        <div class="divider-custom-icon">
          <i class="fas fa-star"></i>
        </div>
        <div class="divider-custom-line"></div>
      </div>

      <div class="row">
                            <div class="col-lg-1">
                            </div>
                            <div class="col-lg-10">
                                <div class="card alert">
                                    <div class="card-title">
                                        <h4>標準差</h4>
                                    </div>
                                    
                                    <div class="chartjs-wrapper"><canvas id="chartjs-6" class="chartjs" width="undefined" height="undefined"></canvas>
                                        <script>new Chart(document.getElementById("chartjs-6"),
                                            {"type":"line",
                                            "data":{"labels":<?php echo "[ $date_arr ]"; ?>,
                                            "datasets":[{"label":"每年再平衡","data": <?php echo "[ $std_y ]"; ?>,"fill":false,"borderColor":"rgb(75, 192, 192)","lineTension":0.1},
                                                        {"label":"每月再平衡","data": <?php echo "[ $std_m ]"; ?>,"fill":false,"borderColor":"rgb(255, 0, 0)","lineTension":0.1},
                                                        {"label":"價值再平衡","data": <?php echo "[ $std_d ]"; ?>,"fill":false,"borderColor":"rgb(0, 255, 0)","lineTension":0.1},
                                                        {"label":"無再平衡","data":   <?php echo "[ $std_n ]"; ?>,"fill":false,"borderColor":"rgb(0, 0, 255)","lineTension":0.1}]},
                                                        "options":{}});
                                        </script>
                                    </div>
                                </div>
                               
                            <div class="row">
                            <div class="col-lg-1">
                            </div>
                            
                            <!-- /# column -->
                            <div class="col-lg-10">
                                <div class="card">
                                    <div class="card-title">
                                        <br/>
                                        <h3>    投資至今風險矩陣 </h3>
                                    </div>
                                    <div class="card-body">
                                        <div class="table-responsive">
                                            <table class="table">
                                                <thead>
                                                    <tr> <th>再平衡類別</th> <th>標準差</th>                      <th>夏普值</th>                   <th>最大回撤率</th>            </tr>
                                                </thead>
                                                <tbody>
                                                    <tr> <td>每年再平衡</td> <td><?php echo($risk_y[0]) ?></td> <td><?php echo($risk_y[1]) ?></td>  <td><?php echo($risk_y[2]) ?></td> </tr>
                                                    <tr> <td>每月再平衡</td> <td><?php echo($risk_m[0]) ?></td> <td><?php echo($risk_y[1]) ?></td>  <td><?php echo($risk_y[2]) ?></td> </tr>
                                                    <tr> <td>價值再平衡</td> <td><?php echo($risk_d[0]) ?></td> <td><?php echo($risk_y[1]) ?></td>  <td><?php echo($risk_y[2]) ?></td> </tr>
                                                    <tr> <td>無再平衡</td>   <td><?php echo($risk_n[0]) ?></td> <td><?php echo($risk_y[1]) ?></td>  <td><?php echo($risk_y[2]) ?></td> </tr>
                                                    
                                                </tbody>
                                            </table>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="col-lg-1">
                            </div>
        </div>
  </section>
  <!-- Footer -->
  <footer class="footer text-center" style = "background: 	#2E8B57;">
    <div class="container">
      <div class="row">
        <!-- Footer Location -->
        <div class="col-lg-4 mb-5 mb-lg-0">
          <h4 class="text-uppercase mb-4">Location</h4>
          <p class="lead mb-0">NCKU ES
          <br>East District ,Tainan City ,Taiwan
            <br>No.1, University Road </p>
        </div>
        <!-- Footer Social Icons -->
        <div class="col-lg-4 mb-5 mb-lg-0">
          <h4 class="text-uppercase mb-4">Around the Web</h4>
          <br>
          <a class="btn btn-outline-light btn-social mx-1" href="#">
            <i class="fab fa-fw fa-facebook-f"></i>
          </a>
          <a class="btn btn-outline-light btn-social mx-1" href="#">
            <i class="fab fa-fw fa-twitter"></i>
          </a>
          <a class="btn btn-outline-light btn-social mx-1" href="#">
            <i class="fab fa-fw fa-linkedin-in"></i>
          </a>
          <a class="btn btn-outline-light btn-social mx-1" href="#">
            <i class="fab fa-fw fa-dribbble"></i>
          </a>
        </div>
        <!-- Footer About Text -->
        <div class="col-lg-4">
          <h4 class="text-uppercase mb-4">About us</h4>
          <p class="lead mb-0"> DADA智能理財致力於為投資人客製化投資組合，以達成投資人的理財目標。 </p>
        </div>
      </div>
    </div>
  </footer>
  <!-- Copyright Section -->
  <section class="copyright py-4 text-center text-white" style = "background: 	#2F4F4F;">
    <div class="container">
    <div class="container">
      <small>Copyright &copy; Your Website 2019</small>
    </div>
  </section>

  <!-- Scroll to Top Button (Only visible on small and extra-small screen sizes) -->
  <div class="scroll-to-top d-lg-none position-fixed ">
    <a class="js-scroll-trigger d-block text-center text-white rounded" href="#page-top">
      <i class="fa fa-chevron-up"></i>
    </a>
  </div>

  <!-- Portfolio Modals -->

  <!-- Portfolio Modal 1 -->
  <div class="portfolio-modal modal fade" id="portfolioModal1" tabindex="-1" role="dialog" aria-labelledby="portfolioModal1Label" aria-hidden="true">
    <div class="modal-dialog modal-xl" role="document">
      <div class="modal-content">
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">
            <i class="fas fa-times"></i>
          </span>
        </button>
        <div class="modal-body text-center">
          <div class="container">
            <div class="row justify-content-center">
              <div class="col-lg-8">
                <!-- Portfolio Modal - Title -->
                <h2 class="portfolio-modal-title text-secondary text-uppercase mb-0">Log Cabin</h2>
                <!-- Icon Divider -->
                <div class="divider-custom">
                  <div class="divider-custom-line"></div>
                  <div class="divider-custom-icon">
                    <i class="fas fa-star"></i>
                  </div>
                  <div class="divider-custom-line"></div>
                </div>
                <!-- Portfolio Modal - Image -->
                <img class="img-fluid rounded mb-5" src="img/portfolio/cabin.png" alt="">
                <!-- Portfolio Modal - Text -->
                <p class="mb-5">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Mollitia neque assumenda ipsam nihil, molestias magnam, recusandae quos quis inventore quisquam velit asperiores, vitae? Reprehenderit soluta, eos quod consequuntur itaque. Nam.</p>
                <button class="btn btn-primary" href="#" data-dismiss="modal">
                  <i class="fas fa-times fa-fw"></i>
                  Close Window
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Portfolio Modal 2 -->
  <div class="portfolio-modal modal fade" id="portfolioModal2" tabindex="-1" role="dialog" aria-labelledby="portfolioModal2Label" aria-hidden="true">
    <div class="modal-dialog modal-xl" role="document">
      <div class="modal-content">
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">
            <i class="fas fa-times"></i>
          </span>
        </button>
        <div class="modal-body text-center">
          <div class="container">
            <div class="row justify-content-center">
              <div class="col-lg-8">
                <!-- Portfolio Modal - Title -->
                <h2 class="portfolio-modal-title text-secondary text-uppercase mb-0">Tasty Cake</h2>
                <!-- Icon Divider -->
                <div class="divider-custom">
                  <div class="divider-custom-line"></div>
                  <div class="divider-custom-icon">
                    <i class="fas fa-star"></i>
                  </div>
                  <div class="divider-custom-line"></div>
                </div>
                <!-- Portfolio Modal - Image -->
                <img class="img-fluid rounded mb-5" src="img/portfolio/cake.png" alt="">
                <!-- Portfolio Modal - Text -->
                <p class="mb-5">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Mollitia neque assumenda ipsam nihil, molestias magnam, recusandae quos quis inventore quisquam velit asperiores, vitae? Reprehenderit soluta, eos quod consequuntur itaque. Nam.</p>
                <button class="btn btn-primary" href="#" data-dismiss="modal">
                  <i class="fas fa-times fa-fw"></i>
                  Close Window
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Portfolio Modal 3 -->
  <div class="portfolio-modal modal fade" id="portfolioModal3" tabindex="-1" role="dialog" aria-labelledby="portfolioModal3Label" aria-hidden="true">
    <div class="modal-dialog modal-xl" role="document">
      <div class="modal-content">
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">
            <i class="fas fa-times"></i>
          </span>
        </button>
        <div class="modal-body text-center">
          <div class="container">
            <div class="row justify-content-center">
              <div class="col-lg-8">
                <!-- Portfolio Modal - Title -->
                <h2 class="portfolio-modal-title text-secondary text-uppercase mb-0">Circus Tent</h2>
                <!-- Icon Divider -->
                <div class="divider-custom">
                  <div class="divider-custom-line"></div>
                  <div class="divider-custom-icon">
                    <i class="fas fa-star"></i>
                  </div>
                  <div class="divider-custom-line"></div>
                </div>
                <!-- Portfolio Modal - Image -->
                <img class="img-fluid rounded mb-5" src="img/portfolio/circus.png" alt="">
                <!-- Portfolio Modal - Text -->
                <p class="mb-5">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Mollitia neque assumenda ipsam nihil, molestias magnam, recusandae quos quis inventore quisquam velit asperiores, vitae? Reprehenderit soluta, eos quod consequuntur itaque. Nam.</p>
                <button class="btn btn-primary" href="#" data-dismiss="modal">
                  <i class="fas fa-times fa-fw"></i>
                  Close Window
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Portfolio Modal 4 -->
  <div class="portfolio-modal modal fade" id="portfolioModal4" tabindex="-1" role="dialog" aria-labelledby="portfolioModal4Label" aria-hidden="true">
    <div class="modal-dialog modal-xl" role="document">
      <div class="modal-content">
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">
            <i class="fas fa-times"></i>
          </span>
        </button>
        <div class="modal-body text-center">
          <div class="container">
            <div class="row justify-content-center">
              <div class="col-lg-8">
                <!-- Portfolio Modal - Title -->
                <h2 class="portfolio-modal-title text-secondary text-uppercase mb-0">Controller</h2>
                <!-- Icon Divider -->
                <div class="divider-custom">
                  <div class="divider-custom-line"></div>
                  <div class="divider-custom-icon">
                    <i class="fas fa-star"></i>
                  </div>
                  <div class="divider-custom-line"></div>
                </div>
                <!-- Portfolio Modal - Image -->
                <img class="img-fluid rounded mb-5" src="img/portfolio/game.png" alt="">
                <!-- Portfolio Modal - Text -->
                <p class="mb-5">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Mollitia neque assumenda ipsam nihil, molestias magnam, recusandae quos quis inventore quisquam velit asperiores, vitae? Reprehenderit soluta, eos quod consequuntur itaque. Nam.</p>
                <button class="btn btn-primary" href="#" data-dismiss="modal">
                  <i class="fas fa-times fa-fw"></i>
                  Close Window
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Portfolio Modal 5 -->
  <div class="portfolio-modal modal fade" id="portfolioModal5" tabindex="-1" role="dialog" aria-labelledby="portfolioModal5Label" aria-hidden="true">
    <div class="modal-dialog modal-xl" role="document">
      <div class="modal-content">
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">
            <i class="fas fa-times"></i>
          </span>
        </button>
        <div class="modal-body text-center">
          <div class="container">
            <div class="row justify-content-center">
              <div class="col-lg-8">
                <!-- Portfolio Modal - Title -->
                <h2 class="portfolio-modal-title text-secondary text-uppercase mb-0">Locked Safe</h2>
                <!-- Icon Divider -->
                <div class="divider-custom">
                  <div class="divider-custom-line"></div>
                  <div class="divider-custom-icon">
                    <i class="fas fa-star"></i>
                  </div>
                  <div class="divider-custom-line"></div>
                </div>
                <!-- Portfolio Modal - Image -->
                <img class="img-fluid rounded mb-5" src="img/portfolio/safe.png" alt="">
                <!-- Portfolio Modal - Text -->
                <p class="mb-5">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Mollitia neque assumenda ipsam nihil, molestias magnam, recusandae quos quis inventore quisquam velit asperiores, vitae? Reprehenderit soluta, eos quod consequuntur itaque. Nam.</p>
                <button class="btn btn-primary" href="#" data-dismiss="modal">
                  <i class="fas fa-times fa-fw"></i>
                  Close Window
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Portfolio Modal 6 -->
  <div class="portfolio-modal modal fade" id="portfolioModal6" tabindex="-1" role="dialog" aria-labelledby="portfolioModal6Label" aria-hidden="true">
    <div class="modal-dialog modal-xl" role="document">
      <div class="modal-content">
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">
            <i class="fas fa-times"></i>
          </span>
        </button>
        <div class="modal-body text-center">
          <div class="container">
            <div class="row justify-content-center">
              <div class="col-lg-8">
                <!-- Portfolio Modal - Title -->
                <h2 class="portfolio-modal-title text-secondary text-uppercase mb-0">Submarine</h2>
                <!-- Icon Divider -->
                <div class="divider-custom">
                  <div class="divider-custom-line"></div>
                  <div class="divider-custom-icon">
                    <i class="fas fa-star"></i>
                  </div>
                  <div class="divider-custom-line"></div>
                </div>
                <!-- Portfolio Modal - Image -->
                <img class="img-fluid rounded mb-5" src="img/portfolio/submarine.png" alt="">
                <!-- Portfolio Modal - Text -->
                <p class="mb-5">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Mollitia neque assumenda ipsam nihil, molestias magnam, recusandae quos quis inventore quisquam velit asperiores, vitae? Reprehenderit soluta, eos quod consequuntur itaque. Nam.</p>
                <button class="btn btn-primary" href="#" data-dismiss="modal">
                  <i class="fas fa-times fa-fw"></i>
                  Close Window
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Bootstrap core JavaScript -->
  <script src="vendor/jquery/jquery.min.js"></script>
  <script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

  <!-- Plugin JavaScript -->
  <script src="vendor/jquery-easing/jquery.easing.min.js"></script>

  <!-- Contact Form JavaScript -->
  <script src="js/jqBootstrapValidation.js"></script>
  <script src="js/contact_me.js"></script>

  <!-- Custom scripts for this template -->
  <script src="js/freelancer.min.js"></script>
          <!-- jquery vendor -->
          <script src="assets/js/lib/jquery.min.js"></script>
        <script src="assets/js/lib/jquery.nanoscroller.min.js"></script>
        <!-- nano scroller -->
        <script src="assets/js/lib/menubar/sidebar.js"></script>
        <script src="assets/js/lib/preloader/pace.min.js"></script>
        <!-- sidebar -->
        <script src="assets/js/lib/bootstrap.min.js"></script>

        <!-- bootstrap -->

        <script src="assets/js/lib/circle-progress/circle-progress.min.js"></script>
        <script src="assets/js/lib/circle-progress/circle-progress-init.js"></script>

        <script src="assets/js/lib/morris-chart/raphael-min.js"></script>
        <script src="assets/js/lib/morris-chart/morris.js"></script>
        <script src="assets/js/lib/morris-chart/morris-init.js"></script>

        <!--  flot-chart js -->
        <script src="assets/js/lib/flot-chart/jquery.flot.js"></script>
        <script src="assets/js/lib/flot-chart/jquery.flot.resize.js"></script>
        <script src="assets/js/lib/flot-chart/flot-chart-init.js"></script>
        <!-- // flot-chart js -->


        <script src="assets/js/lib/vector-map/jquery.vmap.js"></script>
        <!-- scripit init-->
        <script src="assets/js/lib/vector-map/jquery.vmap.min.js"></script>
        <!-- scripit init-->
        <script src="assets/js/lib/vector-map/jquery.vmap.sampledata.js"></script>
        <!-- scripit init-->
        <script src="assets/js/lib/vector-map/country/jquery.vmap.world.js"></script>
        <!-- scripit init-->
        <script src="assets/js/lib/vector-map/country/jquery.vmap.algeria.js"></script>
        <!-- scripit init-->
        <script src="assets/js/lib/vector-map/country/jquery.vmap.argentina.js"></script>
        <!-- scripit init-->
        <script src="assets/js/lib/vector-map/country/jquery.vmap.brazil.js"></script>
        <!-- scripit init-->
        <script src="assets/js/lib/vector-map/country/jquery.vmap.france.js"></script>
        <!-- scripit init-->
        <script src="assets/js/lib/vector-map/country/jquery.vmap.germany.js"></script>
        <!-- scripit init-->
        <script src="assets/js/lib/vector-map/country/jquery.vmap.greece.js"></script>
        <!-- scripit init-->
        <script src="assets/js/lib/vector-map/country/jquery.vmap.iran.js"></script>
        <!-- scripit init-->
        <script src="assets/js/lib/vector-map/country/jquery.vmap.iraq.js"></script>
        <!-- scripit init-->
        <script src="assets/js/lib/vector-map/country/jquery.vmap.russia.js"></script>
        <!-- scripit init-->
        <script src="assets/js/lib/vector-map/country/jquery.vmap.tunisia.js"></script>
        <!-- scripit init-->
        <script src="assets/js/lib/vector-map/country/jquery.vmap.europe.js"></script>
        <!-- scripit init-->
        <script src="assets/js/lib/vector-map/country/jquery.vmap.usa.js"></script>
        <!-- scripit init-->
        <script src="assets/js/lib/vector-map/vector.init.js"></script>

        <script src="assets/js/lib/weather/jquery.simpleWeather.min.js"></script>
        <script src="assets/js/lib/weather/weather-init.js"></script>
        <script src="assets/js/lib/owl-carousel/owl.carousel.min.js"></script>
        <script src="assets/js/lib/owl-carousel/owl.carousel-init.js"></script>
        <script src="assets/js/scripts.js"></script>
        <!-- scripit init-->
</body>
</html>
