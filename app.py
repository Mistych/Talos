"""
Generador de códigos de elementos de tubería (Piping Class - Annex A Item Codes)
Basado en: CSK1-00-VBR-TI-GHV-003

Estructura del código:
  Primera parte (piping class datasheets):  TT EX CC ST MAT
  Segunda parte (isométricos y MTOs):        MC DD1 DD2 SC1 SC2
  Separadas por un guion "-"

Ejemplo: CDBW0008121-0036180900
"""

# ----------------------------------------------------------------------
# TABLAS DE CÓDIGOS (extraídas de Codigos.pdf)
# ----------------------------------------------------------------------

DD = {
    "-": "00", "6": "01", "8": "02", "10": "03", "15": "04", "20": "05",
    "25": "06", "32": "07", "40": "08", "50": "09", "65": "10", "80": "11",
    "90": "12", "100": "13", "125": "14", "150": "15", "200": "16", "250": "17",
    "300": "18", "350": "19", "400": "20", "450": "21", "500": "22", "550": "23",
    "600": "24", "650": "25", "700": "26", "750": "27", "800": "28", "850": "29",
    "900": "30", "950": "31", "1000": "32", "1050": "33", "1100": "34", "1150": "35",
    "1200": "36", "1300": "37", "1400": "38", "1500": "39", "1600": "40",
    "1700": "41", "1800": "42", "1900": "43", "2000": "44",
    "1/2": "70", "5/8": "71", "3/4": "72", "7/8": "73", "1": "74",
    "1.1/8": "75", "1.1/4": "76", "1.3/8": "77", "1.1/2": "78", "1.5/8": "79",
    "1.3/4": "80", "1.7/8": "81", "2": "82", "2.1/4": "83", "2.1/2": "84",
    "2.3/4": "85", "3": "86", "3.1/4": "87", "3.1/2": "88",
}

TT = {
    "-": "00", "Adapter transition": "AT", "Bend 3D": "B3", "Bend 5D": "B5",
    "Cap": "CP", "Cap Drilled": "CD", "Full Face gasket": "GC", "Coupling": "CF",
    "Coupling w/ welding ring": "CW", "Cross": "CS", "Double hexagonal nipple": "NH",
    "Elbolet": "TB", "Elbow 30": "ED", "Elbow 45": "EB", "Elbow 45 LR": "EC",
    "Elbow 45 radius 2D": "EE", "Elbow 45 radius 3D": "EF", "Elbow 45 radius 5D": "EG",
    "Elbow 45 SR": "EH", "Elbow 60": "EI", "Elbow 90": "EJ", "Elbow 90 LR": "EA",
    "Elbow 90 radius 2D": "EK", "Elbow 90 radius 3D": "EL", "Elbow 90 radius 5D": "EM",
    "Elbow 90 SR": "EN", "Figure 8 blank": "F8", "Flange adapter": "FA",
    "Flange Blind": "FB", "Flange OF": "FO", "Flange SO": "FP", "Flange SW": "FS",
    "Flange TH": "FT", "Flange WN": "FW", "Flat ring gasket": "GF",
    "Half Coupling": "CH", "Heavy nuts": "HZ", "Lap Joint": "LJ", "Latrolet": "TL",
    "Machine Bolts": "MZ", "Nipple": "NP", "Nuts": "ZZ", "Pipe": "PP", "Plug": "CT",
    "Plug square head": "CL", "Reducer Concentric": "RC", "Reducer Coupling": "CR",
    "Reducer Eccentric": "RE", "Reducer Insert": "RI", "Reduction bushing": "RB",
    "RTJ gasket": "GR", "Sockolet": "TS", "Spiral wound gasket": "GS",
    "Stub End": "SB", "Stud bolts": "ST", "Swage nipple Concentric": "SC",
    "Swage nipple Eccentric": "SE", "Tee equal": "TE", "Tee reducer": "TR",
    "Threadolet": "TT", "Tubing": "TU", "Union": "UN", "Weldolet": "TW",
    "Paddle Blank": "FC", "Paddle Spacer": "FD", "Adapter nipple": "AN",
    "Branch connection": "BR", "Flange LJ": "FJ", "Stub End SL": "SL",
    "Elbow 90 mitered": "EP", "Elbow 45 mitered": "EQ",
    "Spiral wound gasket w/ inner ring": "GI", "Dielectric joint gasket": "GD",
    "Quick Connector MK": "MK", "Quick Connector VK": "VK",
}

EX = {
    "-": "00", "BW": "BW", "BF": "BF", "SW": "SW", "SF": "SF", "TH (NPT)": "TH",
    "RF": "RF", "FF": "FF", "RTJ": "RJ", "PE": "PE", "BE": "BE", "PBE": "PA",
    "TBE (NPT)": "TA", "BBE": "BB", "POExTOE (NPT)": "TP", "PLExTSE (NPT)": "PT",
    "TLExPSE (NPT)": "TE", "BOExTOE (NPT)": "TB", "BLExTSE (NPT)": "BT",
    "BOExPOE": "PB", "BLExPSE": "BP", "COMPRESSION": "CP", "GROOVED": "GR",
    "PRESSFIT": "PF", "TBE (BSP)": "TC", "POExTOE (BSP)": "TD",
    "PLExTSE (BSP)": "PR", "TLExPSE (BSP)": "TF", "BOExTOE (BSP)": "TG",
    "BLExTSE (BSP)": "BR", "TH (BSP)": "TI", "EF": "EF", "SV": "SV",
    "TF NPT x TM BSP": "NB", "Connection MK": "MK", "Connection VK": "VK",
}

CLASE = {
    "-": "00", "#125": "AA", "#150": "AB", "#250": "AC", "#300": "AD",
    "#400": "AE", "#600": "AF", "#900": "AG", "#1500": "AH", "#2500": "AI",
    "#2000": "AJ", "#3000": "AK", "#6000": "AL", "#9000": "AM",
    "PN2.5": "BA", "PN6": "BC", "PN10": "BD", "PN16": "BF", "PN20": "BG",
    "PN25": "BH", "PN40": "BI", "PN63": "BJ", "PN100": "BK", "PN160": "BL",
    "PN250": "BM", "PN320": "BN", "PN400": "BO",
}

SCH = {
    "-": "00", "Sch 5S": "01", "Sch 10S": "02", "Sch 10": "03", "Sch 20": "04",
    "Sch 30": "05", "Sch 40S": "06", "Sch 40": "07", "Sch STD": "08",
    "Sch 60": "09", "Sch 80S": "10", "Sch 80": "11", "Sch XS": "12",
    "Sch 100": "13", "Sch 120": "14", "Sch 140": "15", "Sch 160": "16",
    "Sch XXS": "17", "1.5mm": "18", "1.6mm": "19", "2mm": "20", "3.2mm": "21",
    "3.6mm": "22", "4mm": "23", "4.4mm": "24", "0.438\"": "25", "0.250\"": "26",
    "0.750\"": "27", "0.065\"": "28", "SDR9": "29", "SDR11": "30",
    "33.32mm": "31", "15.88mm": "32", "11.91mm": "33", "SDR13.6": "34",
    "SDR17": "35", "SDR21": "36", "0.8mm": "37",
}

ST = {
    "-": "00", "AWWA CLASS D C207": "01", "API 564": "02", "API 594": "03",
    "API 600": "04", "API 602": "05", "API 6D": "06", "ASME B16.5": "07",
    "ASME B16.9": "08", "ASME B16.10": "09", "ASME B16.11": "10",
    "ASME B16.20": "11", "ASME B16.34": "12", "ASME B16.36": "13",
    "ASME B16.39": "14", "ASME B16.47 SERIES A": "15", "ASME B16.47 SERIES B": "16",
    "ASME B18.2.1": "17", "ASME B18.2.2": "18", "ASME B36.19": "19",
    "ASME B36.10": "20", "BS 1873": "21", "DIN 8074": "22", "DIN 8078": "23",
    "DIN EN 10217-1": "24", "DIN EN 10242": "25", "DIN EN 10254": "26",
    "DIN EN 10255": "27", "DIN EN 1092-1": "28", "DIN EN 1514-1": "29",
    "DIN 16963": "30", "DIN 16966/DIN 16965": "31", "DIN-ISO 16135": "32",
    "DIN-ISO 16137": "33", "EN ISO 10931": "34", "UNE EN 10088": "35",
    "MSS-SP-67": "36", "MSS-SP-68": "37", "MSS-SP-79": "38", "MSS-SP-80": "39",
    "MSS-SP-83": "40", "MSS-SP-95": "41", "MSS-SP-97": "42", "ASME B16.48": "43",
    "ASME B16.3": "44", "ASME B16.14": "45", "ASME B16.21": "46",
    "MSS-SP-75": "47", "MSS-SP-44": "48", "ISO 4427 (49)": "49",
    "Manufacturer standard": "50", "ISO 4427 (51)": "51", "EN 12201-3": "52",
    "AWWA C950/ISO 14692": "53", "ASTM 5685/D2996": "54", "EN 12201": "55",
    "EN ISO 23856": "56", "AWWA C950/EN ISO 23856": "57", "EN ISO 15493": "58",
    "EN ISO 15494": "59", "EN 14420-6": "60",
}

MAT = {
    "-": "000", "API 5L Gr.B PSL1 (SAW)": "001", "A105N": "002", "A105": "003",
    "A106 Gr.B": "004", "A182 Gr.F22 Cl.3": "005", "A182 Gr.F5": "006",
    "A182 Gr.F9": "007", "A182 Gr.F11 Cl.2": "008", "A182 Gr.F304L": "009",
    "A182 Gr.F304": "010", "A182 Gr.F304H": "011", "A182 Gr.F321": "012",
    "A182 Gr.F316": "013", "A182 Gr.F316L": "014", "A182 Gr.F347": "015",
    "A193 Gr.B7": "016", "A193 Gr.B8": "017", "A193 Gr.B8M": "018",
    "A193 Gr.B16": "019", "A194 Gr.2H": "020", "A194 Gr.4": "021",
    "A194 Gr.7": "022", "A194 Gr.8A": "023", "A194 Gr.8M": "024",
    "A234 Gr.WPB (SMLS)": "025", "A234 Gr.WP11 Cl.3 (SMLS)": "026",
    "A234 Gr.WP22 Cl.3 (SMLS)": "027", "A234 Gr.WP22 Cl.3 (WLDD)": "028",
    "A234 Gr.WP5 (SMLS)": "029", "A234 Gr.WP5 (WLDD)": "030",
    "A234 Gr.WP9 (SMLS)": "031", "A234 Gr.WP9 (WLDD)": "032",
    "A234 Gr.WPB (WLDD)": "034", "A269 Gr.TP316": "035",
    "A312 Gr.TP304L (SMLS)": "036", "A312 Gr.TP304 (SMLS)": "037",
    "A312 Gr.TP304H (SMLS)": "038", "A312 Gr.TP316L (SMLS)": "039",
    "A312 Gr.TP316 (SMLS)": "040", "A312 Gr.TP321 (SMLS)": "041",
    "A333 Gr.6": "042", "A335 Gr.P5": "043", "A335 Gr.P9": "044",
    "A335 Gr.P11": "045", "A335 Gr.P22": "046", "A350 LF2": "047",
    "A358 Gr.304L": "048", "A358 Gr.304": "049", "A358 Gr.304H": "050",
    "A358 Gr.316L": "051", "A358 Gr.316": "052", "A358 Gr.321": "053",
    "A403 Gr.WP304L (SMLS)": "054", "A403 Gr.WP304L (WLDD)": "055",
    "A403 Gr.WP304 (SMLS)": "056", "A403 Gr.WP304 (WLDD)": "057",
    "A403 Gr.WP304H (SMLS)": "058", "A403 Gr.WP304H (WLDD)": "059",
    "A403 Gr.WP316 (SMLS)": "060", "A403 Gr.WP316 (WLDD)": "061",
    "A403 Gr.WP316L (SMLS)": "062", "A403 Gr.WP316L (WLDD)": "063",
    "A403 Gr.WP321 (SMLS)": "064", "A403 Gr.WP321 (WLDD)": "065",
    "A403 Gr.WP347 (SMLS)": "066", "A403 Gr.WP347 (WLDD)": "067",
    "A420 WPL6": "068", "A672 C70": "069", "A691 Gr.2.1/4 Cr. Cl.22": "070",
    "A691 Gr.5": "071", "A691 Gr.1.1/4": "072", "A691 Gr.2.1/4": "073",
    "A691 Gr.9": "074", "SOFT IRON": "075",
    "Filler mat. Gaph.- internal ring 316 - carbon steel outer ring": "076",
    "PE100": "077", "A53 Gr.B": "078", "A516 Gr.70": "079",
    "Filler mat. Gaph.- I.R 304 - C.S O.R": "080",
    "Aramid bonded with NBR": "081", "API 5L Gr.X42 PSL2": "082",
    "A694 Gr.WPHY 42": "083", "A694 Gr.F42": "084", "Copper": "085",
    "Flat ring neoprene rubber": "086", "A387 Gr.11 Cl.2": "087",
    "304L SS + Graphite Filler - 304 SS C.R": "088",
    "A193 Gr.B16 Bichromated": "089", "A194 Gr.7 Bichromated": "090",
    "A691 Gr. 21/4CR Cl.21": "091", "A387 Gr.22 Cl.2": "092",
    "304L SS + Mica Filler - 304 SS C.R": "093", "A335 Gr.P91": "094",
    "A234 Gr.WP91 (SMLS)": "095", "A234 Gr.WP91 (WLDD)": "096",
    "A182 Gr.F91": "097", "A387 Gr.91 Cl.2": "098",
    "304L SS + Mica Filler - 304 SS I.R. - 304 SS C.R": "099",
    "A515 Gr.70": "100", "A193 Gr.B7 Bichromated": "101",
    "A194 Gr.2H Bichromated": "102",
    "304L SS + Graphite Filler - C.S. C.R": "103",
    "304L SS + Graphite Filler - 304 I.R. - C.S. C.R": "104",
    "A106 Gr.B HDG": "105", "A105N HDG": "106", "A105 HDG": "107",
    "ASTM A536 60-42-10 HDG": "108", "A515 Gr.70 HDG": "109",
    "A193 Gr.B7 HDG": "110", "A194 Gr.2H HDG": "111",
    "A234 Gr.WPB HDG (SMLS)": "112", "A234 Gr.WPB HDG (WLDD)": "113",
    "GRP Isophtalic Resin Isophtalic Liner": "114", "EPDM": "115",
    "EPDM Maximum Hardness 70º Shore-A": "116", "PE4710": "117",
    "A269 Gr.TP316/316L (SMLS)": "118", "A182 Gr.F316/316L": "119",
}

MISC = {
    "-": "00", "Nipple L=100": "NA", "Nipple L=150": "NB",
    "Nipple L=200": "NC", "Nipple L=250": "ND",
}


# ----------------------------------------------------------------------
# UTILIDAD: búsqueda flexible dentro de un diccionario
# ----------------------------------------------------------------------
def _buscar(tabla, clave, nombre_tabla):
    """Busca `clave` en `tabla`; si no existe pero `clave` ya es un código
    válido (2-3 caracteres del set de valores), se usa directamente."""
    if clave is None:
        clave = "-"
    if clave in tabla:
        return tabla[clave]
    # ¿ya viene como código directo? (ej. material '121' que no está en catálogo)
    if clave in tabla.values() or clave.isdigit() or clave.isalpha():
        return clave
    raise KeyError(f'"{clave}" no encontrado en la tabla {nombre_tabla}. '
                    f'Revisa el nombre exacto o pasa el código directamente.')


def generar_codigo(tt, ex, clase, st, mat, dd1, dd2="-", sc1="-", sc2="-", mc="-"):
    """
    Genera el código completo del elemento.

    Cada parámetro puede ser:
      - el nombre tal como aparece en el catálogo (ej. "Elbow 90", "ASME B16.9")
      - o el código directo (ej. "13" para un diámetro, "121" para un material
        que no está en el catálogo, como en el ejemplo del Cap Drilled).

    dd2/sc2 son opcionales (solo aplican a reducciones / doble diámetro).
    """
    p1 = (
        _buscar(TT, tt, "TT")
        + _buscar(EX, ex, "EX")
        + _buscar(CLASE, clase, "CC")
        + _buscar(ST, st, "ST")
        + _buscar(MAT, mat, "MAT")
    )
    p2 = (
        _buscar(MISC, mc, "MC")
        + _buscar(DD, dd1, "DD1")
        + _buscar(DD, dd2, "DD2")
        + _buscar(SCH, sc1, "SC1")
        + _buscar(SCH, sc2, "SC2")
    )
    return f"{p1}-{p2}"


# ----------------------------------------------------------------------
# MODO INTERACTIVO
# ----------------------------------------------------------------------
def modo_interactivo():
    print("=== Generador de códigos de elementos de tubería ===")
    print("(deja en blanco y presiona Enter para usar '-' / ninguno)\n")

    def ask(msg):
        v = input(msg).strip()
        return v if v else "-"

    tt = ask("Descripción del ítem (ej. 'Elbow 90'): ")
    ex = ask("Extremos (ej. 'BW'): ")
    clase = ask("Clase (ej. '#150', o '-' si no aplica): ")
    st = ask("Estándar (ej. 'ASME B16.9'): ")
    mat = ask("Material (nombre o código directo, ej. '121'): ")
    dd1 = ask("Diámetro 1 (ej. '48' -> usar valor en mm de la tabla DD, o el código): ")
    dd2 = ask("Diámetro 2 (si aplica, si no Enter): ")
    sc1 = ask("Schedule 1 (ej. 'Sch 40', o código): ")
    sc2 = ask("Schedule 2 (si aplica, si no Enter): ")
    mc = ask("Miscelánea (ej. 'Nipple L=100', si no Enter): ")

    codigo = generar_codigo(tt, ex, clase, st, mat, dd1, dd2, sc1, sc2, mc)
    print(f"\nCódigo generado: {codigo}")


if __name__ == "__main__":
    # Ejemplo (Cap Drilled 48" -> 12", BW, ASME B16.9, material 121, Sch60):
    ejemplo = generar_codigo(
        tt="Cap Drilled", ex="BW", clase="-", st="ASME B16.9", mat="121",
        dd1="1200", dd2="300", sc1="Sch 60", sc2="-", mc="-",
    )
    print("Ejemplo (Cap Drilled 48\"->12\"):", ejemplo)

    print()
    modo_interactivo()
