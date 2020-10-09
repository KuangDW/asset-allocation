
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
        <script>
        function add() {
          var age = parseFloat(document.getElementById('age').value);
          var retireAge = parseFloat(document.getElementById('retireAge').value);
          var expectAge = parseFloat(document.getElementById('expectAge').value);
          var expenses = parseFloat(document.getElementById('expenses').value);
          var in_per_year = parseFloat(document.getElementById('in_per_year').value);
          var risk = parseFloat(document.getElementById('risk').value);
          var year = retireAge - age;
          var goal_money = expenses*(expectAge-retireAge)*12*10000*(1.0172**year);
          in_per_year =  in_per_year*10000;
          var first_input = risk*10000;
          var money = [];

          // var year = 40
          // var goal_money = 5*15*12*10000*(1.0172**40)
          // var in_per_year =  120000
          // var first_input = 20*10000


          for(i=0;i<(year*12+1);i++)
          {
            if(i==0)
            {
              money.push(first_input*(-1));
            }
            else if(i>0 && i<(year*12))
            {
              money.push(in_per_year/12*(-1));
            }
            else if(i==(year*12))
            {
              money.push(goal_money);
            }
            
          }
          maxrate = 100/100 //折扣率上限 100%
          minrate = 0.0           //折扣率下限 
          C0 = first_input   //初期成本
          CT = money.slice(); //現金流量矩陣(CFM)
          k = 100000       //防止無限回圈計數器
          while (k-- > 0) {
            IRR = (maxrate + minrate) / 2   //取折扣率上下限的中間值估算 IRR
            NPV = 0.0 //因 NPV 與 r 成反比關係, 為了讓 NPV 下降需提高 r, 反之使 NPV 上升則降低 r
            for (i in CT) NPV = NPV + CT[i]/((1+IRR)**i)  // 藉由累加 CFM, 計算 NPV
            if ( Math.abs(NPV) < 1e-6 || (maxrate - minrate) < 1e-6)  break;//上下限逼近時離開
            if( NPV > 0 ) minrate = IRR //為了讓 NPV 下降為零, 修正下限以提升 IRR 估算
            else  maxrate = IRR //為了讓 NPV 上升為零, 修正上限以降低 IRR 估算
          }
          console.log("投資成本=" + C0 + "\tNPV=" + NPV + "\tIRR: " + IRR*100 + "%");
          document.getElementById('result').value = (IRR*12*100+ "%") ;
        }
    </script>


</head>

<body id="page-top">
<?php
$yourname = $_POST["yourname"];
$password = $_POST["password"];
?>

  <!-- Navigation -->
  <nav class="navbar navbar-expand-lg text-uppercase fixed-top" id="mainNav" style = "background: 	#2E8B57;">
    <div class="container">
      <a class="navbar-brand js-scroll-trigger" href="http://localhost/asset-allocation-pages/start-pages/start.php">DA DA 智能理財</a>
      <button class="navbar-toggler navbar-toggler-right text-uppercase font-weight-bold bg-primary text-white rounded" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
        Menu
        <i class="fas fa-bars"></i>
      </button>
    </div>
  </nav>

  <!-- Masthead -->
  <header class="masthead text-white text-center" style = "background: #FFBF00;">
    <div class="container d-flex align-items-center flex-column">

      <!-- Masthead Avatar Image -->
      <img class="masthead-avatar mb-5" src="img/bee_5.png" alt="">

      <!-- Masthead Heading -->
      <h2 class="masthead-heading text-uppercase mb-0">世界在變，你的投資方式也要跟著改變</h2><br>
      <h2 class="masthead-heading text-uppercase mb-0">快來體驗智能投資吧!</h2>

      <!-- Icon Divider -->
      <div class="divider-custom divider-light">
        <div class="divider-custom-line"></div>
        <div class="divider-custom-icon">
          <i class="fas fa-star"></i>
        </div>
        <div class="divider-custom-line"></div>
      </div>

      <!-- Masthead Subheading -->
      <a class="nav-link py-3 px-0 px-lg-3 rounded js-scroll-trigger" style="color:white;" href="#portfolio"><img class="masthead-avatar mb-5" src="img/bee_4.png" alt=""></a>

      <!-- <br> -->

            <!-- About Section Content -->
      <!-- <div class="row">
          
        <div class="col-lg-4 ml-auto">
          <h2>個性化投資組合</h2>
          <p class="lead">幾分鐘的問卷馬上為你制定產品</p>
        </div>
        <div class="col-lg-4 mr-auto">
        <h2>線上投資</h2>
          <p class="lead">投資這點小事，手機即可搞定！</p>
        </div>
        <div class="col-lg-4 mr-auto">
        <h2>追蹤調整</h2>
          <p class="lead">依據數據分析重新平衡投資配置</p>
        </div>
      </div> -->
      


    </div>
  </header>

  <!-- Portfolio Section -->
  <section class="page-section portfolio" id="portfolio">
    <div class="container">

      <!-- Portfolio Section Heading -->
      <h2 class="page-section-heading text-center text-uppercase text-secondary mb-0">樂活退休</h2>

      <!-- Icon Divider -->
      <div class="divider-custom">
        <div class="divider-custom-line"></div>
        <div class="divider-custom-icon">
          <i class="fas fa-star"></i>
        </div>
        <div class="divider-custom-line"></div>
      </div>


      <!-- Portfolio Grid Items -->
      <form id = "info" action="模擬結果.php" method="post" name="info" class="fullwidth">

      <div class="row">

        <!-- Portfolio Item 1 -->
        <div class="col-md-6 col-lg-3">
          <br>
<!-- <div class="card text-center"  style = "background: #ccdcde"> -->
<div class="card text-center" style = "background: #007bff">
                                    <div class="stat-widget-two">
                                        <div class="stat-content">
                                            <!-- <div class="card bg-retired"  style = "background: #dae8e8"> -->
                                            <div class="card bg-retired" style = "background: #c0defc">
                                                <h3 class="card-title">1. 您現在幾歲 </h3>
                                                <!-- <div class="row p-l-10 p-r-10"> -->
                                                    <div class="col-xs-9" >
                                                      <!-- <div class="input-group mb-3"> -->
                                                        <div class="input-group" >
                                                            <input type="hidden" name="yourname" value="<?php print_r($yourname);?>"/>
                                                            <input type="hidden" name="password" value="<?php print_r($password);?>"/>
                                                            <input boundaryMsg="建議現在的年齡為18至70歲" placeholder="歲" class="form-control typeahead tt-input" id="age" max="70" min="18" name="age" type="number" value="" />
                                                            <!-- <span class="unitname">歲</span> -->

                                                        </div>
                                                        <!-- <div class="input-group-append">
                                                          <span class="input-group-text">歲</span>
                                                        </div> -->
                                                      <!-- </div> -->
                                                    </div>
                                                    
                                                <!-- </div> -->
                                                <p class="inputDesc">請設定您現在的年齡。建議現在的年齡為18至70歲<br></p>
                                                <div class="notification error closeable" id="ageMsg" style="display: none">
                                                    <p><span>Error!</span></p>
                                                    <a class="close"></a>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
        </div>

        <!-- Portfolio Item 2 -->
        <div class="col-md-6 col-lg-3">
        <br>
        <div class="card text-center" style = "background: #007bff">
                                    <div class="stat-widget-two">
                                        <div class="stat-content">
                                            <div class="card bg-retired" style = "background: #c0defc">
                                                <h3 class="card-title">2. 預計幾歲退休 </h3>
                                                <!-- <div class="row p-l-10 p-r-10"> -->
                                                    <div class="col-xs-9">
                                                        <div class="input-group">
                                                            <input boundaryMsg="建議退休的年齡為50至80歲" placeholder="歲" class="form-control typeahead tt-input" id="retireAge" max="80" min="50" name="retireAge" type="number" value="" />
                                                            <!-- <span class="unitname">歲</span> -->
                                                        </div>
                                                    </div>
                                                <!-- </div> -->
                                                <p class="inputDesc">依行政院主計處統計顯示，國人近五年平均退休年齡約56.3歲</p>
                                                <div class="notification error closeable" id="retireAgeMsg" style="display: none">
                                                    <p><span>Error!</span></p>
                                                    <a class="close"></a>
                                                </div>
                                            </div>    

                                        </div>
                                        
                                    </div>
                                </div>
        </div>

        <!-- Portfolio Item 3 -->
        <div class="col-md-6 col-lg-3">
        <br>
        <div class="card text-center" style = "background: #007bff">
                                    <div class="stat-widget-two">
                                        <div class="stat-content">
                                            <div class="card bg-retired" style = "background: #c0defc">
                                                <h3 class="card-title">3. 預計規劃到幾歲 </h3>
                                                <!-- <div class="row p-l-10 p-r-10"> -->
                                                    <div class="col-xs-9">
                                                        <div class="input-group">
                                                            <input boundaryMsg="建議規劃的年齡為50至100歲" placeholder="歲" class="form-control typeahead tt-input" id="expectAge" max="100" min="50" name="expectAge" type="number" value="" />
                                                            <!-- <span class="unitname">歲</span> -->
                                                        </div>
                                                    </div>
                                                    
                                                <!-- </div> -->
                                                <p class="inputDesc">依經建會推計，台灣男性平均預期壽命將達82歲，女性則為88歲。</p>
                                                <div class="notification error closeable" id="expectAgeMsg" style="display: none">
                                                    <p><span>Error!</span></p>
                                                    <a class="close"></a>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
        </div>

        <div class="col-md-6 col-lg-3">
          <br>
        <div class="card text-center" style = "background: #007bff">
                                    <div class="stat-widget-two">
                                        <div class="stat-content">
                                            <div class="card bg-retired" style = "background: #c0defc">
                                                <h3 class="card-title">4. 退休後每月花費 </h3>
                                                <!-- <div class="row p-l-10 p-r-10"> -->
                                                    <div class="col-xs-9">
                                                        <div class="input-group">
                                                            <input boundaryMsg="建議每月花費金額為1至100萬" placeholder="萬元" class="form-control typeahead tt-input" id="expenses" max="100" min="1" name="expenses" type="number" value="" />
                                                            <!-- <span class="unitname">萬元</span> -->
                                                        </div>
                                                    </div>
                                                    
                                                <!-- </div> -->
                                                <p class="inputDesc">建議先了解需要多少退休金，扣除勞保年金及勞工退休金後再試算</p>
                                                <div class="notification error closeable" id="expensesMsg" style="display: none">
                                                    <p><span>Error!</span></p>
                                                    <a class="close"></a>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
        </div>

        <!-- Portfolio Item 5 -->
        <div class="col-md-6 col-lg-3">
        <br>
        <div class="card text-center" style = "background: #007bff">
                                    <div class="stat-widget-two">
                                        <div class="stat-content">
                                            <div class="card bg-retired" style = "background: #c0defc">
                                                <h3 class="card-title">5. 每年投入金額</h3>
                                                <!-- <div class="row p-l-10 p-r-10"> -->
                                                    <div class="col-xs-9">
                                                        <div class="input-group">
                                                            <input boundaryMsg="建議每年投入金額為1至100萬" placeholder="萬元" class="form-control typeahead tt-input" id="in_per_year" max="100" min="1" name="in_per_year" type="number" value="" />
                                                            <!-- <span class="unitname">萬元</span> -->
                                                        </div>
                                                    </div>
                                                    
                                                <!-- </div> -->
                                                <p class="inputDesc">建議每月花費金額為1至100萬，請評估您自身負擔能力進行試算。<br> </p>
                                                <div class="notification error closeable" id="expensesMsg" style="display: none">
                                                    <p><span>Error!</span></p>
                                                    <a class="close"></a>
                                                </div>
                                            </div>    

                                        </div>
                                        
                                    </div>
                                </div>
        </div>

        
        

        

        <!-- Portfolio Item 6 -->
        <div class="col-md-6 col-lg-3">
        <br>
        <div class="card text-center" style = "background: #007bff">
                                    <div class="stat-widget-two">
                                        <div class="stat-content">
                                            <div class="card bg-retired" style = "background: #c0defc">
                                                <h3 class="card-title">6. 第一次投入金額 </h3><!-- 設定可承受之投資風險 -->
                                                <!-- <div class="row p-l-10 p-r-10"> -->
                                                    <div class="col-xs-9">
                                                        <div class="input-group">
                                                            <input boundaryMsg="投入金額為0~2000萬" placeholder="萬" class="form-control typeahead tt-input" id="risk" max="2000" min="0" name="risk" type="number" value="" />
                                                            <!-- <span class="unitname">級</span> -->
                                                        </div>
                                                    </div>
                                                    
                                                <!-- </div> -->
                                                <p class="inputDesc">
                                                <!-- <input class="risk-value" id="risk" name="risk" type="hidden" /> -->
                                                <!-- 風險分1~4級:保守型->1級, 穩健型->2級, 成長型->3級, 積極型->4級 -->
                                                第一次投入金額越多，越增加您的投資報酬率
                                                </p>
                                                <div class="notification error closeable" id="expectAgeMsg" style="display: none">
                                                    <p><span>Error!</span></p>
                                                    <a class="close"></a>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
        </div>

        <div class="col-md-6 col-lg-3">
        <br>
        <div class="card text-center" style = "background: #007bff">
                                    <div class="stat-widget-two">
                                        <div class="stat-content">
                                            <div class="card bg-retired" style = "background: #c0defc">
                                                <h3 class="card-title">7.資料時間長度 </h3><!-- 設定可承受之投資風險 -->
                                                <!-- <div class="row p-l-10 p-r-10"> -->
                                                    <div class="col-xs-9">
                                                        <div class="input-group">
                                                            <input boundaryMsg="資料長度為5年內" placeholder="年" class="form-control typeahead tt-input" id="want_calc" max="5" min="1" name="want_calc" type="number" value="" />
                                                            <!-- <span class="unitname">級</span> -->
                                                        </div>
                                                    </div>
                                                    
                                                <!-- </div> -->
                                                <p class="inputDesc">
                                                <!-- <input class="risk-value" id="risk" name="risk" type="hidden" /> -->
                                                <!-- 風險分1~4級:保守型->1級, 穩健型->2級, 成長型->3級, 積極型->4級 -->
                                                欲使用過去幾年的資料計算，<br>請輸入1~5之整數
                                                </p>
                                                <div class="notification error closeable" id="expectAgeMsg" style="display: none">
                                                    <p><span>Error!</span></p>
                                                    <a class="close"></a>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
        </div>

        <div class="col-md-6 col-lg-3">
        <br>
        <div class="card text-center" style = "background: #007bff">
                                    <div class="stat-widget-two">
                                        <div class="stat-content">
                                            <div class="card bg-retired" style = "background: #c0defc">
                                                <h3 class="card-title">8. 開始投資時間  </h3>
                                                <!-- <div class="row p-l-10 p-r-10"> -->
                                                    <div class="col-xs-9">
                                                        <div class="input-group">
                                                            <input class="form-control" id="want_see" name="want_see" type="date" value="" />
                                                            
                                                            <!-- <span class="unitname"> -->
                                                            <!-- <input  class="form-control" id="ymd" name="ymd" type="text" value="" /> -->
                                                              <!-- <input type="text" class="form-control" placeholder = '年/月/日' id="ymd" name="ymd" list="category" value="">
                                                              <datalist id="category">  
                                                                   <option value="年">
                                                                   <option value="月">
                                                                   <option value="日">
                                                              </datalist> -->
                                                            <!-- </span> -->
                                                        </div>
                                                        <!-- <div class="input-group">
                                                            <input boundaryMsg="建議規劃的年齡為60至100歲" placeholder="天" class="form-control typeahead tt-input" id="want_see" max="10000" min="0" name="want_see" type="number" value="" />
                                                            <span class="unitname">歲</span>
                                                        </div> -->
                                                    </div>
                                                    
                                                <!-- </div> -->
                                                <p class="inputDesc">設定欲開始投資日期，至多從2010開始</p>
                                                <div class="notification error closeable" id="expectAgeMsg" style="display: none">
                                                    <p><span>Error!</span></p>
                                                    <a class="close"></a>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
        </div>
        <!-- Portfolio Item 4 -->

      </div>
      <!-- /.row -->

    </div>
    <div class="text-center mt-4">
    <button type="button" class="btn btn-primary btn-xl" onclick="add()" >開始試算</button>
    <output class="btn btn-primary btn-xl" style = "background: #97CBFF" id="result">報酬率試算結果</output>
    </div>

    <div class="text-center mt-4">
    <button type="submit" class="btn btn-primary btn-xl" id="sendMessageButton">Send</button>
    </div>
    </form>
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
