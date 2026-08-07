const entrada = require('readline-sync');

console.log("- CLASSIFICADOR DE ATLETAS DE NATACAO MAGNUM OLIMPIC -");

const idade = entrada.questionInt("Qual a sua idade? ");

if (idade >= 1 && idade <= 4) {
    console.log("Você ainda é muito novo para participar :(");
}
else if (idade >= 5 && idade <= 10) {
    console.log("Sua classificação é Infantil");
} 
else if (idade >= 11 && idade <= 17) {
    console.log("Sua classificação é Juvenil");
} 
else if (idade >= 18 && idade <= 60) {
    console.log("Sua classificação é Adulto");
} 
else {
    console.log("Sua classificação é Sênior");
}