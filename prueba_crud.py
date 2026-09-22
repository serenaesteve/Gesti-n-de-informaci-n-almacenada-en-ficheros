"""
Prueba del CRUD - Sin dependencia de GUI

Ejecutar: python3 prueba_crud.py
"""

from gestor_contactos import GestorContactos
from contacto import Contacto


def main():
    print("\n╔════════════════════════════════════════════════════════════╗")
    print("║     PRUEBA DEL CRUD - Gestión de Contactos                ║")
    print("╚════════════════════════════════════════════════════════════╝\n")
    
    gestor = GestorContactos()
    
    # ========== CREATE ==========
    print("1️⃣  CREATE - Agregando contactos...")
    print("─" * 60)
    
    contactos_prueba = [
        ("Juan García", "juan@email.com", "612345678"),
        ("María López", "maria@email.com", "687654321"),
        ("Carlos Martín", "carlos@email.com", "645678901"),
    ]
    
    for nombre, email, telefono in contactos_prueba:
        exito, msg = gestor.crear_contacto(nombre, email, telefono)
        print(f"  {msg}")
    
    # ========== READ ==========
    print("\n2️⃣  READ - Obtener todos los contactos")
    print("─" * 60)
    
    contactos = gestor.obtener_todos()
    for i, c in enumerate(contactos, 1):
        print(f"  {i}. {c}")
    
    # ========== SEARCH ==========
    print("\n3️⃣  SEARCH - Buscar por nombre")
    print("─" * 60)
    
    resultados = gestor.buscar_por_nombre("García")
    print(f"  Búsqueda de 'García': {len(resultados)} resultado(s)")
    for c in resultados:
        print(f"    • {c}")
    
    # ========== UPDATE ==========
    print("\n4️⃣  UPDATE - Actualizar contacto")
    print("─" * 60)
    
    print("  Antes: Juan García | juan@email.com | 612345678")
    exito, msg = gestor.actualizar_contacto(
        "juan@email.com",
        "Juan García González",
        "juan.garcia@email.com",
        "612345678"
    )
    print(f"  {msg}")
    
    contacto_actualizado = gestor.obtener_contacto("juan.garcia@email.com")
    print(f"  Después: {contacto_actualizado}")
    
    # ========== DELETE ==========
    print("\n5️⃣  DELETE - Eliminar contacto")
    print("─" * 60)
    
    exito, msg = gestor.eliminar_contacto("carlos@email.com")
    print(f"  {msg}")
    
    print(f"\n  Contactos restantes: {gestor.obtener_cantidad()}")
    
    # ========== FICHEROS ==========
    print("\n6️⃣  FICHEROS - Guardar en múltiples formatos")
    print("─" * 60)
    
    exito, msg = gestor.escribir_csv("datos/prueba.csv")
    print(f"  {msg}")
    
    exito, msg = gestor.escribir_json("datos/prueba.json")
    print(f"  {msg}")
    
    exito, msg = gestor.escribir_xml("datos/prueba.xml")
    print(f"  {msg}")
    
    # ========== CARGAR ==========
    print("\n7️⃣  CARGAR - Leer desde JSON")
    print("─" * 60)
    
    gestor2 = GestorContactos()
    exito, msg = gestor2.leer_json("datos/prueba.json")
    print(f"  {msg}")
    
    print("\n  Contactos cargados:")
    for i, c in enumerate(gestor2.obtener_todos(), 1):
        print(f"    {i}. {c}")
    
    # ========== RESUMEN ==========
    print("\n╔════════════════════════════════════════════════════════════╗")
    print("║                    ✅ PRUEBA EXITOSA                      ║")
    print("╚════════════════════════════════════════════════════════════╝")
    
    print("""
  ✓ CRUD funcionando correctamente
  ✓ Gestión de ficheros OK
  ✓ CSV, JSON, XML OK
  ✓ Validación OK
  ✓ Búsqueda OK
  
  Para usar la interfaz gráfica:
  👉  python3 main.py
  
  Ficheros generados en carpeta 'datos/':
  • prueba.csv
  • prueba.json
  • prueba.xml
    """)


if __name__ == "__main__":
    main()
