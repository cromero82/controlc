
var modulo = "configuracion";
var admin = "Metodologia";
var formulario = "formMetodologia"
var continuacion = false;

// ------- Carga modal del formulario para actualizar existente
$("#divLista").on("click", ".itemEditar", function (e) {
    e.preventDefault();    
    var id = $(this).data('id');
    $.ajax({
        url: "/" + modulo + "/editar" + admin + "/" + id,  // <-- AND HERE
        type: 'get',
        dataType: 'json',
        beforeSend: function () {
            $("#modal-form").modal("show");
        },
        success: function (data) {
            if (data.transaccion) {                
                mostrarModal(data.html_form, data.titulo, "normal","no");                
            }
        },
        error: function (data) {
            $("#modal-form").modal("hide");
            alerta("Error al intentar conectarse con el servidor", data.mensaje, "error");
        }
    });
});

// ------- Carga modal del formulario para registrar nuevo 
var formularioRegistrar = function (id) {
    $.ajax({
        url: "/" + modulo + "/registrar" + admin,  // <-- AND HERE
        type: 'get',
        dataType: 'json',
        beforeSend: function () {
            $("#modal-form").modal("show");
        },
        success: function (data) {
            if (data.transaccion) {                
                mostrarModal(data.html_form, data.titulo, "normal","si");                
            }
        },
        error: function (data) {
            $("#modal-form").modal("hide");
            alerta("Error al intentar conectarse con el servidor", data.mensaje, "error");
        }
    });
}

// ------- Resultado de consulta JSON al servidor
function resultadoConsultaSimple(result) {
    if (result.transaccion) {
        $("#codigoDepartamento").html(" Código departamento: <code>" + result.datos.misDatos + "</code>");
        $("#codigoDepartamento").show();
    }
    else {
        alerta("Error al intentar consultar código de departamento", result.mensaje, "error");
        $("#codigoDepartamento").hide();
    }
}

// ------- Eventos clic de envio de formularios diligenciados
var clicActualizarPost = function () {
    continuacion = false;    
    enviarPost("editar");
}
var clicRegistrarPost = function () {                
    continuacion = false;
    enviarPost("registrar");    
}
var clicRegistrarContinuarPost = function () {                
    continuacion = true;
    enviarPost("registrar");    
}

// ------- ejecución del método post de envio de formularios diligenciados
var enviarPost = function (accion) {
    var url;
    // Controla el tipo de formulario para efecto de ocultar botones (Editar - Registrar)
    tipoForm = accion;
    if (accion == "editar") {
        url = "/" + modulo + "/" + accion + admin + "/" + $("#id").val() + "/";
    } else {
        url = "/" + modulo + "/" + accion + admin + "/";
    }
    // if ($("#" + formulario).valid()) {
        $("#" + formulario).attr("action", url);
        var form = $('#' + formulario);
        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function (data) {
                if (data.transaccion) {
                    miTabla.fnReloadAjax(null, null, true);
                    $("#modal-form").modal("hide");
                    alerta("Confirmando transacción", data.mensaje, "success");
                    if (continuacion){
                        formularioRegistrar();
                    }
                }
                else {                    
                    actualizarModal(data.html_form);                    
                }
            }
        });
    // }
    return false;
};

var miTabla = null;
var miTablaConsultada = null;
datos();

function datos() {
    if (miTabla != undefined) {
        miTabla.dataTable().fnDestroy();
    }
    miTabla = $('#postsTable').dataTable({
        sDom: '<"top">tipr',        
        "iDisplayLength": 9,
        "ajax": {
            "processing": true,
            "url": "/" + modulo + "/" + admin + "sJson/",
            "data": {
                "estregistro": $("#estregistro").val(),
                "nombre": $("#nombre").val()
            },
            "dataSrc": ""
        },
        "columns": [
            {
                "data": function (data, type, row, meta) {
                    return '<a class="btn btn-primary itemEditar" href="#" data-id="' + data.pk + '"><i class="fa fa-pencil"></i></a>';
                }
            },
            { "data": "fields.codigo" },
            { "data": "fields.nombre" }            
        ],
        "language": { "url": "//cdn.datatables.net/plug-ins/9dcbecd42ad/i18n/Spanish.json" }
    });
}

function iniciarModal() {  
    // var reglas = {
    //     nombre: {
    //         required: true
    //     },
    //     estregistro: {
    //         required: true
    //     }
    // };

    // var mensajes = {
    //     nombre: {
    //         required: 'Ingrese el nombre de la metodología'
    //     },
    //     estregistro: {
    //         required: 'Seleccione estado del registro'
    //     }
    // };
    // validarFormulario(formulario, reglas, mensajes);
}

// ---- Activacion de filtros de la tabla
$('#estregistro').change(function (e) { datos(); });
function filtrarNombre() { datos(); }
$("#nombre").on("keydown", function (event) {
    if (event.which == 13)
        datos();
});