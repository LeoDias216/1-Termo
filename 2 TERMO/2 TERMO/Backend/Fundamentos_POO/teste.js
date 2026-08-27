// A classe, que define a estrutura da programação.
class Casa {
    // O constructor pega as informações quando uma nova casa é registrada e salva nas variáveis.
    constructor(numeroCasa, corCasa) {

        this.numero = numeroCasa
        this.cor = corCasa
        this.pronta = false
        // Os atributos definem o estado da casa, como qual o número dela, qual a cor e se a casa está pronta.
    }

    // Métodos são como funções, que alteram as variáveis existentes. São as ações e comportamentos do objeto.
    casaPronta() {
        this.pronta = true
        console.log(`A casa do numero ${this.numero} está finalizada e pronta para entrega!`)
    }

    definirCor(texto) {
        console.log(`O proprietario da casa de numero ${this.numero} definiu uma nova cor: "${texto}" `)
        this.cor = texto
        console.log(`A nova cor da casa ${this.numero} é ${this.cor}`)
    }
}

// Os objetos são os itens criados a partir do molde definido no "class". Para dar vida ao objeto e instancia-lo, usamos o "new".
const casa1 = new Casa("261", "Vermelha")
const casa2 = new Casa("12", "Laranja")

casa1.casaPronta()
casa2.definirCor("Azul")

console.log(casa1.pronta)
console.log(casa2.pronta)