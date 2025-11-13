console.log("Inicio")
alert("Exibindo uma mensagem")
console.log("Fim...")

console.log()

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
