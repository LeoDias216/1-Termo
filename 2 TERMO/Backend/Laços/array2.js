const entrada = require('readline-sync');

console.log("=== SISTEMA DE CONTROLE DE QUALIDADE - PESAGEM ===");

// 1. Definição de variáveis
const pesos = []; // Array para guardar o histórico (dia 4)
let somaTotal = 0; // Acumulador (dia 3)

const qtdpecas = entrada.questionInt("Quantas pecas deseja avaliar? ");

// 2. Loop para coletar dados
for (let i = 0; i < qtdpecas; i++) {
    let peso = entrada.questionFloat(`Digite o peso da peca ${i + 1} (kg): `);

    pesos.push(peso); // Guarda no prédio/Array
    somaTotal += peso; // Soma no cofre/Acumulador
}

// 3. Cálculos
const media = somaTotal / qtdpecas;

// 4. Exibição do relatório

console.log("\n--- RELATÓRIO DE AUDITORIA ---");
console.log(`Pesos registrados: [${pesos.join(" kg | ")} kg ]`);
console.log(`Média de peso do lote: ${media.toFixed(2)} kg `);

// 5. Decisão (Lógica combinada da semana 2)
if (media >= 4.8 && media <= 5.2) {
    console.log("STATUS FINAL: LOTE APROVADO!");
} else {
    console.log("STATUS FINAL: LOTE REPROVADO! (fora do padrão)")
}