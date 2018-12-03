
function getinput() {
    var firstinput = document.getElementById("input").value.split(" ").map(Number)
    console.log(firstinput)
    return firstinput
}

function calculate() {
    getinputs = getinput()
    reduced = getinputs.reduce((a, b)=> a+b);
    console.log(reduced);
    document.getElementById("output").innerHTML = 'Result ' + reduced;
}