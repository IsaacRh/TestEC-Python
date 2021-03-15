# Exercise C1
## Como Cliente, quiero suscribirme a un canal Premium por períodos flexibles de tiempo por medio del sitio web.

> ### Basado en las siguientes prepociones
>> - La plataforma WEB, está preparada para ofrecer diferentes opciones de suscripción
>> - Identificación de la opción seleccionada por el usuario
>> - La plataforma WEB, tiene sistema de pagos con las diferente formas(Transferencia bancaria, PyPal, Credito, Efectivo OXXO, etc)
>> - La plataforma WEB, cuenta con versiones o apartado dependiento de la suscripción echa por el usuario, es decir tener acceso o no a ciertos contenidos de la plataforma

> ## Con base en la información dicha anteriormente, puedo definir que:
>> - El servicio de sucripción se hace a travez de una API
>> - Para la aplicación de pagos se hace a travez de una conexión a algun sistema de pagos
>> - Existen varias opciones para adquirir el servicio
>> - El usuario podrá cambiar su tipo de suscripción cuando lo desee
>> - La plataforma WEB, posiblemente tiene una versión movil


> ### Las pruebas propuestas son las siguientes
> los estados que se manejarian en cada prueba podrían ser: Given, When y Then
> esto con el fin de aclarar el estado previo(given), lo que se está probando (when) y el resultado que se espera(then)

>> - Hacer pruebas aisladas de cada API o microservicio que integra toda la funcionalidad de suscripciones
>> - Ejecutar pruebas de interfaz, es decir con base al tipo de suscripción que aspectos o herramientas se habilitan dentro de la plataforma WEB
>> - Realizar pruebas unitarias con todas las opciones de pago disponibles dentro de la plataforma
>> - Hacer pruebas con los servicios WEB y APIS para la versión movil