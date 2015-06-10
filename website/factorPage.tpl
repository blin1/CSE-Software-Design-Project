<html>
	<head>
		<title>MATH</title>
		
		<meta http-equiv="content-type" content="text/html; charset=UTF-8">
    <link rel="stylesheet" type="text/css" href="http://twitter.github.com/bootstrap/assets/css/bootstrap.css">
		<script type="text/javascript" src="http://code.jquery.com/jquery-1.9.1.js"></script>
    <style type='text/css'>
        body, html {
        height: 100%;
        margin: 0;
        overflow:hidden;
        font-family: Helvetica Neue, Helvetica, Arial, sans-serif;
        font-weight: 100;
      }

      .container {
          position: relative;
          height: 100%;
          width: 100%;
          left: 0;
          -webkit-transition:  left 0.5s ease-in-out;
          -moz-transition:  left 0.5s ease-in-out;
          -ms-transition:  left 0.5s ease-in-out;
          -o-transition:  left 0.5s ease-in-out;
          transition:  left 0.5s ease-in-out;
      }

      .container.open-sidebar {
        left: 250px;
      }

      .swipe-area {
        position: absolute;
        width: 50px;
        left: 0;
          top: 0;
        height: 100%;
        background: #f3f3f3;
        z-index: 0;
      }

      #sidebar {
        background: #DF314D;
        position: absolute;
        width: 250px;
        height: 100%;
        left: -250px;
        box-sizing: border-box;
        -moz-box-sizing: border-box;
      }

      #sidebar ul {
        margin: 0;
        padding: 0;
        list-style: none;
      }

      #sidebar ul li {
        margin: 0;
      }

      #sidebar ul li a {
        padding: 15px 20px;
        font-size: 16px;
        color: white;
        text-decoration: none;
        display: block;
        border-bottom: 1px solid #C9223D;
      }

      #sidebar ul li ul {
        display: none;
      }

      #sidebar ul li:hover ul {
        padding: 15px 20px;
        font-size: 16px;
        color: white;
        text-decoration: none;
        display: block;
      }

      .main-content {
        width: 100%;
        height: 100%;
        padding: 10px;
        box-sizing: border-box;
        -moz-box-sizing: border-box;
        position: relative;
        background-color: #DF314D;
        padding-right: 200px;
      }

      .main-content .content{
        box-sizing: border-box;
        -moz-box-sizing: border-box;
        padding-left: 50px;
        width: 100%;
        vertical-align: center;
        text-align: center;
      }


      .main-content .content h1{
        font-weight: 100;
        color: white;
        font-size: 75pt;
        font-weight: bolder;
        font-family: Georgia; Helvetica Neue, Helvetica, Arial, sans-serif;
        text-align: center;
      }

      .main-content .content h2{
        color: white;
        font-size: 60pt;
        font-weight: bold;
        font-family: Helvetica Neue, Helvetica, Arial, sans-serif;
        text-align: center;
      }

      .main-content .content p{
        width: 100%;
        line-height: 150%;
      }

      .main-content .content{
        font-family:  Helvetica Neue, Helvetica, Arial, sans-serif;
        font-size: 16pt;
        color: white;
        line-height: 64pt;
      }
      .main-content .content input[type=submit] {
        -moz-box-shadow:inset 0px 1px 0px 0px #ffffff;
        -webkit-box-shadow:inset 0px 1px 0px 0px #ffffff;
        box-shadow:inset 0px 1px 0px 0px #ffffff;
        background:-webkit-gradient(linear, left top, left bottom, color-stop(0.05, #ffffff), color-stop(1, #f6f6f6));
        background:-moz-linear-gradient(top, #ffffff 5%, #f6f6f6 100%);
        background:-webkit-linear-gradient(top, #ffffff 5%, #f6f6f6 100%);
        background:-o-linear-gradient(top, #ffffff 5%, #f6f6f6 100%);
        background:-ms-linear-gradient(top, #ffffff 5%, #f6f6f6 100%);
        background:linear-gradient(to bottom, #ffffff 5%, #f6f6f6 100%);
        filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#ffffff', endColorstr='#f6f6f6',GradientType=0);
        background-color:#ffffff;
        -moz-border-radius:6px;
        -webkit-border-radius:6px;
        border-radius:6px;
        border:1px solid #dcdcdc;
        display:inline-block;
        cursor:pointer;
        color:#DF314D;
        font-size: 16pt;
        padding:6px 24px;
        text-decoration:none;
      }

      .main-content .content input[type=submit]:hover {
        background:-webkit-gradient(linear, left top, left bottom, color-stop(0.05, #f6f6f6), color-stop(1, #ffffff));
        background:-moz-linear-gradient(top, #f6f6f6 5%, #ffffff 100%);
        background:-webkit-linear-gradient(top, #f6f6f6 5%, #ffffff 100%);
        background:-o-linear-gradient(top, #f6f6f6 5%, #ffffff 100%);
        background:-ms-linear-gradient(top, #f6f6f6 5%, #ffffff 100%);
        background:linear-gradient(to bottom, #f6f6f6 5%, #ffffff 100%);
        filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#f6f6f6', endColorstr='#ffffff',GradientType=0);
        background-color:#f6f6f6;
      }

      .main-content .content input[type=submit]:active {
        position:relative;
        top:1px;
      }

      .main-content #sidebar-toggle {
        background: #DF314D;
        border-radius: 2px;
        display: block;
        position: relative;
        padding: 8px 5px;
        float: left;
      }
      .main-content #sidebar-toggle .bar {
        display: block;
        width: 18px;
        margin-bottom: 3px;
        height: 2px;
        background-color: #fff;
        border-radius: 1px;   
      }

      .main-content #sidebar-toggle .bar:last-child {
        margin-bottom: 0;   
      }

      #B {
        visibility: hidden;
      }

      #function {
        line-height: 16pt;
      }


      #nostep::-webkit-outer-spin-button, input[type=number]::-webkit-inner-spin-button {
        -webkit-appearance: none;
        margin: 0;
      }

      #no-step {
        -moz-appearance:textfield;
      }

      #bound {
        width: 50px;
      }
      </style>
      <script type="text/javascript">
        $(window).load(function(){
            $("[data-toggle]").click(function() {
              var toggle_el = $(this).data("toggle");
              $(toggle_el).toggleClass("open-sidebar");
            });
            $(".swipe-area").swipe({
              swipeStatus:function(event, phase, direction, distance, duration, fingers){
                if (phase=="move" && direction=="right") {
                  $(".container").addClass("open-sidebar");
                  return false;
                }
                if (phase=="move" && direction=="left") {
                  $(".container").removeClass("open-sidebar");
                  return false;
                }
              }
            }); 
          });

          function hideA(x) {
            if (x.checked) {
              document.getElementById("A").style.visibility="hidden";
              document.getElementById("B").style.visibility="visible";    
            }
          }

          function hideB(x) {
              if (x.checked) {
                document.getElementById("B").style.visibility="hidden";
                document.getElementById("A").style.visibility="visible";
              }
          }
        </script>

      
	</head>
	<body>
  <div class = "container">
    <div id = "sidebar">
      <ul>
        <li><a href = "/">Home</a></li>
        <li><a href = "#">Algebra</a>
          <ul>
            <li><a href = "/factor/"> Factor </a></li>
            <li><a href = "/solve/"> Solve </a></li>
            <li><a href = "/simplify/"> Simplify </a></li>
          </ul>
        </li>
        <li><a href = "#"> Calculus </a>
          <ul>
            <li><a href = "/riemann/"> Riemann Sums </a></li>
            <li><a href = "/integral/"> Integration </a></li>
            <li><a href = "/derivative/"> Derivatives </a></li>
            <li><a href = "/tangent/"> Tangent Line </a></li>
            <li><a href = "/maxmin/"> Maximum/Minimum </a></li>
          </ul>
        </li>
        <li><a href = "#"> Graphing </a>
          <ul>
            <li><a href = "/intersection/"> Intersection </a></li>
            <li><a href = "/arclen/"> Arc Length </a></li>
            <li><a href = "/holes/"> Discontinuities </a></li>
          </ul>
        </li>
        <li><a href = "#">Data Analysis</a></li>
        <li><a href = "#">Help</a></li>
        <li><a href = "#">Program Info</a></li>
      </ul>
    </div>
			<div class = "main-content">
				<div class = "swipe-area"></div>
				<a href = "#" data-toggle = ".container" id = "sidebar-toggle">
					<span class = "bar"></span>
					<span class = "bar"></span>
					<span class = "bar"></span>
				</a>
				<div class="content">
          <div id="function">
            <h1>
            {{title}}
            </h1>
            <br/>
            Input to be factored:
            <br/><br/>
            <form action="#.php">
              <div class="radio">
              <input type="radio" name="mode" value="number" onchange="hideB(this)" checked><label for="number">Number</label>
              <label for="expression"><input type="radio" name="mode" value="expression" onchange="hideA(this)">Expression</label>
              </div>
              <br/>
              <div id="A">
                <input type="number" step="any" name="number" id="no-step">
              </div>
              <div id="B">
                <input type="text" name="expression">
              </div>
              <br/>
              <button class = "btn"> Submit </button>
            </form>
    			</div>
          Answer: {{answer}}
        </div>
		</div>
	</body>
</html>