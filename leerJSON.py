import json
import csv
import time
class archivos:

    def leerJson(self):
            archivosJ = '''
            {
  "INDEX": 2,
  "TIMESTAMP": "02-10-19-::14:30:25",
  "CLASS": "Estructuras de datos",
  "DATA": {
    "value": "201403525-Nery",
    "left": {
      "value": "201212963-Andres",
      "left": {
        "value": "201005874-Estudiante1",
        "left": null,
        "right": null
      },
      "right": {
        "value": "201313526-Alan",
        "left": null,
        "right": null
      }
    },
    "right": {
      "value": "201403819-Anne",
      "left": {
        "value": "201403624-Fernando",
        "left": null,
        "right": null
      },
      "right": {
        "value": "201602255-Estudiante2",
        "left": null,
        "right": null
      }
    }
  },
  "PREVIOUSHASH": "fd5f6d5fdfdf232Y232312QW12196255",
  "HASH": "34334523435252DWDSDSDSDSsdsDEDS12121"
}'''
            estudiantes = json.loads(archivosJ)
            #b = estudiantes['DATA']
            b = json.dumps(estudiantes['DATA'],indent=2)
            print(b)
            #self.preordenJson(estudiantes)
          
    def preordenJson(self,estudiantes):
            if not estudiantes:
                return

            #ingresar los datos al arbol
            print(estudiantes["value"])
            self.preordenJson(estudiantes["left"])
            self.preordenJson(estudiantes["right"])
obj = archivos()
obj.leerJson()