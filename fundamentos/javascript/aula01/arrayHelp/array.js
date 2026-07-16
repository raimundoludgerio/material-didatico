const pessoas = [
    { nome: "Alice", idade: 18, cidade: "São Paulo" },
    { nome: "Bruno", idade: 14, cidade: "Rio de Janeiro" },
    { nome: "Carla", idade: 12, cidade: "Belo Horizonte" },
    { nome: "Diego", idade: 20, cidade: "Curitiba" },
    { nome: "Eduarda", idade: 19, cidade: "Porto Alegre" },
    { nome: "Fábio", idade: 32, cidade: "Recife" },
    { nome: "Gabriela", idade: 37, cidade: "Fortaleza" },
    { nome: "Henrique", idade: 15, cidade: "Manaus" },
    { nome: "Isabela", idade: 43, cidade: "Salvador" },
    { nome: "João", idade: 77, cidade: "Brasília" }
];

const nome_pessoas = pessoas.map(pessoa => pessoa.nome);
console.log(nome_pessoas);

const pessoas_de_jampa = pessoas.filter(function (p) {
    return p.cidade == "João Pessoa"
});

// contando quantas pessoas tem em cada cidade
const resultado = pessoas.reduce((contador, pessoa) => {
    if(!contador[pessoa.cidade]){
        contador[pessoa.cidade] = 0;
    }
    contador[pessoa.cidade]++;
    return contador
},{});
console.log(resultado)





pessoas.forEach((pessoa, indice) => console.log(`${pessoa.nome} - ${indice}`))

// const comecaComA = pessoas.every(pessoa => pessoa.nome.charAt(0).toUpperCase() === "A");

const comecaComA = pessoas.every(function (pessoa) {
    return pessoa.nome.charAt(0).toUpperCase() === "A";
});
// console.log(comecaComA) // false



let maioridade = pessoas.find(function (pessoa) {
    return pessoa.idade >= 18;
})
// console.log(maioridade)

// for (p of pessoas) {
//     console.log(p["nome"]);
//     console.log(p.idade)
// }

let pessoas_mais_20 = []
for (p of pessoas) {
    if (p.idade >= 20) pessoas_mais_20.push(p)
}
// for (p of pessoas_mais_20) {
//     console.log(p)
// }

