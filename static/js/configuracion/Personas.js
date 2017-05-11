
var modulo = "configuracion";
var admin = "Personas";
var formulario = "frmPersona"

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
                $("#modal-form .modal-content").html(data.html_form);
                $("#tituloForm").html(data.titulo);                
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
                tamanioformularioModal("xxl");
                $("#modal-form .modal-content").html(data.html_form);
                $("#tituloForm").html(data.titulo);                
                $("#btnRegistrar").show();
                $("#btnEditar").hide();
            }
        },
        error: function (data) {
            $("#modal-form").modal("hide");
            alerta("Error al intentar conectarse con el servidor", data.mensaje, "error");
        }
    });
}

// ------- Eventos clic de envio de formularios diligenciados
var clicActualizarPost = function () {
    enviarPost("editar");
}
var clicRegistrarPost = function () {
    enviarPost("registrar");
}

// ------- ejecución del método post de envio de formularios diligenciados
var enviarPost = function (accion) {    
    var url;
    if(accion == "editar"){
        url=  "/" + modulo + "/" + accion + admin + "/" +$("#id").val() +"/";
    }else{
        url = "/" + modulo + "/" + accion + admin + "/";
    }
    var token = $('input[name="csrfmiddlewaretoken"]').prop('value');
    if ($("#" + formulario).valid()) {
        $("#" + formulario).attr("action",url);
        var form = $('#' + formulario);
        var data = new FormData($('#' + formulario).get(0));
        form.append("csrftoken",   token)
        $.ajax({
            url: form.attr("action"),
            data: data,
            type: form.attr("method"),
            processData: false,
            contentType: false,
            cache: false,
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
            
            { "data": function (data, type, row, meta) {              
                    return '<img src="/media/'+ data.fields.foto +'" class="media-object mn thumbnail mw50">';
                  }},
            { "data": "fields.nombres" },
            { "data": "fields.apellidos" },
            { "data": "fields.numerodocumento" },
            { "data": "fields.telefono" },
            { "data": "fields.correoelectronico" },            
            {
                "data": function (data, type, row, meta) {
                    return '<a class="btn btn-primary itemEditar" href="#" data-id="' + data.pk + '">Editar</a>';
                }
            }
        ],
        "language": { "url": "//cdn.datatables.net/plug-ins/9dcbecd42ad/i18n/Spanish.json" }
    });
}

function iniciarModal() {
    var reglas = {
        nombres: {
            required: true
        },
        estregistro: {
            required: true
        }
    };

    var mensajes = {
        nombres: {
            required: 'Ingrese el nombre'
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