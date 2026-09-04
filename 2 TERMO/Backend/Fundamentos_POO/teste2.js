class Edificio {

    constructor(trabalhadorEdificio, funcaoEdificio, materialFeito) {

        this.trabalhador = trabalhadorEdificio
        this.funcao = funcaoEdificio
        this.material = materialFeito
        this.aberto = false
    }

    edificioAberto() {
        this.aberto = true
        console.log(`O edificio do ${this.trabalhador} esta aberto para ${this.funcao}`)
    }

    trocarMaterial() {
        if (this.material === "Tijolos") {
            console.log(`O edificio do ${this.trabalhador} e de Tijolos e esta seguro!`)
        } else {
            console.log(`ATENCAO! O edificio do ${this.trabalhador} deve ser reformado, de ${this.material} para tijolos, para a segurança da vila!`)
        }
    }
}

const edificio1 = new Edificio("Ferreiro", "Forjar equipamentos", "Tijolos")
const edificio2 = new Edificio("Alfaiate", "Costurar roupas", "Pedra")
const edificio3 = new Edificio("Prefeito", "Reunioes", "Tijolos")
const edificio4 = new Edificio("Mercador", "Venda de produtos", "Madeira")

edificio1.edificioAberto()
edificio3.edificioAberto()
edificio4.edificioAberto()

edificio1.trocarMaterial()
edificio2.trocarMaterial()
edificio3.trocarMaterial()
edificio4.trocarMaterial()