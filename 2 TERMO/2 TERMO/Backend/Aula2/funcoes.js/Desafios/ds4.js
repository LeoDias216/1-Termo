const entrada = require('readline-sync') 

const cinema = [
    { titulo: "Moana Live Action", censura: 10},
    { titulo: "Indiana Jones", censura: 14},
    { titulo: "Resident Evil", censura: 18}
];
const idadeUser = entrada.questionInt("Qual a sua idade? ")
for (let i = 0; i < cinema.length; i++) {
    if (idadeUser >= cinema[i].censura) {
        console.log(`Pode ver: ${cinema[i].titulo}`);
    }
}