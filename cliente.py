class Cliente:

    def __init__(self, nombreCompleto,
                usuario,
                password,
                documento,
                correo,
                pregunta1,
                respuesta1,
                pregunta2,
                respuesta2,
                pregunta3,
                respuesta3,
                ):
        self.nombreCompleto = nombreCompleto
        self.usuario = usuario
<<<<<<< HEAD
=======
        #
>>>>>>> 958890bc9c3c25431af55f892028f2b3c9303013
        self.password = password
        self.documento = documento
        self.correo = correo
        self.pregunta1 = pregunta1
        self.respuesta1 = respuesta1
        self.pregunta2 = pregunta2
        self.respuesta2 = respuesta2
        self.pregunta3 = pregunta3
        self.respuesta3 = respuesta3

    def __str__(self):
<<<<<<< HEAD
        return f"Nombre: {self.nombreCompleto} Documento: {self.documento}"
=======
        return f"Nombre: {self.nombreCompleto} Documento: {self.documento}"

>>>>>>> 958890bc9c3c25431af55f892028f2b3c9303013
