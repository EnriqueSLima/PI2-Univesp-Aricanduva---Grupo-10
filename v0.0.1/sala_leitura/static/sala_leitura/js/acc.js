let fonteTamanho = 1; // Tamanho da fonte inicial (1 = normal)
let modoContrasteAtivo = false;

function ajustarFonte(acao) {
    const body = document.body;
    
    // Aumenta ou diminui o tamanho da fonte com base na ação
    if (acao === 'aumentar') {
        fonteTamanho += 0.1;
    } else if (acao === 'diminuir') {
        fonteTamanho -= 0.1;
    }

    // Aplica o novo tamanho de fonte
    body.style.fontSize = fonteTamanho + 'em';
}

function mudarContraste() {
    const body = document.body;
    
    // Alterna entre o modo normal e o de alto contraste
    if (modoContrasteAtivo) {
        body.classList.remove('alto-contraste');
    } else {
        body.classList.add('alto-contraste');
    }

    modoContrasteAtivo = !modoContrasteAtivo; // Alterna o estado do contraste
}
