import tkinter as tk
from tkinter import filedialog, messagebox
import nbformat
from nbconvert import HTMLExporter, MarkdownExporter

# Función genérica para convertir notebook
def convert_notebook(input_notebook_path, output_path, exporter_class):
    try:
        with open(input_notebook_path, 'r', encoding='utf-8') as f:
            notebook_content = nbformat.read(f, as_version=4)
        
        exporter = exporter_class()
        body, _ = exporter.from_notebook_node(notebook_content)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(body)
    except Exception as e:
        messagebox.showerror("Error", f"Error al convertir el archivo: {e}")
        return False
    return True

# Función para guardar como HTML
def save_as_html():
    notebook_path = entry_file_path.get()
    if not notebook_path:
        messagebox.showerror("Error", "Por favor, selecciona un archivo .ipynb.")
        return

    save_path = filedialog.asksaveasfilename(defaultextension=".html", filetypes=[("HTML files", "*.html")])
    if save_path:
        if convert_notebook(notebook_path, save_path, HTMLExporter):
            messagebox.showinfo("Éxito", f"Convertido y guardado como HTML: {save_path}")

# Función guardar como Markdown
def save_as_markdown():
    notebook_path = entry_file_path.get()
    if not notebook_path:
        messagebox.showerror("Error", "Por favor, selecciona un archivo .ipynb.")
        return

    save_path = filedialog.asksaveasfilename(defaultextension=".md", filetypes=[("Markdown files", "*.md")])
    if save_path:
        if convert_notebook(notebook_path, save_path, MarkdownExporter):
            messagebox.showinfo("Éxito", f"Convertido y guardado como Markdown: {save_path}")

# Función para seleccionar el archivo .ipynb
def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Jupyter Notebooks", "*.ipynb")])
    if file_path:
        entry_file_path.delete(0, tk.END)
        entry_file_path.insert(0, file_path)

if __name__ == "__main__":
    # Crear la ventana de la app
    root = tk.Tk()
    root.title("Convertidor de Notebooks")

    # Título y descripción
    title_label = tk.Label(root, text="Convertidor de Notebooks", font=("Helvetica", 16))
    title_label.grid(row=0, column=0, columnspan=3, pady=10)

    description_label = tk.Label(root, text="Selecciona un archivo .ipynb y elige el formato de conversión.")
    description_label.grid(row=1, column=0, columnspan=3, pady=5)

    # Frame para la selección de archivo
    file_frame = tk.Frame(root)
    file_frame.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

    label_file_path = tk.Label(file_frame, text="Archivo .ipynb:")
    label_file_path.grid(row=0, column=0, padx=5, pady=5)

    entry_file_path = tk.Entry(file_frame, width=50)
    entry_file_path.grid(row=0, column=1, padx=5, pady=5)

    button_browse = tk.Button(file_frame, text="Seleccionar archivo", command=select_file)
    button_browse.grid(row=0, column=2, padx=5, pady=5)

    # LabelFrame para los botones de conversión
    convert_frame = tk.LabelFrame(root, text="Opciones de Conversión", labelanchor='n')
    convert_frame.grid(row=3, column=0, columnspan=3, padx=10, pady=10, ipadx=10, ipady=10)

    button_html = tk.Button(convert_frame, text="Convertir a HTML", command=save_as_html)
    button_html.grid(row=0, column=0, padx=10, pady=10)

    button_markdown = tk.Button(convert_frame, text="Convertir a Markdown", command=save_as_markdown)
    button_markdown.grid(row=0, column=1, padx=10, pady=10)

    # Label para mostrar el estado de la conversión
    status_label = tk.Label(root, text="", fg="green")
    status_label.grid(row=4, column=0, columnspan=3, pady=10)

    # Ejecutar la app
    root.mainloop()