from pathlib import Path
from pprint import pprint


class MiConfig:
    """obten valores de un archivo de config (.txt)"""
    def __init__(
        self, archivo_config:str,
        header:str, sep=" = "
    ):
        self.archivo = archivo_config
        self.header = header
        self.sep = sep
        self.data = self.carga()

    def lee(self):
        """lee el archivo de texto"""
        with open(self.archivo, 'r') as txt:
            return [l.strip('\n') for l in txt.readlines()\
                    if l.strip('\n') if not l.startswith('#')]

    def carga(self):
        """lee el archivo de texto y pasa la data a un diccionario"""
        data = {}
        if Path(self.archivo).exists():
            print("si")
            lineas = iter(self.lee())
            if next(lineas)==self.header:
                for linea in lineas:
                    if self.sep in linea:
                        clave, valor = linea.split(self.sep)
                        valor = valor.strip()
                        data[clave] = valor
        return data
    
    def get(self, nom:str) -> str:
        """obten valor de config: nom(clave) return valor"""
        return self.data.get(nom)

    
if __name__=="__main__":
    cf = MiConfig('mi_player.config', header='[[CONFIG]] MI PLAYER')
    # dt = cf.carga()
    # pprint(dt)
    # _ = cf.get('bg')
    # print(_, type(_))
    # help(cf)