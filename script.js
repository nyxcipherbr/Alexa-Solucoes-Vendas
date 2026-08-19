// Sistema de vendas - Alexa Soluções

const botoes = document.querySelectorAll("button");

botoes[0].addEventListener("click", function () {
    mostrarProvedores();
});

botoes[1].addEventListener("click", function () {
    alert("Em breve você poderá escolher seu plano de Internet Móvel.");
});

function mostrarProvedores() {
    const area = document.createElement("div");

    area.innerHTML = `
        <h2>Escolha seu provedor</h2>

        <button onclick="selecionarProvedor('Nio')">Nio</button>
        <button onclick="selecionarProvedor('Amigo')">Amigo</button>
        <button onclick="selecionarProvedor('Vivo')">Vivo</button>
        <button onclick="selecionarProvedor('Pedranet')">Pedranet</button>
        <button onclick="selecionarProvedor('Claro')">Claro</button>
        <button onclick="selecionarProvedor('TIM')">TIM</button>
    `;

    document.body.appendChild(area);
}

function selecionarProvedor(provedor) {
    alert("Você escolheu o provedor: " + provedor);
}
