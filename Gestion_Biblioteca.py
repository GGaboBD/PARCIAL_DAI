class Recurso:
    def __init__(self, ID_recurso: str, cantidad_horas_retraso = 0):
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
            return total_cuotas_multas * 2.50

        return self.cantidad_horas_retraso
    
class UsoSalaEstudio(Recurso):
    def __init__(self, ID_recurso, cantidad_horas_retraso = 0, demanda_estudiantil = 0):
        super().__init__(ID_recurso, cantidad_horas_retraso)
        self.demanda_estudiantil = demanda_estudiantil

    def calcular_multa(self):
        multa = self.cantidad_horas_retraso * self.demanda_estudiantil
        return multa

class RegistroAtencion:
    def __init__(self, ID_registro: str, carnet: str, nombre_empleado: str, codigo_usuario: str):
        self.ID_registro = ID_registro
        self.carnet = carnet
        self._recursos = []
        self.nombre_empleado = nombre_empleado
        self.codigo_usuario = codigo_usuario
        self.estado_cuenta = "CUENTA_ACTIVA"

    def agregar_recurso(self, recurso: Recurso):
        if len(self._recursos) >= 4:
            raise ValueError("Limite de recursos alcanzados")
        self._recursos.append(recurso)

    @property
    def Mostrar_datos(self):
        return tuple(self._recursos)
    
    def calcular_multa_total(self):
        total_multa = 0
        for recurso in self._recursos:
            total_multa += recurso.calcular_multa()
        return total_multa

    def verificar_restricciones(self):
        if self.calcular_multa_total() > 15.00:
            return "CUENTA_SUSPENDIDA"
        if self.codigo_usuario[:3] == "AUX":
            for recurso in self._recursos:
                if isinstance(recurso, UsoSalaEstudio) and recurso.demanda_estudiantil > 10:
                    return "CUENTA_SUSPENDIDA"
        return "CUENTA_ACTIVA"





print("\n--- Caso base con multa inferior a $15 ---")
print("")
registro1 = RegistroAtencion("REG001", "12345678", "Juan Perez", "AUX001")
libro1 = PrestamoLibro("LIB001", 48)
sala1 = UsoSalaEstudio("SALA001", 2, 2)
libro2 = PrestamoLibro("LIB002", 24)
libro3 = PrestamoLibro("LIB003", 24)
registro1.agregar_recurso(libro1)
registro1.agregar_recurso(sala1)
registro1.agregar_recurso(libro2)
registro1.agregar_recurso(libro3)
print(f"Multa total: {registro1.calcular_multa_total()}")
print(f"Estado de la cuenta: {registro1.verificar_restricciones()}")


print("")
print("\n--- Caso con multa superior a 15.00 ---")
print("")
registro2 = RegistroAtencion("REG002", "87654321", "Maria Lopez", "AUX002")
libro5 = PrestamoLibro("LIB005", cantidad_horas_retraso=120)
sala6 = UsoSalaEstudio("SALA006", cantidad_horas_retraso=6, demanda_estudiantil=3)
registro2.agregar_recurso(libro5)
registro2.agregar_recurso(sala6)
print(f"Multa total: {registro2.calcular_multa_total()}")
print(f"Estado de la cuenta: {registro2.verificar_restricciones()}")

