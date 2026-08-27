const entrada = require('readline-sync');

console.log("-- SISTEMA DE VERIFICAÇÃO DE APOSENTADORIA --");

const nome = entrada.question("Nome: ");
const idade = entrada.questionInt("Idade: ");
const contrib = entrada.questionInt("Tempo de Contribuicao(anos): ");

if (idade >= 65 || contrib >= 30) {
    console.log(`\n${nome}, você ja pode se aposentar!`);
} else {
    console.log(`\nSinto muito, ${nome}, sua aposentadoria não sera possível`);
}
