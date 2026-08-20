function calcularBase(distanciaRecebida) {
    const freteTotal = distanciaRecebida * 2.10
    return freteTotal
}

function calcularSeguro(valorCarga) {
    return valorCarga * 0.01
}

function verificarPrazo(distanciaRecebida) {
    if (distanciaRecebida < 100) {
        return "1 dia util"
    } else {
        return "3 a 5 dias uteis"
    }
}

module.exports = {
    calcularBase,
    calcularSeguro,
    verificarPrazo
}
