const entrada = require(`readline-sync`)

console.log(" GERADOR DE PARCELAS - PREÇO DE FERRAMENTAS ");

const valorTotal = entrada.questionFloat("Qual o preco da ferramenta que deseja comprar? ")
const qtdParcelas = entrada.questionInt("Quer parcelar em quantas vezes(max 12)? ")

for (let i = 0; i < qtdParcelas; i++) {
    console.log(`Parcela ${i + 1}: R$ ${(valorTotal / qtdParcelas).toFixed(2)}`)
}
