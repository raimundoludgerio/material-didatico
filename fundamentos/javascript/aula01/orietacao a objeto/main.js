import Pessoa, { Gerente } from "./Pessoa.js";

var p1 = new Pessoa();
p1.idade = 37;
p1.nome = "Maria";
p1.apresentar();


const estudante = {
    matricula: 123,
    nome: "Maylson",
    endereco: {
        rua: "BR-230",
        bairro: "Tibiri",
        numero: 0
    },
    efetuarMatricula: () => {
        console.log("Estudante efetuou a matricula");
    }
}


console.log(estudante[nome])

const { nome, endereco, efetuarMatricula } = estudante
const {numero} = endereco
console.log(estudante.endereco.numero)
console.log(numero)

var pessoa = {
    nome: ["Bob", "Smith"],
    idade: 32,
    sexo: "masculino",
    interesses: ["música", "esquiar"],
    bio: function () {
        alert(
            this.nome[0] +
            " " +
            this.nome[1] +
            " tem " +
            this.idade +
            " anos de idade. Ele gosta de " +
            this.interesses[0] +
            " e " +
            this.interesses[1] +
            ".",
        );
    },
    saudacao: function () {
        alert("Oi! Eu sou " + this.nome[0] + ".");
    },
};

console.log(null || "valor padrão"); // "valor padrão"
console.log("texto" && 123);         // 123
console.log(0 && "oi");              // 0 (false)
console.log(!0);                     // true


pessoa.nome || pessoa["nome"];
pessoa.nome[0];
pessoa.idade;
pessoa.interesses[1];
pessoa.bio();
pessoa.saudacao();