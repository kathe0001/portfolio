
document.getElementById("formulario").addEventListener("submit", function(event) {
  event.preventDefault();

  let nome = document.getElementById("nome").value;
  let idade = document.getElementById("idade").value;
  let sexo = document.getElementById("sexo").value;
  let pressao = document.getElementById("pressao").value;
  let temperatura = document.getElementById("temperatura").value;
  let frequencia = document.getElementById("frequencia").value;
  let saturacao = document.getElementById("saturacao").value;
  let evolucao = document.getElementById("evolucao").value;
  let medicamento = document.getElementById("medicamento").value;
  let dosagem = document.getElementById("dosagem").value;
  let horario = document.getElementById("horario").value;

  let resultado = `
  <ul class="list-group">
    <li class="list-group-item"><strong>Nome:</strong> ${nome}</li>
    <li class="list-group-item"><strong>Idade:</strong> ${idade}</li>
    <li class="list-group-item"><strong>Sexo:</strong> ${sexo}</li>
    <li class="list-group-item"><strong>Pressão:</strong> ${pressao}</li>
    <li class="list-group-item"><strong>Temperatura:</strong> ${temperatura}</li>
    <li class="list-group-item"><strong>Frequência:</strong> ${frequencia}</li>
    <li class="list-group-item"><strong>Saturação:</strong> ${saturacao}</li>
    <li class="list-group-item"><strong>Evolução:</strong> ${evolucao}</li>
    <li class="list-group-item"><strong>Medicamento:</strong> ${medicamento}</li>
    <li class="list-group-item"><strong>Dosagem:</strong> ${dosagem}</li>
    <li class="list-group-item"><strong>Horário:</strong> ${horario}</li>
  </ul>
  `;

  let caixa = document.getElementById("caixa");
  caixa.querySelector(".card-body").innerHTML = resultado;
  caixa.classList.remove("d-none");

  let toast = new bootstrap.Toast(document.getElementById('toastSucesso'));
  toast.show();

  document.getElementById("formulario").reset();
});
