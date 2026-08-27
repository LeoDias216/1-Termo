const entrada = require('readline-sync');

console.log(" - SISTEMA DE DESCONTO MAGNUS EAT - ");

const valor = entrada.questionInt("Qual o valor da sua conta no restaurante? ");

if (valor >= 100) {
    console.log(`\nVoce tera que pagar ${valor * 0.9} reais, com desconto`);
} else {
    console.log(`Voce tera que pagar ${valor}, sem desconto`);
}
