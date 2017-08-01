#!/bin/sh

cat <<eof
Content-type: text/html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="Clemm's page on cse">
    <meta name="author" content="Clement Ng">
    <title>KAWAII NEKO</title>

    <!-- Bootstrap -->
    <link href="https://maxcdn.bootstrapcdn.com/bootswatch/3.3.6/paper/bootstrap.min.css" rel="stylesheet" integrity="sha384-2mX2PSpkRSXLQzmNzH3gwK6srb06+OfbDlYjbog8LQuALYJjuQ3+Yzy2JIWNV9rW" crossorigin="anonymous">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.5.0/css/font-awesome.min.css">

    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
    <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
    <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->

    <!-- THIS SITE IS CREATED USING BOOTSTRAP AND GLYPHICONS -->
    <!-- *links here that go to bootstrap and glyphicons* -->

    <style>
    body {
        background: #fff; /* For browsers that do not support gradients */
        background: -webkit-radial-gradient(#fff, #ddd); /* Safari 5.1 to 6.0 */
        background: -o-radial-gradient(#fff, #ddd); /* For Opera 11.6 to 12.0 */
        background: -moz-radial-gradient(#fff, #ddd); /* For Firefox 3.6 to 15 */
        background: radial-gradient(#fff, #ddd); /* Standard syntax (must be last) */
    }
    </style>
</head>

<body>
    <!--[if lt IE 8]>
    <p class="browserupgrade">You are using an <strong>outdated</strong> browser. Please <a href="http://browsehappy.com/">upgrade your browser</a> to improve your experience.</p>
    <![endif]-->

    <div class="container">
        <div id="header">
            <h1><strong>CATS ARE VERY CUTE</strong></h1>
            <h4>z5015618 -- <a href="http://clemm.me/">Clement Ng</a></h4>
        </div>
    </div>

    <div class="container">
        <div class="row">
            <div class="col-md-6">
                <img class="img-responsive" src="neko.jpg" alt="KAWAII IS JUSTICE" style="box-shadow: 5px 5px 5px #aaa">
            </div>

            <div class="col-md-6">
                <div class="row">
                    <div class="col-lg-6">
                        <h4><strong>MY STUFF (use http):</strong></h4>
                        <h5>
eof

# # # # # #
# echo "<span class=\"glyphicon glyphicon-folder-close\"></span>&nbsp;<a href=\"_careers\">_careers/</a><br>"

for item in `ls | sort`; do
    if [ -d $item -a -x $item ]; then
        if ! [[ $item =~ '_careers' ]]; then
            echo "<span class=\"glyphicon glyphicon-folder-close\"></span>&nbsp;<a href=\"$item\">$item/</a><br>"
        fi
    fi
done

for item in `ls | sort`; do
    if [ -x $item -a ! -d $item ]; then
        if ! [[ $item =~ 'index.cgi' ]]; then
            echo "<span class=\"glyphicon glyphicon-file\"></span>&nbsp;<a href=\"$item\">$item</a><br>"
        fi
    fi
done

cat <<eof
                        </h5>
                    </div>
                    <div class="col-lg-6">
                        <h4><strong>MY&nbsp;OTHER&nbsp;COOL&nbsp;STUFF:</strong></h4>
                        <h5>
                            <span class="glyphicon glyphicon-star"></span>&nbsp;<a href="http://clemm.me">My other website</a><br>
                            <span class="glyphicon glyphicon-star"></span>&nbsp;<a href="http://github.com/clemmyn23">My Github</a><br>
                        </h5>
                    </div>  <!-- end col-lg-6 -->

                </div>  <!-- end row -->
            </div>  <!-- end col-md-6 -->

        </div>  <!-- end row -->
    </div>  <!-- end container -->

    <!-- FOOTER START -->
    <footer class="docs-footer">
        <div class="container">
            <div class="row">
                <div class="col-md-12">
                    <p></p>
                    BUILT WITH LOVE USING BOOTSTRAP AND LOTS OF COFFEE. 2016

                </div> <!-- end col-md-12 -->
            </div> <!-- end row -->
        </div> <!-- end containter -->
    </footer>
    <!-- FOOTER END -->

    <!-- Scripts -->
    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>

    <!-- <script src="https://cdnjs.cloudflare.com/ajax/libs/trianglify/0.4.0/trianglify.min.js"></script>-->

</body>
</html>
eof
