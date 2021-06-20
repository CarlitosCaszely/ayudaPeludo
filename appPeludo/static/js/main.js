function validarEnvio(){
    if (document.formulario.nombre.value.length==0) {
        alert("Tienes que escribir tu nombre")
        document.formulario.nombre.focus()
        return 0;
    }

    edad= parseInt(document.formulario.edad.value)
    if (isNaN(edad)){
        alert("Ingrese su edad")
        document.formulario.edad.focus()
        return 0;

    }else{
        if (edad<18){
            alert ("Debe tener 18 o mas años")
            document.formulario.edad.focus()
            return 0;
        }

    }

    alert("Datos ingresados correctamente");
    document.formulario.submit();

}