var getinput = () => document.getElementById("input").value
    .split(" ")
    .map(Number)

var calculate = () => {
    getinputs = getinput()
    reduced = getinputs.reduce((a, b)=> a+b)
    setresult (reduced)
}

var pattcalculate = () => {
    let frequency = 0
    let pastfrequencies = []
    let found = 0
    //while (found == 0) {
        for (var value of getinput()) {
            frequency += value
            if (pastfrequencies.indexOf(frequency) > -1) {
                setresult(frequency)
                found = 1
            }
            else {
                pastfrequencies.push(frequency)
                setresult("Not yet found")
            }
        }
    //}
}

var setresult = (result) => document.getElementById("output").innerHTML = result