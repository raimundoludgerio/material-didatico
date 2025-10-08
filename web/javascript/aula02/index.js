console.log("Inicio")
alert("Exibindo uma mensagem")
console.log("Fim...")

function funcaoBase(callback) {
    setTimeout(() => {
        callback("Argumento passado...");
    }, 2000);
};

funcaoBase((argumento) => {
    console.log(argumento);
});
console.log("Início do processo...");
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

