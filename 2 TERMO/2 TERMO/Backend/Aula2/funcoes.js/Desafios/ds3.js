const entrada = require(`readline-sync`)

console.log(" CALCULADOR DE AREA DE TERRENO ");


for (let i = 1; i < 4; i++) {
    const largura = entrada.questionFloat(`Informe a largura do terreno ${i}: `)
    const comprimento = entrada.questionFloat(`Informe o comprimento do terreno ${i}: `)
    console.log(`A area do terreno é ${(largura / comprimento).toFixed(2)}m²`)
}