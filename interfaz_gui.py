"""
Interfaz Gráfica Moderna - Aplicación de Gestión de Contactos

Tema oscuro elegante con colores modernos

@author: Profesor JV - TAME DAM
@version: 2.0
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from gestor_contactos import GestorContactos
from contacto import Contacto


# ========== COLORES PERSONALIZADOS ==========
COLORES = {
    'bg_principal': '#0f0f0f',      # Negro oscuro
    'bg_secundario': '#1a1a1a',     # Gris muy oscuro
    'bg_terciario': '#2a2a2a',      # Gris oscuro
    'fg_principal': '#ffffff',       # Blanco
    'fg_secundario': '#b0b0b0',      # Gris claro
    'acento1': '#00d4ff',            # Cyan
    'acento2': '#00ff88',            # Verde neón
    'acento3': '#ff6b00',            # Naranja
    'error': '#ff3333',              # Rojo
    'success': '#00ff88',            # Verde
    'borde': '#404040',              # Gris borde
}


class InterfazContactos:
    """Interfaz gráfica moderna para gestión de contactos"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Contactos")
        self.root.geometry("1200x700")
        self.root.configure(bg=COLORES['bg_principal'])
        self.root.resizable(True, True)
        
        self.gestor = GestorContactos()
        
        # Configurar estilo
        self._configurar_estilo()
        self._crear_interfaz()
        self._actualizar_tabla()
    
    def _configurar_estilo(self):
        """Configura el tema oscuro"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Colores para elementos
        style.configure('TFrame', background=COLORES['bg_principal'])
        style.configure('TLabel', background=COLORES['bg_principal'], foreground=COLORES['fg_principal'])
        style.configure('TButton', font=('Segoe UI', 9, 'bold'))
        style.map('TButton', foreground=[('active', COLORES['acento1'])])
        
        style.configure('TEntry', fieldbackground=COLORES['bg_terciario'], 
                       foreground=COLORES['fg_principal'], font=('Segoe UI', 10))
        
        style.configure('Treeview', background=COLORES['bg_terciario'], 
                       foreground=COLORES['fg_principal'], fieldbackground=COLORES['bg_terciario'],
                       font=('Segoe UI', 9))
        style.configure('Treeview.Heading', background=COLORES['bg_secundario'], 
                       foreground=COLORES['acento1'], font=('Segoe UI', 10, 'bold'))
    
    def _crear_interfaz(self):
        """Crea la interfaz gráfica"""
        
        # Frame principal
        main_frame = tk.Frame(self.root, bg=COLORES['bg_principal'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        # ========== HEADER ==========
        self._crear_header(main_frame)
        
        # ========== CONTENEDOR PRINCIPAL ==========
        container = tk.Frame(main_frame, bg=COLORES['bg_principal'])
        container.pack(fill=tk.BOTH, expand=True, pady=(15, 0))
        
        # Frame izquierdo (formulario)
        left_frame = tk.Frame(container, bg=COLORES['bg_principal'])
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, padx=(0, 15))
        
        # Frame derecho (tabla)
        right_frame = tk.Frame(container, bg=COLORES['bg_principal'])
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # ========== FORMULARIO ==========
        self._crear_formulario(left_frame)
        
        # ========== TABLA ==========
        self._crear_tabla(right_frame)
        
        # ========== FOOTER ==========
        self._crear_footer(main_frame)
    
    def _crear_header(self, parent):
        """Crea el encabezado"""
        header = tk.Frame(parent, bg=COLORES['bg_principal'])
        header.pack(fill=tk.X, pady=(0, 15))
        
        titulo = tk.Label(header, text="Gestor de Contactos", 
                         bg=COLORES['bg_principal'], fg=COLORES['acento1'],
                         font=('Segoe UI', 28, 'bold'))
        titulo.pack(anchor=tk.W)
        
        subtitulo = tk.Label(header, text="Manage your contacts • CSV, JSON, XML", 
                            bg=COLORES['bg_principal'], fg=COLORES['fg_secundario'],
                            font=('Segoe UI', 11))
        subtitulo.pack(anchor=tk.W, pady=(5, 0))
        
        # Línea divisora
        linea = tk.Frame(parent, bg=COLORES['borde'], height=1)
        linea.pack(fill=tk.X, pady=(10, 0))
    
    def _crear_formulario(self, parent):
        """Crea el formulario de entrada"""
        
        # Contenedor formulario
        form_frame = tk.Frame(parent, bg=COLORES['bg_secundario'], 
                             relief=tk.FLAT, borderwidth=0)
        form_frame.pack(fill=tk.BOTH, padx=0, pady=0)
        
        # Ajustar ancho del formulario
        form_frame.configure(width=350)
        
        # Título
        titulo = tk.Label(form_frame, text="Nuevo Contacto", 
                         bg=COLORES['bg_secundario'], fg=COLORES['acento2'],
                         font=('Segoe UI', 14, 'bold'))
        titulo.pack(anchor=tk.W, padx=20, pady=(20, 15))
        
        # Campo Nombre
        self._crear_campo_entrada(form_frame, "Nombre", "nombre")
        
        # Campo Email
        self._crear_campo_entrada(form_frame, "Email", "email")
        
        # Campo Teléfono
        self._crear_campo_entrada(form_frame, "Teléfono", "telefono")
        
        # Botones
        botones_frame = tk.Frame(form_frame, bg=COLORES['bg_secundario'])
        botones_frame.pack(fill=tk.X, padx=20, pady=(20, 20))
        
        self._crear_boton(botones_frame, "➕ Agregar", self._agregar_contacto, 
                         bg=COLORES['acento2'], fg=COLORES['bg_principal']).pack(fill=tk.X, pady=(0, 10))
        
        self._crear_boton(botones_frame, "✏️  Actualizar", self._actualizar_contacto,
                         bg=COLORES['acento1'], fg=COLORES['bg_principal']).pack(fill=tk.X, pady=(0, 10))
        
        self._crear_boton(botones_frame, "🗑️  Eliminar", self._eliminar_contacto,
                         bg=COLORES['error'], fg=COLORES['fg_principal']).pack(fill=tk.X, pady=(0, 10))
        
        self._crear_boton(botones_frame, "🔄 Limpiar", self._limpiar_campos,
                         bg=COLORES['fg_secundario'], fg=COLORES['bg_principal']).pack(fill=tk.X)
        
        # Separador
        sep = tk.Frame(form_frame, bg=COLORES['borde'], height=1)
        sep.pack(fill=tk.X, pady=(20, 15), padx=20)
        
        # Sección Búsqueda
        busqueda_titulo = tk.Label(form_frame, text="Búsqueda", 
                                  bg=COLORES['bg_secundario'], fg=COLORES['acento1'],
                                  font=('Segoe UI', 12, 'bold'))
        busqueda_titulo.pack(anchor=tk.W, padx=20, pady=(0, 10))
        
        busqueda_inner = tk.Frame(form_frame, bg=COLORES['bg_secundario'])
        busqueda_inner.pack(fill=tk.X, padx=20, pady=(0, 20))
        
        self.entry_busqueda = tk.Entry(busqueda_inner, bg=COLORES['bg_terciario'],
                                       fg=COLORES['fg_principal'], font=('Segoe UI', 10),
                                       insertbackground=COLORES['acento1'], 
                                       relief=tk.FLAT, borderwidth=1)
        self.entry_busqueda.pack(fill=tk.X, pady=(0, 10))
        self.entry_busqueda.bind('<KeyRelease>', lambda e: self._buscar_contactos())
        
        btn_buscar = tk.Frame(busqueda_inner, bg=COLORES['bg_secundario'])
        btn_buscar.pack(fill=tk.X)
        
        self._crear_boton(btn_buscar, "🔍 Buscar", self._buscar_contactos,
                         bg=COLORES['acento1'], fg=COLORES['bg_principal'], 
                         width=16).pack(side=tk.LEFT, padx=(0, 5))
        
        self._crear_boton(btn_buscar, "Mostrar todos", self._mostrar_todos,
                         bg=COLORES['fg_secundario'], fg=COLORES['bg_principal'],
                         width=16).pack(side=tk.LEFT)
    
    def _crear_campo_entrada(self, parent, etiqueta, variable_name):
        """Crea un campo de entrada con etiqueta"""
        frame = tk.Frame(parent, bg=COLORES['bg_secundario'])
        frame.pack(fill=tk.X, padx=20, pady=(0, 12))
        
        label = tk.Label(frame, text=etiqueta, bg=COLORES['bg_secundario'],
                        fg=COLORES['acento1'], font=('Segoe UI', 10, 'bold'))
        label.pack(anchor=tk.W, pady=(0, 5))
        
        entry = tk.Entry(frame, bg=COLORES['bg_terciario'], fg=COLORES['fg_principal'],
                        font=('Segoe UI', 10), insertbackground=COLORES['acento1'],
                        relief=tk.FLAT, borderwidth=1)
        entry.pack(fill=tk.X, ipady=8)
        
        setattr(self, f'entry_{variable_name}', entry)
    
    def _crear_boton(self, parent, texto, comando, bg=None, fg=None, width=None):
        """Crea un botón personalizado"""
        if bg is None:
            bg = COLORES['acento1']
        if fg is None:
            fg = COLORES['bg_principal']
        
        btn = tk.Button(parent, text=texto, command=comando, bg=bg, fg=fg,
                       font=('Segoe UI', 10, 'bold'), relief=tk.FLAT, 
                       borderwidth=0, cursor='hand2', padx=15, pady=10,
                       activebackground=self._ajustar_color(bg, 1.2),
                       activeforeground=fg)
        
        if width:
            btn.configure(width=width)
        
        return btn
    
    def _ajustar_color(self, color_hex, factor):
        """Ajusta el brillo de un color hex"""
        color_hex = color_hex.lstrip('#')
        r, g, b = tuple(int(color_hex[i:i+2], 16) for i in (0, 2, 4))
        r = min(255, int(r * factor))
        g = min(255, int(g * factor))
        b = min(255, int(b * factor))
        return f'#{r:02x}{g:02x}{b:02x}'
    
    def _crear_tabla(self, parent):
        """Crea la tabla de contactos"""
        
        # Contenedor tabla
        tabla_container = tk.Frame(parent, bg=COLORES['bg_secundario'])
        tabla_container.pack(fill=tk.BOTH, expand=True)
        
        # Encabezado
        titulo = tk.Label(tabla_container, text="Contactos", 
                         bg=COLORES['bg_secundario'], fg=COLORES['acento2'],
                         font=('Segoe UI', 14, 'bold'))
        titulo.pack(anchor=tk.W, padx=20, pady=(20, 15))
        
        # Frame para tabla y scrollbar
        tabla_frame = tk.Frame(tabla_container, bg=COLORES['bg_terciario'])
        tabla_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 20))
        
        # Scrollbar
        scrollbar = tk.Scrollbar(tabla_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Tabla
        self.tabla = ttk.Treeview(tabla_frame, columns=('Nombre', 'Email', 'Teléfono'),
                                 height=20, yscrollcommand=scrollbar.set,
                                 style='Treeview')
        scrollbar.config(command=self.tabla.yview)
        
        # Configurar columnas
        self.tabla.column('#0', width=0, stretch=tk.NO)
        self.tabla.column('Nombre', anchor=tk.W, width=200)
        self.tabla.column('Email', anchor=tk.W, width=250)
        self.tabla.column('Teléfono', anchor=tk.CENTER, width=120)
        
        # Encabezados
        self.tabla.heading('#0', text='')
        self.tabla.heading('Nombre', text='Nombre')
        self.tabla.heading('Email', text='Email')
        self.tabla.heading('Teléfono', text='Teléfono')
        
        # Estilos de fila
        self.tabla.tag_configure('oddrow', background=COLORES['bg_terciario'])
        self.tabla.tag_configure('evenrow', background=COLORES['bg_secundario'])
        
        self.tabla.pack(fill=tk.BOTH, expand=True)
        self.tabla.bind('<ButtonRelease-1>', self._seleccionar_fila)
    
    def _crear_footer(self, parent):
        """Crea el pie de página"""
        
        footer = tk.Frame(parent, bg=COLORES['bg_principal'])
        footer.pack(fill=tk.X, pady=(15, 0))
        
        # Línea divisora
        linea = tk.Frame(parent, bg=COLORES['borde'], height=1)
        linea.pack(fill=tk.X, pady=(0, 15))
        
        # Frame de botones
        btn_frame = tk.Frame(footer, bg=COLORES['bg_principal'])
        btn_frame.pack(fill=tk.X, side=tk.LEFT)
        
        tk.Label(btn_frame, text="📁 Ficheros:", bg=COLORES['bg_principal'],
                fg=COLORES['fg_secundario'], font=('Segoe UI', 9)).pack(side=tk.LEFT, padx=(0, 10))
        
        self._crear_boton(btn_frame, "CSV", self._guardar_csv,
                         bg=COLORES['acento1'], fg=COLORES['bg_principal']).pack(side=tk.LEFT, padx=3)
        self._crear_boton(btn_frame, "JSON", self._guardar_json,
                         bg=COLORES['acento1'], fg=COLORES['bg_principal']).pack(side=tk.LEFT, padx=3)
        self._crear_boton(btn_frame, "XML", self._guardar_xml,
                         bg=COLORES['acento1'], fg=COLORES['bg_principal']).pack(side=tk.LEFT, padx=3)
        
        # Separador
        tk.Label(btn_frame, text="│", bg=COLORES['bg_principal'],
                fg=COLORES['borde']).pack(side=tk.LEFT, padx=10)
        
        tk.Label(btn_frame, text="📂 Cargar:", bg=COLORES['bg_principal'],
                fg=COLORES['fg_secundario'], font=('Segoe UI', 9)).pack(side=tk.LEFT, padx=(0, 10))
        
        self._crear_boton(btn_frame, "CSV", self._cargar_csv,
                         bg=COLORES['acento3'], fg=COLORES['fg_principal']).pack(side=tk.LEFT, padx=3)
        self._crear_boton(btn_frame, "JSON", self._cargar_json,
                         bg=COLORES['acento3'], fg=COLORES['fg_principal']).pack(side=tk.LEFT, padx=3)
        self._crear_boton(btn_frame, "XML", self._cargar_xml,
                         bg=COLORES['acento3'], fg=COLORES['fg_principal']).pack(side=tk.LEFT, padx=3)
        
        # Label estado
        self.label_estado = tk.Label(footer, text="0 contactos", 
                                    bg=COLORES['bg_principal'], fg=COLORES['acento1'],
                                    font=('Segoe UI', 9, 'bold'))
        self.label_estado.pack(side=tk.RIGHT, padx=0)
    
    # ==================== MÉTODOS CRUD ====================
    
    def _agregar_contacto(self):
        nombre = self.entry_nombre.get().strip()
        email = self.entry_email.get().strip()
        telefono = self.entry_telefono.get().strip()
        
        if not nombre or not email or not telefono:
            messagebox.showwarning("Incompleto", "Completa todos los campos")
            return
        
        exito, mensaje = self.gestor.crear_contacto(nombre, email, telefono)
        
        if exito:
            messagebox.showinfo("Éxito", mensaje)
            self._limpiar_campos()
            self._actualizar_tabla()
        else:
            messagebox.showerror("Error", mensaje)
    
    def _actualizar_tabla(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        
        contactos = self.gestor.obtener_todos()
        for i, contacto in enumerate(contactos):
            tag = 'oddrow' if i % 2 == 0 else 'evenrow'
            self.tabla.insert('', tk.END, values=(
                contacto.nombre, contacto.email, contacto.telefono
            ), tags=(tag,))
        
        cantidad = self.gestor.obtener_cantidad()
        self.label_estado.config(text=f"{cantidad} contacto{'s' if cantidad != 1 else ''}")
    
    def _seleccionar_fila(self, event):
        seleccion = self.tabla.selection()
        if seleccion:
            item = seleccion[0]
            valores = self.tabla.item(item)['values']
            
            self.entry_nombre.delete(0, tk.END)
            self.entry_nombre.insert(0, valores[0])
            
            self.entry_email.delete(0, tk.END)
            self.entry_email.insert(0, valores[1])
            
            self.entry_telefono.delete(0, tk.END)
            self.entry_telefono.insert(0, valores[2])
    
    def _buscar_contactos(self):
        nombre = self.entry_busqueda.get().strip()
        
        if not nombre:
            self._actualizar_tabla()
            return
        
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        
        resultados = self.gestor.buscar_por_nombre(nombre)
        
        for i, contacto in enumerate(resultados):
            tag = 'oddrow' if i % 2 == 0 else 'evenrow'
            self.tabla.insert('', tk.END, values=(
                contacto.nombre, contacto.email, contacto.telefono
            ), tags=(tag,))
        
        if not resultados:
            messagebox.showinfo("Búsqueda", f"No encontrado: '{nombre}'")
    
    def _mostrar_todos(self):
        self.entry_busqueda.delete(0, tk.END)
        self._actualizar_tabla()
    
    def _actualizar_contacto(self):
        email_original = self.entry_email.get().strip()
        
        if not email_original:
            messagebox.showwarning("Seleccionar", "Selecciona un contacto")
            return
        
        nombre = self.entry_nombre.get().strip()
        email = self.entry_email.get().strip()
        telefono = self.entry_telefono.get().strip()
        
        if not nombre or not email or not telefono:
            messagebox.showwarning("Incompleto", "Completa todos los campos")
            return
        
        exito, mensaje = self.gestor.actualizar_contacto(email_original, nombre, email, telefono)
        
        if exito:
            messagebox.showinfo("Éxito", mensaje)
            self._limpiar_campos()
            self._actualizar_tabla()
        else:
            messagebox.showerror("Error", mensaje)
    
    def _eliminar_contacto(self):
        email = self.entry_email.get().strip()
        
        if not email:
            messagebox.showwarning("Seleccionar", "Selecciona un contacto")
            return
        
        if messagebox.askyesno("Confirmar", f"¿Eliminar '{self.entry_nombre.get()}'?"):
            exito, mensaje = self.gestor.eliminar_contacto(email)
            
            if exito:
                messagebox.showinfo("Éxito", mensaje)
                self._limpiar_campos()
                self._actualizar_tabla()
            else:
                messagebox.showerror("Error", mensaje)
    
    def _limpiar_campos(self):
        self.entry_nombre.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_telefono.delete(0, tk.END)
        self.entry_busqueda.delete(0, tk.END)
    
    # ==================== FICHEROS ====================
    
    def _guardar_csv(self):
        ruta = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV", "*.csv"), ("Todos", "*.*")],
            initialfile="contactos.csv"
        )
        
        if ruta:
            exito, mensaje = self.gestor.escribir_csv(ruta)
            if exito:
                messagebox.showinfo("Éxito", mensaje)
            else:
                messagebox.showerror("Error", mensaje)
    
    def _guardar_json(self):
        ruta = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON", "*.json"), ("Todos", "*.*")],
            initialfile="contactos.json"
        )
        
        if ruta:
            exito, mensaje = self.gestor.escribir_json(ruta)
            if exito:
                messagebox.showinfo("Éxito", mensaje)
            else:
                messagebox.showerror("Error", mensaje)
    
    def _guardar_xml(self):
        ruta = filedialog.asksaveasfilename(
            defaultextension=".xml",
            filetypes=[("XML", "*.xml"), ("Todos", "*.*")],
            initialfile="contactos.xml"
        )
        
        if ruta:
            exito, mensaje = self.gestor.escribir_xml(ruta)
            if exito:
                messagebox.showinfo("Éxito", mensaje)
            else:
                messagebox.showerror("Error", mensaje)
    
    def _cargar_csv(self):
        ruta = filedialog.askopenfilename(
            filetypes=[("CSV", "*.csv"), ("Todos", "*.*")]
        )
        
        if ruta:
            exito, mensaje = self.gestor.leer_csv(ruta)
            if exito:
                messagebox.showinfo("Éxito", mensaje)
                self._actualizar_tabla()
            else:
                messagebox.showerror("Error", mensaje)
    
    def _cargar_json(self):
        ruta = filedialog.askopenfilename(
            filetypes=[("JSON", "*.json"), ("Todos", "*.*")]
        )
        
        if ruta:
            exito, mensaje = self.gestor.leer_json(ruta)
            if exito:
                messagebox.showinfo("Éxito", mensaje)
                self._actualizar_tabla()
            else:
                messagebox.showerror("Error", mensaje)
    
    def _cargar_xml(self):
        ruta = filedialog.askopenfilename(
            filetypes=[("XML", "*.xml"), ("Todos", "*.*")]
        )
        
        if ruta:
            exito, mensaje = self.gestor.leer_xml(ruta)
            if exito:
                messagebox.showinfo("Éxito", mensaje)
                self._actualizar_tabla()
            else:
                messagebox.showerror("Error", mensaje)


def main():
    root = tk.Tk()
    app = InterfazContactos(root)
    root.mainloop()


if __name__ == "__main__":
    main()
