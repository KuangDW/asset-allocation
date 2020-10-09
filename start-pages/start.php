<!DOCTYPE html>
<html lang="en">

<head>

  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="">
  <meta name="author" content="">

  <title>Coming Soon - Start Bootstrap Theme</title>

  <!-- Bootstrap core CSS -->
  <link href="vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

  <!-- Custom fonts for this template -->
  <link href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:200,200i,300,300i,400,400i,600,600i,700,700i,900,900i" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css?family=Merriweather:300,300i,400,400i,700,700i,900,900i" rel="stylesheet">
  <link href="vendor/fontawesome-free/css/all.min.css" rel="stylesheet" type="text/css">

  <!-- Custom styles for this template -->
  <link href="css/coming-soon.min.css" rel="stylesheet">



</head>

<body>

  <div class="overlay"></div>
  <video playsinline="playsinline" autoplay="autoplay" muted="muted" loop="loop">
    <source src="mp4/bg.mp4" type="video/mp4">
  </video>

  <div class="masthead">
    <div class="masthead-bg"></div>
    <div class="container h-100">
      <div class="row h-100">
        <div class="col-12 my-auto">
          <div class="masthead-content text-white py-5 py-md-0">
            <h1 class="mb-3">Coming Soon!</h1>
            <p class="mb-5">We're working hard to finish the development of this site. Our target launch date is
              <strong>December 2020</strong>! Sign up for updates using the form below!</p>
        <form id = "info"  method="post" name="info">
            <div class="input-group input-group-newsletter">
              <input  class="form-control" id="yourname" name="yourname" type="text" autocomplete="off" value="" placeholder="Enter your name..." >
            </div>
            <br>
            <div class="input-group input-group-newsletter">
              <input  class="form-control" id="password" name="password" type="text" autocomplete="off" value="" placeholder="Enter your password...">
            </div>
            <br>
              <div class="input-group-append">
                <input class="btn btn-secondary" type="button" id="sign1" value = "開始資產配置!" onclick="sign();" >
              </div>
                <br>
              <div class="input-group-append">
                <input class="btn btn-secondary" type="button" id="check1" value = "查看目前資產!" onclick="check();" >
              </div>
              <br>
              <div class="input-group-append">
                <input class="btn btn-secondary" type="button" id="try1" value = "開始模擬投資!" onclick="trytry();" >
              </div>
            </div>
        </form>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="social-icons">
    <ul class="list-unstyled text-center mb-0">
      <li class="list-unstyled-item">
        <a href="#">
          <i class="fab fa-twitter"></i>
        </a>
      </li>
      <li class="list-unstyled-item">
        <a href="#">
          <i class="fab fa-facebook-f"></i>
        </a>
      </li>
      <li class="list-unstyled-item">
        <a href="#">
          <i class="fab fa-instagram"></i>
        </a>
      </li>
    </ul>
  </div>

  <!-- Bootstrap core JavaScript -->
  <script type="text/javascript">
    function check()
    {
        document.info.action="http://localhost/asset-allocation-pages/%E6%9F%A5%E8%A9%A2%E7%B5%90%E6%9E%9C.php";
        document.info.submit();
    }

    function sign()
    {
        document.info.action="http://localhost/asset-allocation-pages/%E8%B3%87%E7%94%A2%E9%85%8D%E7%BD%AE%E8%A1%A8%E5%96%AE%E9%A0%81%E9%9D%A2.php";
        document.info.submit();
    }

    function trytry()
    {
        document.info.action="http://localhost/asset-allocation-pages/%E6%A8%A1%E6%93%AC%E6%8A%95%E8%B3%87%E8%A1%A8%E5%96%AE%E9%A0%81%E9%9D%A2.php";
        document.info.submit();
    }
  </script>

  <script src="vendor/jquery/jquery.min.js"></script>
  <script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

  <!-- Custom scripts for this template -->
  <script src="js/coming-soon.min.js"></script>

</body>

</html>
