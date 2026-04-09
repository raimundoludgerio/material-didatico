function compararValores() {
    const campoEmail = document.getElementById("campoEmail").value;
    const campoSenha = document.getElementById("campoSenha").value;
    const mensagemErro = document.createElement('div');
    document.getElementById("info").innerHTML = ""
    let statusClass = "";
    let statusName = ""
    if (campoEmail == "admin" && campoSenha == "admin") {
        statusClass = "alert-success"
        statusName = "Você conseguiu"
    } else {
        statusClass = "alert-danger"
        statusName = "Tente novamente"
    }

    mensagemErro.className = "alert " + statusClass;
    mensagemErro.setAttribute('role', 'alert');
    mensagemErro.textContent = statusName
    document.getElementById("info").appendChild(mensagemErro);
    
}


const nome = document.getElementById("campoSenha").value;
document.getElementById("info").innerHTML = `<h1> Testando o ${nome} </h1>`


document.getElementById("campoEmail").addEventListener("click", () => {
    alert("Deus ilumine nossas vidas")
});


