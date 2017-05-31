
var modulo = "establecimiento";
var admin = "Establecimientos";
var formulario = "formEstablecimiento"
var datosConsultados = null;

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
                mostrarModal(data.html_form, data.titulo, "extragrande");
                suscribirEventos();
                $("#btnRegistrar").show();
                $("#btnEditar").hide();
                $('#divDatosConsultados').hide()               
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
        consultaModulo(modulo, 'codigoDepartamento', $("#id_departamento").val());
    });
}


// ------- Eventos clic de envio de formularios diligenciados
var clicActualizarPost = function () {
    enviarPost("editar");
}
var clicRegistrarPost = function () {                
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
var miTablaConsultada = null;
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
            {
                "data": function (data, type, row, meta) {
                    debugger;
                    return '<a class="btn btn-primary itemEditar" href="#" data-id="' + data.pk + '"><i class="fa fa-pencil"></i></a>';
                }
            },
            { "data": "fields.nombre" },
            { "data": "fields.telefono" },
            { "data": "fields.nombreRector" },
            { "data": "fields.direccion" },
            { "data": "fields.correoelectronico" },
            { "data": "fields.municipio" }
            // { "data": "fields.estregistro" }

                                // <th>Nombre</th>
                                // <th>Teléfono</th>
                                // <th>Rector</th>
                                // <th>Direccion</th>
                                // <th>Email</th>
                                // <th>Municipio</th>
                                // <th>Departamento</th>                                                                
                                // <th>Acciones</th>

            
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