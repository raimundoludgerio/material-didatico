(function(){
    console.log("Mensagem da função")
})

function mensagem(){
    console.log("Mensgem")
}
mensagem();
console.log("TESTANDOOO")
window.alert("Bom dia!!")
let nome = window.prompt("NOME: ")
!nome ?
    window.prompt("Informe alguma coisa: ") : 
    console.log("Não passou")
const elemento_p = document.getElementById("resultado")
console.log(elemento_p)
elemento_p.style.fontSize = "2.5rem"
elemento_p.style.background = "red"
elemento_p.style.fontSize = "font-weight: bold;"
elemento_p.innerHTML = nome

let numero = 50
let numero2 = "50"
if(numero != numero2) console.log("É DIFERENTE")
else console.log("NÃO É")
