import tkinter as tk
from tkinter.messagebox import showerror

oceny = (1, 2, 3, 4, 5, 6)
przedmioty = ("biologia", "geografia", "historia", "informatyka", "język angielski", "język polski", "matematyka",
              "muzyka", "plastyka", "religia", "technika", "wychowanie fizyczne", "zachowanie")


class Aplikacja:
    def __init__(self):
        self.root = tk.Tk()

        #   Utworzenie etykiet dla każdego przedmiotu
        i = 0
        for przedmiot in przedmioty:
            tk.Label(self.root, text=przedmiot).grid(row=i, column=0)
            i += 1

        #   Utworzenie pola wejściowego dla każdego przedmiotu
        self.biologia = tk.Entry(self.root)
        self.biologia.grid(row=0, column=1)
        self.geografia = tk.Entry(self.root)
        self.geografia.grid(row=1, column=1)
        self.historia = tk.Entry(self.root)
        self.historia.grid(row=2, column=1)
        self.informatyka = tk.Entry(self.root)
        self.informatyka.grid(row=3, column=1)
        self.angielski = tk.Entry(self.root)
        self.angielski.grid(row=4, column=1)
        self.polski = tk.Entry(self.root)
        self.polski.grid(row=5, column=1)
        self.matematyka = tk.Entry(self.root)
        self.matematyka.grid(row=6, column=1)
        self.muzyka = tk.Entry(self.root)
        self.muzyka.grid(row=7, column=1)
        self.plastyka = tk.Entry(self.root)
        self.plastyka.grid(row=8, column=1)
        self.religia = tk.Entry(self.root)
        self.religia.grid(row=9, column=1)
        self.technika = tk.Entry(self.root)
        self.technika.grid(row=10, column=1)
        self.wf = tk.Entry(self.root)
        self.wf.grid(row=11, column=1)
        self.zachowanie = tk.Entry(self.root)
        self.zachowanie.grid(row=12, column=1)

        self.informacja = tk.Label(self.root, text="Wszystkie liczby proszę wpisać jako cyfry (1-6)")
        self.informacja.grid(row=0, column=2, columnspan=2)

        self.przycisk_srednia = tk.Button(self.root, command=self.oblicz_srednia, text="Oblicz\nŚrednią")
        self.przycisk_srednia.grid(row=5, column=2, rowspan=2, padx=5)

        self.etykieta_srednia_ocen = tk.Label(self.root, text="Średnia ocen:")
        self.srednia_ocen = tk.StringVar()
        self.srednia_ocen.set("0.0")
        self.wyswietl_srednia_ocen = tk.Entry(self.root, textvariable=self.srednia_ocen, width=10,
                                              justify="center", state="disabled")
        self.wyswietl_srednia_ocen.insert(0, "0.00")

        self.etykieta_rodzaj_swiadectwa = tk.Label(self.root, text="Rodzaj świadectwa:")
        self.rodzaj_swiadectwa = tk.StringVar()
        self.rodzaj_swiadectwa.set("Świadectwo")
        self.wyswietl_rodzaj_swiadectwa = tk.Entry(self.root, textvariable=self.rodzaj_swiadectwa, width=30,
                                                   justify='center', state="disabled")

        self.etykieta_srednia_ocen.grid(row=4, column=3)
        self.wyswietl_srednia_ocen.grid(row=5, column=3)
        self.etykieta_rodzaj_swiadectwa.grid(row=6, column=3)
        self.wyswietl_rodzaj_swiadectwa.grid(row=7, column=3)

    def oblicz_srednia(self):
        #   Dodanie ocen (opórcz oceny z zachowania) w typie String do listy
        oceny_string = [self.biologia.get(), self.geografia.get(), self.historia.get(), self.informatyka.get(),
                        self.angielski.get(), self.polski.get(), self.matematyka.get(), self.muzyka.get(),
                        self.plastyka.get(), self.religia.get(), self.technika.get(), self.wf.get()]

        #   Konwersja ocen z typu String na Int, sprawdzenie poprawności wprowadzonych danych, obliczenie średniej
        oceny_int = []
        try:
            for ocena in oceny_string:
                oceny_int.append(int(ocena))
            if (max(oceny_int) <= 6 and min(oceny_int) >= 1) and (1 <= int(self.zachowanie.get()) <= 6):
                srednia = round(sum(oceny_int)/len(oceny_int), 2)
                self.srednia_ocen.set(srednia)
                if int(self.zachowanie.get()) >= 5 and srednia >= 4.75:
                    self.rodzaj_swiadectwa.set("świadectwo z wyróżnieniem")
                else:
                    self.rodzaj_swiadectwa.set("świadectwo bez wyróżnienia")

            else:
                showerror("Błąd", "Wprowadzono wartość większą niż 6 i/lub mniejszą niż 1")

        except Exception as e:
            showerror("Błąd", f"Wprowadzono nieprawidłowe dane.\nTekst błędu: {e}")


app = Aplikacja()
app.root.mainloop()
