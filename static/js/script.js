$(document).ready(function() {

    //$('#btn-submit-form-input').prop( "display", none );

    //[12:45 PM, 6/16/2018] wilmar uv: Las validaciones serían:
    //[12:47 PM, 6/16/2018] wilmar uv: Número de reinas no puede ser negativo y debe ser menos que 8
    //[12:48 PM, 6/16/2018] wilmar uv: tiempo entre llegadas debe ser mayor que sero
    //[12:49 PM, 6/16/2018] wilmar uv: la desviación debe ser mayor o igual a 0 y no puede ser mayor que el tiempo entre llegadas
    //[12:50 PM, 6/16/2018] wilmar uv: se debe validar que solo se puedan recibir valores numéricos
    //[12:51 PM, 6/16/2018] wilmar uv: en resumen:
    //[12:52 PM, 6/16/2018] wilmar uv: Una GUI que reciba 3 valores numéricos con sus validaciones
    //[12:53 PM, 6/16/2018] wilmar uv: ah y que permita descargar un archivo


    
    

    //console.log(typeof(tiempo_llegada));
    //console.log(tiempo_llegada);
    //console.log(tiempo_llegada) 

    tiempo_llegada = null;
    desviacion_tiempo = null;
    numero_reinas = null;

    tiempo_llegada_valido = false;
    desviacion_tiempo_valido = false;
    numero_reinas_valido = false;



    $( "#input_tiempo_llegadas" ).blur(function() {
      tiempo_llegada = parseInt($("#input_tiempo_llegadas").val());
      if (tiempo_llegada >= 0){        
        tiempo_llegada_valido=true;
        $( "#input_tiempo_llegadas" ).addClass("valid");
        console.log("tiempo_llegada_valido: "+tiempo_llegada_valido);
      }
    });

    $( "#input_desviacion_tiempo" ).blur(function() {
      if (tiempo_llegada_valido==true){        
        desviacion_tiempo = parseInt($("#input_desviacion_tiempo").val());
        if (desviacion_tiempo >= 0 && desviacion_tiempo < tiempo_llegada){
          desviacion_tiempo_valido = true;
          console.log("desviacion_tiempo_valido: "+desviacion_tiempo_valido);        
        }
        else{
          $( "#input_desviacion_tiempo" ).addClass("invalid");
        }
      }            
    });    

    $( "#input_numero_reinas" ).blur(function() {
      numero_reinas = parseInt($("#input_numero_reinas").val());
      if (numero_reinas >= 0 && numero_reinas <= 8){
        numero_reinas_valido = true;
        console.log("numero_reinas_valido: "+numero_reinas_valido);
      }
      else{
        $( "#input_numero_reinas" ).addClass("invalid");
      }      
    });

    
    $('#btn-submit-form-input').click(function(){
      if (tiempo_llegada_valido == true && desviacion_tiempo_valido == true && numero_reinas_valido == true){
        console.log("Esta bien");
        document.getElementById('id-form-input').submit();
      }
      else{
        alert("Hay valores incorrectos en los campos.")

      }

    });

    //invalid
    //valid


    //onclick="document.getElementById('id-form-input').submit(); return false;"

    

    //console.log(tiempo_llegada_valido);
    //console.log(desviacion_tiempo_valido);
    //console.log(numero_reinas_valido);

    

});