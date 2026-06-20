from abc import ABC, abstractmethod

class Recurso:
    def __init__(self, ID_recurso: str, cantidad_horas_retraso: int = 0):
        self.ID_recurso = ID_recurso
        self.cantidad_horas_retraso = cantidad_horas_retraso

    def calcular_multa(self):
        raise NotImplementedError("Es un metodo que se aplicara solo a las clases hijas")
    




class PrestamoLibro(Recurso):
    def __init__(self, ID_recurso, cantidad_horas_retraso = 0):
        super().__init__(ID_recurso, cantidad_horas_retraso)

    def calcular_multa(self): 
        total_cuotas_multas = self.cantidad_horas_retraso/24

        if total_cuotas_multas >= 1 and total_cuotas_multas == int(total_cuotas_multas):
            self.cantidad_horas_retraso = total_cuotas_multas*2.5

        return self.cantidad_horas_retraso
    

    
class UsoSalaEstudio(Recurso):
    def __init__(self, ID_recurso, cantidad_horas_retraso = 0):
        super().__init__(ID_recurso, cantidad_horas_retraso)

    def calcular_multa(self):

        demanda_estudiantil = 1.5 # Valor de ejemplo JSAJHASJH no se me ocurrio una forma de calcular la demanda estudiantil
        multa = self.cantidad_horas_retraso * demanda_estudiantil
        return multa


class RegistroAtencion:
    def __init__(self, ID_registro: str, carnet: str, nombre_empleado: str, codigo_usuario: str):
        self.ID_registro = ID_registro
        self.carnet = carnet
        self._recursos = []
        self.nombre_empleado = nombre_empleado
        self.codigo_usuario = codigo_usuario

    def agregar_recurso(self, recurso: Recurso):
        if len(self._recursos) >= 4:
            raise ValueError("Limite de recursos alcanzados")
        self._recursos.append(recurso)

    @property
    def Mostrar_datos(self):
        return tuple(self._recursos)
    


    