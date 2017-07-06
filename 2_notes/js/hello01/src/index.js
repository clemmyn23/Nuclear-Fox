function main() {
    return "test";
};

function printer(arg1) {
    document.write(arg1)
};

// buried document.write call
printer(main() + " 1");
document.write("</br>");

// simple function call
document.write(main() + " 1");
document.write("</br>");

// assigning anon function to variable (inline functions)
var x = function () {return "test 3"};
document.write(x());
document.write("</br>");

// self-involking anon function
// syntax:    ( function(){ /* definitions */ } )()
document.write( (function(){return "test 4"})() )
document.write("</br>")
