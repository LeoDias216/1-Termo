const entrada = require('readline-sync');

console.log("- SISTEMA DE VOTOS MAGNUM ENTERPRISES -");

const ano = entrada.questionInt("Em que ano voce nasceu? ");

if ((2026 - ano) >= 16) {
    console.log(`\nVocê ja pode votar, que belo feito!`);
} else {
    console.log(`\nAinda nao e sua hora de votar :(`);
}
