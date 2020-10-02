# Desarrollo de servicio web (API REST) que sirva endpointspara un sistema de gestión de historia clínica centralizada.

## Requerimientos:

1.Permitir registro de usuarios con Identificación, Email, Teléfono y contraseña.Condiciones: Los tipos de usuario 
permitidos en registro son Hospital y Paciente.

2.Confirmación de registro por parte de usuario a través de uno de sus datos de contacto.Condiciones:El usuario no podrá acceder al sistema hasta que confirme su registro.

3.Inicio de sesión de usuario utilizando Identificación y Contraseña.

4.Registro de datos básicos de usuarioSi el usuario es de tipo Hospital debe registrar: Nombre, Dirección, Servicios médicos que brinda.Si el usuario es de tipo paciente debe registrar: Nombre, Dirección, fecha de nacimiento.

5.Registro de usuario tipo Médico por parte de un usuario Hospital.Condiciones:Condiciones similares al registro de los otros tipos de usuario.La primera vez que inicie sesión debe cambiar la contraseña y establecer una nueva contraseña.

6.Todos los usuarios deben cambiar y/o recuperar su contraseña cuando lo deseen.

7.Permitir a un usuario de Tipo Médico registrar observaciones médicas y estado de salud de un usuario de tipo Paciente.Condiciones:Obligatorio indicar especialidad médicabrindada al Paciente

8.Cualquier usuario debe poder consultar todos los registros de observaciones médicas registradas. Condiciones:Mostrar: hospital, médico, especialidad y detalle de cada registro asociado al paciente.Usuario Paciente, solo puede consultar sus registros.Usuario Médico, puede consultar registros realizados por él mismo.Usuario Hospital, puede consultar los registros realizados por sus Médicos.

9.Descargar archivo con todas las observaciones de un Paciente registradas en el sistema.Condiciones iguales al punto 7.
