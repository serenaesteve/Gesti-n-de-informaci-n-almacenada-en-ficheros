"""
Módulo GestorContactos - CRUD completo con múltiples formatos

@author: Profesor JV - TAME DAM
@version: 2.0
"""

import os
import json
import csv
import xml.etree.ElementTree as ET
from pathlib import Path
from contacto import Contacto
from datetime import datetime


class GestorContactos:
    """Gestor completo de contactos con CRUD"""
    
    CARPETA_DATOS = 'datos'
    ARCHIVO_CSV = 'datos/contactos.csv'
    ARCHIVO_JSON = 'datos/contactos.json'
    ARCHIVO_XML = 'datos/contactos.xml'
    
    def __init__(self):
        self.contactos = []
        self.archivo_actual = None
        self._crear_carpeta_datos()
    
    def _crear_carpeta_datos(self):
        try:
            Path(self.CARPETA_DATOS).mkdir(exist_ok=True)
        except OSError:
            pass
    
    # ==================== CREATE ====================
    
    def crear_contacto(self, nombre, email, telefono):
        """Crea un nuevo contacto"""
        try:
            if self._existe_contacto(email):
                return False, f"Email {email} ya existe"
            
            contacto = Contacto(nombre, email, telefono)
            self.contactos.append(contacto)
            return True, f"✓ Contacto creado"
            
        except ValueError as e:
            return False, f"✗ {e}"
        except Exception as e:
            return False, f"✗ Error: {e}"
    
    # ==================== READ ====================
    
    def obtener_contacto(self, email):
        """Obtiene un contacto por email"""
        for contacto in self.contactos:
            if contacto.email == email:
                return contacto
        return None
    
    def obtener_todos(self):
        """Retorna todos los contactos"""
        return self.contactos.copy()
    
    def buscar_por_nombre(self, nombre):
        """Busca contactos por nombre"""
        resultado = []
        nombre_lower = nombre.lower()
        for contacto in self.contactos:
            if nombre_lower in contacto.nombre.lower():
                resultado.append(contacto)
        return resultado
    
    def buscar_por_email(self, email):
        """Busca un contacto por email"""
        email_lower = email.lower()
        for contacto in self.contactos:
            if email_lower in contacto.email.lower():
                return contacto
        return None
    
    def _existe_contacto(self, email):
        """Verifica si existe un contacto"""
        return self.obtener_contacto(email) is not None
    
    # ==================== UPDATE ====================
    
    def actualizar_contacto(self, email_original, nombre, email, telefono):
        """Actualiza un contacto"""
        try:
            contacto = self.obtener_contacto(email_original)
            if not contacto:
                return False, f"Contacto no encontrado"
            
            if email != email_original and self._existe_contacto(email):
                return False, f"Email ya en uso"
            
            nuevo_contacto = Contacto(nombre, email, telefono)
            contacto.nombre = nuevo_contacto.nombre
            contacto.email = nuevo_contacto.email
            contacto.telefono = nuevo_contacto.telefono
            
            return True, f"✓ Contacto actualizado"
            
        except ValueError as e:
            return False, f"✗ {e}"
        except Exception as e:
            return False, f"✗ Error: {e}"
    
    # ==================== DELETE ====================
    
    def eliminar_contacto(self, email):
        """Elimina un contacto"""
        try:
            contacto = self.obtener_contacto(email)
            if not contacto:
                return False, f"Contacto no encontrado"
            
            self.contactos.remove(contacto)
            return True, f"✓ Contacto eliminado"
            
        except Exception as e:
            return False, f"✗ Error: {e}"
    
    def limpiar_contactos(self):
        """Elimina todos los contactos"""
        self.contactos.clear()
        return True, "Todos los contactos eliminados"
    
    # ==================== FICHEROS ====================
    
    def leer_csv(self, ruta):
        """Lee contactos desde CSV"""
        try:
            if not os.path.exists(ruta):
                raise FileNotFoundError(f"Archivo no encontrado")
            
            self.contactos.clear()
            
            with open(ruta, 'r', encoding='utf-8') as archivo:
                lector = csv.DictReader(archivo)
                for fila in lector:
                    try:
                        contacto = Contacto(
                            fila['nombre'].strip(),
                            fila['email'].strip(),
                            fila['telefono'].strip()
                        )
                        self.contactos.append(contacto)
                    except ValueError:
                        continue
            
            self.archivo_actual = ruta
            return True, f"✓ {len(self.contactos)} contactos cargados"
            
        except FileNotFoundError as e:
            return False, f"✗ {e}"
        except Exception as e:
            return False, f"✗ Error: {e}"
    
    def leer_json(self, ruta):
        """Lee contactos desde JSON"""
        try:
            if not os.path.exists(ruta):
                raise FileNotFoundError(f"Archivo no encontrado")
            
            self.contactos.clear()
            
            with open(ruta, 'r', encoding='utf-8') as archivo:
                datos = json.load(archivo)
                lista = datos.get('contactos', datos if isinstance(datos, list) else [])
                
                for item in lista:
                    try:
                        contacto = Contacto.desde_diccionario(item)
                        self.contactos.append(contacto)
                    except ValueError:
                        continue
            
            self.archivo_actual = ruta
            return True, f"✓ {len(self.contactos)} contactos cargados"
            
        except FileNotFoundError as e:
            return False, f"✗ {e}"
        except json.JSONDecodeError:
            return False, f"✗ JSON inválido"
        except Exception as e:
            return False, f"✗ Error: {e}"
    
    def leer_xml(self, ruta):
        """Lee contactos desde XML"""
        try:
            if not os.path.exists(ruta):
                raise FileNotFoundError(f"Archivo no encontrado")
            
            self.contactos.clear()
            arbol = ET.parse(ruta)
            raiz = arbol.getroot()
            
            for elemento in raiz.findall('contacto'):
                try:
                    nombre = elemento.find('nombre').text or ''
                    email = elemento.find('email').text or ''
                    telefono = elemento.find('telefono').text or ''
                    
                    contacto = Contacto(nombre, email, telefono)
                    self.contactos.append(contacto)
                except ValueError:
                    continue
            
            self.archivo_actual = ruta
            return True, f"✓ {len(self.contactos)} contactos cargados"
            
        except FileNotFoundError as e:
            return False, f"✗ {e}"
        except ET.ParseError:
            return False, f"✗ XML inválido"
        except Exception as e:
            return False, f"✗ Error: {e}"
    
    def escribir_csv(self, ruta):
        """Escribe contactos en CSV"""
        try:
            with open(ruta, 'w', newline='', encoding='utf-8') as archivo:
                writer = csv.DictWriter(archivo, fieldnames=['nombre', 'email', 'telefono'])
                writer.writeheader()
                for contacto in self.contactos:
                    writer.writerow(contacto.a_diccionario())
            
            self.archivo_actual = ruta
            return True, f"✓ Guardado en CSV"
            
        except IOError as e:
            return False, f"✗ Error: {e}"
    
    def escribir_json(self, ruta):
        """Escribe contactos en JSON"""
        try:
            datos = {
                'contactos': [c.a_diccionario() for c in self.contactos],
                'fecha_guardado': datetime.now().isoformat()
            }
            
            with open(ruta, 'w', encoding='utf-8') as archivo:
                json.dump(datos, archivo, indent=2, ensure_ascii=False)
            
            self.archivo_actual = ruta
            return True, f"✓ Guardado en JSON"
            
        except IOError as e:
            return False, f"✗ Error: {e}"
    
    def escribir_xml(self, ruta):
        """Escribe contactos en XML"""
        try:
            raiz = ET.Element('contactos')
            
            for contacto in self.contactos:
                elem_contacto = ET.SubElement(raiz, 'contacto')
                
                elem_nombre = ET.SubElement(elem_contacto, 'nombre')
                elem_nombre.text = contacto.nombre
                
                elem_email = ET.SubElement(elem_contacto, 'email')
                elem_email.text = contacto.email
                
                elem_telefono = ET.SubElement(elem_contacto, 'telefono')
                elem_telefono.text = contacto.telefono
            
            self._indentar_xml(raiz)
            arbol = ET.ElementTree(raiz)
            arbol.write(ruta, encoding='utf-8', xml_declaration=True)
            
            self.archivo_actual = ruta
            return True, f"✓ Guardado en XML"
            
        except IOError as e:
            return False, f"✗ Error: {e}"
    
    @staticmethod
    def _indentar_xml(elem, nivel=0):
        indentacion = "\n" + nivel * "  "
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = indentacion + "  "
            if not elem.tail or not elem.tail.strip():
                elem.tail = indentacion
            for hijo in elem:
                GestorContactos._indentar_xml(hijo, nivel + 1)
            if not hijo.tail or not hijo.tail.strip():
                hijo.tail = indentacion
        else:
            if nivel and (not elem.tail or not elem.tail.strip()):
                elem.tail = indentacion
    
    def obtener_cantidad(self):
        return len(self.contactos)
    
    def ordenar_por_nombre(self):
        self.contactos.sort(key=lambda x: x.nombre.lower())
