function VerificarPalavra() {
const palavras = ["sol, lua, estrela"];
const input = document.getElementById("palavra").value; 
const men = document.getElementById("mensagem");
let encontrado = false; 

for(let i = 0; i < palavras.length; i++){
if(input === palavras[i]){
encontrado = true;
men.innerHTML = "Você digitou uma palavra correta!";
}
}
if(!encontrado) {
  men.innerHTML = "Palavra não encontrada";  
}
}
<script>    
</script>