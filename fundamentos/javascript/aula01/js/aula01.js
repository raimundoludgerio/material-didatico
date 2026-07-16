function multiplicacao(num1, num2) {
    let result = num1 * num2;
    return result;
}

function multiplicacaoOpc(num1 = 0, num2 = 1) {
    let result = num1 * num2;
    return result;
}

const minhaFun = function (numero) {
    return numero * 3
}

let array = [];
(function(){
    return "olá"
})()
const funAnonima = num => num * 2
function funcaoTest(num){
    return num * 2;
}
console.log(funAnonima(8))

for (let i = 0; i < 5; i++) {
    console.log("Número: " + i);
}

let contador = 0;
while (contador < 3) {
    console.log("Repetição " + contador);
    contador++;
}

let i = 0;
do {
    console.log("Número:", i);
    i++;
} while (i < 5);

const dobro = x => x * 2;
console.log(dobro(5));

(function () {
    console.log('Esta função executa imediatamente!');
})();


// Com parâmetros
(function (mensagem) {
    console.log(mensagem);
})('Hello World!');

array.map(function (item) {
    return item * 2;
})


console.log(minhaFun(8))


