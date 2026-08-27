const entrada = require('readline-sync');

console.log("- SISTEMA DE EMPRESTIMOS MAGNUM BANK -");

const renda = entrada.questionFloat("Qual a sua renda mensal? ");
const nome = entrada.keyInYNStrict("Seu nome esta limpo? ");

if (renda >= 2000 && nome === true) {
    console.log("Empréstimo Aprovado");
}
else {
    console.log("Empréstimo Negado");
}