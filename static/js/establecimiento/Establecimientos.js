
var modulo = "establecimiento";
var admin = "Establecimientos";
var formulario = "formEstablecimiento"

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
                mostrarModal(data.html_form, data.titulo, "normal")
                $("#btnRegistrar").hide();
                $("#btnEditar").show();
                $('#estregistro option[value="' + $("#hdEstregistro").val() + '"]').attr('selected', true);
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
                mostrarModal(data.html_form, data.titulo, "grande");
                suscribirEventos();
                $("#btnRegistrar").show();
                $("#btnEditar").hide();
                $("#codigo").focus();
            }
        },
        error: function (data) {
            $("#modal-form").modal("hide");
            alerta("Error al intentar conectarse con el servidor", data.mensaje, "error");
        }
    });
}
// ------- Eventos del form una vez cargado
var suscribirEventos = function () {
    $(".modal-content").on("change", $("input[name*='departamento']"), function (e) {
        consultaModulo(modulo,'codigoDepartamento',$("#id_departamento").val());
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
    enviarPost("editar");
}
var clicRegistrarPost = function () {
    // alert($("#id_departamento").val());
    enviarPost("registrar");
}

var clicBuscarDatosCo = function () { 
    debugger;   
    $.ajax({
    url: "https://www.datos.gov.co/resource/xax6-k7eu.json?codigoestablecimiento="+$("#id_codigo").val(),
    type: "GET",
    data: {
      "$limit" : 10,      
      "$$app_token" : "KLhKnhKZUVbEIcGgYN1XH8P73"
    }
}).done(function(data) {
    //debugger;
    alert("Retrieved " + data.length + " records from the dataset!");
    
    //console.log(data);
    });
    //enviarPost("registrar");
}


// ------- ejecución del método post de envio de formularios diligenciados
var enviarPost = function (accion) {
    var url;
    if (accion == "editar") {
        url = "/" + modulo + "/" + accion + admin + "/" + $("#id").val() + "/";
    } else {
        url = "/" + modulo + "/" + accion + admin + "/";
    }
    if ($("#" + formulario).valid()) {
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
                }
                else {
                    alerta("Confirmando error", data.mensaje, "error");
                }
            }
        });
    }
    return false;
};

var miTabla = null;
datos();

function datos() {
    if (miTabla != undefined) {
        miTabla.dataTable().fnDestroy();
    }
    miTabla = $('#postsTable').dataTable({
        sDom: '<"top">tipr',
        // "dom": '<"top"i>rt<"bottom"flp><"clear">',
        "iDisplayLength": 9,
        "ajax": {
            "processing": true,
            "url": "/" + modulo + "/" + admin + "Json/",
            "data": {
                "estregistro": $("#estregistro").val(),
                "nombre": $("#nombre").val()
            },
            "dataSrc": ""
        },
        "columns": [
            { "data": "fields.codigo" },
            { "data": "fields.nombre" },
            { "data": "fields.departamento" },
            { "data": "fields.estregistro" },
            {
                "data": function (data, type, row, meta) {
                    return '<a class="btn btn-primary itemEditar" href="#" data-id="' + data.pk + '"><i class="fa fa-pencil"></i></a>';

                    
                }
            }
        ],
        "language": { "url": "//cdn.datatables.net/plug-ins/9dcbecd42ad/i18n/Spanish.json" }
    });
}

function iniciarModal() {
    $("#codigoDepartamento").hide();
    var reglas = {
        nombre: {
            required: true
        },
        estregistro: {
            required: true
        }
    };

    var mensajes = {
        nombre: {
            required: 'Ingrese el nombre del municipio'
        },
        estregistro: {
            required: 'Seleccione estado del registro'
        }
    };
    validarFormulario(formulario, reglas, mensajes);
}

// ---- Activacion de filtros de la tabla
$('#estregistro').change(function (e) { datos(); });
function filtrarNombre() { datos(); }
$("#nombre").on("keydown", function (event) {
    if (event.which == 13)
        datos();
});