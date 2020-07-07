  // search by vehicle tires
   $(document).ready(function(){
   
       $("#sel_make").change(function(){
           var year = $("#sel_year option:selected").text();
           var makeid = $(this).val();
           //var makeid = $("#sel_make option:selected").val();
           var api = '4a7488fedfd6685e3ba26c495bf569c9'
   
           $("#msg").css("display", "none");
           //https://api.wheel-size.com/v1/years/?make=mitsubishi&user_key=4a7488fedfd6685e3ba26c495bf569c9
           // working for makes
           //https://api.wheel-size.com/v1/makes/?user_key=4a7488fedfd6685e3ba26c495bf569c9
   
           $.ajax({
               url: 'https://api.wheel-size.com/v1/models/?',
               type: 'get',
               data: {make:makeid, year:year, user_key:api},
               dataType: 'json',
               success:function(response){
   
                   var len = response.length;
                   if(len == 0){
                       $("#msg").css("display", "block");
                       $("#sel_model").css("display", "none");
                   }else{
                   $("#sel_model").css("display", "block");
                   }
   
                   $("#sel_model").empty();
                   for( var i = 0; i<len; i++){
                       //var id = response[i]['id'];
                       var name = response[i]['name'];
   
                       $("#sel_model").append("<option value='"+name+"'>"+name+"</option>");
   
                   }
               }
           });
       });
   
   });
   $(document).ready(function(){
   
       $("#sel_year").change(function(){
           //var year = $("#sel_year option:selected").text();
           var year = $(this).val();
           var makeid = $("#sel_make option:selected").val();
           //console.log(makeid)
           if(makeid == "---Select Make---")
           {
           	makeid = 'Acura'
           }
           var api = '4a7488fedfd6685e3ba26c495bf569c9'
   
           $("#msg").css("display", "none");
           //https://api.wheel-size.com/v1/years/?make=mitsubishi&user_key=4a7488fedfd6685e3ba26c495bf569c9
           // working for makes
           //https://api.wheel-size.com/v1/makes/?user_key=4a7488fedfd6685e3ba26c495bf569c9
   
           $.ajax({
               url: 'https://api.wheel-size.com/v1/models/?',
               type: 'get',
               data: {make:makeid, year:year, user_key:api},
               dataType: 'json',
               success:function(response){
   
                   var len = response.length;
                   if(len == 0){
                       $("#msg").css("display", "block");
                       $("#sel_model").css("display", "none");
                   }else{
                   $("#sel_model").css("display", "block");
                   }
   
                   $("#sel_model").empty();
                   for( var i = 0; i<len; i++){
                       //var id = response[i]['id'];
                       var name = response[i]['name'];
   
                       $("#sel_model").append("<option value='"+name+"'>"+name+"</option>");
   
                   }
               }
           });
       });
   
   });

   // search by size wheels
   $(document).ready(function(){
   
       $("#sel_make-s").change(function(){
           var year = $("#sel_years option:selected").text();
           var makeid = $(this).val();
           //var makeid = $("#sel_make option:selected").val();
           var api = '4a7488fedfd6685e3ba26c495bf569c9'
   
           $("#msg").css("display", "none");
           //https://api.wheel-size.com/v1/years/?make=mitsubishi&user_key=4a7488fedfd6685e3ba26c495bf569c9
           // working for makes
           //https://api.wheel-size.com/v1/makes/?user_key=4a7488fedfd6685e3ba26c495bf569c9
   
           $.ajax({
               url: 'https://api.wheel-size.com/v1/models/?',
               type: 'get',
               data: {make:makeid, year:year, user_key:api},
               dataType: 'json',
               success:function(response){
   
                   var len = response.length;
                   if(len == 0){
                       $("#msg").css("display", "block");
                       $("#sel_model-s").css("display", "none");
                   }else{
                   $("#sel_model-s").css("display", "block");
                   }
   
                   $("#sel_model-s").empty();
                   for( var i = 0; i<len; i++){
                       //var id = response[i]['id'];
                       var name = response[i]['name'];
   
                       $("#sel_model-s").append("<option value='"+name+"'>"+name+"</option>");
   
                   }
               }
           });
       });
   
   });
   
   //search by model Tires
   
   
   $(document).ready(function(){
   
       $("#sel_makes").change(function(){
           var year = $("#sel_years option:selected").text();
           var makeid = $(this).val();
           //var makeid = $("#sel_make option:selected").val();
           var api = '4a7488fedfd6685e3ba26c495bf569c9'
   
           $("#msg").css("display", "none");
           //https://api.wheel-size.com/v1/years/?make=mitsubishi&user_key=4a7488fedfd6685e3ba26c495bf569c9
           // working for makes
           //https://api.wheel-size.com/v1/makes/?user_key=4a7488fedfd6685e3ba26c495bf569c9
   
           $.ajax({
               url: 'https://api.wheel-size.com/v1/models/?',
               type: 'get',
               data: {make:makeid, year:year, user_key:api},
               dataType: 'json',
               success:function(response){
   
                   var len = response.length;
                   if(len == 0){
                       $("#msg").css("display", "block");
                       $("#sel_models").css("display", "none");
                   }else{
                   $("#sel_models").css("display", "block");
                   }
   
                   $("#sel_models").empty();
                   for( var i = 0; i<len; i++){
                       //var id = response[i]['id'];
                       var name = response[i]['name'];
   
                       $("#sel_models").append("<option value='"+name+"'>"+name+"</option>");
   
                   }
               }
           });
       });
   
   });
   $(document).ready(function(){
   
       $("#sel_years").change(function(){
           //var year = $("#sel_year option:selected").text();
           var year = $(this).val();
           var makeid = $("#sel_makes option:selected").val();
           //console.log(makeid)
           if(makeid == "---Select Make---")
           {
           	makeid = 'Acura'
           }
           var api = '4a7488fedfd6685e3ba26c495bf569c9'
   
           $("#msg").css("display", "none");
           //https://api.wheel-size.com/v1/years/?make=mitsubishi&user_key=4a7488fedfd6685e3ba26c495bf569c9
           // working for makes
           //https://api.wheel-size.com/v1/makes/?user_key=4a7488fedfd6685e3ba26c495bf569c9
   
           $.ajax({
               url: 'https://api.wheel-size.com/v1/models/?',
               type: 'get',
               data: {make:makeid, year:year, user_key:api},
               dataType: 'json',
               success:function(response){
   
                   var len = response.length;
                   if(len == 0){
                       $("#msg").css("display", "block");
                       $("#sel_models").css("display", "none");
                   }else{
                   $("#sel_models").css("display", "block");
                   }
   
                   $("#sel_models").empty();
                   for( var i = 0; i<len; i++){
                       //var id = response[i]['id'];
                       var name = response[i]['name'];
   
                       $("#sel_models").append("<option value='"+name+"'>"+name+"</option>");
   
                   }
               }
           });
       });
   
   });

   
   // search by wheels Size
   $(document).ready(function(){
   
       $("#sel_year-s").change(function(){
           //var year = $("#sel_year option:selected").text();
           var year = $(this).val();
           var makeid = $("#sel_make-s option:selected").val();
           //console.log(makeid)
           if(makeid == "---Select Make---")
           {
           	makeid = 'Acura'
           }
           var api = '4a7488fedfd6685e3ba26c495bf569c9'
   
           $("#msg").css("display", "none");
           //https://api.wheel-size.com/v1/years/?make=mitsubishi&user_key=4a7488fedfd6685e3ba26c495bf569c9
           // working for makes
           //https://api.wheel-size.com/v1/makes/?user_key=4a7488fedfd6685e3ba26c495bf569c9
   
           $.ajax({
               url: 'https://api.wheel-size.com/v1/models/?',
               type: 'get',
               data: {make:makeid, year:year, user_key:api},
               dataType: 'json',
               success:function(response){
   
                   var len = response.length;
                   if(len == 0){
                       $("#msg").css("display", "block");
                       $("#sel_model-s").css("display", "none");
                   }else{
                   $("#sel_model-s").css("display", "block");
                   }
   
                   $("#sel_model-s").empty();
                   for( var i = 0; i<len; i++){
                       //var id = response[i]['id'];
                       var name = response[i]['name'];
   
                       $("#sel_model-s").append("<option value='"+name+"'>"+name+"</option>");
   
                   }
               }
           });
       });
   
   });
      // search by wheels Model
   $(document).ready(function(){
   
       $("#sel_year-m").change(function(){
           //var year = $("#sel_year option:selected").text();
           var year = $(this).val();
           var makeid = $("#sel_make-m option:selected").val();
           //console.log(makeid)
           if(makeid == "---Select Make---")
           {
           	makeid = 'Acura'
           }
           var api = '4a7488fedfd6685e3ba26c495bf569c9'
   
           $("#msg").css("display", "none");
           //https://api.wheel-size.com/v1/years/?make=mitsubishi&user_key=4a7488fedfd6685e3ba26c495bf569c9
           // working for makes
           //https://api.wheel-size.com/v1/makes/?user_key=4a7488fedfd6685e3ba26c495bf569c9
   
           $.ajax({
               url: 'https://api.wheel-size.com/v1/models/?',
               type: 'get',
               data: {make:makeid, year:year, user_key:api},
               dataType: 'json',
               success:function(response){
   
                   var len = response.length;
                   if(len == 0){
                       $("#msg").css("display", "block");
                       $("#sel_model-m").css("display", "none");
                   }else{
                   $("#sel_model-m").css("display", "block");
                   }
   
                   $("#sel_model-m").empty();
                   for( var i = 0; i<len; i++){
                       //var id = response[i]['id'];
                       var name = response[i]['name'];
   
                       $("#sel_model-m").append("<option value='"+name+"'>"+name+"</option>");
   
                   }
               }
           });
       });
   
   });
   // search by wheels Size
   $(document).ready(function(){
   
       $("#sel_years-s").change(function(){
           //var year = $("#sel_year option:selected").text();
           var year = $(this).val();
           var makeid = $("#sel_makes-s option:selected").val();
           //console.log(makeid)
           if(makeid == "---Select Make---")
           {
           	makeid = 'Acura'
           }
           var api = '4a7488fedfd6685e3ba26c495bf569c9'
   
           $("#msg").css("display", "none");
           //https://api.wheel-size.com/v1/years/?make=mitsubishi&user_key=4a7488fedfd6685e3ba26c495bf569c9
           // working for makes
           //https://api.wheel-size.com/v1/makes/?user_key=4a7488fedfd6685e3ba26c495bf569c9
   
           $.ajax({
               url: 'https://api.wheel-size.com/v1/models/?',
               type: 'get',
               data: {make:makeid, year:year, user_key:api},
               dataType: 'json',
               success:function(response){
   
                   var len = response.length;
                   if(len == 0){
                       $("#msg").css("display", "block");
                       $("#sel_models-s").css("display", "none");
                   }else{
                   $("#sel_models-s").css("display", "block");
                   }
   
                   $("#sel_models-s").empty();
                   for( var i = 0; i<len; i++){
                       //var id = response[i]['id'];
                       var name = response[i]['name'];
   
                       $("#sel_models-s").append("<option value='"+name+"'>"+name+"</option>");
   
                   }
               }
           });
       });
   
   });
      // search by wheels Model
   $(document).ready(function(){
   
       $("#sel_years-m").change(function(){
           //var year = $("#sel_year option:selected").text();
           var year = $(this).val();
           var makeid = $("#sel_makes-m option:selected").val();
           //console.log(makeid)
           if(makeid == "---Select Make---")
           {
           	makeid = 'Acura'
           }
           var api = '4a7488fedfd6685e3ba26c495bf569c9'
   
           $("#msg").css("display", "none");
           //https://api.wheel-size.com/v1/years/?make=mitsubishi&user_key=4a7488fedfd6685e3ba26c495bf569c9
           // working for makes
           //https://api.wheel-size.com/v1/makes/?user_key=4a7488fedfd6685e3ba26c495bf569c9
   
           $.ajax({
               url: 'https://api.wheel-size.com/v1/models/?',
               type: 'get',
               data: {make:makeid, year:year, user_key:api},
               dataType: 'json',
               success:function(response){
   
                   var len = response.length;
                   if(len == 0){
                       $("#msg").css("display", "block");
                       $("#sel_models-m").css("display", "none");
                   }else{
                   $("#sel_model-m").css("display", "block");
                   }
   
                   $("#sel_models-m").empty();
                   for( var i = 0; i<len; i++){
                       //var id = response[i]['id'];
                       var name = response[i]['name'];
   
                       $("#sel_models-m").append("<option value='"+name+"'>"+name+"</option>");
   
                   }
               }
           });
       });
   
   });
   
   
