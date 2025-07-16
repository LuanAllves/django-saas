function atualizarDataHora() {
    const dataHoraElemento = document.getElementById("current-time");
    const agora = new Date();
    const dataHoraFormatada = agora.toLocaleString('pt-BR'); // Formata para o padrão brasileiro
    dataHoraElemento.textContent = dataHoraFormatada;
}

// Chama a função imediatamente para exibir a data e hora ao carregar a página
atualizarDataHora();

// Atualiza a data e hora a cada segundo (1000 milissegundos)
setInterval(atualizarDataHora, 1000);