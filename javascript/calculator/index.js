const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('Enter A Number? ', function (numberOne) {
    
    rl.question('Enter Operation ? ', function (operation) {
      
        rl.question('Enter Another Number ? ', function (numberTwo) {
           
            let result;
            switch (operation) {
                case "+":
                    result = add(numberOne, numberTwo);
                    break;
                case "-":
                    result = subtract(numberOne, numberTwo);
                    break;
                case "/":
                    result = divide(numberOne, numberTwo);
                    break;
                case "*":
                    result = multiply(numberOne, numberTwo);
                    break;
            
                default:
                    result = "Error Choose between + ,- ,/ ,*";
                    break;
            }

            console.log(result);


            rl.close();
      
        });
    });
    
});


rl.on('close', function () {
  process.exit(0);
});

function add(numberOne, numberTwo) {
    return parseInt(numberOne) + parseInt(numberTwo)
}

function subtract(numberOne, numberTwo) {
    return numberOne - numberTwo
}

function divide(numberOne, numberTwo) {
    return numberOne / numberTwo
}

function multiply(numberOne, numberTwo) {
    return numberOne * numberTwo
}