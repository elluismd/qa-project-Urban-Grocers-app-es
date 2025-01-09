## Proyecto Urban Grocers 

José Luis Meza Diyarza/Protecto No.7, grupo 17

1. Abrir el proecto "qa-project-Urban-Grocers-app-es" en PyCharm.
2. Asegurarse que los paquetes "request" y "pytest" estén descargados y actualizados.
3. Selecciona el archivo configuration.py, coregir desde ahí la URL por la de un servidor nuevo. 
4. Selecciona el archivo "create_kit_name_kit_test.py".
5. En parte superior en el boton "v" (Flecha). En la barra superior de PyCharm, cuando se despliega la lista los elemetos diran "Current File".
6. Hacer clic en el botón de "Play" que está al lado de "Current File".

   

LISTA DE COMPROBACIÓN "create_name_kit_test".

Lista de comprobación de pruebas.
1. Maximo de caracteres permitidos (1): kit_body = { "name": "a"} Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
2. Maximo de caracteres permitidos (511): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a"} Código de respuesta: 201 El campo "name" en el cuerpo de la respuesta coincide con el campo "name" en el cuerpo de la solicitud
3. El número de caracteres no alcanza el mínimo requerido (0): kit_body = { "name": "" } Código de respuesta: 400
4. El número de caracteres es mayor que la cantidad permitida (512): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a” } Código de respuesta: 400 
5. Se permiten caracteres especiales: kit_body = { "name": ""?%@"," } Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud 
6. Es posible incluir espacios: kit_body = { "name": " A Aaa " } Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
7. Los números son válidos: kit_body = { "name": "456" } Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud 
8. El parámetro no se incluye en la solicitud: kit_body = { } Código de respuesta: 400 
9. Se proporcionó un parámetro con un tipo incorrecto (número): kit_body = { "name": 456 } Código de respuesta: 400 


<
