import threading
import customtkinter as ctk
from PIL import Image, ImageDraw
from Ustawienia import *
from ultralytics import YOLO
import os


def draw_labels_on_image(image, label_path):

    if not os.path.exists(label_path):
        print(f"Brak pliku label: {label_path}")
        return image

    draw = ImageDraw.Draw(image)


    with open(label_path, "r") as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) < 5:
                continue

            _, x_center, y_center, width, height = map(float, parts)

            img_width, img_height = image.size
            x_min = (x_center - width / 2) * img_width
            y_min = (y_center - height / 2) * img_height
            x_max = (x_center + width / 2) * img_width
            y_max = (y_center + height / 2) * img_height

            draw.rectangle([x_min, y_min, x_max, y_max], outline="blue", width=3)

    return image


class pred_img(threading.Thread):
    def __init__(self, model=None, iou=0.5, pew=0.25, image_label=None, selected=None, image_to_save=None):
        super(pred_img, self).__init__()
        self.model = model
        self.iou = iou
        self.pew = pew
        self.image_label = image_label
        self.selected = selected
        self.image_to_save = image_to_save if image_to_save is not None else {}

    def run(self):
        if self.model is not None:

            self.model = YOLO(f'{Path_to_model}\\{self.model}')

            results = self.model.predict(self.selected, iou=self.iou, conf=self.pew)

            image_with_boxes = results[0].plot()


            image = Image.fromarray(image_with_boxes[..., ::-1])


            file_name = os.path.basename(self.selected).replace(".jpg", ".txt")
            label_path = os.path.join(Path_to_label, file_name)


            image = draw_labels_on_image(image, label_path)

            if self.image_label is not None:

                img = ctk.CTkImage(light_image=image,
                                   dark_image=image,
                                   size=(640, 384))
                self.image_label.configure(image=img)
                self.image_label.image = img


            if isinstance(self.image_to_save, dict):
                self.image_to_save["image"] = image
            else:
                print("Błąd: self.image_to_save nie jest słownikiem!")
                self.image_to_save = {"image": image}

            print("Predykcja zakończona, obraz z ramkami gotowy do zapisania.")
