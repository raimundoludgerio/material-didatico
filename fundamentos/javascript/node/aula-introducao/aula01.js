console.log("Hello, world!")
import lib, {recuperarUsuariosVazios} from "./lib";

lib()

usuario = {
    nome: "Maria",
    idade: 30,
    email: "maria@teste.com"
}

let { nome, idade, email } = usuario;

console.log(nome);

recuperarUsuarios.recuperarUsuarios().forEach(usuario => {
    console.log(usuario);
});