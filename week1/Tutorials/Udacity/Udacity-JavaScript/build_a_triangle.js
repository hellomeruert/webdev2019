/*
 * Programming Quiz: Build A Triangle (5-3)
 */

// creates a line of * for a given length
function makeLine(length) {
    var line = "";
    for (var j = 1; j <= length; j++) {
        line += "* ";
    }
    return line + "\n";
}
function buildTriangle(num){
    var str = "";
    for(var i = 1; i <= num; i++){
        str+= makeLine(i);
    }
    return str;
}
console.log(buildTriangle(10));