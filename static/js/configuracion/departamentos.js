
var modulo = "configuracion";
var admin = "departamentos";
var formulario = "frmDepartamento"

// ------- Carga modal del formulario para actualizar existente
$("#divLista").on("click", ".itemEditar", function (e) {
    e.preventDefault();
    var id = $(this).data('id');
    $.ajax({
        url: "/"+modulo+"/editar" + admin + "/" + id,  // <-- AND HERE
        type: 'get',
        dataType: 'json',
        beforeSend: function () {
            $("#modal-form").modal("show");
        },
        success: function (data) {
            if (data.transaccion) {
                // $("#modal-form .modal-content").html(data.html_form);
                mostrarModal(data.html_form, data.titulo, "normal" ); 
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
        url: "/"+modulo+"/nuevo" + admin,  // <-- AND HERE
        type: 'get',
        dataType: 'json',
        beforeSend: function () {
            $("#modal-form").modal("show");
        },
        success: function (data) {
            if (data.transaccion) {
                mostrarModal(data.html_form, data.titulo, "normal" );
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
    enviarPost("nuevo");
}

// ------- ejecución del método post de envio de formularios diligenciados
var enviarPost = function (accion) {
    if ($("#"+formulario).valid()) {
        $("#"+formulario).attr("action", "/"+modulo+"/" + accion + admin + "Post/");
        var form = $('#'+formulario);
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
            "url": "/"+modulo+"/"+admin+"Json/",
            "data": {
                "estregistro": $("#estregistro").val(),                
                "nombre": $("#nombre").val()
            },
            "dataSrc": ""
        },
        "columns": [
            { "data": "fields.codigo" },
            { "data": "fields.nombre" },
            { "data": "fields.estregistro" },
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
        nombre: {
            required: true
        },
        estregistro: {
            required: true
        }
    };

    var mensajes = {
        nombre: {
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