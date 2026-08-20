const entrada = require('readline-sync')

const calculadora = require('./calculadoraFrete');

console.log("-- SISTEMA DE CALCULO DE FRETE --");

const produto = entrada.question("Insira o nome do produto: ")
const distancia = entrada.questionInt("Distancia de Entrega(Km): ")
const carga = entrada.questionFloat("Valor da Carga: ");

const freteTotal = calculadora.calcularBase(distancia);
const seguroTotal = calculadora.calcularSeguro(carga);
const prazoFinal = calculadora.verificarPrazo(distancia);

console.log("\n--- RELATORIO FINAL ---");
console.log(`Nome do Produto: ${produto}`);
console.log(`Valor do Frete: R$ ${freteTotal}`)
console.log(`Taxa do Seguro: R$ ${seguroTotal}`)
console.log("=======================")
console.log(`Valor total: R$ ${(freteTotal + seguroTotal).toFixed(2)}`);
console.log(`Status da Entrega: ${prazoFinal}`);