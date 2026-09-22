"""
Módulo Contacto - Clase modelo con validación

@author: Profesor JV - TAME DAM
@version: 2.0
"""

import re


class Contacto:
    """Representa un contacto con validación"""
    
    def __init__(self, nombre, email, telefono):
        self.nombre = nombre.strip()
        self.email = email.strip()
        self.telefono = telefono.strip()
        self._validar()
    
    def _validar(self):
        """Valida los datos del contacto"""
        if not self.nombre:
            raise ValueError("El nombre no puede estar vacío")
        
        if not self._validar_email(self.email):
            raise ValueError("Email inválido")
        
        if not self._validar_telefono(self.telefono):
            raise ValueError("Teléfono debe tener 9 dígitos")
    
    @staticmethod
    def _validar_email(email):
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(patron, email) is not None
    
    @staticmethod
    def _validar_telefono(telefono):
        patron = r'^[0-9]{9}$'
        return re.match(patron, telefono) is not None
    
    def __str__(self):
        return f"{self.nombre} | {self.email} | {self.telefono}"
    
    def __eq__(self, otro):
        if not isinstance(otro, Contacto):
            return False
        return self.email == otro.email
    
    def a_diccionario(self):
        return {
            'nombre': self.nombre,
            'email': self.email,
            'telefono': self.telefono
        }
    
    @classmethod
    def desde_diccionario(cls, datos):
        return cls(
            datos.get('nombre', ''),
            datos.get('email', ''),
            datos.get('telefono', '')
        )
