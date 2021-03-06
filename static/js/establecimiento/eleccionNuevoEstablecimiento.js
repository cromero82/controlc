
var modulo = "establecimiento";
var admin = "Establecimientos";
var formulario = "formEstablecimiento"
var datosConsultados = null;
$('#divDatosConsultados').hide()  
// ------- Carga modal del formulario para actualizar existente
//$("#divLista").on("click", ".itemEditar", function (e) {
$("#divDatosConsultados").on("click", ".itemEditar", function (e) {
   debugger;
    // form.next(0)
    //form.steps.next
    form.steps("setStep", 1);
    // e.preventDefault();
    // var id = $(this).data('id');
    // $.ajax({
    //     url: "/" + modulo + "/editar" + admin + "/" + id,  // <-- AND HERE
    //     type: 'get',
    //     dataType: 'json',
    //     beforeSend: function () {
    //         $("#modal-form").modal("show");
    //     },
    //     success: function (data) {
    //         if (data.transaccion) {
    //             mostrarModal(data.html_form, data.titulo, "normal")
    //             $("#btnRegistrar").hide();
    //             $("#btnEditar").show();
    //             $('#estregistro option[value="' + $("#hdEstregistro").val() + '"]').attr('selected', true);
    //         }
    //     },
    //     error: function (data) {
    //         $("#modal-form").modal("hide");
    //         alerta("Error al intentar conectarse con el servidor", data.mensaje, "error");
    //     }
    // });
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
    //enviarPost("registrar");    
}

var clicBuscarDatosCo = function () {
    datosConsultados= null;
    $.ajax({
        url: "https://www.datos.gov.co/resource/xax6-k7eu.json?codigoestablecimiento=" + $("#id_codigo").val(),
        type: "GET",
        data: {
            "$limit": 200,
            "$$app_token": "KLhKnhKZUVbEIcGgYN1XH8P73"
        }
    }).done(function (data) {
        $("#divDatosConsultados").show();                
        datosConsultados = data;                      
        miTablaConsultada = $('#datosConsultados').dataTable({
            sDom: '<"top">t',           
            "sPaginationType": "bootstrap",
            "sScrollX": "100%",
            data: datosConsultados,
            "columns": [                
                {
                    "data": function (data, type, row, meta) {
                        return '<a class="btn btn-primary itemEditar" href="#" data-id="' + data.codigoestablecimiento + '">Seleccionar</a>';
                    }
                },
                { "data": "nombreestablecimiento" },
                { "data": "nombremunicipio" },
                {
                    "data": function (data, type, row, meta) {
                        if (typeof(data.nombre_rector) != 'undefined' && element != null){
                        return  "<div>"+data.nombre_rector +"</div>";                    
                    }else{
                        return  "<div>"+data.codigo_etc +"</div>";
                    }
                    }
                },
                { "data": "tipo_establecimiento" },
                { "data": "nombredepartamento" },                
                { "data": "zona" },
                { "data": "direccion" },
                { "data": "telefono" },                                                
                { "data": "etnias" },
                { "data": "sector" },
                { "data": "genero" },
                { "data": "niveles" },
                { "data": "jornadas" },
                { "data": "caracter" },
                { "data": "especialidad" },
                { "data": "grados" },
                { "data": "modelos_educativos" },
                { "data": "capacidades_excepcionales" },
                { "data": "discapacidades" },
                { "data": "idiomas" },
                { "data": "numero_de_sedes" },
                { "data": "estado" },
                { "data": "prestador_de_servicio" },
                { "data": "propiedad_planta_Fisica" },
                { "data": "resguardo" },
                { "data": "matricula_contratada" },
                { "data": "calendario" },
                { "data": "internado" },
                { "data": "estrado_socio_economico" },
                { "data": "correo_electronico" }
            ],                     
            columnDefs: [
            { width: 220, targets: 1 ,defaultContent:"-"},
            { width: 140, targets: 2 ,defaultContent:"-"},
            { width: 200, targets: 3 ,defaultContent:"-"},
            { width: 120, targets: 4 ,defaultContent:"-"},
            { width: 120, targets: 5 ,defaultContent:"-"},
            { width: 120, targets: 6 ,defaultContent:"-"},
            { width: 120, targets: 7 ,defaultContent:"-"},
            { width: 120, targets: 8 ,defaultContent:"-"},
            { width: 120, targets: 9 ,defaultContent:"-"},
            { width: 120, targets: 10 ,defaultContent:"-"},
            { width: 120, targets: 11 ,defaultContent:"-"},
            { width: 120, targets: 12 ,defaultContent:"-"},
            { width: 380, targets: 13 ,defaultContent:"-"},
            { width: 120, targets: 14 ,defaultContent:"-"},
            { width: 120, targets: 15 ,defaultContent:"-"},
            { width: 120, targets: 16 ,defaultContent:"-"},
            { width: 320, targets: 17 ,defaultContent:"-"},
            { width: 140, targets: 18 ,defaultContent:"-"},
            { width: 320, targets: 19 ,defaultContent:"-"},
            { width: 120, targets: 20 ,defaultContent:"-"},
            { width: 90, targets: 21 ,defaultContent:"-"},            
            { width: 120, targets: 22 ,defaultContent:"-"},
            { width: 120, targets: 23 ,defaultContent:"-"},
            { width: 120, targets: 24 ,defaultContent:"-"},
            { width: 120, targets: 25 ,defaultContent:"-"},
            { width: 120, targets: 26 ,defaultContent:"-"},
            { width: 120, targets: 27 ,defaultContent:"-"},
            { width: 120, targets: 28 ,defaultContent:"-"},
            { width: 160, targets: 29 ,defaultContent:"-"}            
        ],
        fixedColumns:   {
            leftColumns: 3
        },
            "language": { "url": "//cdn.datatables.net/plug-ins/9dcbecd42ad/i18n/Spanish.json" }
        });
$.fn.dataTableExt.sErrMode = 'throw';
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
var miTablaConsultada = null;

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

var form = null;
jQuery(document).ready(function() {
    var tituloInicialBoton = "Registrar como establecimiento nuevo";   
            "use strict";

            // Init Theme Core    
            Core.init();

            // Init Demo JS     
            Demo.init();

            // Form Wizard 
            form = $("#form-wizard");
            form.validate({
                errorPlacement: function errorPlacement(error, element) {
                    element.before(error);
                },
                rules: {
                    confirm: {
                        equalTo: "#password"
                    }
                }
            });            
            //  
            form.children(".wizard").steps({
                headerTag: ".wizard-section-title",
                bodyTag: ".wizard-section",                                
                onStepChanging: function(event, currentIndex, newIndex) {                   
                       if(newIndex==0){
                          $('a[href$="next"]').text(tituloInicialBoton);
                       }else{
                           $('a[href$="next"]').text("Siguiente");
                       }
                   
                    form.validate().settings.ignore = ":disabled,:hidden";
                    return form.valid();
                },
                onFinishing: function(event, currentIndex) {
                    form.validate().settings.ignore = ":disabled";
                    return form.valid();
                },
                onFinished: function(event, currentIndex) {
                    alert("Submitted!");
                }
            });

            // Demo Wizard Functionality
            var formWizard = $('.wizard');
            var formSteps = formWizard.find('.steps');
            // Boton al inicializar el wirzard
            $('a[href$="next"]').text(tituloInicialBoton);
            $('a[href$="previous"]').text("Anterior");
            $('a[href$="finish"]').text("Finalizar");

            $('.wizard-options .holder-style').on('click', function(e) {
                e.preventDefault();

                var stepStyle = $(this).data('steps-style');

                var stepRight = $('.holder-style[data-steps-style="steps-right"');
                var stepLeft = $('.holder-style[data-steps-style="steps-left"');
                var stepJustified = $('.holder-style[data-steps-style="steps-justified"');

                if (stepStyle === "steps-left") {
                    stepRight.removeClass('holder-active');
                    stepJustified.removeClass('holder-active');
                    formWizard.removeClass('steps-right steps-justified');
                }
                if (stepStyle === "steps-right") {
                    stepLeft.removeClass('holder-active');
                    stepJustified.removeClass('holder-active');
                    formWizard.removeClass('steps-left steps-justified');
                }
                if (stepStyle === "steps-justified") {
                    stepLeft.removeClass('holder-active');
                    stepRight.removeClass('holder-active');
                    formWizard.removeClass('steps-left steps-right');
                }

                // Assign new style 
                if ($(this).hasClass('holder-active')) {
                    formWizard.removeClass(stepStyle);
                } else {
                    formWizard.addClass(stepStyle);
                }
// formWizard.find(".actions a:eq(1)").text("Next Oneee")

                // Assign new active holder
                $(this).toggleClass('holder-active');
            });


        });


// ---- Activacion de filtros de la tabla
$('#estregistro').change(function (e) { datos(); });
function filtrarNombre() { datos(); }
$("#nombre").on("keydown", function (event) {
    if (event.which == 13)
        datos();
});



