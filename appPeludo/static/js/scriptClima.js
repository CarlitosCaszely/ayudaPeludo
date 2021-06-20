function cargarClima(){
    //1.-Llamada a webservice lectura JSON
    var clima = new XMLHttpRequest();
    var ciudad = document.getElementById("ciudadClima").value;
    clima.open("get","http://api.openweathermap.org/data/2.5/weather?q="+ciudad+"&appid=978366e305b7d1e131b3d99a37a0c383&lang=es&units=metric", false);
    clima.send(null);
    //2.- Capturar los datos
    var datos= JSON.parse(clima.response);

    var ciudadClima = datos.name

    var temperatura = datos.main.temp
    var humedad = datos.main.humidity
    var velocidadViento = datos.wind.speed
    var presionAtmosferica =datos.main.pressure
    //3.- Disponer de los datos capturados
    $(".ubicacion").html(ciudadClima);
    $("#temperatura").html(temperatura);
    $("#humedad").html(humedad);
    $("#velocidadViento").html(velocidadViento);
    $("#presionAtmosferica").html(presionAtmosferica);
}