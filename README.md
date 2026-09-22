# Gestor de Contactos - RA1 Manejo de Ficheros

## 📱 Aplicación Moderna de Gestión de Contactos

Aplicación profesional en Python con **CRUD completo** (Create, Read, Update, Delete) e **interfaz gráfica moderna** con tema oscuro.

Desarrollada para demostrar el **Resultado de Aprendizaje 1: Gestión de Ficheros** del módulo de Acceso a Datos.

---

## ✨ Características

### 🎨 Interfaz Moderna
- **Tema oscuro elegante** (dark mode)
- Colores modernos: Cyan, Verde neón, Naranja
- Diseño limpio y profesional
- Tabla interactiva
- Formularios intuitivos

### 📝 CRUD Completo
- ✅ **CREATE** - Agregar contactos con validación
- ✅ **READ** - Obtener/buscar contactos
- ✅ **UPDATE** - Modificar datos existentes
- ✅ **DELETE** - Eliminar contactos

### 💾 Múltiples Formatos
- 📄 **CSV** - Ligero y compatible
- 📄 **JSON** - Estructurado y moderno
- 📄 **XML** - Válido y profesional

---

## ✅ Criterios del RA1

| Criterio | ✓ | Implementación |
|----------|---|----------------|
| **a)** Gestión de ficheros | ✓ | `pathlib.Path`, `os` |
| **b)** Ventajas/inconvenientes | ✓ | CSV vs JSON vs XML |
| **c)** Recuperación información | ✓ | `leer_csv/json/xml()` |
| **d)** Almacenamiento | ✓ | `escribir_csv/json/xml()` |
| **e)** Conversiones formato | ✓ | CSV ↔ JSON ↔ XML |
| **f)** Manejo excepciones | ✓ | 6+ excepciones |
| **g)** Documentación/pruebas | ✓ | Documentación completa |

---

## 🚀 Instalación

### Requisitos
- Python 3.6+
- tkinter (incluido)
- **Sin dependencias externas**

### Ejecutar
```bash
python3 main.py
```

---

## 📖 Guía Rápida

| Acción | Pasos |
|--------|-------|
| **Agregar** | Rellena campos → Haz clic "➕ Agregar" |
| **Buscar** | Escribe nombre → Búsqueda en tiempo real |
| **Actualizar** | Selecciona → Modifica → "✏️ Actualizar" |
| **Eliminar** | Selecciona → "🗑️ Eliminar" → Confirma |
| **Guardar** | Elige formato → CSV/JSON/XML |
| **Cargar** | Selecciona fichero → CSV/JSON/XML |

---

## 🎨 Diseño Visual

- **Fondo:** Negro oscuro (`#0f0f0f`)
- **Paneles:** Gris oscuro (`#1a1a1a`)
- **Acentos:** Cyan (`#00d4ff`), Verde (`#00ff88`)
- **Errores:** Rojo (`#ff3333`)

---

## 📝 Licencia

Desarrollado para fines educativos - TAME DAM

**Versión:** 2.0 | **Estado:** ✅ Completo
