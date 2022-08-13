HERO = "HÉROE"
ENEMY = "ENEMIGO"
OPTIONS_INPUT = f"""
                                    MENU
-------------------------------------------------------------------------------
1) Crear {HERO}        3) Mostrar {HERO}        5) Selección de {HERO}

2) Crear {ENEMY}       4) Mostrar {ENEMY}       6) Iniciar juego


                              7) Salir
-------------------------------------------------------------------------------
Ingrese opción: """

# Constantes Héroe

BREED_ELF = "Elfo"
BREED_WIZARD = "Mago"
BREED_DWARF = "Enano"
GENERATE_HERO_WIZARD = f"""|<>-<>-<>-<>-<>-<>GENERADOR DE {HERO}<>-<>-<>-<>-<>-<>|
|    --->      --->  [{BREED_WIZARD}]  <---     <---    |
|<>-<>-<>-<>-<>-<><>-<>-<>-<>-<>-<>-<>-<>-<>|"""
GENERATE_HERO_ELF = f"""|<>-<>-<>-<>-<>-<>GENERADOR DE {HERO}<>-<>-<>-<>-<>-<>|
|    --->      --->  [{BREED_ELF}]  <---     <---    |
|<>-<>-<>-<>-<>-<><>-<>-<>-<>-<>-<>-<>-<>-<>|"""
GENERATE_HERO_DWARF = f"""|<>-<>-<>-<>-<>-<>GENERADOR DE {HERO}<>-<>-<>-<>-<>-<>-|
|    --->     --->  [{BREED_DWARF}]  <---     <---   |
|<>-<>-<>-<>-<>-<><>-<>-<>-<>-<>-<>-<>-<>-<>-|"""
CHARACTER_HERO_INPUT = f"""
----------------------------
- {BREED_ELF}
- {BREED_WIZARD}
- {BREED_DWARF}
----------------------------
Seleccione el personaje: """
NAME_HERO_INPUT = "Ingrese nombre: "
AGE_HERO_INPUT = "Ingrese edad: "
STRENGTH_HERO_INPUT = "Ingrese fuerza: "
AGILITY_HERO_INPUT = "Ingrese agilidad: "
VITALITY_HERO_INPUT = "Ingrese vitalidad: "
MAX_ATRIBUTE_HERO = 15
ONE_HERO = f"""
********************************
* ███                          *
*  ██                          *
*  ██                          *
*  ██            {HERO}        *
*  ██                          *
*  ██                          *
* ████                         *
********************************
"""
TWO_HERO = f"""
********************************
* ███████                      *
*       █                      *
*       █                      *
* ███████          {HERO}      *
* █                            *
* █                            *
* ███████                      *
********************************
"""
THREE_HERO = f"""
*********************************
* ████                          *
*     █                         *
*     █                         *
* █████          {HERO}         *
*     █                         *
*     █                         *
* ████                          *
*********************************
"""
OPTION_SELECT_CHARACTER = f"Selección de {HERO}:"
NAME_INPUT_SELECT_CHARACTER = "Ingrese nombre del personaje: "
# Constantes enemigo

AGE_ENEMY_ELF = 30
AGE_ENEMY_DWARF = 30
AGE_ENEMY_WIZARD = 30
NAME_ENEMY_ELF = "Elfo maldito"
NAME_ENEMY_DWARF = "Enano maldito"
NAME_ENEMY_WIZARD = "Mago oscuro"
MIN_RANDOM_ATTRIBUTE_ENEMY = 2
MAX_RANDOM_ATTRIBUTE_ENEMY = 4
MAX_ATTRIBUTE_ENEMY = 10
NUMBER_ENEMIES_INPUT = "Ingrese cantidad de enemigos: "
NUMBER_OF_ENEMY_INPUT = "Ingrese cantidad de enemigos a generar: "
GENERATE_ENEMY = """|<>-<>-<>-<>-<>-<>GENERADOR DE ENEMIGO<>-<>-<>-<>-<>-<>-<|
|    --->     --->  [RANDOM]  <---     <---              |
|<>-<>-<>-<>-<>-<><>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-|"""

ONE_ENEMY = f"""
********************************
* ███                          *
*  ██                          *
*  ██                          *
*  ██           {ENEMY}        *
*  ██                          *
*  ██                          *
* ████                         *
********************************
"""
TWO_ENEMY = f"""
********************************
* ███████                      *
*       █                      *
*       █                      *
* ███████         {ENEMY}      *
* █                            *
* █                            *
* ███████                      *
********************************
"""
THREE_ENEMY = f"""
*********************************
* ████                          *
*     █                         *
*     █                         *
* █████         {ENEMY}         *
*     █                         *
*     █                         *
* ████                          *
*********************************
"""
FOUR_ENEMY = f"""
*********************************
*    ██                         *
*   █ █                         *
*  █  █                         *
* █   █         {ENEMY}         *
* █████                         *
*     █                         *
*     █                         *
*********************************
"""
FIVE_ENEMY = f"""
*********************************
* ███████                       *
* █                             *
* █                             *
* ███████         {ENEMY}       *
*       █                       *
*       █                       *
* ███████                       *
*********************************
"""
SIX_ENEMY = f"""
**********************************
*   █████                        *
*  ██                            *
* ██                             *
* █               {ENEMY}        *
* █  ███                         *
* █     █                        *
* ███████                        *
**********************************
"""
SEVEN_ENEMY = f"""
**********************************
* ███████                        *
*       █                        *
*       █                        *
*    ██████       {ENEMY}        *
*       █                        *
*       █                        *
*       █                        *
**********************************
"""
EIGHT_ENEMY = f"""
**********************************
*  █████                         *
* █     █                        *
* █     █                        *
*  █████          {ENEMY}        *
* █     █                        *
* █     █                        *
*  █████                         *
**********************************
"""
NINE_ENEMY = f"""
**********************************
* ███████                        *
* █     █                        *
* █     █                        *
* ███████         {ENEMY}        *
*       █                        *
*       █                        *
*       █                        *
**********************************
"""

# Errores y salida.

ERROR_MAX_LIMIT_CREATE_CHARACTER = f"Error: Has alcanzado el límite de {HERO} creados."
ERROR_NO_NAME_CHARACTER_EXIST = f"Error: No hay {HERO} con ese nombre."
ERROR_NAME_ALREDY_EXIST = f"Error: El nombre ingresado ya existe."
ERROR_IN_POINTS = f"""Error:
La Fuerza + Agilidad + Vitalidad debe ser igual a {MAX_ATRIBUTE_HERO}.
Los atributos no pueden ser menor o igual a 0."""
ERROR_IN_SELECT_CHARACTER = "Error al ingresar el personaje. Intente de nuevo."
ERROR_NOTHING_CHARACTER_HERO = f"Error: No hay {HERO} creado."
ERROR_NOTHING_CHARACTER_ENEMY = f"Error: No hay {ENEMY} creado."
ERROR_NOTHING_CHARACTER_HERO_AND_ENEMY = f"Error, falta crear {HERO} o {ENEMY} o seleccionar un {HERO}."
ERROR_BAD_OPTION = "Error: No has ingresado un número del menú"
ERROR_IN_SELECT_ENEMY = "Error: El número de enemigo no es correcto."
NO_ENEMY_SELECT_WITH_THAT_NUMBER = "Error: No hay ningún enemigo con ese número"
EXIT = "¡saliste!"

# Turnos de juego.

TURN_OF_PLAYER = "Tu turno"
TURN_OF_ENEMY = """
Turno del oponente
pensando..."""
ROLL_DICE_INPUT = "Presione ENTER para atacar"
SELECT_ENEMY_TO_ATTACK_INPUT = "Ingrese el NÚMERO del enemigo a quien atacar: "
ENEMY_DEAD = f"El {ENEMY} ha muerto."
ENEMY_LIVE = f"El {ENEMY} aún sigue con vida. "
HERO_DEAD = """Has muerto.
        <<<GAME OVER>>>"""
HERO_LIVE = "Aún sigues con vida."
HERO_WIN = f"""Has derrotado a todos los {ENEMY}.
        <<<HAS GANADO>>>"""