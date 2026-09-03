const fs = require('fs');
const entrada = require('readline-sync');

console.log("=== SISTEMA DE CONSULTA DE ESTOQUE(Quantidade) ===\n");

try {
    const dadosTexto = fs.readFileSync('estoque.json', 'utf-8');
    const produtos = JSON.parse(dadosTexto);

    const termoBusca = entrada.question("Digite uma quantidade base para a listagem: ");

    const resultado = produtos.find(p => p.qtd <= termoBusca);

    if (resultado) {
        console.log("\n PRODUTOS DE VALOR SEMELHANTE OU ABAIXO:")
        const baixoEstoque = produtos.filter(p => p.qtd <= termoBusca);
        console.log(baixoEstoque);

    } else {
        console.log("\n Produtos não encontrados...");
    }
} catch(erro) {
    console.log("Erro ao acessar o banco de dados: " + erro.message);
}