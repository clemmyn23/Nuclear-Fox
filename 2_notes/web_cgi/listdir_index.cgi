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
        background: #dddddd;
    }
    </style>
</head>

<body>
    <!--[if lt IE 8]>
    <p class="browserupgrade">You are using an <strong>outdated</strong> browser. Please <a href="http://browsehappy.com/">upgrade your browser</a> to improve your experience.</p>
    <![endif]-->

    <div class="container">
        <div id="header">

eof
printf '<h1><strong>Index of %s</strong></h1>' "${PWD##*/}"

cat <<eof
        </div>
    </div>

    <div class="container">
        <div class="row">
            <div class="col-md-12">
                <div class="row">
                    <div class="col-lg-12">
                        <h5>
                            <span class="glyphicon glyphicon-folder-close"></span> &nbsp;<a href="../">../</a><br>
eof

for item in `ls | sort`; do
if [ -d $item -a -x $item ]; then
echo "<span class=\"glyphicon glyphicon-folder-close\"></span>&nbsp;<a href=\"$item/\">$item/</a><br>"
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

                </div>  <!-- end row -->
            </div>  <!-- end col-md-6 -->

        </div>  <!-- end row -->
    </div>  <!-- end container -->


    <!-- Scripts -->
    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>

    <!-- <script src="https://cdnjs.cloudflare.com/ajax/libs/trianglify/0.4.0/trianglify.min.js"></script>
-->

</body>
</html>
eof
