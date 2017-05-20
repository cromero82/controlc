var titulo = "";
var tipoForm = "";
function alerta(titulo, mensaje, tipoAlerta) {
    switch (tipoAlerta) {
        case "success":
            swal(titulo, mensaje, "success");
            break;
        case "warning":
            swal(titulo, mensaje, "warning");
            break;
        case "error":
            swal(titulo, mensaje, "error");
            break;
    }
}

function notificacion (titulo, mensaje){
    new PNotify({
                    title: titulo,
                    text: mensaje,
                    type: 'success',
                    shadow: true,
                    width: 380,
                    delay: 3000
                });
}

function mostrarModal(htmlForm, tituloForm, medidaForm, esRegistrar) { 
    if(esRegistrar=="si" || esRegistrar =="SI"){
        tipoForm = "registrar";
    }else{
        tipoForm = "editar";
    }   
    switch (medidaForm) {
        case "grande":
            $("#modal-box").removeClass("modal-xxl");
            $("#modal-box").addClass("modal-xl");
            break;
        case "normal":
            $("#modal-box").removeClass("modal-xl");
            $("#modal-box").removeClass("modal-xxl");
            break;
        case "extragrande":
            $("#modal-box").removeClass("modal-xl");
            $("#modal-box").addClass("modal-xxl");
            break;
    }    
    titulo = tituloForm;  
    actualizarModal(htmlForm);          
}

function cerrarModal(){
    $("#modal-form").modal("hide");
    $("#modal-form").html("");
}

function actualizarModal(htmlForm){    
    $("#modal-form .modal-content").html(htmlForm);
    $("#tituloForm").html(titulo);
    if ( tipoForm == "registrar" ){
        $("#btnRegistrar").show();
        $("#btnRegistrarContinuar").show();                
        $("#btnEditar").hide();   
    }else{
        $("#btnRegistrar").hide();
        $("#btnRegistrarContinuar").hide();                
        $("#btnEditar").show();   
    }
}

function consultaModulo(modulo, consultaObjetivo, dato) {
    var token = $('input[name="csrfmiddlewaretoken"]').prop('value');
    var data = {
        tipoConsulta: consultaObjetivo,
        dato: dato,
        csrfmiddlewaretoken: token
    }
    $.ajax({
        url: "/" + modulo + "/consulta/",
        data: data,
        type: "POST",
        dataType: 'json',
        success: function (result) {
            resultadoConsultaSimple(result);
        }
    });
}

function validarFormulario(formulario, reglas, mensajes) {
    $("#" + formulario).validate({

        /* @validation states + elements 
        ------------------------------------------- */
        errorClass: "state-error",
        validClass: "state-success",
        errorElement: "em",
        /* @validation rules 
        ------------------------------------------ */
        rules: reglas,
        /* @validation error messages 
        ---------------------------------------------- */
        messages: mensajes,
        /* @validation highlighting + error placement  
        ---------------------------------------------------- */

        highlight: function (element, errorClass, validClass) {
            $(element).closest('.field').addClass(errorClass).removeClass(validClass);
        },
        unhighlight: function (element, errorClass, validClass) {
            $(element).closest('.field').removeClass(errorClass).addClass(validClass);
        },
        errorPlacement: function (error, element) {
            if (element.is(":radio") || element.is(":checkbox")) {
                element.closest('.option-group').after(error);
            } else {
                error.insertAfter(element.parent());
            }
        }

    });

    jQuery.extend(jQuery.validator.messages, {
        required: "Este campo es requerido.",
        remote: "Favor corregir este campo.",
        email: "Por favor ingrese un email válido.",
        url: "Por favor ingrese una URL válida.",
        date: "Por favor ingrese una fecha válida.",
        dateISO: "Por favor ingrese una fecha válida (ISO).",
        number: "Por favor ingrese un número válido.",
        digits: "Por favor ingrese unicamente dígitos.",
        creditcard: "Por favor ingrese una tarjeta de crédito válida.",
        equalTo: "Por favor ingrese el mismo valor nuevamente.",
        accept: "Por favor ingrese un valor con la extensión válida.",
        maxlength: jQuery.validator.format("Por favor ingrese no más de {0} carácteres."),
        minlength: jQuery.validator.format("Por  favor ingrese al menos {0} carácteres."),
        rangelength: jQuery.validator.format("Por favor ingrese el dato entre {0} y {1} longitud de carácteres."),
        range: jQuery.validator.format("Por favor ingrese un número entre el rango {0} y {1}."),
        max: jQuery.validator.format("Por favor ingrese un número menor o igual a {0}."),
        min: jQuery.validator.format("Por favor ingrese un número mayor a {0}.")
    });

}