
var modulo = "establecimiento";
var admin = "Establecimientos";
var formulario = "form-wizard"
var datosConsultados = null;
var codigoEstablecimiento = null;
var idEE = $('#hdId').val();
var tipoForm = "";
var esPrimerSede = true;

var miTablaSedes = null;
var miTablaJornadas = null;
var miTablaNivelesaprobados = null;

datosJornadas()
datosSedes();
datosNivelesaprobados();
;

function ocultarEstablecimientoEnSede(){
    $("#id_establecimiento").hide();  
    $("label[for='id_establecimiento']").hide()
}

// ------- Evento modificar Nivelesaprobados
function suscribirEventosNivelesaprobados(){
    $(".itemEditarNivelesaprobados").click(function(e){
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

// ------- Eventos del form una vez cargado
function suscribirEventosSedes(){
    $(".itemEditarSede").click(function(e){
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

// -----    Clic Sede
var clicRegistrarSedePost = function (){    
    enviarPostSede("registrar");
}
var clicActualizarSedePost = function (){    
    enviarPostSede("editar");
}

// -----    Clic Jornada
var clicRegistrarJornadaPost = function (){    
    enviarPostJornada("registrar");
}
var clicActualizarJornadaPost = function (){    
    enviarPostJornada("editar");
}

// -----    Clic Niveles aprobados
var clicRegistrarNivelaprobadoPost = function (){    
    enviarPostNivelAprobado("registrar");
}
var clicActualizarNivelaprobadoPost = function (){    
    enviarPostNivelAprobado("editar");
}

// ------- ejecución form editado NIVEL APROBADO
var enviarPostNivelAprobado  = function (accion) {
    var url;
    // Controla el tipo de formulario para efecto de ocultar botones (Editar - Registrar)
    if(accion=="registrar"){
        url = "/" + modulo + "/registrarNivelesAprobados/"; 
    }else{
        url = "/" + modulo + "/editarNivelesAprobados/"+ $("#id").val() + "/"; 
    }
    if ($("#formNivelesaprobados").valid()) {
        $("#formNivelesaprobados").attr("action",url);
            var form = $('#formNivelesaprobados');
            var token = $('input[name="csrfmiddlewaretoken"]').prop('value');
            var data = new FormData($('#formNivelesaprobados').get(0));
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
                        datosNivelesaprobados();
                        // miTabla.fnReloadAjax(null, null, true);
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
}

// ------- ejecución form editado JORNADA
var enviarPostJornada  = function (accion) {
    var url;
    // Controla el tipo de formulario para efecto de ocultar botones (Editar - Registrar)
    if(accion=="registrar"){
        url = "/" + modulo + "/registrarJornadas/"; 
    }else{
        url = "/" + modulo + "/editarJornadas/"+ $("#id").val() + "/"; 
    }
        
    // if ($("#" + formulario).valid()) {
        $("#formJornada").attr("action", url);
        var form = $('#formJornada');
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
                }
                else {                    
                    actualizarModal(data.html_form);                    
                }
            }, error: function (data){
                alerta("Confirmando transaccion", "El sistema no pudo procesar la información, inténtelo mas tarde","error")
            }
        });
}

// ------- ejecución form editado SEDE
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
                    datosSedes();                    
                }
                else {                    
                    actualizarModal(data.html_form);                    
                }
            }
        });
}

function datosNivelesaprobados() {
    if (miTablaNivelesaprobados != undefined) {
        miTablaNivelesaprobados.dataTable().fnDestroy();
    }   
    miTablaNivelesaprobados = $('#postsTableNivelesaprobados').dataTable({
        // sDom: '<"top">tipr',        
        sDom: '<"top">t', 
        "iDisplayLength": 9,
        "ajax": {
            "processing": true,
            "url": "/establecimiento/NivelesAprobadosJson/",
            "data": {               
                "establecimiento": idEE
            },
            "dataSrc": ""
        },
        "columns": [
            {
                "data": function (data, type, row, meta) {
                    suscribirEventosNivelesaprobados();
                   
                    return '<a class="btn btn-xs  btn-primary itemEditarNivelesaprobados" data-id="' + data.pk + '"><i class="fa fa-pencil"></i></a>';
                }
            },
            { "data": "fields.nivel" },
            { "data": "fields.tipoaprobacion" } ,    
            { "data": "fields.numeroActo" },

           { "data": function (data, type, row, meta) {               
               return '<a href="/media/'+  data.fields.anexo +'" download> descargar </a>';
            }},   
        ]
    });
    $("#numNiveles").html(miTablaNivelesaprobados.fnGetData.length);    
}

function datosSedes() {
    if (miTablaSedes != undefined) {
        miTablaSedes.dataTable().fnDestroy();
    }   
    miTablaSedes = $('#postsTableSedes').dataTable({
        // sDom: '<"top">tipr',        
        sDom: '<"top">t', 
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
                    return '<a class="btn btn-xs  btn-primary itemEditarSede" data-id="' + data.pk + '"><i class="fa fa-pencil"></i></a>';
                }
            },
            { "data": "fields.nombre" },
            { "data": "fields.codigo" } ,    
            { "data": "fields.direccion" },
            { "data": "fields.telefono" },
            { "data": "fields.correoelectronico" },
            { "data": "fields.responsable" }                                                       
        ]
    });
    $("#numSedes").html(miTablaSedes.fnGetData.length);    
}

function datosJornadas() {
    if (miTablaJornadas != undefined) {
        miTablaJornadas.dataTable().fnDestroy();
    }   
    miTablaJornadas = $('#postsTableJornada').dataTable({     
        sDom: '<"top">t', 
        "iDisplayLength": 9,
        "ajax": {
            "processing": true,
            "url": "/establecimiento/JornadasJson/",
            "data": {               
                "establecimiento": idEE
            },
            "dataSrc": ""
        },
        "columns": [
            {
                "data": function (data, type, row, meta) {
                    suscribirEventosSedes();
                    return '<a class="btn btn-xs  btn-primary itemEditarJornada" data-id="' + data.id + '"><i class="fa fa-pencil"></i></a>';
                }
            },
            {
                "data": function (data, type, row, meta) {                    
                    return '' + data.sede + '';
                }
            },
            {
                "data": function (data, type, row, meta) {                   
                    return '' + data.tipojornada + '';
                }
            },          
        ]
    });    
    $("#numJornadas").html(miTablaJornadas.fnGetData.length);    
}

// ------- Carga modal del formulario para registrar nueva NIVEL APROBADO
var formularioRegistrarNivelAprobado = function (id) {    
    $.ajax({
        url: "/" + modulo + "/registrarNivelesAprobados",  // <-- AND HERE
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

            }
        },
        error: function (data) {
            $("#modal-form").modal("hide");
            alerta("Error al intentar conectarse con el servidor", data.mensaje, "error");
        }
    });
}

// ------- Carga modal del formulario para registrar nueva SEDE
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
                              
            }
        },
        error: function (data) {
            $("#modal-form").modal("hide");
            alerta("Error al intentar conectarse con el servidor", data.mensaje, "error");
        }
    });
}

// ------- Carga modal del formulario para registrar nueva JORNADA
var formularioRegistrarJornada = function (id) {    
    $.ajax({
        url: "/" + modulo + "/registrarJornadas",  // <-- AND HERE
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
            }
        },
        error: function (data) {
            $("#modal-form").modal("hide");
            alerta("Error al intentar conectarse con el servidor", data.mensaje, "error");
        }
    });
}


function iniciarModal() {
    // $("#codigoDepartamento").hide();
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
    //         required: 'Ingrese el nombre del municipio'
    //     },
    //     estregistro: {
    //         required: 'Seleccione estado del registro'
    //     }
    // };
    // validarFormulario(formulario, reglas, mensajes);
}

var form = null;
jQuery(document).ready(function () {    
    // Init Theme Core    
    // Core.init();

    // Init Demo JS     
    // Demo.init();
});