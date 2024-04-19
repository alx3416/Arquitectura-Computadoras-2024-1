import random

boards = ['ASUS TUF GAMING B760-PLUS WIFI',
          'ASRock H110M-HDV',
          'Intel NUC 12 Extreme',
          'ROG STRIX B250H GAMING',
          'H610MH D5',
          'BIWLA-IHT',
          'EVGA Z790 DARK K|NGP|N',
          'Z13PE-D16',
          'MZ33-CP0',
          'TB350-BTC',
          'Z790 AORUS XTREME X ICE',
          'raspberry pi 5',
          'H510TM-ITX',
          'GeForce GTX 1660 Super',
          'RTX 2080 SUPER',
          'RTX 3060 Ti',
          'RTX 4090',
          'NVIDIA RTX A6000',
          'AMD Radeon™ RX 7900 GRE',
          'AMD Radeon™ RX 6700 XT']

alumnos = ['ALVARADO RESENDIZ ERICK',
           'BAUTISTA RODRIGUEZ TERESA VIANNEY',
           'CHAPARRO SERRANO ISRAEL OZIEL',
           'DIAZ CIRO ANDERSON FRANCISCO',
           'DÍAZ OCAMPO MARIO',
           'GUTIERREZ BARRERA DANIELA',
           'HERNÁNDEZ DE LA CRUZ JENNIFER',
           'MONROY MATOS GERARDO RAFAEL',
           'MORALES VEGA JUAN CARLOS',
           'MUÑOZ ESTRADA ISAAC ALEJANDRO',
           'NUÑEZ RAZON EDOUARD ALIGHIERI',
           'OLVERA PADILLA JOSE ESTEBAN',
           'OVIEDO CUEVAS EDGAR URIEL',
           'PEREZ MONTES EDGAR ADRIAN',
           'RAMOS HERNANDEZ MATTHEW ALBERTO',
           'RANGEL LUNA BRYAN',
           'ROMERO DE LEÓN MARIO ALBERTO',
           'SEGURA MENDOZA GAEL ALEJANDRO',
           'SORIA GONZALEZ JOSE SANTOS',
           'SORIA ORTIZ JUAN URIEL']

random.shuffle(boards)
for alumno, shuffledBoard in zip(alumnos, boards):
    print(alumno + " --> " + shuffledBoard)
