
var modulo = "establecimiento";
var admin = "Establecimientos";
var formulario = "form-wizard"
var datosConsultados = null;
var codigoEstablecimiento = null;
var idEE = null;
var tipoForm = "";
var esPrimerSede = true;
$('#divDatosConsultados').hide()
$('#divJornadas').hide()
// ------- Carga modal del formulario para actualizar existente
//$("#divLista").on("click", ".itemEditar", function (e) {
$("#divDatosConsultados").on("click", ".itemEditar", function (e) {   
    form.steps("setStep", 1);
});

function ocultarEstablecimientoEnSede(){
    $("#id_establecimiento").hide();  
    $("label[for='id_establecimiento']").hide()
}


// ------- Carga modal del formulario para registrar nuevo 
var formularioRegistrarSede = function (id) {    
    $.ajax({
        url: "/" + modulo + "/registrarSedes",  // <-- AND HERE
        type: 'get',
        dataType: 'json',
        beforeSend: function () {
            $("#modal-form").modal("show");
        },
        success: function (data) {
            if (data.transaccion) {
                mostrarModal(data.html_form, data.titulo, "normal");
                // suscribirEventos();
                $("#btnEditar").hide();
                $("#btnRegistrar").show();
                // Oculta la columna establecimiento
                ocultarEstablecimientoEnSede();
                // Asigna información a la primera sede (inf. provenientes de datos.gov.co)
                if(esPrimerSede){
                    $("#id_establecimiento").val(idEE);
                    $("#id_direccion").val(datosConsultados[0].direccion);
                    $("#id_telefono").val(datosConsultados[0].telefono);
                    $("#id_correoelectronico").val(datosConsultados[0].correo_electronico);                
                }                
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
        $("#id_municipio").val(result.datos.misDatos);   
    }
    else {
        alerta("Error al intentar consultar código de departamento", result.mensaje, "error");
        $("#codigoDepartamento").hide();
    }
}

var clicRegistrarSedePost = function (){    
    enviarPostSede("registrar");
}
var clicActualizarSedePost = function (){    
    enviarPostSede("editar");
}

// ------- ejecución del método post de envio de formularios diligenciados
var enviarPostSede  = function (accion) {
    var url;
    // Controla el tipo de formulario para efecto de ocultar botones (Editar - Registrar)
    if(accion=="registrar"){
        url = "/" + modulo + "/registrarSedes/"; 
    }else{
        url = "/" + modulo + "/editarSedes/"+ $("#id").val() + "/"; 
    }
        
    // if ($("#" + formulario).valid()) {
        $("#formSede").attr("action", url);
        var form = $('#formSede');
        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function (data) {
                if (data.transaccion) {
                    // miTablaSedes.fnReloadAjax(null, null, true);
                    $("#modal-form").modal("hide");      
                    alerta("Confirmando transaccion", data.mensaje,"success")
                    datosSedes("Confirmando transaccion", data.mensaje,"");
                    $('#divJornadas').show()
                }
                else {                    
                    actualizarModal(data.html_form);                    
                }
            }
        });
}
// ------- Eventos del form una vez cargado
function suscribirEventosSedes(){
    $(".itemEditar2").click(function(e){
        e.preventDefault();    
        $.ajax({
            url: "/" + modulo + "/editarSedes/" + $(this).data('id'),  // <-- AND HERE
            type: 'get',
            dataType: 'json',
            success: function (data) {
                if (data.transaccion) {                                                  
                    mostrarModal(data.html_form, data.titulo, "normal");
                    $("#modal-form").modal("show");
                    // Oculta la columna establecimiento      
                    ocultarEstablecimientoEnSede();  
                    $("#btnEditar").show();
                    $("#btnRegistrar").hide();            
                }
            },
            error: function (data) {
                $("#modal-form").modal("hide");
                alerta("Error al intentar conectarse con el servidor", data.mensaje, "error");
            }
        });
    });
}

var miTablaSedes = null;
function datosSedes() {
    if (miTablaSedes != undefined) {
        miTablaSedes.dataTable().fnDestroy();
    }   
    miTablaSedes = $('#postsTable').dataTable({
        sDom: '<"top">tipr',        
        "iDisplayLength": 9,
        "ajax": {
            "processing": true,
            "url": "/establecimiento/SedesJson/",
            "data": {               
                "establecimiento": idEE
            },
            "dataSrc": ""
        },
        "columns": [
            {
                "data": function (data, type, row, meta) {
                    suscribirEventosSedes();
                    return '<a class="btn btn-xs  btn-primary itemEditar2" data-id="' + data.pk + '"><i class="fa fa-pencil"></i></a>';
                }
            },
            { "data": "fields.nombre" },
            { "data": "fields.codigo" } ,    
            { "data": "fields.direccion" },
            { "data": "fields.telefono" },
            { "data": "fields.correoelectronico" },
            { "data": "fields.responsable" }
                
               
            
            
        ],
        "language": {
                "url": "../../static/admindesigns/vendor/plugins/datatables/espaniol.js"
            }
    });
}

var clicBuscarDatosCo = function () {
    datosConsultados = null;
    $.ajax({
        url: "https://www.datos.gov.co/resource/xax6-k7eu.json?codigoestablecimiento=" + $("#id_codigo").val(),
        type: "GET",
        data: {
            "$limit": 200,
            "$$app_token": "KLhKnhKZUVbEIcGgYN1XH8P73"
        }
    }).done(function (data) {
        if (data.length > 0) {  // Si se encuentra un colegio
            $("#divDatosConsultados").show();
            datosConsultados = data;
            codigoEstablecimiento = data[0].codigoestablecimiento;
            $('a[href$="next"]').show();
            //--- Asignación de datos del establecimiento provenientes de datos.gov.co 
            //$("#id_codigoestablecimiento").val(datosConsultados[0].codigoestablecimiento);           
            $("#id_nombre").val(datosConsultados[0].nombreestablecimiento);
            $("#id_nombreRector").val(datosConsultados[0].codigo_etc);
            
            consultaModulo('configuracion','getCodigoMunicipio',datosConsultados[0].codigomunicipio);

            miTablaConsultada = $('#datosConsultados').dataTable({
                sDom: '<"top">t',
                "sPaginationType": "bootstrap",
                "sScrollX": "100%",
                data: datosConsultados,
                "columns": [                    
                    { "data": "nombreestablecimiento" },
                    { "data": "nombremunicipio" },
                    {
                        "data": function (data, type, row, meta) {
                            if (typeof (data.nombre_rector) != 'undefined' && element != null) {
                                return "<div>" + data.nombre_rector + "</div>";
                            } else {
                                return "<div>" + data.codigo_etc + "</div>";
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
                    { width: 220, targets: 1, defaultContent: "-" },
                    { width: 140, targets: 2, defaultContent: "-" },
                    { width: 200, targets: 3, defaultContent: "-" },
                    { width: 120, targets: 4, defaultContent: "-" },
                    { width: 120, targets: 5, defaultContent: "-" },
                    { width: 120, targets: 6, defaultContent: "-" },
                    { width: 120, targets: 7, defaultContent: "-" },
                    { width: 120, targets: 8, defaultContent: "-" },
                    { width: 120, targets: 9, defaultContent: "-" },
                    { width: 120, targets: 10, defaultContent: "-" },
                    { width: 120, targets: 11, defaultContent: "-" },
                    { width: 120, targets: 12, defaultContent: "-" },
                    { width: 380, targets: 13, defaultContent: "-" },
                    { width: 120, targets: 14, defaultContent: "-" },
                    { width: 120, targets: 15, defaultContent: "-" },
                    { width: 120, targets: 16, defaultContent: "-" },
                    { width: 320, targets: 17, defaultContent: "-" },
                    { width: 140, targets: 18, defaultContent: "-" },
                    { width: 320, targets: 19, defaultContent: "-" },
                    { width: 120, targets: 20, defaultContent: "-" },
                    { width: 90, targets: 21, defaultContent: "-" },
                    { width: 120, targets: 22, defaultContent: "-" },
                    { width: 120, targets: 23, defaultContent: "-" },
                    { width: 120, targets: 24, defaultContent: "-" },
                    { width: 120, targets: 25, defaultContent: "-" },
                    { width: 120, targets: 26, defaultContent: "-" },
                    { width: 120, targets: 27, defaultContent: "-" },
                    { width: 120, targets: 28, defaultContent: "-" },
                    { width: 160, targets: 29, defaultContent: "-" }
                ],
                fixedColumns: {
                    leftColumns: 3
                },
                "language": { "url": "//cdn.datatables.net/plug-ins/9dcbecd42ad/i18n/Spanish.json" }
            });
            $.fn.dataTableExt.sErrMode = 'throw';
        } else {
            alerta("Consulta de datos oficiales", "No se encontró ningún establecimiento. Verifique el código DANE e inténtelo nuevamente", "warning");
        }
    });
    //enviarPost("registrar");
}


// -------Creación de EE (Boton siguiente, Tab 2: Datos básicos)
var registrarDatosBasicosEE = function (accion) {
    var url;
    if (accion == "editar") {
        url = "/" + modulo + "/editarRapidoEstablecimiento/" + $("#id").val() + "/";
    } else {
        url = "/" + modulo + "/RegistrarRapidoEstablecimiento/";
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
                    // miTabla.fnReloadAjax(null, null, true);
                    // $("#modal-form").modal("hide");
                    idEE = data.dato;
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
jQuery(document).ready(function () {
    var tituloInicialBoton = "Siguiente";
    "use strict";

    // Init Theme Core    
    // Core.init();

    // // Init Demo JS     
    // Demo.init();

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
    });0
    //  
    form.children(".wizard").steps({
        headerTag: ".wizard-section-title",
        bodyTag: ".wizard-section",
        onStepChanging: function (event, currentIndex, newIndex) {
            // Gestión del boton siguiente y atras (Se deshabilita para la primera parte del paso a paso)
            if (newIndex == 0) {
                $('a[href$="previous"]').hide();
                if (datosConsultados == null) {
                    $('a[href$="next"]').hide();
                } else {
                    $('a[href$="next"]').show();
                }
                //   $('a[href$="next"]').text(tituloInicialBoton);
            } else {                
                $('a[href$="previous"]').show();
                $('a[href$="next"]').text("Siguiente");
                // Si se realiza clic en boton "siguiente" de datos generales. entonces se registra
                // o actualiza el establecimiento
                if(currentIndex==1 && newIndex == 2){
                    if(idEE== null){
                        registrarDatosBasicosEE("registrar");
                    }else{
                        registrarDatosBasicosEE("Editar");
                    }
                    
                }
            }            

            form.validate().settings.ignore = ":disabled,:hidden";
            return form.valid();
        },
        onFinishing: function (event, currentIndex) {
            form.validate().settings.ignore = ":disabled";
            return form.valid();
        },
        onFinished: function (event, currentIndex) {
            alert("Submitted!");
        }
    });

    // Demo Wizard Functionality
    var formWizard = $('.wizard');
    var formSteps = formWizard.find('.steps');
    //---------------------------------------
    // Boton al inicializar el wirzard
    $('a[href$="next"]').text(tituloInicialBoton);
    $('a[href$="previous"]').text("Anterior");
    $('a[href$="finish"]').text("Finalizar");
    $('a[href$="next"]').hide();
    $('a[href$="previous"]').hide();

    $('.wizard-options .holder-style').on('click', function (e) {
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