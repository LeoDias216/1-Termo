const entrada = require('readline-sync')
const balanca = require('./funcoesBalanca')

while (peso != "sair") {
    try {
        console.log("Bem-vindo a Balanca Virtual de pecas!")
        const peso = entrada.questionFloat("Insira o peso da sua peca: ")

        if (peso.toLowerCase() === 'sair') break;
        
        const resultadoFinal = balanca.verificarPeso(peso)

        console.log(`O peso consultado foi: ${resultadoFinal}`)
    }
    catch {
        console.log(`⚠️ ALERTA: ${Erro.mensansagen}`)
    }
}