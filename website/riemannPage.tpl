<html>
  <head>
    <title>MATH</title>
      
      <link rel="stylesheet" type="text/css" href="http://twitter.github.com/bootstrap/assets/css/bootstrap.css">
      <link rel = "stylesheet" type = "text/css" href = "/static/style.css" />
      <link rel = "shortcut icon" href = "/static/icon.png" />
      
      <meta http-equiv = "content-type" content = "text/html; charset=UTF-8">
    
      <script src = "http://code.jquery.com/jquery-latest.js"></script>

      <script type="text/javascript" src="http://latex.codecogs.com/latexit.js"></script>
      <script type = "text/javascript" src = "http://code.jquery.com/jquery-1.9.1.js"></script>
      <script type = "text/javascript" src = "jquery.touchSwipe.min.js"></script>
      <script type = "text/javascript" src = "/static/javaScripts.js"></script>
  </head>
  <body id="algebra1">
  <div class = "container">
   <div id = "sidebar">
      <ul class="navigation">
        <li><a href = "/"> Home </a></li>
        <li><a id="algebra"> Algebra </a>
          <ul class="childNav">
            <li><a href = "/factor/"> Factor </a></li>
            <li><a href = "/simplify/"> Simplify </a></li>
            <li><a href = "/solve/"> Solve </a></li>
          </ul>
        </li>
        <li><a id="calculusNav"> Calculus </a>
          <ul class="childNav">
            <li><a href = "/derivative/"> Derivatives </a></li>
            <li><a href = "/integral/"> Integration </a></li>
            <li><a href = "/maxmin/"> Maximum/Minimum </a></li>
            <li><a href = "/riemann/"> Riemann Sums </a></li>
            <li><a href = "/tangent/"> Tangent Line </a></li>
          </ul>
        </li>
        <li><a id="graphingNav"> Graphing </a>
          <ul class="childNav">
            <li><a href = "2DgraphingPage.html"> 2D Graphing </a></li>
            <li><a href = "3DgraphingPage.html"> 3D Graphing </a></li>
            <li><a href = "/holes/"> Holes </a></li>
            <li><a href = "/intersection/"> Intersection </a></li>
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
            {title}
            </h3>
            <form action="#.php">
              Equation:
              <br/>
              y = <input type="text" name="function" placeholder="x+2x">
              <br/>
              Lower Bound:
              <br/>
              <input type="number" step="any" name="start" class="no-step">
              <br/>
              Upper Bound:
              <input type="number" step="any" name="end" class="no-step">
              <br/>
              Number of Intervals:
              <input type="number" step="any" name="rekt" class="no-step">
              <br/>
              <div class="radio">
              Mode:
              <br/>
              <input type="radio" name="mode" value="left" id="left"><label for="left"><span></span>Left</label>
              <br/>
              <input type="radio" name="mode" value="middle" id="middle"><label for="middle"><span></span>Middle</label>
              <br/>
              <input type="radio" name="mode" value="right" id="right"><label for="right"><span></span>Right</label>
              <br/>
              <input type="radio" name="mode" value="trapezoid" id="trapezoid"><label for="trapezoid" checked><span></span>Trapezoid</label>
              </div>
              <br/>
               <button class = "btn"> Submit </button>
            </form>
            Answer: 
            <br>
            <div class=answer lang="latex">
            {{answer}}
            </div>
            <br/>
            <img src="/static/riemann.jpg" alt="Riemann Picture"/>
          </div>
        </div>
    </div>
  </body>
</html>