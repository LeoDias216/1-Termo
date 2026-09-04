const fs = require('fs');

const maquinas = [
    { id: 1, nome: "Torno_CNC", horasUso: 1200 },
    { id: 2, nome: "Fresadora", horasUso: 800 },
    { id: 3, nome: "Prensa_Hidraulica", horasUso: 1500 },
    { id: 4, nome: "Corte_Laser", horasUso: 500 }
];

function salvarDados() {
    const dadosTexto = JSON.stringify(maquinas, null, 3);

    fs.writeFileSync('maquinas.json', dadosTexto);
    console.log("Dados salvos com sucesso no arquivo estoque.json!");
}

function listarMaquinasPerigosas() {
    console.log("Máquinas em Perigo!");

    const maquinasPerigosas = maquinas.filter(p => p.horasUso > 1000);
    console.log(maquinasPerigosas);

    const dadosTexto = JSON.stringify(maquinasPerigosas, null, 3);
    fs.writeFileSync('manutencao_urgente.json', dadosTexto);
    console.log("Máquinas perigosas salvas no arquivo manutencao_urgente.json!");
}

salvarDados();
listarMaquinasPerigosas();