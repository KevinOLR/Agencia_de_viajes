function incrementarNumeros() {
    const limiteExperiencia = 10;
    const limiteAventuras = 1000;
    const limiteClientes = 11000;

    let experiencia = 0;
    let aventuras = 0;
    let clientes = 0;

    const experienciaElement = document.getElementById("experiencia");
    const aventurasElement = document.getElementById("aventuras");
    const clientesElement = document.getElementById("clientes");

    const intervalo = setInterval(function () {
        experiencia++;
        aventuras += 100;
        clientes += 1100;
        experienciaElement.textContent = `+${experiencia} años de experiencia`;
        aventurasElement.textContent = `+${aventuras} aventuras planificadas`;
        clientesElement.textContent = `+${clientes} clientes felices`;
        if (experiencia >= limiteExperiencia && aventuras >= limiteAventuras && clientes >= limiteClientes) {
            clearInterval(intervalo);
        }
    }, 500);
}
//incremento
incrementarNumeros();
