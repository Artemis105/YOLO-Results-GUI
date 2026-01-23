import customtkinter as ctk
from PIL import Image
from Ustawienia import *
from Predykcja import *



class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Aplikacja")
        self.geometry("1100x600")
        self.resizable(False, False)


        self.katalog_img=img_list();
        self.katalog_model = model_list();
        self.selected = ''
        self.model = ''
        self.variable_pew = '50.0 %'
        self.variable_IoU = 0.5
        self.save_img = None
        self.wybor = 0
        self.save_to_img = {}
        #self.predy = self.selected
        self.predy = self.selected
        self.zaczynamy_predykcje = None

        ctk.set_appearance_mode("system")  # dark/light/system
        ctk.set_default_color_theme("dark-blue")

        self.image = None

        self.image_label = ctk.CTkLabel(master=self, text='')

        self.button = ctk.CTkButton(self, text='Zamknij', command=self.button_exit_click,
                                    font=ctk.CTkFont(size=15), width=350)

        self.button_pred = ctk.CTkButton(self, text='Predykcja', command=self.button_pred_click,
                                         font=ctk.CTkFont(size=15), state=ctk.DISABLED, width=150)

        self.label_iou = ctk.CTkLabel(master=self, text="IoU", font=ctk.CTkFont(size=15), height=10)
        self.label_pew = ctk.CTkLabel(master=self, text="Pewność", font=ctk.CTkFont(size=15), height=10)

        self.var_label_iou = ctk.CTkLabel(master=self, font=ctk.CTkFont(size=15), height=10)
        self.var_label_pew = ctk.CTkLabel(master=self, text=self.variable_pew, font=ctk.CTkFont(size=15), height=10)

        self.label_model = ctk.CTkLabel(master=self, text="  Wybierz model:", font=ctk.CTkFont(size=15), height=10)
        self.label_img = ctk.CTkLabel(master=self, text="  Wybierz źródło:", font=ctk.CTkFont(size=15), height=10)

        self.button_save = ctk.CTkButton(self, text='Zapisz', command=self.button_save_click,
                                         font=ctk.CTkFont(size=15), state=ctk.DISABLED, width=150)

        self.combo_png = ctk.CTkComboBox(self, values=self.katalog_img, command=self.combo_img_fun, width=450)
        self.combo_model = ctk.CTkComboBox(self, values=self.katalog_model, command=self.combo_model_fun, width=450)

        self.slider_iou = ctk.CTkSlider(self, from_=0, to=1, command=self.slider_iou_fun,
                                        number_of_steps=25, orientation="vertical", width=20, height=300)
        self.slider_pew = ctk.CTkSlider(self, from_=0, to=100, command=self.slider_pew_fun,
                                        number_of_steps=25, orientation="vertical", width=20, height=300)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=10)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)


        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=1)
        self.columnconfigure(5, weight=1)

        self.image_label.grid(row=0, column=0, columnspan=3, rowspan=3, padx=10, pady=10,sticky='senw')
        self.button_save.grid(row=4, column=4, columnspan=1, rowspan=1,padx=10, pady=10)
        self.button_pred.grid(row=4, column=3, columnspan=1, rowspan=1,padx=10, pady=10)
        self.button.grid(row=6, column=3, padx=10,columnspan=2, rowspan=1, pady=10,sticky='')
        self.label_iou.grid(row=0, column=4, columnspan=1, rowspan=1, padx=10, pady=30)
        self.label_pew.grid(row=0, column=3, columnspan=1, rowspan=1, padx=10, pady=30)
        self.var_label_iou.grid(row=2, column=4, columnspan=1, rowspan=1, padx=10, pady=30)
        self.var_label_pew.grid(row=2, column=3, columnspan=1, rowspan=1, padx=10, pady=30)
        self.label_img.grid(row=3, column=0,  padx=30, pady=10, sticky="w")
        self.label_model.grid(row=5, column=0,  padx=30, pady=10, sticky="w")
        self.slider_iou.grid(row=1, column=4, columnspan=1, rowspan=1, padx=10, pady=10)
        self.slider_pew.grid(row=1, column=3, columnspan=1, rowspan=1, padx=10, pady=10)
        self.combo_model.grid(row=6, column=0, padx=30, pady=10,sticky="w")
        self.combo_png.grid(row=4, column=0, padx=30, pady=10,sticky="w")
    # add methods to app
    def button_exit_click(self) -> None:

        self.destroy()

    def button_pred_click(self):
        """Obsługa przycisku Predykcji."""
        iou_value = self.variable_IoU
        pew_value = float(self.variable_pew[:-2]) / 100

        # Tworzenie wątku dla predykcji
        self.single_image_thread = pred_img(
            model=self.model,
            iou=iou_value,
            pew=pew_value,
            image_label=self.image_label,
            selected=self.selected,
            image_to_save={"image": Image.new('RGB', (640, 384), color='white')}  # Placeholder image
        )
        self.single_image_thread.start()  # Uruchamiamy wątek
        print("Predykcja została uruchomiona.")

    def button_save_click(self):
        """Obsługa przycisku Zapisz, zapisuje obraz z ramkami predykcji."""
        if 'image' in self.single_image_thread.image_to_save:
            image = self.single_image_thread.image_to_save["image"]  # Pobieramy obraz z ramkami predykcji

            sciezka = Path_to_save
            f1 = self.selected.find('.jpeg')
            f2 = self.selected.find(Path_to_img)
            l = len(Path_to_img)

            if f1 != -1:
                cut = self.selected[f2 + l + 1:-5]
            else:
                cut = self.selected[f2 + l + 1:-4]

            cut2 = str(self.variable_pew)[:-2]
            m1 = self.model.rfind('//')
            s = self.model.find(roz_model)

            image.save(f"{sciezka}//{self.model[m1 + 1:s]}_{cut}_{cut2}_{self.variable_IoU}.png")
            print("Obraz został zapisany pomyślnie.")
        else:
            print("Brak obrazu do zapisania!")


    def slider_iou_fun(self, value):
        self.variable_IoU = round(value, 2)
        self.var_label_iou.configure(text=f"{self.variable_IoU:.2f}")

    def slider_pew_fun(self, value):
        self.variable_pew = f"{round(value)} %"
        self.var_label_pew.configure(text=self.variable_pew)

    def combo_img_fun(self, choice):
        self.selected = f'{Path_to_img}\\{choice}'
        image = Image.open(self.selected)

        self.update_image(image)

        self.predy = image

        self.name = choice

        if self.wybor == 0:
            self.wybor = 1
        else:
            self.button_pred.configure(state='NORMAL')
            self.button_save.configure(state='NORMAL')

    def update_image(self, image):
        image1 = ctk.CTkImage(light_image=Image.open(self.selected),
                                  dark_image=Image.open(self.selected),
                                  size=(640, 384))
        self.image_label.configure(image=image1)

    def combo_model_fun(self,choice):
        self.model=choice

        if self.wybor == 0:
            self.wybor = 1
        else:
          self.button_pred.configure(state='NORMAL')
          self.button_save.configure(state='NORMAL')

        print("combobox dropdown clicked:", choice)

if __name__ == "__main__":

    app = App()
    app.mainloop()
#
