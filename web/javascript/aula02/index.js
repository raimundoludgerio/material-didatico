<<<<<<< HEAD
console.log("Inicio")
alert("Exibindo uma mensagem")
console.log("Fim...")

console.log()

=======
>>>>>>> 36bc7ff2324cd2965ce1e3bbe3e5b39169b7b2e2
function funcaoBase(callback) {
    setTimeout(() => {
        callback();
    }, 2000);
};
funcaoBase(() => {
    console.log("Imprimindo algo na tela")
})
console.log("Início do processo...");
funcaoBase((argumento) => {
    console.log(argumento);
});
setTimeout(() => {
    console.log("Etapa 1 concluída");
    setTimeout(() => {
        console.log("Etapa 2 concluída");
        setTimeout(() => {
            console.log("Etapa 3 concluída");
            setTimeout(() => {
                console.log("Etapa 4 concluída");
                console.log("Processo finalizado.");
            }, 1000);
        }, 1000);
    }, 1000);
}, 1000);

console.log("Fechei")
