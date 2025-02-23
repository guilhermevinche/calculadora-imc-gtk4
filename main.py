#!/usr/bin/env python3
import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

class CalculadoraIMC(Gtk.ApplicationWindow):
    def __init__(self, app):
        super().__init__(application=app)

        self.set_title("Calculadora IMC - GTK 4")
        self.set_default_size(300, 200)

        # Box
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox.set_margin_top(10)
        vbox.set_margin_bottom(10)
        vbox.set_margin_start(10)
        vbox.set_margin_end(10)
        self.set_child(vbox)

        # Input peso
        self.entry_peso = Gtk.Entry()
        self.entry_peso.set_placeholder_text("Peso (KG) - 000.0")
        vbox.append(self.entry_peso)

        # Input altura
        self.entry_altura = Gtk.Entry()
        self.entry_altura.set_placeholder_text("Altura (Mt) - 0.00")
        vbox.append(self.entry_altura)

        # Botão de calcular
        self.btn_calcular = Gtk.Button(label="Calcular")
        self.btn_calcular.connect("clicked", self.calcular_soma)
        vbox.append(self.btn_calcular)

        # Label de resultado
        self.label_resultado = Gtk.Label(label="Resultado: ")
        vbox.append(self.label_resultado)
        self.label_classificacao = Gtk.Label()
        vbox.append(self.label_classificacao)
        
    def calcular_soma(self, button):
        # Cálculo e classificação do IMC
        try:
            peso = float(self.entry_peso.get_text())
            altura = float(self.entry_altura.get_text())
            resultado = peso / (altura * altura)

            if resultado < 18.5:
                self.label_resultado.set_text(f"Resultado: {resultado:.2f}")
                self.label_classificacao.set_text(f"Magreza")
            elif (resultado >= 18.5) and (resultado <= 24.9):
                self.label_resultado.set_text(f"Resultado: {resultado:.2f}")
                self.label_classificacao.set_text(f"Normal")
            elif (resultado >= 25.0) and (resultado <= 29.9):
                self.label_resultado.set_text(f"Resultado: {resultado:.2f}")
                self.label_classificacao.set_text(f"Sobrepeso")
            elif (resultado >= 30.0) and (resultado <= 39.9):
                self.label_resultado.set_text(f"Resultado: {resultado:.2f}")
                self.label_classificacao.set_text(f"Obesidade")
            elif resultado > 40.0:
                self.label_resultado.set_text(f"Resultado: {resultado:.2f}")
                self.label_classificacao.set_text(f"Obesidade Grave")
        except ValueError:
            self.label_resultado.set_text("Erro: Digite números válidos")

# Aplicação
class CalculadoraApp(Gtk.Application):
    def __init__(self):
        super().__init__()

    def do_activate(self):
        # Cria e exibe a janela principal ao iniciar a aplicação.
        win = CalculadoraIMC(self)
        win.present()

if __name__ == "__main__":
    app = CalculadoraApp()
    app.run()
