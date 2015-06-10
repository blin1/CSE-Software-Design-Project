<html>
  <head>
    <title>MATH</title>
      
      <link rel = "stylesheet" type = "text/css" href = "style.css" />
      <link rel = "shortcut icon" href = "icon.png" />
      
    <meta http-equiv = "content-type" content = "text/html; charset=UTF-8">
    
    <script src = "http://code.jquery.com/jquery-latest.js"></script>

      <script type="text/javascript" src="http://latex.codecogs.com/latexit.js"></script>
      <script type = "text/javascript" src = "http://code.jquery.com/jquery-1.9.1.js"></script>
      <script type = "text/javascript" src = "jquery.touchSwipe.min.js"></script>
      <script type = "text/javascript" src = "javaScripts.js"></script>
  </head>
  <body id="algebra1">
  <div class = "container">
   <div id = "sidebar">
      <ul class="navigation">
        <li><a href = "homePage.html"> Home </a></li>
        <li><a id="algebra"> Algebra </a>
          <ul class="childNav">
            <li><a href = "factorPage.html"> Factor </a></li>
            <li><a href = "solvePage.html"> Solve </a></li>
            <li><a href = "simplifyPage.html"> Simplify </a></li>
          </ul>
        </li>
        <li><a id="calculusNav"> Calculus </a>
          <ul class="childNav">
            <li><a href = "riemannPage.html"> Riemann Sums </a></li>
            <li><a href = "integralPage.html"> Integration </a></li>
            <li><a href = "derivativePage.html"> Derivatives </a></li>
            <li><a href = "tagentPage.html"> Tangent Line </a></li>
            <li><a href = "maxminPage.html"> Maximum/Minimum </a></li>
          </ul>
        </li>
        <li><a id="graphingNav"> Graphing </a>
          <ul class="childNav">
            <li><a href = "2DgraphingPage.html"> 2D Graphing </a></li>
            <li><a href = "3DgraphingPage.html"> 3D Graphing </a></li>
            <li><a href = "intersectionPage.html"> Intersection </a></li>
            <li><a href = "holePage.html"> Hole/Asymptote </a></li>
          </ul>
        </li>
        <li><a id="dataNav"> Data Analysis </a></li>
        <li><a href = "helpPage.html" id="helpNav"> Help </a></li>
        <li><a href = "programPage.html" id="programNav"> Program Info </a></li>
      </ul>
    </div>
			<div class = "main-content">
				<div class = "swipe-area"></div>
				<a href = "#" data-toggle = ".container" id = "sidebar-toggle">
					<span class = "bar"></span>
					<span class = "bar"></span>					
          <span class = "bar"></span>
				</a>
				<div class="content" id="pages">
          <div id="function">
            <h3>
            {{title}}
            </h3>
            <form action="#.php">
              Data Set 1:
              <br/>
              <input type="text" name="data1" placeholder="1, 2, 3">
              <br/>
              Data Set 2/Expected Mean:
              <br/>
              <input type="text" name="data2" placeholder="1, 2, 3">
              <br/>
              Independent/Dependent:
              <div class="radio">
              <input type="radio" name="mode" value="independ" id="independ" checked><label for="independ"><span></span>Independent</label>
              <br/>
              <input type="radio" name="mode" value="depend" id="depend"><label for="depend"><span></span>Dependent</label>
              </div>
              <br/>
              Tail:
              <div class="radio">
              <input type="radio" name="tails" value="one" id="onetailed" checked><label for="onetailed"><span></span>One-Tailed</label>
              <br/>
              <input type="radio" name="tails" value="two" id="twotailed"><label for="twotailed"><span></span>Two-Tailed</label>
              </div>
              <br/>
              <input type="submit" value="Submit">
            </form>
            Answer: 
            <br>
            <div class=answer lang="latex">
            {{answer}}
            </div>
    			</div>
        </div>
		</div>
	</body>
</html>