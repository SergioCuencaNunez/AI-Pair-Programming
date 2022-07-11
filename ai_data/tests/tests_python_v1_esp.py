class ArchivoCSV_Mock:
    def __init__(self, ruta):
        self.ruta = ruta

    def leer_lineas(self):
        return "contenidos_csv"

class ArchivoTXT_Mock:
    def __init__(self, ruta):
        self.ruta = ruta
        
    def leer_lineas(self):
        return "contenidos_txt"

class Grafico_Mock:
    def __init__(self, datos):
        self.datos = datos

def test0(solution):
    exec(solution, globals())
    ruta_archivo = "ejemplo_archivo.csv"
    ruta = Ruta(ruta_archivo)
    assert ruta.archivo == "ejemplo_archivo.csv"
    
def test1(solution):
    exec(solution, globals())
    globals()["ArchivoCSV"] = ArchivoCSV_Mock
    globals()["ArchivoTXT"] = ArchivoTXT_Mock
    ruta_archivo = "ejemplo_archivo.csv"
    ruta = Ruta(ruta_archivo)
    assert ruta.archivo == "ejemplo_archivo.csv"
    assert ruta.entidad.__class__.__name__ == "ArchivoCSV_Mock"

def test2(solution):
    exec(solution, globals())
    globals()["ArchivoCSV"] = ArchivoCSV_Mock
    globals()["ArchivoTXT"] = ArchivoTXT_Mock
    globals()["Grafico"] = Grafico_Mock
    ruta_archivo = "ejemplo_archivo.csv"
    ruta = Ruta(ruta_archivo)
    assert ruta.archivo == "ejemplo_archivo.csv"
    assert ruta.entidad.__class__.__name__ == "ArchivoCSV_Mock"
    assert ruta.grafo.__class__.__name__ == "Grafico_Mock"
    assert ruta.grafo.datos == "contenidos_csv"