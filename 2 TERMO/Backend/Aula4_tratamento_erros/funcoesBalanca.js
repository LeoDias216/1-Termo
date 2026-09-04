function verificarPeso(leitura) {
    const peso = Number(leitura)

    if (isNaN(peso)) {
        throw new Error("Entrada Invalida! Digite apenas numeros")
    }

    if (100 < peso && peso < 500) {
        return (`Peca aprovada com ${peso}g.`)
    } else {
        throw new Error("Peso fora do padrão (100g - 500g)! Peça descartada.")
    }
}

module.exports = {
    verificarPeso
}