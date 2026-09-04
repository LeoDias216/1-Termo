// Criando a máquina de calcular média
// function calcularMedia(n1, n2) {
//     return (n1 + n2) / 2;
// }

// // Usando a máquina
// const resultado = calcularMedia(10, 8);
// const resultado1 = calcularMedia(25, 45);
// console.log(`A media calculada foi: ${resultado}`);
// console.log(`A 2° media calculada foi: ${resultado1}`);

// Com pergunta:
const entrada = require('readline-sync');


function calcularMedia(n1, n2) {
    return (n1 + n2) / 2;
}

let numero1 = entrada.questionFloat("Insira o primeiro valor da media: ")
let numero2 = entrada.questionFloat("Insira o segundo valor da media: ")
console.log(`A media calculada foi: ${calcularMedia(numero1, numero2)}`)
