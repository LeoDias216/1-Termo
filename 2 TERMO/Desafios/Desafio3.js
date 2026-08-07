const entrada = require('readline-sync');

console.log("- SISTEMA DE ABASTECIMENTO MAGNUM VEHICLES");

const gasolina = entrada.questionFloat("Qual o preco atual do litro da gasolina? ");
const alcool = entrada.questionFloat("Qual o preco atual  litro do alcool? ");

if ((alcool / gasolina) >= 0.7) {
    console.log("Abasteca com gasolina parceiro");
} else {
    console.log("Abasteca com alcool parça");
}