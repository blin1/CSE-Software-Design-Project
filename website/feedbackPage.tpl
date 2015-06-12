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
        <li><a id="helpNav"> Help </a>
          <ul class="childNav">
          <li><a href = "/program/"> Program Documentation </a></li>
          <li><a href = "/feedback/"> Feedback </a></li>
      </ul>
    </li>
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
            <form action="MAILTO:blin@ctemc.org" method="post" enctype="text/plain">
              Name:
                <input type="text" name="name" value="yourname" placeholder="Name">
              <br/>
              Email:
               <input type="text" name="mail" value="youremail" placeholder="Email">
               <br/>
               Comment:
               <input type="text" name="comment" value="yourcomment" placeholder="Comment" size="100">
               <br/>
               <button class = "btn"> Submit </button>
               <br/><br/>
               <input type="reset" value="Reset">
            </form>
          </div>
        </div>
    </div>
    </html>