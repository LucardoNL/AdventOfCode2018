var getinput = () => document.getElementById("input").value
    .split(" ")
    .map(Number)

var calculate = () => {
    getinputs = getinput()
    reduced = getinputs.reduce((a, b)=> a+b)
    setresult (reduced)
}

// pattcalculate will repeat the frequency list untill a double value is found.
var pattcalculate = () => {
    let frequency = 0
    let pastfrequencies = []
    let found = 0
    let getinputs = getinput()
    let round = 200
    while (found < round ) {
        for (var value of getinputs) {
            frequency += value
            if (pastfrequencies.indexOf(frequency) > -1) {
                setresult("Found " + frequency)
                found = round
                break // Required to stop the search if found in middle of list
            }
            else {
                pastfrequencies.push(frequency)
                setresult("Not yet found " + frequency)
            }
        }
        found += 1
    }
}

var setresult = (result) => document.getElementById("output").innerHTML = result