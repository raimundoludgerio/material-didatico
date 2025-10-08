// carregando usuários de uma API externa (exemplo)
// const usuariosPromise = fetch(
//     "https://raw.githubusercontent.com/raimundoludgerio/material-didatico/refs/heads/main/web/javascript/aula02/usuarios",
// );

// usuariosPromise.then(response => {
//     // Caso de sucesso (resolve)
//     console.log(response.status);
// }).catch(error => {
//     // Caso de sucesso (reject)
//     console.log(error);
// }).finally(() => {
//     // Executa sempre
//     console.log("operação finalizada, mesmo se der erro ou não");
// });


// const minhaPromise = (usuario, senha) => new Promise((resolve, reject) => {
//     setTimeout(() => {
//         if (usuario === "admin" && senha === "1234") {
//             resolve("Login bem-sucedido!");
//         } else {
//             reject("Usuário ou senha incorretos.");
//         }
//     }, 2000); // 2 segundos de "atraso"
// });
// const promiseCarregandoUsuarios = new Promise((resolve, reject) => {
//     setTimeout(() => {
//         const numero = Math.floor(Math.random() * 10)
//         const sucesso = numero >= 5;
//         if (sucesso) resolve("Usuários carregdos - " + numero);
//         else reject("Erro ao carregar os usuários - " + numero);
//     }, 2000);
// });

// promiseCarregandoUsuarios.then(resultado => {
//     console.log("Deu certo: " + resultado);
// }).catch(falha => {
//     console.log("Não deu certo: " + falha);
// });



const promise1 = Promise.resolve(3);
const promise2 = 42; // Valor não-promise é convertido
const promise3 = new Promise((resolve) => {
    setTimeout(resolve, 1000, "foo");
});

// Promise.all([promise1, promise2, promise3])
//     .then((valores) => {
//         console.log(valores); // [3, 42, "foo"] após 1 segundo
//     })
//     .catch(erro => {
//         console.error("Uma das promises falhou:", erro);
//     });

const promiseRapida = new Promise(resolve => setTimeout(resolve, 1000, "Rápida"));
const promiseLenta = new Promise(resolve => setTimeout(resolve, 3000, "Lenta"));

Promise.race([promiseRapida, promiseLenta])
    .then(vencedora => {
        console.log(vencedora); // "Rápida" (após 1s)
    });