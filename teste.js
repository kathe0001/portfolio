function mensagem(){
const mensagem = document.getElementById("mensagem");
const CupomDigitado =("diadecomprar");
const Cupom = document.getElementById("Cupom").value;
const bot= document.getElementById("botao");
if(Cupom == CupomDigitado){

mensagem.innerHTML = "Cupom válido"


  }
else{

mensagem.innerHTML="Cupom inválido"
}
    
  }