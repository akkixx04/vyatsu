import tkinter as tk
import random
import time
import cv2
import numpy as np
import math

class LoadingScreen(tk.Frame):
    def __init__(self, parent, controller):
        """Экран загрузки приложения с анимированной полосой прогресса"""
        super().__init__(parent, bg="#FFFFFF")
        self.controller = controller
        
        try:
            img = cv2.imread("logo.png", cv2.IMREAD_UNCHANGED)
            if img is None:
                raise FileNotFoundError("Файл logo.png не найден")
                
            if img.shape[2] == 4:
                alpha_channel = img[:, :, 3]
                img_rgb = img[:, :, :3]
                white_background = np.ones_like(img_rgb) * 255
                alpha = alpha_channel[:, :, np.newaxis] / 255.0
                img = (img_rgb * alpha + white_background * (1 - alpha)).astype(np.uint8)
            else:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            
            img = cv2.resize(img, (540, 150))
            self.photo = tk.PhotoImage(data=cv2.imencode('.png', img)[1].tobytes())
        except Exception as e:
            print(f"Ошибка загрузки логотипа: {e}")
            self.photo = tk.PhotoImage(width=540, height=150)

        # Основной контейнер
        container = tk.Frame(self, bg="#FFFFFF")
        container.place(relx=0.5, rely=0.5, anchor="center")
        # Отображение логотипа
        self.logo_label = tk.Label(container, image=self.photo, bg="#FFFFFF")
        self.logo_label.pack(pady=(0, 50))
        # Полоса загрузки
        self.loading_canvas = tk.Canvas(container, width=800, height=20, bg="#FFFFFF", highlightthickness=0)
        self.loading_canvas.pack()
        # Инициализация полосы загрузки
        self.loading_bar = self.loading_canvas.create_rectangle(
            0, 0, 0, 20, 
            fill="#4CAF50", outline="" ) 
        # Запуск анимации загрузки
        self.progress = 0
        self.animate_loading()

    def animate_loading(self):
        """Анимация заполнения полосы загрузки"""
        if self.progress < 100:
            self.progress += 2.5
            new_width = 800 * (self.progress / 100)
            self.loading_canvas.coords(self.loading_bar, 0, 0, new_width, 20)
            self.after(20, self.animate_loading)
        else:
            self.controller.show_frame(StartPage)

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        """Главная страница приложения с меню выбора тестов"""
        super().__init__(parent, bg="#FFFFFF")
        
        try:
            img = cv2.imread("logo.png", cv2.IMREAD_UNCHANGED)
            if img is None:
                raise FileNotFoundError("Файл logo.png не найден")
                
            if img.shape[2] == 4:
                alpha_channel = img[:, :, 3]
                img_rgb = img[:, :, :3]
                white_background = np.ones_like(img_rgb) * 255
                alpha = alpha_channel[:, :, np.newaxis] / 255.0
                img = (img_rgb * alpha + white_background * (1 - alpha)).astype(np.uint8)
            else:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = cv2.resize(img, (255, 70))
            photo = tk.PhotoImage(data=cv2.imencode('.png', img)[1].tobytes())
        except Exception as e:
            print(f"Ошибка загрузки логотипа: {e}")
            photo = tk.PhotoImage(width=255, height=70)

        # Верхняя панель с логотипом и кнопками
        top_panel = tk.Frame(self, bg="#FFFFFF")
        top_panel.place(x=0, y=0, width=1920, height=100)
        # Логотип
        image_label = tk.Label(top_panel, image=photo, bg="#FFFFFF")
        image_label.image = photo
        image_label.pack(side="left", padx=10)
        # Кнопка перехода к результатам
        results_btn = tk.Button(top_panel, text="Результаты", font=("Arial", 18), 
                              bg="white", fg="black", height=1, width=20,
                              command=lambda: controller.show_frame(ResultsPage),
                              borderwidth=0, highlightthickness=0)
        results_btn.place(relx=0.4, rely=0.5, anchor='center')
        # Разделительная линия
        line = tk.Frame(top_panel, bg="black", height=2, width=1920)
        line.place(x=0, y=95)
        # Основное содержимое страницы
        label = tk.Label(self, text="Главное меню", font=("Arial", 40), bg="#FFFFFF")
        label.place(relx=0.5, rely=0.27, anchor='center')
        # Кнопка начала тестирования
        button = tk.Button(self, text="Начать", width=20, height=2, 
                         font=("Arial", 14), bg="#21743F", fg="white",
                         command=lambda: controller.show_frame(Manual1))
        button.place(relx=0.5, rely=0.5, anchor='center')
        # Кнопка закрытия приложения
        try:
            close_img = cv2.imread("close_btn.png", cv2.IMREAD_UNCHANGED)
            if close_img is None:
                raise FileNotFoundError("Файл close_btn.png не найден")
                
            if close_img.shape[2] == 4:
                alpha_channel = close_img[:, :, 3]
                img_rgb = close_img[:, :, :3]
                white_background = np.ones_like(img_rgb) * 255
                alpha = alpha_channel[:, :, np.newaxis] / 255.0
                close_img = (img_rgb * alpha + white_background * (1 - alpha)).astype(np.uint8)
            else:
                close_img = cv2.cvtColor(close_img, cv2.COLOR_BGR2RGB)
            
            close_img = cv2.resize(close_img, (105, 80))
            close_photo = tk.PhotoImage(data=cv2.imencode('button2.png', close_img)[1].tobytes())
            close_btn = tk.Button(self, image=close_photo, bg="#FFFFFF",
                                command=controller.destroy, 
                                borderwidth=0, highlightthickness=0)
            close_btn.image = close_photo
            close_btn.place(relx=0.0475, rely=0.935, anchor='center')
        except Exception as e:
            print(f"Ошибка загрузки кнопки закрытия: {e}")
            # Создаем стандартную кнопку закрытия в случае ошибки
            close_btn = tk.Button(self, text="Закрыть", font=("Arial", 14),
                                command=controller.destroy)
            close_btn.place(relx=0.0475, rely=0.935, anchor='center')

class Manual1(tk.Frame):
    def __init__(self, parent, controller):
        """Страница с инструкцией к первому тесту Струпа"""
        super().__init__(parent, bg="#FFFFFF")

        try:
            img = cv2.imread("logo.png", cv2.IMREAD_UNCHANGED)
            if img is None:
                raise FileNotFoundError("Файл logo.png не найден")
            if img.shape[2] == 4:
                alpha_channel = img[:, :, 3]
                img_rgb = img[:, :, :3]
                white_background = np.ones_like(img_rgb) * 255
                alpha = alpha_channel[:, :, np.newaxis] / 255.0
                img = (img_rgb * alpha + white_background * (1 - alpha)).astype(np.uint8)
            else:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = cv2.resize(img, (255, 70))
            self.photo = tk.PhotoImage(data=cv2.imencode('.png', img)[1].tobytes())
        except Exception as e:
            print(f"Ошибка загрузки логотипа: {e}")
            self.photo = tk.PhotoImage(width=255, height=70)

        # Верхняя панель
        top_panel = tk.Frame(self, bg="#FFFFFF")
        top_panel.place(x=0, y=0, width=1920, height=100)
        # Логотип
        self.image_label = tk.Label(top_panel, image=self.photo, bg="#FFFFFF")
        self.image_label.pack(side="left", padx=10)
        # Кнопка возврата в главное меню
        self.back_btn = tk.Button(top_panel, text="Главное меню", font=("Arial", 18),
                           bg="white", fg="black", height=1, width=20, borderwidth=0,
                           command=lambda: controller.show_frame(StartPage))
        self.back_btn.place(relx=0.4, rely=0.5, anchor='center')
        # Разделительная линия
        line = tk.Frame(top_panel, bg="black", height=2, width=1920)
        line.place(x=0, y=95)
        # Заголовок инструкции
        label = tk.Label(self, text="Инструкция к тесту Струпа", 
                       font=("Arial", 40), bg="#FFFFFF")
        label.place(relx=0.5, rely=0.27, anchor='center')
        # Текст инструкции
        instruction_text = (
            "На экране появляются слова, обозначающие цвет. Нужно выбирать цветовой образец\n"
            "в соответствии с заданием. В 1-ой части теста Струпа выбирайте цвет по смыслу и цвету\n"
            "(одновременно). Смысл будет соответствовать цвету слова.")
        instruction_label = tk.Label(self, text=instruction_text, 
                                   font=("Arial", 20), bg="#FFFFFF", justify="center")
        instruction_label.place(relx=0.5, rely=0.45, anchor='center')
        # Кнопка начала теста
        button2 = tk.Button(self, text="Начать тест", 
                          bg="#21743F", fg="white", width=20, height=2,
                          font=("Arial", 14),
                          command=lambda: controller.show_frame(Test1))
        button2.place(relx=0.5, rely=0.65, anchor='center')

class Test1(tk.Frame):
    def __init__(self, parent, controller):
        """Первый тест Струпа (совпадение цвета и значения слова)"""
        super().__init__(parent, bg="#FFFFFF")
        self.controller = controller
        self.active = False
        self.previous_color = None

        try:
            img = cv2.imread("logo.png", cv2.IMREAD_UNCHANGED)
            if img is None:
                raise FileNotFoundError("Файл logo.png не найден") 
            if img.shape[2] == 4:
                alpha_channel = img[:, :, 3]
                img_rgb = img[:, :, :3]
                white_background = np.ones_like(img_rgb) * 255
                alpha = alpha_channel[:, :, np.newaxis] / 255.0
                img = (img_rgb * alpha + white_background * (1 - alpha)).astype(np.uint8)
            else:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = cv2.resize(img, (255, 70))
            self.photo = tk.PhotoImage(data=cv2.imencode('.png', img)[1].tobytes())
        except Exception as e:
            print(f"Ошибка загрузки логотипа: {e}")
            self.photo = tk.PhotoImage(width=255, height=70)

        # Верхняя панель
        self.top_panel = tk.Frame(self, bg="#FFFFFF")
        self.top_panel.place(x=0, y=0, relwidth=1.0, height=100)
        # Основной фрейм для теста
        self.main_frame = tk.Frame(self, bg="#FFFFFF")
        self.main_frame.place(x=0, y=100, relwidth=1.0, relheight=1.0, height=-100)
        # Логотип
        self.image_label = tk.Label(self.top_panel, image=self.photo, bg="#FFFFFF")
        self.image_label.pack(side="left", padx=10)
        # Кнопка возврата в главное меню
        self.back_btn = tk.Button(self.top_panel, text="Главное меню", font=("Arial", 18),
                           bg="white", fg="black", height=1, width=20, borderwidth=0,
                           command=lambda: [
                                   controller.reset_test(),
                                   controller.show_frame(StartPage)])
        self.back_btn.place(relx=0.5, rely=0.5, anchor='center')
        # Разделительная линия
        line = tk.Frame(self.top_panel, bg="black", height=2, width=1920)
        line.place(x=0, y=95)
        # Настройка таймера
        self.timer_width = 1920
        self.timer_height = 20
        # Холст для отображения таймера
        self.timer_canvas = tk.Canvas(self.main_frame, width=self.timer_width, height=self.timer_height, 
                                    bg="white", highlightthickness=0)
        self.timer_canvas.pack(pady=(20), anchor="n")
        # Полоса таймера
        self.timer_bar = self.timer_canvas.create_rectangle(
            0, 0, self.timer_width, self.timer_height, 
            fill="#4CAF50", outline="")
        # Сопоставление цветов и их названий
        self.color_mapping = {
            "ФИОЛЕТОВЫЙ": "purple",
            "СИНИЙ": "blue",
            "ЗЕЛЕНЫЙ": "green",
            "КРАСНЫЙ": "red",
            "ЖЕЛТЫЙ": "yellow",
            "ЧЕРНЫЙ": "black"}
        # Инициализация параметров теста
        self.round_number = 1
        self.score = 0
        self.current_correct_color_name = None
        self.current_correct_color_code = None
        self.timer_id = None
        # Метка для отображения слова
        self.word_label = tk.Label(self.main_frame, text="", font=("Arial", 36), bg="white")
        self.word_label.pack(anchor="center", pady=0)
        # Фрейм для кнопок цветов
        self.buttons_frame = tk.Frame(self.main_frame, bg="#FFFFFF")
        self.buttons_frame.pack(pady=50)
        # Создание кнопок цветов
        self.color_buttons = []
        for i in range(6):
            btn = tk.Button(
                self.buttons_frame, 
                width=70, 
                height=8,
                command=lambda i=i: self.check_answer_by_index(i))  
            btn.grid(row=i//2, column=i%2, padx=90, pady=30)
            self.color_buttons.append(btn)
        self.start_round()

    def check_answer_by_index(self, index):
        """Проверка ответа по индексу кнопки"""
        if not self.active:
            return
        color_name = list(self.current_button_colors.keys())[index]
        color_code = self.current_button_colors[color_name]
        self.check_answer(color_name, color_code)

    def start_round(self):
        """Начало нового раунда теста"""
        if not self.active:
            return
        if self.round_number > 10:
            self.end_game()
            return
        # Сброс таймера
        if hasattr(self, 'timer_id') and self.timer_id:
            self.after_cancel(self.timer_id)
            self.timer_id = None
        # Сброс полосы таймера
        self.timer_canvas.delete("all")
        self.timer_bar = self.timer_canvas.create_rectangle(
            0, 0, self.timer_width, self.timer_height, 
            fill="#4CAF50", outline="")
        # Выбор случайного цвета, отличного от предыдущего
        available_colors = [c for c in self.color_mapping.items() if c[0] != self.previous_color]
        if not available_colors:  # Если остался только один цвет
            available_colors = list(self.color_mapping.items())
        color_name, color_code = random.choice(available_colors)
        self.current_correct_color_name = color_name
        self.current_correct_color_code = color_code
        self.previous_color = color_name
        # Отображение слова (название цвета) с соответствующим цветом
        self.word_label.config(text=color_name, fg=color_code)
        # Случайное распределение цветов по кнопкам
        color_items = list(self.color_mapping.items())
        random.shuffle(color_items)
        self.current_button_colors = dict(color_items)
        # Обновление цветов кнопок
        for i, (color_name, color_code) in enumerate(color_items):
            self.color_buttons[i].config(bg=color_code)
        # Запуск таймера
        self.start_time = time.time()
        self.animate_timer()

    def animate_timer(self):
        """Анимация таймера для текущего раунда"""
        if not self.active:
            return 
        elapsed = time.time() - self.start_time
        progress = elapsed / 2  # 2 секунды на раунд
        if progress < 1:
            new_width = self.timer_width * (1 - progress)
            self.timer_canvas.coords(self.timer_bar, 0, 0, new_width, self.timer_height)
            # Изменение цвета полосы в зависимости от оставшегося времени
            if progress > 0.5:
                self.timer_canvas.itemconfig(self.timer_bar, fill="#FFC107")
            if progress > 0.75:
                self.timer_canvas.itemconfig(self.timer_bar, fill="#F44336")
            self.timer_id = self.after(20, self.animate_timer)
        else:
            # Время вышло
            self.timer_canvas.coords(self.timer_bar, 0, 0, 0, self.timer_height)
            self.next_round()

    def check_answer(self, chosen_color_name, chosen_color_code):
        """Проверка выбранного пользователем ответа"""
        if not self.active:
            return
        if hasattr(self, 'timer_id') and self.timer_id:
            self.after_cancel(self.timer_id)
            self.timer_id = None
        if self.round_number <= 10:
            # Проверка совпадения выбранного цвета с правильным ответом
            if chosen_color_name == self.current_correct_color_name:
                self.score += 1
            self.next_round()

    def next_round(self):
        """Переход к следующему раунду"""
        self.round_number += 1
        self.start_round()
        
    def end_game(self):
        """Завершение теста и сохранение результатов"""
        self.active = False
        try:
            with open("results.txt", "w", encoding="utf-8") as file:
                file.write(f"1 тест: {self.score} правильных ответов из 10\n")
        except Exception as e:
            print(f"Ошибка сохранения результатов: {e}")
        self.controller.show_frame(Manual2)
        
    def reset_test(self):
        """Сброс теста перед новым прохождением"""
        self.active = True
        self.round_number = 1
        self.score = 0
        self.current_correct_color_name = None
        self.current_correct_color_code = None
        if hasattr(self, 'timer_id') and self.timer_id:
            self.after_cancel(self.timer_id)
            self.timer_id = None
        self.start_round()

    def reset(self):
        """Полный сброс теста"""
        self.active = False
        self.previous_color = None
        self.round_number = 1
        self.score = 0
        self.current_correct_color_name = None
        self.current_correct_color_code = None
        # Сброс таймера
        if hasattr(self, 'timer_id') and self.timer_id:
            self.after_cancel(self.timer_id)
            self.timer_id = None
        # Сброс полосы таймера
        self.timer_canvas.delete("all")
        self.timer_bar = self.timer_canvas.create_rectangle(
            0, 0, self.timer_width, self.timer_height, 
            fill="#4CAF50", outline="")
        # Очистка отображаемого слова
        self.word_label.config(text="")

class Manual2(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#FFFFFF")

        img = cv2.imread("logo.png", cv2.IMREAD_UNCHANGED)
        if img.shape[2] == 4:
            alpha_channel = img[:, :, 3]
            img_rgb = img[:, :, :3]
            white_background = np.ones_like(img_rgb) * 255
            alpha = alpha_channel[:, :, np.newaxis] / 255.0
            img = (img_rgb * alpha + white_background * (1 - alpha)).astype(np.uint8)
        else:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (255, 70))
        self.photo = tk.PhotoImage(data=cv2.imencode('.png', img)[1].tobytes())

        # Верхняя панель
        top_panel = tk.Frame(self, bg="#FFFFFF")
        top_panel.place(x=0, y=0, width=1920, height=100)
        # Логотип слева
        self.image_label = tk.Label(top_panel, image=self.photo, bg="#FFFFFF")
        self.image_label.pack(side="left", padx=10)
        self.back_btn = tk.Button(top_panel, text="Главное меню", font=("Arial", 18),
                           bg="white", fg="black", height=1, width=20, borderwidth=0,
                           command=lambda: controller.show_frame(StartPage))
        self.back_btn.place(relx=0.4, rely=0.5, anchor='center')
        # Разделительная линия
        line = tk.Frame(top_panel, bg="black", height=2, width=1920)
        line.place(x=0, y=95)
        #Заголовок
        label = tk.Label(self, text="Инструкция к тесту Струпа, часть 2", 
                       font=("Arial", 40), bg="#FFFFFF")
        label.place(relx=0.5, rely=0.27, anchor='center')
        # Инструкция
        instruction_text = ("Во 2-ой части выбирайте цвет по смыслу")
        instruction_label = tk.Label(self, text=instruction_text, 
                                   font=("Arial", 20), bg="#FFFFFF", justify="center")
        instruction_label.place(relx=0.5, rely=0.45, anchor='center')
        # Кнопка для начала теста
        button2 = tk.Button(self, text="Начать тест", 
                          bg="#21743F", fg="white", width=20, height=2,
                          font=("Arial", 14),
                          command=lambda: controller.show_frame(Test2))
        button2.place(relx=0.5, rely=0.65, anchor='center')

class Test2(tk.Frame):
    def __init__(self, parent, controller):
        """Тест Струпа (часть 2) - выбор цвета по смыслу слова"""
        super().__init__(parent, bg="#FFFFFF")
        self.controller = controller
        self.active = False
        self.previous_color = None

        img = cv2.imread("logo.png", cv2.IMREAD_UNCHANGED)
        if img is None:
            raise FileNotFoundError("Не удалось загрузить logo.png")
        if img.shape[2] == 4:
            alpha_channel = img[:, :, 3]
            img_rgb = img[:, :, :3]
            white_background = np.ones_like(img_rgb) * 255
            alpha = alpha_channel[:, :, np.newaxis] / 255.0
            img = (img_rgb * alpha + white_background * (1 - alpha)).astype(np.uint8)
        else:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (255, 70))
        self.photo = tk.PhotoImage(data=cv2.imencode('.png', img)[1].tobytes())

        # Верхняя панель интерфейса
        self.top_panel = tk.Frame(self, bg="#FFFFFF")
        self.top_panel.place(x=0, y=0, relwidth=1.0, height=100)
        # Основной фрейм для содержимого теста
        self.main_frame = tk.Frame(self, bg="#FFFFFF")
        self.main_frame.place(x=0, y=100, relwidth=1.0, relheight=1.0, height=-100)
        # Логотип в верхней панели
        self.image_label = tk.Label(self.top_panel, image=self.photo, bg="#FFFFFF")
        self.image_label.pack(side="left", padx=10)
        # Кнопка возврата в главное меню
        self.back_btn = tk.Button(
            self.top_panel, 
            text="Главное меню", 
            font=("Arial", 18),
            bg="white", 
            fg="black", 
            height=1, 
            width=20, 
            borderwidth=0,
            command=lambda: [controller.reset_test(), controller.show_frame(StartPage)])
        self.back_btn.place(relx=0.5, rely=0.5, anchor='center')
        # Разделительная линия
        line = tk.Frame(self.top_panel, bg="black", height=2, width=1920)
        line.place(x=0, y=95)
        # Настройка визуального таймера
        self.timer_width = 1920
        self.timer_height = 20
        self.timer_canvas = tk.Canvas(
            self.main_frame, 
            width=self.timer_width, 
            height=self.timer_height, 
            bg="white", 
            highlightthickness=0)
        self.timer_canvas.pack(pady=(20), anchor="n")
        self.timer_bar = self.timer_canvas.create_rectangle(
            0, 0, self.timer_width, self.timer_height, 
            fill="#4CAF50", outline="")
        # Соответствие названий цветов и их кодов
        self.color_mapping = {
            "ФИОЛЕТОВЫЙ": "purple",
            "СИНИЙ": "blue",
            "ЗЕЛЕНЫЙ": "green",
            "КРАСНЫЙ": "red",
            "ЖЕЛТЫЙ": "yellow",
            "ЧЕРНЫЙ": "black"
        }
        # Параметры теста
        self.round_number = 1
        self.score = 0
        self.current_text_color_name = None
        self.current_text_color_code = None
        self.current_word_color_name = None
        self.current_word_color_code = None
        self.timer_id = None
        # Метка для отображения слова
        self.word_label = tk.Label(self.main_frame, text="", font=("Arial", 36), bg="white")
        self.word_label.pack(anchor="center", pady=0)
        # Фрейм для кнопок выбора цвета
        self.buttons_frame = tk.Frame(self.main_frame, bg="#FFFFFF")
        self.buttons_frame.pack(pady=50)
        # Создание кнопок цветов
        self.color_buttons = []
        for i in range(6):  # Создаем 6 кнопок без привязки к конкретным цветам
            btn = tk.Button(
                self.buttons_frame, 
                width=70, 
                height=8,
                command=lambda i=i: self.check_answer_by_index(i))  
            btn.grid(row=i//2, column=i%2, padx=90, pady=30)
            self.color_buttons.append(btn)
        self.start_round()

    def check_answer_by_index(self, index):
        """Проверка ответа по индексу кнопки"""
        if not self.active:
            return
        # Получаем цвет и имя по текущему индексу кнопки
        color_name = list(self.current_button_colors.keys())[index]
        color_code = self.current_button_colors[color_name]
        self.check_answer(color_name, color_code)

    def start_round(self):
        """Начало нового раунда теста"""
        if not self.active:
            return
        if self.round_number > 10:
            self.end_game()
            return
        # Сброс таймера
        if hasattr(self, 'timer_id') and self.timer_id:
            self.after_cancel(self.timer_id)
            self.timer_id = None
        # Сброс полосы таймера
        self.timer_canvas.delete("all")
        self.timer_bar = self.timer_canvas.create_rectangle(
            0, 0, self.timer_width, self.timer_height, 
            fill="#4CAF50", outline="")
        # Выбор цвета слова (правильный ответ)
        available_colors = list(self.color_mapping.items())
        if hasattr(self, 'previous_word_color'):
            available_word_colors = [c for c in available_colors if c[0] != self.previous_word_color]
        else:
            available_word_colors = available_colors 

        word_color_name, word_color_code = random.choice(available_word_colors)
        self.previous_word_color = word_color_name
        # Выбор цвета текста (должен отличаться от цвета слова)
        text_color_options = [c for c in available_colors if c[0] != word_color_name]
        if hasattr(self, 'previous_text_color'):
            text_color_options = [c for c in text_color_options if c[0] != self.previous_text_color]

        text_color_name, text_color_code = random.choice(text_color_options)
        self.previous_text_color = text_color_name
        # Сохранение текущих параметров
        self.current_word_color_name = word_color_name
        self.current_word_color_code = word_color_code
        self.current_text_color_code = text_color_code
        # Отображение слова
        self.word_label.config(text=word_color_name, fg=text_color_code)
        # Случайное распределение цветов по кнопкам
        color_items = list(self.color_mapping.items())
        random.shuffle(color_items)
        self.current_button_colors = dict(color_items)
        # Обновление цветов кнопок
        for i, (color_name, color_code) in enumerate(color_items):
            self.color_buttons[i].config(bg=color_code)
        # Запуск таймера (2 секунды на раунд)
        self.start_time = time.time()
        self.animate_timer()

    def animate_timer(self):
        """Анимация таймера"""
        if not self.active:
            return
        elapsed = time.time() - self.start_time
        progress = elapsed / 2

        if progress < 1:
            new_width = self.timer_width * (1 - progress)
            self.timer_canvas.coords(self.timer_bar, 0, 0, new_width, self.timer_height)
            if progress > 0.5:
                self.timer_canvas.itemconfig(self.timer_bar, fill="#FFC107")
            if progress > 0.75:
                self.timer_canvas.itemconfig(self.timer_bar, fill="#F44336")
            self.timer_id = self.after(20, self.animate_timer)
        else:
            self.timer_canvas.coords(self.timer_bar, 0, 0, 0, self.timer_height)
            self.next_round()

    def check_answer(self, chosen_color_name, chosen_color_code):
        """Проверка ответа пользователя"""
        if not self.active:
            return
        if hasattr(self, 'timer_id') and self.timer_id:
            self.after_cancel(self.timer_id)
            self.timer_id = None
        if self.round_number <= 10:
            if chosen_color_name == self.current_word_color_name:
                self.score += 1
            self.next_round()

    def next_round(self):
        """Переход к следующему раунду"""
        self.round_number += 1
        self.start_round()
        
    def end_game(self):
        """Завершение теста и сохранение результатов"""
        self.active = False
        with open("results.txt", "a", encoding="utf-8") as file:
            file.write(f"2 тест: {self.score} правильных ответов из 10\n")
        self.controller.show_frame(Manual3)
        
    def reset_test(self):
        """Сброс теста для повторного прохождения"""
        self.active = True
        self.round_number = 1
        self.score = 0
        self.current_text_color_name = None
        self.current_text_color_code = None
        self.current_word_color_name = None
        self.current_word_color_code = None
        if hasattr(self, 'timer_id') and self.timer_id:
            self.after_cancel(self.timer_id)
            self.timer_id = None
        self.start_round()

    def reset(self):
        """Полный сброс теста"""
        self.active = False
        self.previous_color = None
        self.round_number = 1
        self.score = 0
        self.current_text_color_name = None
        self.current_text_color_code = None
        self.current_word_color_name = None
        self.current_word_color_code = None
        if hasattr(self, 'timer_id') and self.timer_id:
            self.after_cancel(self.timer_id)
            self.timer_id = None
        self.timer_canvas.delete("all")
        self.timer_bar = self.timer_canvas.create_rectangle(
            0, 0, self.timer_width, self.timer_height, 
            fill="#4CAF50", outline="")
        self.word_label.config(text="")


class Manual3(tk.Frame):
    def __init__(self, parent, controller):
        """Инструкция к третьей части теста Струпа"""
        super().__init__(parent, bg="#FFFFFF")

        img = cv2.imread("logo.png", cv2.IMREAD_UNCHANGED)
        if img.shape[2] == 4:
            alpha_channel = img[:, :, 3]
            img_rgb = img[:, :, :3]
            white_background = np.ones_like(img_rgb) * 255
            alpha = alpha_channel[:, :, np.newaxis] / 255.0
            img = (img_rgb * alpha + white_background * (1 - alpha)).astype(np.uint8)
        else:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (255, 70))
        self.photo = tk.PhotoImage(data=cv2.imencode('.png', img)[1].tobytes())

        # Верхняя панель
        top_panel = tk.Frame(self, bg="#FFFFFF")
        top_panel.place(x=0, y=0, width=1920, height=100)
        # Логотип и кнопка возврата
        self.image_label = tk.Label(top_panel, image=self.photo, bg="#FFFFFF")
        self.image_label.pack(side="left", padx=10)
        self.back_btn = tk.Button(
            top_panel, 
            text="Главное меню", 
            font=("Arial", 18),
            bg="white", 
            fg="black", 
            height=1, 
            width=20, 
            borderwidth=0,
            command=lambda: controller.show_frame(StartPage))
        self.back_btn.place(relx=0.4, rely=0.5, anchor='center')
        # Разделительная линия
        line = tk.Frame(top_panel, bg="black", height=2, width=1920)
        line.place(x=0, y=95)
        # Основное содержимое инструкции
        label = tk.Label(
            self, 
            text="Инструкция к тесту Струпа, часть 3", 
            font=("Arial", 40), 
            bg="#FFFFFF")
        label.place(relx=0.5, rely=0.27, anchor='center')
        instruction_text = "В последней части теста Струпа выбирайте цвет по цвету слова"
        instruction_label = tk.Label(
            self, 
            text=instruction_text, 
            font=("Arial", 20), 
            bg="#FFFFFF", 
            justify="center")
        instruction_label.place(relx=0.5, rely=0.45, anchor='center')
        # Кнопка начала теста
        button2 = tk.Button(
            self, 
            text="Начать тест", 
            bg="#21743F", 
            fg="white", 
            width=20, 
            height=2,
            font=("Arial", 14),
            command=lambda: controller.show_frame(Test3))
        button2.place(relx=0.5, rely=0.65, anchor='center')


class Test3(tk.Frame):
    def __init__(self, parent, controller):
        """Тест Струпа (часть 3) - выбор цвета по цвету слова"""
        super().__init__(parent, bg="#FFFFFF")
        self.controller = controller
        self.active = False
        self.previous_color = None

        img = cv2.imread("logo.png", cv2.IMREAD_UNCHANGED)
        if img is None:
            raise FileNotFoundError("Не удалось загрузить logo.png")
        if img.shape[2] == 4:
            alpha_channel = img[:, :, 3]
            img_rgb = img[:, :, :3]
            white_background = np.ones_like(img_rgb) * 255
            alpha = alpha_channel[:, :, np.newaxis] / 255.0
            img = (img_rgb * alpha + white_background * (1 - alpha)).astype(np.uint8)
        else:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (255, 70))
        self.photo = tk.PhotoImage(data=cv2.imencode('.png', img)[1].tobytes())

        # Интерфейс теста
        self.top_panel = tk.Frame(self, bg="#FFFFFF")
        self.top_panel.place(x=0, y=0, relwidth=1.0, height=100)
        self.main_frame = tk.Frame(self, bg="#FFFFFF")
        self.main_frame.place(x=0, y=100, relwidth=1.0, relheight=1.0, height=-100)
        self.image_label = tk.Label(self.top_panel, image=self.photo, bg="#FFFFFF")
        self.image_label.pack(side="left", padx=10)
        self.back_btn = tk.Button(
            self.top_panel, 
            text="Главное меню", 
            font=("Arial", 18),
            bg="white", 
            fg="black", 
            height=1, 
            width=20, 
            borderwidth=0,
            command=lambda: [controller.reset_test(), controller.show_frame(StartPage)])
        self.back_btn.place(relx=0.5, rely=0.5, anchor='center')
        line = tk.Frame(self.top_panel, bg="black", height=2, width=1920)
        line.place(x=0, y=95)
        # Таймер
        self.timer_width = 1920
        self.timer_height = 20
        self.timer_canvas = tk.Canvas(
            self.main_frame, 
            width=self.timer_width, 
            height=self.timer_height, 
            bg="white", 
            highlightthickness=0)
        self.timer_canvas.pack(pady=(20), anchor="n")
        self.timer_bar = self.timer_canvas.create_rectangle(
            0, 0, self.timer_width, self.timer_height, 
            fill="#4CAF50", outline="")
        # Цвета для теста
        self.color_mapping = {
            "ФИОЛЕТОВЫЙ": "purple",
            "СИНИЙ": "blue",
            "ЗЕЛЕНЫЙ": "green",
            "КРАСНЫЙ": "red",
            "ЖЕЛТЫЙ": "yellow",
            "ЧЕРНЫЙ": "black"}
        # Параметры теста
        self.round_number = 1
        self.score = 0
        self.current_text_color_name = None
        self.current_text_color_code = None
        self.current_word_color_code = None
        self.timer_id = None
        # Элементы интерфейса
        self.word_label = tk.Label(self.main_frame, text="", font=("Arial", 36), bg="white")
        self.word_label.pack(anchor="center", pady=0)
        self.buttons_frame = tk.Frame(self.main_frame, bg="#FFFFFF")
        self.buttons_frame.pack(pady=50)
        # Кнопки выбора цвета
        self.color_buttons = []
        for i in range(6):
            btn = tk.Button(
                self.buttons_frame, 
                width=70, 
                height=8,
                command=lambda i=i: self.check_answer_by_index(i))  
            btn.grid(row=i//2, column=i%2, padx=90, pady=30)
            self.color_buttons.append(btn)
        self.start_round()

    def check_answer_by_index(self, index):
        """Проверка ответа по индексу кнопки"""
        if not self.active:
            return 
        # Получаем цвет и имя по текущему индексу кнопки
        color_name = list(self.current_button_colors.keys())[index]
        color_code = self.current_button_colors[color_name]
        self.check_answer(color_name, color_code)

    def start_round(self):
        """Начало нового раунда теста"""
        if not self.active:
            return
        if self.round_number > 10:
            self.end_game()
            return
        # Сброс таймера
        if hasattr(self, 'timer_id') and self.timer_id:
            self.after_cancel(self.timer_id)
            self.timer_id = None
        # Сброс полосы таймера
        self.timer_canvas.delete("all")
        self.timer_bar = self.timer_canvas.create_rectangle(
            0, 0, self.timer_width, self.timer_height, 
            fill="#4CAF50", outline="")
        
        available_colors = list(self.color_mapping.items())
        # Выбор цвета слова (правильный ответ)
        if hasattr(self, 'previous_word_color'):
            word_color_options = [c for c in available_colors if c[0] != self.previous_word_color]
        else:
            word_color_options = available_colors 
        word_color_name, word_color_code = random.choice(word_color_options)
        self.previous_word_color = word_color_name
        # Выбор названия цвета (текста) - должно отличаться от цвета слова
        text_color_options = [name for name in self.color_mapping.keys() 
                            if name != word_color_name]
        if hasattr(self, 'previous_text_name'):
            text_color_options = [name for name in text_color_options 
                                if name != self.previous_text_name]
        text_color_name = random.choice(text_color_options)
        self.previous_text_name = text_color_name
        # Сохранение текущих параметров
        self.current_word_color_code = word_color_code
        self.current_text_color_name = text_color_name
        # Отображение слова
        self.word_label.config(text=text_color_name, fg=word_color_code)
        # Случайное распределение цветов по кнопкам
        color_items = list(self.color_mapping.items())
        random.shuffle(color_items)
        self.current_button_colors = dict(color_items)
        # Обновление цветов кнопок
        for i, (color_name, color_code) in enumerate(color_items):
            self.color_buttons[i].config(bg=color_code)
        # Запуск таймера (2 секунды на раунд)
        self.start_time = time.time()
        self.animate_timer()

    def animate_timer(self):
        """Анимация таймера"""
        if not self.active:
            return
        elapsed = time.time() - self.start_time
        progress = elapsed / 2

        if progress < 1:
            new_width = self.timer_width * (1 - progress)
            self.timer_canvas.coords(self.timer_bar, 0, 0, new_width, self.timer_height)
            if progress > 0.5:
                self.timer_canvas.itemconfig(self.timer_bar, fill="#FFC107")
            if progress > 0.75:
                self.timer_canvas.itemconfig(self.timer_bar, fill="#F44336")
            self.timer_id = self.after(20, self.animate_timer)
        else:
            self.timer_canvas.coords(self.timer_bar, 0, 0, 0, self.timer_height)
            self.next_round()

    def check_answer(self, chosen_color_name, chosen_color_code):
        """Проверка ответа (сравниваем с цветом слова)"""
        if not self.active:
            return
        if hasattr(self, 'timer_id') and self.timer_id:
            self.after_cancel(self.timer_id)
            self.timer_id = None
        if self.round_number <= 10:
            if chosen_color_code == self.current_word_color_code:
                self.score += 1
            self.next_round()

    def next_round(self):
        """Переход к следующему раунду"""
        self.round_number += 1
        self.start_round()
        
    def end_game(self):
        """Завершение теста и сохранение результатов"""
        self.active = False
        with open("results.txt", "a", encoding="utf-8") as file:
            file.write(f"3 тест: {self.score} правильных ответов из 10\n")
        self.controller.show_frame(Manual4)
        
    def reset_test(self):
        """Сброс теста для повторного прохождения"""
        self.active = True
        self.round_number = 1
        self.score = 0
        self.current_text_color_name = None
        self.current_text_color_code = None
        self.current_word_color_code = None
        if hasattr(self, 'timer_id') and self.timer_id:
            self.after_cancel(self.timer_id)
            self.timer_id = None
        self.start_round()

    def reset(self):
        """Полный сброс теста"""
        self.active = False
        self.previous_color = None
        self.round_number = 1
        self.score = 0
        self.current_text_color_name = None
        self.current_text_color_code = None
        self.current_word_color_code = None
        if hasattr(self, 'timer_id') and self.timer_id:
            self.after_cancel(self.timer_id)
            self.timer_id = None
        self.timer_canvas.delete("all")
        self.timer_bar = self.timer_canvas.create_rectangle(
            0, 0, self.timer_width, self.timer_height, 
            fill="#4CAF50", outline="")
        self.word_label.config(text="")


class Manual4(tk.Frame):
    def __init__(self, parent, controller):
        """Инструкция к арифметическому тесту"""
        super().__init__(parent, bg="#FFFFFF")

        img = cv2.imread("logo.png", cv2.IMREAD_UNCHANGED)
        if img.shape[2] == 4:
            alpha_channel = img[:, :, 3]
            img_rgb = img[:, :, :3]
            white_background = np.ones_like(img_rgb) * 255
            alpha = alpha_channel[:, :, np.newaxis] / 255.0
            img = (img_rgb * alpha + white_background * (1 - alpha)).astype(np.uint8)
        else:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (255, 70))
        self.photo = tk.PhotoImage(data=cv2.imencode('.png', img)[1].tobytes())
        
        # Верхняя панель
        top_panel = tk.Frame(self, bg="#FFFFFF")
        top_panel.place(x=0, y=0, width=1920, height=100)
        # Логотип и кнопка возврата
        self.image_label = tk.Label(top_panel, image=self.photo, bg="#FFFFFF")
        self.image_label.pack(side="left", padx=10)
        self.back_btn = tk.Button(
            top_panel, 
            text="Главное меню", 
            font=("Arial", 18),
            bg="white", 
            fg="black", 
            height=1, 
            width=20, 
            borderwidth=0,
            command=lambda: controller.show_frame(StartPage))
        self.back_btn.place(relx=0.4, rely=0.5, anchor='center')
        # Разделительная линия
        line = tk.Frame(top_panel, bg="black", height=2, width=1920)
        line.place(x=0, y=95)
        # Основное содержимое инструкции
        label = tk.Label(
            self, 
            text="Инструкция к арифметическому тесту", 
            font=("Arial", 40), 
            bg="#FFFFFF")
        label.place(relx=0.5, rely=0.27, anchor='center')
        instruction_text = (
            "Нажимайте ДА (зеленое поле слева), если показано верное числовое равенство,\n"
            "иначе - НЕТ (красное поле справа)")
        instruction_label = tk.Label(
            self, 
            text=instruction_text, 
            font=("Arial", 20), 
            bg="#FFFFFF", 
            justify="center")
        instruction_label.place(relx=0.5, rely=0.45, anchor='center')
        # Кнопка начала теста
        button2 = tk.Button(
            self, 
            text="Начать тест", 
            bg="#21743F", 
            fg="white", 
            width=20, 
            height=2,
            font=("Arial", 14),
            command=lambda: controller.show_frame(Test4))
        button2.place(relx=0.5, rely=0.65, anchor='center')

class Test4(tk.Frame):
    def __init__(self, parent, controller):
        """Арифметический тест - проверка правильности уравнений"""
        super().__init__(parent, bg="#FFFFFF")
        self.controller = controller
        self.active = False
        self.previous_equation = None 
        self.total_rounds = 20  # Установлено 20 раундов вместо 10

        img = cv2.imread("logo.png", cv2.IMREAD_UNCHANGED)
        if img is None:
            raise FileNotFoundError("Не удалось загрузить logo.png")
        if img.shape[2] == 4:
            alpha_channel = img[:, :, 3]
            img_rgb = img[:, :, :3]
            white_background = np.ones_like(img_rgb) * 255
            alpha = alpha_channel[:, :, np.newaxis] / 255.0
            img = (img_rgb * alpha + white_background * (1 - alpha)).astype(np.uint8)
        else:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (255, 70))
        self.photo = tk.PhotoImage(data=cv2.imencode('.png', img)[1].tobytes())

        # Верхняя панель интерфейса
        self.top_panel = tk.Frame(self, bg="#FFFFFF")
        self.top_panel.place(x=0, y=0, relwidth=1.0, height=100)
        # Основной фрейм для содержимого теста
        self.main_frame = tk.Frame(self, bg="#FFFFFF")
        self.main_frame.place(x=0, y=100, relwidth=1.0, relheight=1.0, height=-100)
        # Логотип и кнопка возврата
        self.image_label = tk.Label(self.top_panel, image=self.photo, bg="#FFFFFF")
        self.image_label.pack(side="left", padx=10)
        self.back_btn = tk.Button(
            self.top_panel, 
            text="Главное меню", 
            font=("Arial", 18),
            bg="white", 
            fg="black", 
            height=1, 
            width=20, 
            borderwidth=0,
            command=lambda: [controller.reset_test(), controller.show_frame(StartPage)])
        self.back_btn.place(relx=0.5, rely=0.5, anchor='center')

        # Разделительная линия
        line = tk.Frame(self.top_panel, bg="black", height=2, width=1920)
        line.place(x=0, y=95)
        # Настройка визуального таймера
        self.timer_width = 1920
        self.timer_height = 20
        self.timer_canvas = tk.Canvas(
            self.main_frame, 
            width=self.timer_width, 
            height=self.timer_height, 
            bg="white", 
            highlightthickness=0)
        self.timer_canvas.pack(pady=(20), anchor="n")
        self.timer_bar = self.timer_canvas.create_rectangle(
            0, 0, self.timer_width, self.timer_height, 
            fill="#4CAF50", outline="")
        # Список арифметических уравнений (правильных и неправильных)
        self.equations = [
             # Простые сложения
            ("2 + 2 = 4", True),
            ("3 + 5 = 8", True),
            ("7 + 1 = 9", False),
            ("4 + 6 = 10", True),
            ("8 + 3 = 10", False),
            ("9 + 2 = 11", True),
            ("5 + 7 = 12", True),
            ("6 + 4 = 9", False),
            ("10 + 15 = 25", True),
            ("12 + 8 = 20", True),
            ("7 + 9 = 15", False),
            # Простые вычитания
            ("5 - 3 = 2", True),
            ("7 - 2 = 5", True),
            ("9 - 4 = 6", False),
            ("10 - 5 = 5", True),
            ("8 - 3 = 4", False),
            ("12 - 6 = 6", True),
            ("15 - 8 = 7", True),
            ("11 - 4 = 6", False),
            ("20 - 9 = 11", True),
            ("16 - 7 = 8", False),
            ("25 - 13 = 12", True),
            # Простые умножения
            ("2 × 3 = 6", True),
            ("4 × 5 = 20", True),
            ("3 × 7 = 24", False),
            ("6 × 4 = 24", True),
            ("5 × 5 = 30", False),
            ("7 × 3 = 21", True),
            ("8 × 2 = 16", True),
            ("9 × 4 = 32", False),
            ("10 × 6 = 60", True),
            ("7 × 8 = 54", False),
            ("9 × 9 = 81", True),
            # Простые деления
            ("10 ÷ 2 = 5", True),
            ("15 ÷ 3 = 5", True),
            ("20 ÷ 4 = 6", False),
            ("18 ÷ 6 = 3", True),
            ("21 ÷ 7 = 4", False),
            ("24 ÷ 8 = 3", True),
            ("36 ÷ 9 = 4", True),
            ("28 ÷ 7 = 3", False),
            ("50 ÷ 10 = 5", True),
            ("64 ÷ 8 = 7", False),
            ("81 ÷ 9 = 9", True)]
        
        # Параметры теста
        self.round_number = 1
        self.score = 0
        self.current_equation = None
        self.current_is_correct = None
        self.timer_id = None
        # Элементы интерфейса
        self.equation_label = tk.Label(
            self.main_frame, 
            text="", 
            font=("Arial", 46), 
            bg="white")
        self.equation_label.pack(anchor="center", pady=80)
        # Фрейм для кнопок ответа
        self.buttons_frame = tk.Frame(self.main_frame, bg="#FFFFFF")
        self.buttons_frame.pack(pady=100)
        # Кнопка ДА (зеленая)
        self.yes_button = tk.Button(
            self.buttons_frame, 
            text="ДА", 
            font=("Arial", 24),
            bg="#3D9140", 
            fg="black",
            width=30,
            height=8,
            command=lambda: self.check_answer(True))
        self.yes_button.pack(side="left", padx=50)
        # Кнопка НЕТ (красная)
        self.no_button = tk.Button(
            self.buttons_frame, 
            text="НЕТ", 
            font=("Arial", 24),
            bg="#FF4040", 
            fg="black",
            width=30,
            height=8,
            command=lambda: self.check_answer(False))
        self.no_button.pack(side="right", padx=50)
        self.active = True
        self.start_round()

    def get_random_equation(self):
        """Получение случайного уравнения, отличного от предыдущего"""
        available_eqs = [eq for eq in self.equations if eq[0] != self.previous_equation]
        if not available_eqs: 
            available_eqs = self.equations
        return random.choice(available_eqs)

    def start_round(self):
        """Начало нового раунда теста"""
        if not self.active:
            return
        if self.round_number > self.total_rounds:  # Используем self.total_rounds вместо жестко заданного 10
            self.end_game()
            return
        # Сброс таймера
        if hasattr(self, 'timer_id') and self.timer_id:
            self.after_cancel(self.timer_id)
            self.timer_id = None
        # Сброс полосы таймера
        self.timer_canvas.delete("all")
        self.timer_bar = self.timer_canvas.create_rectangle(
            0, 0, self.timer_width, self.timer_height, 
            fill="#4CAF50", outline="")
        # Выбор случайного уравнения
        equation, is_correct = self.get_random_equation()
        self.current_equation = equation
        self.current_is_correct = is_correct
        self.previous_equation = equation
        # Отображение уравнения
        self.equation_label.config(text=equation)
        # Запуск таймера (4 секунды на раунд)
        self.start_time = time.time()
        self.animate_timer()

    def animate_timer(self):
        """Анимация таймера"""
        if not self.active:
            return
        elapsed = time.time() - self.start_time
        progress = elapsed / 4

        if progress < 1:
            # Обновление полосы таймера
            new_width = self.timer_width * (1 - progress)
            self.timer_canvas.coords(self.timer_bar, 0, 0, new_width, self.timer_height)
            # Изменение цвета таймера
            if progress > 0.5:
                self.timer_canvas.itemconfig(self.timer_bar, fill="#FFC107")
            if progress > 0.75:
                self.timer_canvas.itemconfig(self.timer_bar, fill="#F44336")
            self.timer_id = self.after(20, self.animate_timer)
        else:
            # Время вышло - переход к следующему раунду
            self.timer_canvas.coords(self.timer_bar, 0, 0, 0, self.timer_height)
            self.next_round()

    def check_answer(self, user_answer):
        """Проверка ответа пользователя"""
        if not self.active:
            return
        if hasattr(self, 'timer_id') and self.timer_id:
            self.after_cancel(self.timer_id)
            self.timer_id = None
        if self.round_number <= self.total_rounds:  # Используем self.total_rounds вместо жестко заданного 10
            if user_answer == self.current_is_correct:
                self.score += 1
            self.next_round()

    def next_round(self):
        """Переход к следующему раунду"""
        self.round_number += 1
        self.start_round()
        
    def end_game(self):
        """Завершение теста и сохранение результатов"""
        self.active = False
        with open("results.txt", "a", encoding="utf-8") as file:
            file.write(f"4 тест: {self.score} правильных ответов из {self.total_rounds}\n")  # Используем self.total_rounds в сообщении
        self.controller.show_frame(Manual5)
        
    def reset_test(self):
        """Сброс теста для повторного прохождения"""
        self.active = True
        self.round_number = 1
        self.score = 0
        if hasattr(self, 'timer_id') and self.timer_id:
            self.after_cancel(self.timer_id)
            self.timer_id = None
        self.start_round()

    def reset(self):
        """Полный сброс теста"""
        self.active = False
        self.round_number = 1
        self.score = 0
        if hasattr(self, 'timer_id') and self.timer_id:
            self.after_cancel(self.timer_id)
            self.timer_id = None
        self.timer_canvas.delete("all")
        self.timer_bar = self.timer_canvas.create_rectangle(
            0, 0, self.timer_width, self.timer_height, 
            fill="#4CAF50", outline="")
        self.equation_label.config(text="")  # Очистка уравнения

class Manual5(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#FFFFFF")

        img = cv2.imread("logo.png", cv2.IMREAD_UNCHANGED)
        if img.shape[2] == 4: 
            alpha_channel = img[:, :, 3]
            img_rgb = img[:, :, :3]
            white_background = np.ones_like(img_rgb) * 255
            alpha = alpha_channel[:, :, np.newaxis] / 255.0
            img = (img_rgb * alpha + white_background * (1 - alpha)).astype(np.uint8)
        else:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (255, 70))
        self.photo = tk.PhotoImage(data=cv2.imencode('.png', img)[1].tobytes())

        # Верхняя панель с логотипом и кнопкой возврата
        top_panel = tk.Frame(self, bg="#FFFFFF")
        top_panel.place(x=0, y=0, width=1920, height=100)
        self.image_label = tk.Label(top_panel, image=self.photo, bg="#FFFFFF")
        self.image_label.pack(side="left", padx=10)
        self.back_btn = tk.Button(top_panel, text="Главное меню", font=("Arial", 18),
                           bg="white", fg="black", height=1, width=20, borderwidth=0,
                           command=lambda: controller.show_frame(StartPage))
        self.back_btn.place(relx=0.4, rely=0.5, anchor='center')
        # Разделительная линия
        line = tk.Frame(top_panel, bg="black", height=2, width=1920)
        line.place(x=0, y=95)
        # Основной контент страницы инструкции
        label = tk.Label(self, text="Инструкция к тесту на повторения положения", 
                       font=("Arial", 40), bg="#FFFFFF")
        label.place(relx=0.5, rely=0.27, anchor='center')
        instruction_text = (
            "Вам будет показан ряд фигур, имеющие различные форму, цвет и положение на экране.\n"
            "Нажимайте ДА, если ПОЛОЖЕНИЕ (сверху, по середине, снизу) \n"
            "текущей фигуры полностью совпадает с ПОЛОЖЕНИЕМ предыдущей, иначе - НЕТ")
        instruction_label = tk.Label(self, text=instruction_text, 
                                   font=("Arial", 20), bg="#FFFFFF", justify="center")
        instruction_label.place(relx=0.5, rely=0.45, anchor='center')
        # Кнопка начала теста
        button2 = tk.Button(self, text="Начать тест", 
                          bg="#21743F", fg="white", width=20, height=2,
                          font=("Arial", 14),
                          command=lambda: controller.show_frame(Test5))
        button2.place(relx=0.5, rely=0.65, anchor='center')

class Test5(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#FFFFFF")
        self.controller = controller
        self.active = False
        self.previous_position = None  # Положение предыдущей фигуры
        self.current_position = None   # Положение текущей фигуры
        self.round_number = 1          # Номер текущего раунда
        self.score = 0                 # Количество правильных ответов
        self.total_rounds = 11         # Общее количество раундов (1 демо + 10 тестовых)

        img = cv2.imread("logo.png", cv2.IMREAD_UNCHANGED)
        if img is None:
            raise FileNotFoundError("Не удалось загрузить logo.png - проверьте путь к файлу")
        if img.shape[2] == 4:
            alpha_channel = img[:, :, 3]
            img_rgb = img[:, :, :3]
            white_background = np.ones_like(img_rgb) * 255
            alpha = alpha_channel[:, :, np.newaxis] / 255.0
            img = (img_rgb * alpha + white_background * (1 - alpha)).astype(np.uint8)
        else:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (255, 70))
        self.photo = tk.PhotoImage(data=cv2.imencode('.png', img)[1].tobytes())

        # Верхняя панель интерфейса
        self.top_panel = tk.Frame(self, bg="#FFFFFF")
        self.top_panel.place(x=0, y=0, relwidth=1.0, height=100)
        # Основной фрейм для содержимого теста
        self.main_frame = tk.Frame(self, bg="#FFFFFF")
        self.main_frame.place(x=0, y=100, relwidth=1.0, relheight=1.0, height=-100)
        # Элементы верхней панели
        self.image_label = tk.Label(self.top_panel, image=self.photo, bg="#FFFFFF")
        self.image_label.pack(side="left", padx=10)
        self.back_btn = tk.Button(self.top_panel, text="Главное меню", font=("Arial", 18),
                           bg="white", fg="black", height=1, width=20, borderwidth=0,
                           command=lambda: [
                                   controller.reset_test(),
                                   controller.show_frame(StartPage)])
        self.back_btn.place(relx=0.5, rely=0.5, anchor='center')
        line = tk.Frame(self.top_panel, bg="black", height=2, width=1920)
        line.place(x=0, y=95)
        # Настройка таймера
        self.timer_width = 1920
        self.timer_height = 20
        self.timer_canvas = tk.Canvas(self.main_frame, width=self.timer_width, height=self.timer_height, 
                                    bg="white", highlightthickness=0)
        self.timer_canvas.pack(pady=(20), anchor="n")
        self.timer_bar = self.timer_canvas.create_rectangle(
            0, 0, self.timer_width, self.timer_height, 
            fill="#4CAF50", outline="")
        # Параметры фигур
        self.colors = ["red", "blue", "green", "yellow", "purple", "black"]
        self.shapes = ["circle", "square", "triangle", "star", "hexagon"]
        self.positions = ["top", "middle", "bottom"]  # Возможные позиции фигур
        # Настройки отображения фигур
        self.shape_size = 130      # Размер фигур в пикселях
        self.shape_outline = "#333333"  # Цвет контура фигур
        self.shape_outline_width = 0.5  # Толщина контура
        # Холст для отображения фигур
        self.shape_canvas = tk.Canvas(
            self.main_frame, 
            width=300, 
            height=1000, 
            bg="white", 
            highlightthickness=0)
        self.shape_canvas.pack(padx=400)
        # Фреймы для кнопок ответа
        self.button_frame1 = tk.Frame(self.main_frame, bg="#FFFFFF")
        self.button_frame1.place(x=0, y=400, width=600, height=400)
        self.button_frame2 = tk.Frame(self.main_frame, bg="#FFFFFF")
        self.button_frame2.place(x=940, y=400, width=600, height=400)
        # Кнопки ответа
        self.yes_button = tk.Button(
            self.button_frame1, 
            text="ДА", 
            font=("Arial", 24),
            bg="#3D9140",  # Зеленый цвет
            fg="black",
            width=30,
            height=8,
            command=lambda: self.check_answer(True))
        self.no_button = tk.Button(
            self.button_frame2, 
            text="НЕТ", 
            font=("Arial", 24),
            bg="#FF4040",  # Красный цвет
            fg="black",
            width=30,
            height=8,
            command=lambda: self.check_answer(False))
        # Начало теста
        self.active = True
        self.start_round()
    def draw_shape(self, position):
        """Отрисовка фигуры в указанной позиции"""
        self.shape_canvas.delete("all")
        # Выбор цвета, отличного от предыдущего
        color = random.choice([c for c in self.colors if c != getattr(self, 'last_color', None)])
        self.last_color = color
        # Выбор формы, отличной от предыдущей
        shape = random.choice([s for s in self.shapes if s != getattr(self, 'last_shape', None)])
        self.last_shape = shape
        # Координаты центра фигуры в зависимости от позиции
        x_center = 150
        y_center = {
            "top": 100,
            "middle": 300,
            "bottom": 600}[position]
        # Отрисовка фигуры с тенью
        shadow_offset = 3
        if shape == "circle":
            # Тень
            self.shape_canvas.create_oval(
                x_center-self.shape_size/2+shadow_offset,
                y_center-self.shape_size/2+shadow_offset,
                x_center+self.shape_size/2+shadow_offset,
                y_center+self.shape_size/2+shadow_offset,
                fill="#DDDDDD", outline="")
            # Основная фигура
            self.shape_canvas.create_oval(
                x_center-self.shape_size/2,
                y_center-self.shape_size/2,
                x_center+self.shape_size/2,
                y_center+self.shape_size/2,
                fill=color, 
                outline=self.shape_outline,
                width=self.shape_outline_width)
        elif shape == "square":
            # Тень
            self.shape_canvas.create_rectangle(
                x_center-self.shape_size/2+shadow_offset,
                y_center-self.shape_size/2+shadow_offset,
                x_center+self.shape_size/2+shadow_offset,
                y_center+self.shape_size/2+shadow_offset,
                fill="#DDDDDD", outline="")
            # Основная фигура
            self.shape_canvas.create_rectangle(
                x_center-self.shape_size/2,
                y_center-self.shape_size/2,
                x_center+self.shape_size/2,
                y_center+self.shape_size/2,
                fill=color, 
                outline=self.shape_outline,
                width=self.shape_outline_width)       
        elif shape == "triangle":
            points = [
                x_center, y_center-self.shape_size/2,
                x_center-self.shape_size/2, y_center+self.shape_size/2,
                x_center+self.shape_size/2, y_center+self.shape_size/2]
            shadow_points = [
                x_center, y_center-self.shape_size/2+shadow_offset,
                x_center-self.shape_size/2+shadow_offset, y_center+self.shape_size/2+shadow_offset,
                x_center+self.shape_size/2+shadow_offset, y_center+self.shape_size/2+shadow_offset]
            # Тень
            self.shape_canvas.create_polygon(
                shadow_points,
                fill="#DDDDDD", outline="")
            # Основная фигура
            self.shape_canvas.create_polygon(
                points,
                fill=color, 
                outline=self.shape_outline,
                width=self.shape_outline_width) 
        elif shape == "star":
            # Рисуем звезду
            outer_radius = self.shape_size/2
            inner_radius = outer_radius * 0.4
            points = []
            shadow_points = []
            for i in range(5):
                # Внешняя точка
                angle = 2 * math.pi * i / 5 - math.pi/2
                x_outer = x_center + outer_radius * math.cos(angle)
                y_outer = y_center + outer_radius * math.sin(angle)
                points.extend([x_outer, y_outer])
                shadow_points.extend([x_outer+shadow_offset, y_outer+shadow_offset])
                # Внутренняя точка
                angle += 2 * math.pi / 10
                x_inner = x_center + inner_radius * math.cos(angle)
                y_inner = y_center + inner_radius * math.sin(angle)
                points.extend([x_inner, y_inner])
                shadow_points.extend([x_inner+shadow_offset, y_inner+shadow_offset])
            # Тень
            self.shape_canvas.create_polygon(
                shadow_points,
                fill="#DDDDDD", outline="")
            # Основная фигура
            self.shape_canvas.create_polygon(
                points,
                fill=color, 
                outline=self.shape_outline,
                width=self.shape_outline_width)
        else:
            # Рисуем шестиугольник
            radius = self.shape_size/2
            points = []
            shadow_points = []
            for i in range(6):
                angle = 2 * math.pi * i / 6
                x = x_center + radius * math.cos(angle)
                y = y_center + radius * math.sin(angle)
                points.extend([x, y])
                shadow_points.extend([x+shadow_offset, y+shadow_offset])
            # Тень
            self.shape_canvas.create_polygon(
                shadow_points,
                fill="#DDDDDD", outline="")
            # Основная фигура
            self.shape_canvas.create_polygon(
                points,
                fill=color, 
                outline=self.shape_outline,
                width=self.shape_outline_width)
        return position

    def start_round(self):
        """Начало нового раунда теста"""
        if not self.active:
            return
        if self.round_number > self.total_rounds:
            self.end_game()
            return
        # Сброс флага ответа
        if hasattr(self, 'answer_given'):
            del self.answer_given
        # Разблокируем кнопки
        self.yes_button.config(state=tk.NORMAL)
        self.no_button.config(state=tk.NORMAL)
        # Сброс таймера
        if hasattr(self, 'timer_id') and self.timer_id:
            self.after_cancel(self.timer_id)
            self.timer_id = None
        # Сброс полосы таймера
        self.timer_canvas.delete("all")
        self.timer_bar = self.timer_canvas.create_rectangle(
            0, 0, self.timer_width, self.timer_height, 
            fill="#4CAF50", outline="")
        # Сохранение предыдущего положения
        self.previous_position = self.current_position
        # Генерация нового положения фигуры
        position = random.choice(self.positions)
        self.current_position = self.draw_shape(position)
        # Управление видимостью кнопок (скрываем для демо-раунда)
        if self.round_number == 1:
            self.yes_button.pack_forget()
            self.no_button.pack_forget()
        else:
            self.yes_button.pack(side="left", padx=50)
            self.no_button.pack(side="right", padx=50)
        # Скрываем фигуру через 2 секунды
        self.after(1000, self.hide_shape)
        # Запуск таймера
        self.start_time = time.time()
        self.animate_timer()
    def hide_shape(self):
        """Скрывает фигуру, но не завершает раунд"""
        self.shape_canvas.delete("all")

    def animate_timer(self):
        """Анимация таймера"""
        if not self.active:
            return
        elapsed = time.time() - self.start_time
        total_time = 3  # Время на ответ - 3 секунды
        progress = elapsed / total_time
        
        if progress < 1:
            new_width = self.timer_width * (1 - progress)
            self.timer_canvas.coords(self.timer_bar, 0, 0, new_width, self.timer_height)
            # Изменение цвета таймера в зависимости от оставшегося времени
            if progress > 0.75:
                self.timer_canvas.itemconfig(self.timer_bar, fill="#F44336")  # Красный
            elif progress > 0.5:
                self.timer_canvas.itemconfig(self.timer_bar, fill="#FFC107")  # Желтый
            else:
                self.timer_canvas.itemconfig(self.timer_bar, fill="#4CAF50")  # Зеленый
            self.timer_id = self.after(20, self.animate_timer)
        else:
            # Время вышло - проверяем ответ (если был дан)
            if hasattr(self, 'answer_given') and self.answer_given:
                if self.round_number > 1:  # Проверяем только начиная со 2 раунда
                    correct_answer = (self.current_position == self.previous_position)
                    if self.user_answer == correct_answer:
                        self.score += 1
                del self.answer_given  # Удаляем флаг ответа
            # Переход к следующему раунду
            self.timer_canvas.coords(self.timer_bar, 0, 0, 0, self.timer_height)
            self.next_round()

    def check_answer(self, user_answer):
        """Проверка ответа пользователя"""
        if not self.active:
            return
        # Если ответ уже был дан - игнорируем
        if hasattr(self, 'answer_given') and self.answer_given:
            return
        # Блокируем кнопки
        self.yes_button.config(state=tk.DISABLED)
        self.no_button.config(state=tk.DISABLED)
        # Запоминаем ответ пользователя
        self.user_answer = user_answer
        self.answer_given = True
        # Функция для отображения и поддержания сообщения
        def show_and_keep_message():
            if hasattr(self, 'answer_given') and self.answer_given:
                self.shape_canvas.delete("all")
                self.shape_canvas.create_text(
                    150, 300,  # Центр холста
                    text="Ответ сохранен",
                    font=("Arial", 24, "bold"),
                    fill="#4CAF50",  # Зеленый цвет
                    tags="answer_text")
                # Продолжаем обновлять сообщение каждые 100 мс
                self.after(100, show_and_keep_message)
        # Первоначальное отображение сообщения
        show_and_keep_message()

    def next_round(self):
        """Переход к следующему раунду"""
        self.round_number += 1
        self.start_round()
        
    def end_game(self):
        """Завершение теста и сохранение результатов"""
        self.active = False
        with open("results.txt", "a", encoding="utf-8") as file:
            file.write(f"5 тест: {self.score} правильных ответов из 10\n")
        self.controller.show_frame(Manual6)
        
    def reset_test(self):
        """Сброс теста к начальному состоянию"""
        self.active = True
        self.round_number = 1
        self.score = 0
        self.previous_position = None
        self.current_position = None
        if hasattr(self, 'timer_id') and self.timer_id:
            self.after_cancel(self.timer_id)
            self.timer_id = None
        self.yes_button.pack_forget()
        self.no_button.pack_forget()
        self.start_round()

    def reset(self):
        """Полный сброс теста (очистка всех элементов)"""
        self.active = False
        self.round_number = 1
        self.score = 0
        self.previous_position = None
        self.current_position = None
        if hasattr(self, 'timer_id') and self.timer_id:
            self.after_cancel(self.timer_id)
            self.timer_id = None
        self.timer_canvas.delete("all")
        self.timer_bar = self.timer_canvas.create_rectangle(
            0, 0, self.timer_width, self.timer_height, 
            fill="#4CAF50", outline="")
        self.shape_canvas.delete("all")
        self.yes_button.pack_forget()
        self.no_button.pack_forget()

class Manual6(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#FFFFFF")

        img = cv2.imread("logo.png", cv2.IMREAD_UNCHANGED)
        if img.shape[2] == 4:
            alpha_channel = img[:, :, 3]
            img_rgb = img[:, :, :3]
            white_background = np.ones_like(img_rgb) * 255
            alpha = alpha_channel[:, :, np.newaxis] / 255.0
            img = (img_rgb * alpha + white_background * (1 - alpha)).astype(np.uint8)
        else:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (255, 70))
        self.photo = tk.PhotoImage(data=cv2.imencode('.png', img)[1].tobytes())

        # Верхняя панель
        top_panel = tk.Frame(self, bg="#FFFFFF")
        top_panel.place(x=0, y=0, width=1920, height=100)
        self.image_label = tk.Label(top_panel, image=self.photo, bg="#FFFFFF")
        self.image_label.pack(side="left", padx=10)
        self.back_btn = tk.Button(top_panel, text="Главное меню", font=("Arial", 18),
                           bg="white", fg="black", height=1, width=20, borderwidth=0,
                           command=lambda: controller.show_frame(StartPage))
        self.back_btn.place(relx=0.4, rely=0.5, anchor='center')
        line = tk.Frame(top_panel, bg="black", height=2, width=1920)
        line.place(x=0, y=95)
        # Инструкция для теста на повторение формы
        label = tk.Label(self, text="Инструкция к тесту на повторения фигур", 
                       font=("Arial", 40), bg="#FFFFFF")
        label.place(relx=0.5, rely=0.27, anchor='center')
        instruction_text = (
            "Нажимайте ДА, если ФОРМА (круг, квадрат, треугольник, шестиугольник, звезда) \n"
            "текущей фигуры полностью совпадает с ФОРМОЙ предыдущей, иначе - НЕТ")
        instruction_label = tk.Label(self, text=instruction_text, 
                                   font=("Arial", 20), bg="#FFFFFF", justify="center")
        instruction_label.place(relx=0.5, rely=0.45, anchor='center')
        button2 = tk.Button(self, text="Начать тест", 
                          bg="#21743F", fg="white", width=20, height=2,
                          font=("Arial", 14),
                          command=lambda: controller.show_frame(Test6))
        button2.place(relx=0.5, rely=0.65, anchor='center')

class Test6(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#FFFFFF")
        self.controller = controller
        self.active = False
        self.previous_shape = None  # Предыдущая форма фигуры
        self.current_shape = None   # Текущая форма фигуры
        self.round_number = 1
        self.score = 0
        self.total_rounds = 11      # 1 демо-раунд + 10 тестовых

        img = cv2.imread("logo.png", cv2.IMREAD_UNCHANGED)
        if img is None:
            raise FileNotFoundError("Не удалось загрузить logo.png - проверьте путь к файлу")
        if img.shape[2] == 4:
            alpha_channel = img[:, :, 3]
            img_rgb = img[:, :, :3]
            white_background = np.ones_like(img_rgb) * 255
            alpha = alpha_channel[:, :, np.newaxis] / 255.0
            img = (img_rgb * alpha + white_background * (1 - alpha)).astype(np.uint8)
        else:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (255, 70))
        self.photo = tk.PhotoImage(data=cv2.imencode('.png', img)[1].tobytes())

        self.top_panel = tk.Frame(self, bg="#FFFFFF")
        self.top_panel.place(x=0, y=0, relwidth=1.0, height=100)
        self.main_frame = tk.Frame(self, bg="#FFFFFF")
        self.main_frame.place(x=0, y=100, relwidth=1.0, relheight=1.0, height=-100)
        self.image_label = tk.Label(self.top_panel, image=self.photo, bg="#FFFFFF")
        self.image_label.pack(side="left", padx=10)
        self.back_btn = tk.Button(self.top_panel, text="Главное меню", font=("Arial", 18),
                           bg="white", fg="black", height=1, width=20, borderwidth=0,
                           command=lambda: [
                                   controller.reset_test(),
                                   controller.show_frame(StartPage)])
        self.back_btn.place(relx=0.5, rely=0.5, anchor='center')
        line = tk.Frame(self.top_panel, bg="black", height=2, width=1920)
        line.place(x=0, y=95)
        # Таймер
        self.timer_width = 1920
        self.timer_height = 20
        self.timer_canvas = tk.Canvas(self.main_frame, width=self.timer_width, height=self.timer_height, 
                                    bg="white", highlightthickness=0)
        self.timer_canvas.pack(pady=(20), anchor="n")
        self.timer_bar = self.timer_canvas.create_rectangle(
            0, 0, self.timer_width, self.timer_height, 
            fill="#4CAF50", outline="")
        # Параметры фигур
        self.colors = ["red", "blue", "green", "yellow", "purple", "black"]
        self.shapes = ["circle", "square", "triangle", "star", "hexagon"]
        self.positions = ["top", "middle", "bottom"]
        # Настройки отображения
        self.shape_size = 130
        self.shape_outline = "#333333"
        self.shape_outline_width = 0.5
        # Холст для фигур
        self.shape_canvas = tk.Canvas(
            self.main_frame, 
            width=300, 
            height=1000, 
            bg="white", 
            highlightthickness=0)
        self.shape_canvas.pack(padx=400)
        # Кнопки ответа
        self.button_frame1 = tk.Frame(self.main_frame, bg="#FFFFFF")
        self.button_frame1.place(x=0, y=400, width=600, height=400)
        self.button_frame2 = tk.Frame(self.main_frame, bg="#FFFFFF")
        self.button_frame2.place(x=940, y=400, width=600, height=400)
        self.yes_button = tk.Button(
            self.button_frame1, 
            text="ДА", 
            font=("Arial", 24),
            bg="#3D9140",
            fg="black",
            width=30,
            height=8,
            command=lambda: self.check_answer(True))
        self.no_button = tk.Button(
            self.button_frame2, 
            text="НЕТ", 
            font=("Arial", 24),
            bg="#FF4040",
            fg="black",
            width=30,
            height=8,
            command=lambda: self.check_answer(False))
        # Начало теста
        self.active = True
        self.start_round()

    def draw_shape(self, position):
        """Отрисовка фигуры с повышенной вероятностью повторения формы"""
        self.shape_canvas.delete("all")
        color = random.choice([c for c in self.colors if c != getattr(self, 'last_color', None)])
        self.last_color = color
        # Повышенная вероятность (20%) повторения предыдущей формы
        if self.previous_shape and random.random() < 0.2:
            shape = self.previous_shape
        else:
            available_shapes = [s for s in self.shapes if s != getattr(self, 'last_shape', None)]
            shape = random.choice(available_shapes if available_shapes else self.shapes)
        self.last_shape = shape
        # Координаты центра
        x_center = 150
        y_center = {
            "top": 100,
            "middle": 300,
            "bottom": 600}[position]

        shadow_offset = 3
        if shape == "circle":
            # Тень
            self.shape_canvas.create_oval(
                x_center-self.shape_size/2+shadow_offset,
                y_center-self.shape_size/2+shadow_offset,
                x_center+self.shape_size/2+shadow_offset,
                y_center+self.shape_size/2+shadow_offset,
                fill="#DDDDDD", outline="")
            # Основная фигура
            self.shape_canvas.create_oval(
                x_center-self.shape_size/2,
                y_center-self.shape_size/2,
                x_center+self.shape_size/2,
                y_center+self.shape_size/2,
                fill=color, 
                outline=self.shape_outline,
                width=self.shape_outline_width)
        elif shape == "square":
            # Тень
            self.shape_canvas.create_rectangle(
                x_center-self.shape_size/2+shadow_offset,
                y_center-self.shape_size/2+shadow_offset,
                x_center+self.shape_size/2+shadow_offset,
                y_center+self.shape_size/2+shadow_offset,
                fill="#DDDDDD", outline="")
            # Основная фигура
            self.shape_canvas.create_rectangle(
                x_center-self.shape_size/2,
                y_center-self.shape_size/2,
                x_center+self.shape_size/2,
                y_center+self.shape_size/2,
                fill=color, 
                outline=self.shape_outline,
                width=self.shape_outline_width)
        elif shape == "triangle":
            points = [
                x_center, y_center-self.shape_size/2,
                x_center-self.shape_size/2, y_center+self.shape_size/2,
                x_center+self.shape_size/2, y_center+self.shape_size/2]
            shadow_points = [
                x_center, y_center-self.shape_size/2+shadow_offset,
                x_center-self.shape_size/2+shadow_offset, y_center+self.shape_size/2+shadow_offset,
                x_center+self.shape_size/2+shadow_offset, y_center+self.shape_size/2+shadow_offset]
            # Тень
            self.shape_canvas.create_polygon(
                shadow_points,
                fill="#DDDDDD", outline="")
            # Основная фигура
            self.shape_canvas.create_polygon(
                points,
                fill=color, 
                outline=self.shape_outline,
                width=self.shape_outline_width)
        elif shape == "star":
            # Рисуем звезду
            outer_radius = self.shape_size/2
            inner_radius = outer_radius * 0.4
            points = []
            shadow_points = []
            for i in range(5):
                # Внешняя точка
                angle = 2 * math.pi * i / 5 - math.pi/2
                x_outer = x_center + outer_radius * math.cos(angle)
                y_outer = y_center + outer_radius * math.sin(angle)
                points.extend([x_outer, y_outer])
                shadow_points.extend([x_outer+shadow_offset, y_outer+shadow_offset])
                # Внутренняя точка
                angle += 2 * math.pi / 10
                x_inner = x_center + inner_radius * math.cos(angle)
                y_inner = y_center + inner_radius * math.sin(angle)
                points.extend([x_inner, y_inner])
                shadow_points.extend([x_inner+shadow_offset, y_inner+shadow_offset])
            # Тень
            self.shape_canvas.create_polygon(
                shadow_points,
                fill="#DDDDDD", outline="")
            # Основная фигура
            self.shape_canvas.create_polygon(
                points,
                fill=color, 
                outline=self.shape_outline,
                width=self.shape_outline_width)
        else:
            # Рисуем шестиугольник
            radius = self.shape_size/2
            points = []
            shadow_points = []
            for i in range(6):
                angle = 2 * math.pi * i / 6
                x = x_center + radius * math.cos(angle)
                y = y_center + radius * math.sin(angle)
                points.extend([x, y])
                shadow_points.extend([x+shadow_offset, y+shadow_offset])
            # Тень
            self.shape_canvas.create_polygon(
                shadow_points,
                fill="#DDDDDD", outline="")
            # Основная фигура
            self.shape_canvas.create_polygon(
                points,
                fill=color, 
                outline=self.shape_outline,
                width=self.shape_outline_width)
        return shape  # Возвращаем форму фигуры

    def start_round(self):
        """Начало нового раунда теста"""
        if not self.active:
            return
        if self.round_number > self.total_rounds:
            self.end_game()
            return
        # Сброс флага ответа
        if hasattr(self, 'answer_given'):
            del self.answer_given
        # Разблокируем кнопки
        self.yes_button.config(state=tk.NORMAL)
        self.no_button.config(state=tk.NORMAL)
        # Сброс таймера
        if hasattr(self, 'timer_id') and self.timer_id:
            self.after_cancel(self.timer_id)
            self.timer_id = None
        # Сброс полосы таймера
        self.timer_canvas.delete("all")
        self.timer_bar = self.timer_canvas.create_rectangle(
            0, 0, self.timer_width, self.timer_height, 
            fill="#4CAF50", outline="")
        # Сохранение предыдущей формы
        self.previous_shape = self.current_shape
        # Генерация новой фигуры
        position = random.choice(self.positions)
        self.current_shape = self.draw_shape(position)
        # Управление видимостью кнопок
        if self.round_number == 1:
            self.yes_button.pack_forget()
            self.no_button.pack_forget()
        else:
            self.yes_button.pack(side="left", padx=50)
            self.no_button.pack(side="right", padx=50)
        self.after(1000, self.hide_shape)
        # Запуск таймера
        self.start_time = time.time()
        self.animate_timer()

    def hide_shape(self):
        """Скрывает фигуру, но не завершает раунд"""
        self.shape_canvas.delete("all")

    def animate_timer(self):
        """Анимация таймера"""
        if not self.active:
            return
        elapsed = time.time() - self.start_time
        total_time = 3  # Время на ответ - 3 секунды
        progress = elapsed / total_time

        if progress < 1:
            new_width = self.timer_width * (1 - progress)
            self.timer_canvas.coords(self.timer_bar, 0, 0, new_width, self.timer_height)
            # Изменение цвета таймера
            if progress > 0.75:
                self.timer_canvas.itemconfig(self.timer_bar, fill="#F44336")
            elif progress > 0.5:
                self.timer_canvas.itemconfig(self.timer_bar, fill="#FFC107")
            else:
                self.timer_canvas.itemconfig(self.timer_bar, fill="#4CAF50")
            self.timer_id = self.after(20, self.animate_timer)
        else:
            # Время вышло - проверяем ответ (если был дан)
            if hasattr(self, 'answer_given') and self.answer_given:
                if self.round_number > 1:
                    # Для Test6 сравниваем формы фигур
                    correct_answer = (self.current_shape == self.previous_shape)
                    if self.user_answer == correct_answer:
                        self.score += 1
                del self.answer_given
            # Переход к следующему раунду
            self.timer_canvas.coords(self.timer_bar, 0, 0, 0, self.timer_height)
            self.next_round()

    def check_answer(self, user_answer):
        """Проверка ответа пользователя"""
        if not self.active:
            return
        # Если ответ уже был дан - игнорируем
        if hasattr(self, 'answer_given') and self.answer_given:
            return
        # Блокируем кнопки
        self.yes_button.config(state=tk.DISABLED)
        self.no_button.config(state=tk.DISABLED)
        # Запоминаем ответ пользователя
        self.user_answer = user_answer
        self.answer_given = True
        # Функция для отображения и поддержания сообщения
        def show_and_keep_message():
            if hasattr(self, 'answer_given') and self.answer_given:
                self.shape_canvas.delete("all")
                self.shape_canvas.create_text(
                    150, 300,  # Центр холста
                    text="Ответ сохранен",
                    font=("Arial", 24, "bold"),
                    fill="#4CAF50",  # Зеленый цвет
                    tags="answer_text")
                # Продолжаем обновлять сообщение каждые 100 мс
                self.after(100, show_and_keep_message)
        # Первоначальное отображение сообщения
        show_and_keep_message()

    def next_round(self):
        """Переход к следующему раунду"""
        self.round_number += 1
        self.start_round()
        
    def end_game(self):
        """Завершение теста и переход к следующему"""
        self.active = False
        with open("results.txt", "a", encoding="utf-8") as file:
            file.write(f"6 тест: {self.score} правильных ответов из 10\n")
        self.controller.show_frame(Manual7)
        
    def reset_test(self):
        """Сброс теста"""
        self.active = True
        self.round_number = 1
        self.score = 0
        self.previous_shape = None
        self.current_shape = None
        if hasattr(self, 'timer_id') and self.timer_id:
            self.after_cancel(self.timer_id)
            self.timer_id = None
        self.yes_button.pack_forget()
        self.no_button.pack_forget()
        self.start_round()

    def reset(self):
        """Полный сброс теста"""
        self.active = False
        self.round_number = 1
        self.score = 0
        self.previous_shape = None
        self.current_shape = None
        if hasattr(self, 'timer_id') and self.timer_id:
            self.after_cancel(self.timer_id)
            self.timer_id = None
        self.timer_canvas.delete("all")
        self.timer_bar = self.timer_canvas.create_rectangle(
            0, 0, self.timer_width, self.timer_height, 
            fill="#4CAF50", outline="")
        self.shape_canvas.delete("all")
        self.yes_button.pack_forget()
        self.no_button.pack_forget()
        
class Manual7(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#FFFFFF")

        img = cv2.imread("logo.png", cv2.IMREAD_UNCHANGED)
        if img.shape[2] == 4:
            alpha_channel = img[:, :, 3]
            img_rgb = img[:, :, :3]
            white_background = np.ones_like(img_rgb) * 255
            alpha = alpha_channel[:, :, np.newaxis] / 255.0
            img = (img_rgb * alpha + white_background * (1 - alpha)).astype(np.uint8)
        else:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (255, 70))
        self.photo = tk.PhotoImage(data=cv2.imencode('.png', img)[1].tobytes())

        top_panel = tk.Frame(self, bg="#FFFFFF")
        top_panel.place(x=0, y=0, width=1920, height=100)
        self.image_label = tk.Label(top_panel, image=self.photo, bg="#FFFFFF")
        self.image_label.pack(side="left", padx=10)
        self.back_btn = tk.Button(top_panel, text="Главное меню", font=("Arial", 18),
                           bg="white", fg="black", height=1, width=20, borderwidth=0,
                           command=lambda: controller.show_frame(StartPage))
        self.back_btn.place(relx=0.4, rely=0.5, anchor='center')
        line = tk.Frame(top_panel, bg="black", height=2, width=1920)
        line.place(x=0, y=95)
        label = tk.Label(self, text="Инструкция к тесту на повторения фигур и цвета", 
                       font=("Arial", 40), bg="#FFFFFF")
        label.place(relx=0.5, rely=0.27, anchor='center')
        instruction_text = (
            "Нажимайте ДА, если ФОРМА и ЦВЕТ текущей фигуры полностью совпадает\n"
            "с ФОРМОЙ и ЦВЕТОМ предыдущей, иначе - НЕТ")
        instruction_label = tk.Label(self, text=instruction_text, 
                                   font=("Arial", 20), bg="#FFFFFF", justify="center")
        instruction_label.place(relx=0.5, rely=0.45, anchor='center')
        button2 = tk.Button(self, text="Начать тест", 
                          bg="#21743F", fg="white", width=20, height=2,
                          font=("Arial", 14),
                          command=lambda: controller.show_frame(Test7))
        button2.place(relx=0.5, rely=0.65, anchor='center')

class Test7(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#FFFFFF")
        self.controller = controller
        self.active = False
        self.previous_shape = None  # Хранит предыдущую форму (форма + цвет)
        self.current_shape = None   # Хранит текущую форму (форма + цвет)
        self.round_number = 1       # Номер текущего раунда
        self.score = 0             # Счетчик правильных ответов
        self.total_rounds = 11     # Общее количество раундов (1 демо + 10 тестовых)

        img = cv2.imread("logo.png", cv2.IMREAD_UNCHANGED)
        if img is None:
            raise FileNotFoundError("Не удалось загрузить logo.png - проверьте путь к файлу")
        if img.shape[2] == 4:
            alpha_channel = img[:, :, 3]
            img_rgb = img[:, :, :3]
            white_background = np.ones_like(img_rgb) * 255
            alpha = alpha_channel[:, :, np.newaxis] / 255.0
            img = (img_rgb * alpha + white_background * (1 - alpha)).astype(np.uint8)
        else:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (255, 70))
        self.photo = tk.PhotoImage(data=cv2.imencode('.png', img)[1].tobytes())

        self.top_panel = tk.Frame(self, bg="#FFFFFF")
        self.top_panel.place(x=0, y=0, relwidth=1.0, height=100)
        self.main_frame = tk.Frame(self, bg="#FFFFFF")
        self.main_frame.place(x=0, y=100, relwidth=1.0, relheight=1.0, height=-100)
        self.image_label = tk.Label(self.top_panel, image=self.photo, bg="#FFFFFF")
        self.image_label.pack(side="left", padx=10)
        self.back_btn = tk.Button(self.top_panel, text="Главное меню", font=("Arial", 18),
                           bg="white", fg="black", height=1, width=20, borderwidth=0,
                           command=lambda: [
                                   controller.reset_test(),
                                   controller.show_frame(StartPage)])
        self.back_btn.place(relx=0.5, rely=0.5, anchor='center')
        line = tk.Frame(self.top_panel, bg="black", height=2, width=1920)
        line.place(x=0, y=95)
        # Настройки таймера
        self.timer_width = 1920
        self.timer_height = 20
        # Холст для анимированного таймера
        self.timer_canvas = tk.Canvas(self.main_frame, width=self.timer_width, height=self.timer_height, 
                                    bg="white", highlightthickness=0)
        self.timer_canvas.pack(pady=(20), anchor="n")
        # Полоса таймера (зеленая по умолчанию)
        self.timer_bar = self.timer_canvas.create_rectangle(
            0, 0, self.timer_width, self.timer_height, 
            fill="#4CAF50", outline="")
        # Параметры фигур для теста
        self.colors = ["red", "blue", "green", "yellow", "purple", "black"]
        self.shapes = ["circle", "square", "triangle", "star", "hexagon"]
        self.positions = ["top", "middle", "bottom"]
        # Стили фигур
        self.shape_size = 130      # Размер фигур в пикселях
        self.shape_outline = "#333333"  # Цвет контура
        self.shape_outline_width = 0.5  # Толщина контура
        self.canvas_bg = "#FAFAFA"      # Цвет фона холста
        # Холст для отображения фигур
        self.shape_canvas = tk.Canvas(
            self.main_frame, 
            width=300, 
            height=1000, 
            bg="white", 
            highlightthickness=0)
        self.shape_canvas.pack(padx=400)
        # Фреймы для кнопок ответа
        self.button_frame1 = tk.Frame(self.main_frame, bg="#FFFFFF")
        self.button_frame1.place(x=0, y=400, width=600, height=400)
        self.button_frame2 = tk.Frame(self.main_frame, bg="#FFFFFF")
        self.button_frame2.place(x=940, y=400, width=600, height=400)
        # Кнопка "ДА" (зеленая)
        self.yes_button = tk.Button(
            self.button_frame1, 
            text="ДА", 
            font=("Arial", 24),
            bg="#3D9140",  # Зеленый цвет
            fg="black",
            width=30,
            height=8,
            command=lambda: self.check_answer(True))
        self.yes_button.pack(side="left", padx=50)
        # Кнопка "НЕТ" (красная)
        self.no_button = tk.Button(
            self.button_frame2, 
            text="НЕТ", 
            font=("Arial", 24),
            bg="#FF4040",  # Красный цвет
            fg="black",
            width=30,
            height=8,
            command=lambda: self.check_answer(False))
        self.no_button.pack(side="right", padx=50)
        # Скрываем кнопки в первом раунде (демо-раунд)
        self.yes_button.pack_forget()
        self.no_button.pack_forget()
        # Активируем тест и начинаем первый раунд
        self.active = True
        self.start_round()

    def draw_shape(self, position):
        """Отрисовка фигуры в указанной позиции с возможностью повторения формы и цвета"""
        self.shape_canvas.delete("all")
        # С вероятностью 50% повторяем предыдущий цвет, иначе выбираем новый
        if self.previous_shape and random.random() < 0.5:
            color = self.previous_shape['color']
        else:
            color = random.choice([c for c in self.colors if c != getattr(self, 'last_color', None)])
        self.last_color = color
        # С вероятностью 50% повторяем предыдущую форму, иначе выбираем новую
        if self.previous_shape and random.random() < 0.5:
            shape = self.previous_shape['shape']
        else:
            shape = random.choice(self.shapes)
        self.last_shape = shape
        # Координаты центра для разных позиций
        x_center = 150
        y_center = {
            "top": 100,
            "middle": 300,
            "bottom": 600}[position]
        # Параметры тени
        shadow_offset = 3
        # Отрисовка фигур с тенью
        if shape == "circle":
            # Тень
            self.shape_canvas.create_oval(
                x_center-self.shape_size/2+shadow_offset,
                y_center-self.shape_size/2+shadow_offset,
                x_center+self.shape_size/2+shadow_offset,
                y_center+self.shape_size/2+shadow_offset,
                fill="#DDDDDD", outline="")
            # Основная фигура
            self.shape_canvas.create_oval(
                x_center-self.shape_size/2,
                y_center-self.shape_size/2,
                x_center+self.shape_size/2,
                y_center+self.shape_size/2,
                fill=color, 
                outline=self.shape_outline,
                width=self.shape_outline_width)
        elif shape == "square":
            # Тень
            self.shape_canvas.create_rectangle(
                x_center-self.shape_size/2+shadow_offset,
                y_center-self.shape_size/2+shadow_offset,
                x_center+self.shape_size/2+shadow_offset,
                y_center+self.shape_size/2+shadow_offset,
                fill="#DDDDDD", outline="")
            # Основная фигура
            self.shape_canvas.create_rectangle(
                x_center-self.shape_size/2,
                y_center-self.shape_size/2,
                x_center+self.shape_size/2,
                y_center+self.shape_size/2,
                fill=color, 
                outline=self.shape_outline,
                width=self.shape_outline_width)
            
        elif shape == "triangle":
            points = [
                x_center, y_center-self.shape_size/2,
                x_center-self.shape_size/2, y_center+self.shape_size/2,
                x_center+self.shape_size/2, y_center+self.shape_size/2]
            shadow_points = [
                x_center, y_center-self.shape_size/2+shadow_offset,
                x_center-self.shape_size/2+shadow_offset, y_center+self.shape_size/2+shadow_offset,
                x_center+self.shape_size/2+shadow_offset, y_center+self.shape_size/2+shadow_offset]
            # Тень
            self.shape_canvas.create_polygon(
                shadow_points,
                fill="#DDDDDD", outline="")
            # Основная фигура
            self.shape_canvas.create_polygon(
                points,
                fill=color, 
                outline=self.shape_outline,
                width=self.shape_outline_width)
        elif shape == "star":
            # Параметры звезды
            outer_radius = self.shape_size/2
            inner_radius = outer_radius * 0.4
            points = []
            shadow_points = []
            # Расчет точек звезды
            for i in range(5):
                # Внешняя точка
                angle = 2 * math.pi * i / 5 - math.pi/2
                x_outer = x_center + outer_radius * math.cos(angle)
                y_outer = y_center + outer_radius * math.sin(angle)
                points.extend([x_outer, y_outer])
                shadow_points.extend([x_outer+shadow_offset, y_outer+shadow_offset])
                # Внутренняя точка
                angle += 2 * math.pi / 10
                x_inner = x_center + inner_radius * math.cos(angle)
                y_inner = y_center + inner_radius * math.sin(angle)
                points.extend([x_inner, y_inner])
                shadow_points.extend([x_inner+shadow_offset, y_inner+shadow_offset])
            # Тень
            self.shape_canvas.create_polygon(
                shadow_points,
                fill="#DDDDDD", outline="")
            # Основная фигура
            self.shape_canvas.create_polygon(
                points,
                fill=color, 
                outline=self.shape_outline,
                width=self.shape_outline_width)
        else:
            # Расчет точек шестиугольника
            radius = self.shape_size/2
            points = []
            shadow_points = []
            for i in range(6):
                angle = 2 * math.pi * i / 6
                x = x_center + radius * math.cos(angle)
                y = y_center + radius * math.sin(angle)
                points.extend([x, y])
                shadow_points.extend([x+shadow_offset, y+shadow_offset])
            # Тень
            self.shape_canvas.create_polygon(
                shadow_points,
                fill="#DDDDDD", outline="")
            # Основная фигура
            self.shape_canvas.create_polygon(
                points,
                fill=color, 
                outline=self.shape_outline,
                width=self.shape_outline_width)
        return {'shape': shape, 'color': color}

    def start_round(self):
        """Начало нового раунда теста"""
        if not self.active:
            return
        if self.round_number > self.total_rounds:
            self.end_game()
            return
        # Сброс флага ответа
        if hasattr(self, 'answer_given'):
            del self.answer_given
        self.yes_button.config(state=tk.NORMAL)
        self.no_button.config(state=tk.NORMAL)
        # Сброс таймера
        if hasattr(self, 'timer_id') and self.timer_id:
            self.after_cancel(self.timer_id)
            self.timer_id = None
        # Сброс полосы таймера
        self.timer_canvas.delete("all")
        self.timer_bar = self.timer_canvas.create_rectangle(
            0, 0, self.timer_width, self.timer_height, 
            fill="#4CAF50", outline="")
        # Сохранение предыдущей фигуры
        self.previous_shape = self.current_shape
        # Генерация новой фигуры
        position = random.choice(self.positions)
        self.current_shape = self.draw_shape(position)
                # Управление видимостью кнопок
        if self.round_number == 1:
            self.yes_button.pack_forget()
            self.no_button.pack_forget()
        else:
            self.yes_button.pack(side="left", padx=50)
            self.no_button.pack(side="right", padx=50)
        self.after(1000, self.hide_shape)
        # Запуск таймера
        self.start_time = time.time()
        self.animate_timer()

    def hide_shape(self):
        """Скрывает фигуру, но не завершает раунд"""
        self.shape_canvas.delete("all")

    def animate_timer(self):
        """Анимация таймера"""
        if not self.active:
            return
        elapsed = time.time() - self.start_time
        total_time = 3  # Время на ответ - 3 секунды
        progress = elapsed / total_time
        
        if progress < 1:
            new_width = self.timer_width * (1 - progress)
            self.timer_canvas.coords(self.timer_bar, 0, 0, new_width, self.timer_height)
            # Изменение цвета таймера в зависимости от оставшегося времени
            if progress > 0.75:
                self.timer_canvas.itemconfig(self.timer_bar, fill="#F44336")  # Красный
            elif progress > 0.5:
                self.timer_canvas.itemconfig(self.timer_bar, fill="#FFC107")  # Желтый
            else:
                self.timer_canvas.itemconfig(self.timer_bar, fill="#4CAF50")  # Зеленый
            self.timer_id = self.after(20, self.animate_timer)
        else:
            # Время вышло - проверяем ответ (если был дан)
            if hasattr(self, 'answer_given') and self.answer_given:
                if self.round_number > 1:  # Проверяем только начиная со 2 раунда
                    if self.previous_shape and self.current_shape:
                    # Проверка совпадения формы и цвета
                        correct_answer = (self.current_shape['shape'] == self.previous_shape['shape'] and 
                            self.current_shape['color'] == self.previous_shape['color'])
                    
                    if self.user_answer == correct_answer:
                            self.score += 1 
                del self.answer_given  # Удаляем флаг ответа
            # Переход к следующему раунду
            self.timer_canvas.coords(self.timer_bar, 0, 0, 0, self.timer_height)
            self.next_round()

    def check_answer(self, user_answer):
        """Проверка ответа пользователя"""
        if not self.active:
            return
        # Если ответ уже был дан - игнорируем
        if hasattr(self, 'answer_given') and self.answer_given:
            return
        # Блокируем кнопки
        self.yes_button.config(state=tk.DISABLED)
        self.no_button.config(state=tk.DISABLED)
        # Запоминаем ответ пользователя
        self.user_answer = user_answer
        self.answer_given = True
        # Функция для отображения и поддержания сообщения
        def show_and_keep_message():
            if hasattr(self, 'answer_given') and self.answer_given:
                self.shape_canvas.delete("all")
                self.shape_canvas.create_text(
                    150, 300,  # Центр холста
                    text="Ответ сохранен",
                    font=("Arial", 24, "bold"),
                    fill="#4CAF50",  # Зеленый цвет
                    tags="answer_text")
                # Продолжаем обновлять сообщение каждые 100 мс
                self.after(100, show_and_keep_message)
        # Первоначальное отображение сообщения
        show_and_keep_message()

    def next_round(self):
        """Переход к следующему раунду"""
        self.round_number += 1
        self.start_round()
        
    def end_game(self):
        """Завершение теста и сохранение результатов"""
        self.active = False
        with open("results.txt", "a", encoding="utf-8") as file:
            file.write(f"7 тест: {self.score} правильных ответов из 10\n")
        self.controller.show_frame(Manual8)
        
    def reset_test(self):
        """Сброс теста к начальному состоянию"""
        self.active = True
        self.round_number = 1
        self.score = 0
        self.previous_shape = None
        self.current_shape = None
        if hasattr(self, 'timer_id') and self.timer_id:
            self.after_cancel(self.timer_id)
            self.timer_id = None
        self.yes_button.pack_forget()
        self.no_button.pack_forget()
        self.start_round()

    def reset(self):
        """Полный сброс теста (используется при возврате в главное меню)"""
        self.active = False
        self.round_number = 1
        self.score = 0
        self.previous_shape = None
        self.current_shape = None
        # Отмена таймера
        if hasattr(self, 'timer_id') and self.timer_id:
            self.after_cancel(self.timer_id)
            self.timer_id = None
        # Сброс таймера
        self.timer_canvas.delete("all")
        self.timer_bar = self.timer_canvas.create_rectangle(
            0, 0, self.timer_width, self.timer_height, 
            fill="#4CAF50", outline="")
        # Очистка холста с фигурой
        self.shape_canvas.delete("all")
        # Скрытие кнопок
        self.yes_button.pack_forget()
        self.no_button.pack_forget()

class Manual8(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#FFFFFF")

        img = cv2.imread("logo.png", cv2.IMREAD_UNCHANGED)
        if img.shape[2] == 4:
            alpha_channel = img[:, :, 3]
            img_rgb = img[:, :, :3]
            white_background = np.ones_like(img_rgb) * 255
            alpha = alpha_channel[:, :, np.newaxis] / 255.0
            img = (img_rgb * alpha + white_background * (1 - alpha)).astype(np.uint8)
        else:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (255, 70))
        self.photo = tk.PhotoImage(data=cv2.imencode('.png', img)[1].tobytes())
        
        # Верхняя панель
        top_panel = tk.Frame(self, bg="#FFFFFF")
        top_panel.place(x=0, y=0, width=1920, height=100)
        self.image_label = tk.Label(top_panel, image=self.photo, bg="#FFFFFF")
        self.image_label.pack(side="left", padx=10)
        self.back_btn = tk.Button(top_panel, text="Главное меню", font=("Arial", 18),
                           bg="white", fg="black", height=1, width=20, borderwidth=0,
                           command=lambda: controller.show_frame(StartPage))
        self.back_btn.place(relx=0.4, rely=0.5, anchor='center')
        line = tk.Frame(top_panel, bg="black", height=2, width=1920)
        line.place(x=0, y=95)
        label = tk.Label(self, text="Инструкция к тесту на повторения фигур и положения", 
                       font=("Arial", 40), bg="#FFFFFF")
        label.place(relx=0.5, rely=0.27, anchor='center')
        instruction_text = (
            "Нажимайте ДА, если ПОЛОЖЕНИЕ и ФОРМА текущей фигуры полностью совпадает\n"
            "с ПОЛОЖЕНИЕМ и ФОРМОЙ предыдущей, иначе - НЕТ")
        instruction_label = tk.Label(self, text=instruction_text, 
                                   font=("Arial", 20), bg="#FFFFFF", justify="center")
        instruction_label.place(relx=0.5, rely=0.45, anchor='center')
        button2 = tk.Button(self, text="Начать тест", 
                          bg="#21743F", fg="white", width=20, height=2,
                          font=("Arial", 14),
                          command=lambda: controller.show_frame(Test8))
        button2.place(relx=0.5, rely=0.65, anchor='center')

class Test8(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#FFFFFF")
        self.controller = controller
        self.active = False
        self.previous_data = None  # Будет хранить словарь с формой и положением
        self.current_data = None   # Текущие данные фигуры
        self.round_number = 1
        self.score = 0
        self.total_rounds = 11  # 1 демо-раунд + 10 тестовых раундов

        img = cv2.imread("logo.png", cv2.IMREAD_UNCHANGED)
        if img is None:
            raise FileNotFoundError("Не удалось загрузить logo.png - проверьте путь к файлу")
        if img.shape[2] == 4:
            alpha_channel = img[:, :, 3]
            img_rgb = img[:, :, :3]
            white_background = np.ones_like(img_rgb) * 255
            alpha = alpha_channel[:, :, np.newaxis] / 255.0
            img = (img_rgb * alpha + white_background * (1 - alpha)).astype(np.uint8)
        else:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (255, 70))
        self.photo = tk.PhotoImage(data=cv2.imencode('.png', img)[1].tobytes())

        # Верхняя панель
        self.top_panel = tk.Frame(self, bg="#FFFFFF")
        self.top_panel.place(x=0, y=0, relwidth=1.0, height=100)
        # Основной фрейм
        self.main_frame = tk.Frame(self, bg="#FFFFFF")
        self.main_frame.place(x=0, y=100, relwidth=1.0, relheight=1.0, height=-100)
        self.image_label = tk.Label(self.top_panel, image=self.photo, bg="#FFFFFF")
        self.image_label.pack(side="left", padx=10)
        self.back_btn = tk.Button(self.top_panel, text="Главное меню", font=("Arial", 18),
                           bg="white", fg="black", height=1, width=20, borderwidth=0,
                           command=lambda: [
                                   controller.reset_test(),
                                   controller.show_frame(StartPage)])
        self.back_btn.place(relx=0.5, rely=0.5, anchor='center')
        line = tk.Frame(self.top_panel, bg="black", height=2, width=1920)
        line.place(x=0, y=95)
        # Конфигурация таймера
        self.timer_width = 1920
        self.timer_height = 20
        # Холст для анимированной полосы таймера
        self.timer_canvas = tk.Canvas(self.main_frame, width=self.timer_width, height=self.timer_height, 
                                    bg="white", highlightthickness=0)
        self.timer_canvas.pack(pady=(20), anchor="n")
        # Начальная полоса таймера
        self.timer_bar = self.timer_canvas.create_rectangle(
            0, 0, self.timer_width, self.timer_height, 
            fill="#4CAF50", outline="")
        # Параметры фигур
        self.colors = ["red", "blue", "green", "yellow", "purple", "black"]
        self.shapes = ["circle", "square", "triangle", "star", "hexagon"]
        self.positions = ["top", "middle", "bottom"]
        # Настройки стиля
        self.shape_size = 130  # Размер фигур
        self.shape_outline = "#333333"  # Цвет контура
        self.shape_outline_width = 0.5  # Толщина контура
        self.canvas_bg = "#FAFAFA"  # Цвет фона холста
        self.round_number = 1
        self.score = 0
        self.timer_id = None
        # Холст для отображения фигуры
        self.shape_canvas = tk.Canvas(
            self.main_frame, 
            width=300, 
            height=1000, 
            bg="white", 
            highlightthickness=0)
        self.shape_canvas.pack(padx=400)
        self.button_frame1 = tk.Frame(self.main_frame, bg="#FFFFFF")
        self.button_frame1.place(x=0, y=400, width=600, height=400)
        self.button_frame2 = tk.Frame(self.main_frame, bg="#FFFFFF")
        self.button_frame2.place(x=940, y=400, width=600, height=400)
        self.yes_button = tk.Button(
            self.button_frame1, 
            text="ДА", 
            font=("Arial", 24),
            bg="#3D9140",
            fg="black",
            width=30,
            height=8,
            command=lambda: self.check_answer(True))
        self.yes_button.pack(side="left", padx=50)
        self.no_button = tk.Button(
            self.button_frame2, 
            text="НЕТ", 
            font=("Arial", 24),
            bg="#FF4040",
            fg="black",
            width=30,
            height=8,
            command=lambda: self.check_answer(False))
        self.no_button.pack(side="right", padx=50)
        # Скрываем кнопки для первой итерации
        self.yes_button.pack_forget()
        self.no_button.pack_forget()
        # Активируем тест при создании
        self.active = True
        self.start_round()

    def draw_shape(self, position):
        """Отображение фигур с возможностью повторения формы и положения"""
        self.shape_canvas.delete("all")
        # Случайный выбор цвета
        color = random.choice(self.colors)
        # С вероятностью 60% повторяем предыдущую форму, иначе выбираем новую
        if self.previous_data and random.random() < 0.5:
            shape = self.previous_data['shape']
        else:
            shape = random.choice(self.shapes)
        # С вероятностью 60% повторяем предыдущее положение, иначе выбираем новое
        if self.previous_data and random.random() < 0.5:
            position = self.previous_data['position']
        # Центральные координаты
        x_center = 150
        y_center = {
            "top": 100,
            "middle": 300,
            "bottom": 600}[position]
        # Рисуем фигуры
        shadow_offset = 3
        if shape == "circle":
            # Тень
            self.shape_canvas.create_oval(
                x_center-self.shape_size/2+shadow_offset,
                y_center-self.shape_size/2+shadow_offset,
                x_center+self.shape_size/2+shadow_offset,
                y_center+self.shape_size/2+shadow_offset,
                fill="#DDDDDD", outline="")
            # Основная фигура
            self.shape_canvas.create_oval(
                x_center-self.shape_size/2,
                y_center-self.shape_size/2,
                x_center+self.shape_size/2,
                y_center+self.shape_size/2,
                fill=color, 
                outline=self.shape_outline,
                width=self.shape_outline_width)  
        elif shape == "square":
            # Тень
            self.shape_canvas.create_rectangle(
                x_center-self.shape_size/2+shadow_offset,
                y_center-self.shape_size/2+shadow_offset,
                x_center+self.shape_size/2+shadow_offset,
                y_center+self.shape_size/2+shadow_offset,
                fill="#DDDDDD", outline="")
            # Основная фигура
            self.shape_canvas.create_rectangle(
                x_center-self.shape_size/2,
                y_center-self.shape_size/2,
                x_center+self.shape_size/2,
                y_center+self.shape_size/2,
                fill=color, 
                outline=self.shape_outline,
                width=self.shape_outline_width)
        elif shape == "triangle":
            points = [
                x_center, y_center-self.shape_size/2,
                x_center-self.shape_size/2, y_center+self.shape_size/2,
                x_center+self.shape_size/2, y_center+self.shape_size/2]
            shadow_points = [
                x_center, y_center-self.shape_size/2+shadow_offset,
                x_center-self.shape_size/2+shadow_offset, y_center+self.shape_size/2+shadow_offset,
                x_center+self.shape_size/2+shadow_offset, y_center+self.shape_size/2+shadow_offset]
            # Тень
            self.shape_canvas.create_polygon(
                shadow_points,
                fill="#DDDDDD", outline="")
            # Основная фигура
            self.shape_canvas.create_polygon(
                points,
                fill=color, 
                outline=self.shape_outline,
                width=self.shape_outline_width)
        elif shape == "star":
            # Рисуем звезду
            outer_radius = self.shape_size/2
            inner_radius = outer_radius * 0.4
            points = []
            shadow_points = []
            for i in range(5):
                # Внешняя точка
                angle = 2 * math.pi * i / 5 - math.pi/2
                x_outer = x_center + outer_radius * math.cos(angle)
                y_outer = y_center + outer_radius * math.sin(angle)
                points.extend([x_outer, y_outer])
                shadow_points.extend([x_outer+shadow_offset, y_outer+shadow_offset])
                # Внутренняя точка
                angle += 2 * math.pi / 10
                x_inner = x_center + inner_radius * math.cos(angle)
                y_inner = y_center + inner_radius * math.sin(angle)
                points.extend([x_inner, y_inner])
                shadow_points.extend([x_inner+shadow_offset, y_inner+shadow_offset])
            # Тень
            self.shape_canvas.create_polygon(
                shadow_points,
                fill="#DDDDDD", outline="")
            # Основная фигура
            self.shape_canvas.create_polygon(
                points,
                fill=color, 
                outline=self.shape_outline,
                width=self.shape_outline_width)
        else:
            # Рисуем шестиугольник
            radius = self.shape_size/2
            points = []
            shadow_points = []
            for i in range(6):
                angle = 2 * math.pi * i / 6
                x = x_center + radius * math.cos(angle)
                y = y_center + radius * math.sin(angle)
                points.extend([x, y])
                shadow_points.extend([x+shadow_offset, y+shadow_offset])
            # Тень
            self.shape_canvas.create_polygon(
                shadow_points,
                fill="#DDDDDD", outline="")
            # Основная фигура
            self.shape_canvas.create_polygon(
                points,
                fill=color, 
                outline=self.shape_outline,
                width=self.shape_outline_width)
        return {'shape': shape, 'position': position}

    def start_round(self):
        """Начало нового раунда теста"""
        if not self.active:
            return
        if self.round_number > self.total_rounds:
            self.end_game()
            return
        # Сброс флага ответа
        if hasattr(self, 'answer_given'):
            del self.answer_given
        self.yes_button.config(state=tk.NORMAL)
        self.no_button.config(state=tk.NORMAL)
        # Сброс таймера
        if hasattr(self, 'timer_id') and self.timer_id:
            self.after_cancel(self.timer_id)
            self.timer_id = None
        # Полностью перерисовываем полосу таймера
        self.timer_canvas.delete("all")
        self.timer_bar = self.timer_canvas.create_rectangle(
            0, 0, self.timer_width, self.timer_height, 
            fill="#4CAF50", outline="")
        # Сохраняем предыдущие данные
        self.previous_data = self.current_data
        # Генерируем новую фигуру
        position = random.choice(self.positions)
        self.current_data = self.draw_shape(position)
        # Управление видимостью кнопок
        if self.round_number == 1:
            self.yes_button.pack_forget()
            self.no_button.pack_forget()
        else:
            self.yes_button.pack(side="left", padx=50)
            self.no_button.pack(side="right", padx=50)
        self.after(1000, self.hide_shape)
        # Запускаем таймер
        self.start_time = time.time()
        self.animate_timer()

    def hide_shape(self):
        """Скрывает фигуру, но не завершает раунд"""
        self.shape_canvas.delete("all")

    def animate_timer(self):
        """Анимация таймера"""
        if not self.active:
            return
        elapsed = time.time() - self.start_time
        total_time = 3  # Время на ответ - 3 секунды
        progress = elapsed / total_time

        if progress < 1:
            new_width = self.timer_width * (1 - progress)
            self.timer_canvas.coords(self.timer_bar, 0, 0, new_width, self.timer_height)
            # Изменение цвета таймера в зависимости от оставшегося времени
            if progress > 0.75:
                self.timer_canvas.itemconfig(self.timer_bar, fill="#F44336")  # Красный
            elif progress > 0.5:
                self.timer_canvas.itemconfig(self.timer_bar, fill="#FFC107")  # Желтый
            else:
                self.timer_canvas.itemconfig(self.timer_bar, fill="#4CAF50")  # Зеленый
            self.timer_id = self.after(20, self.animate_timer)
        else:
            # Время вышло - проверяем ответ (если был дан)
            if hasattr(self, 'answer_given') and self.answer_given:
                if self.round_number > 1:  # Проверяем только начиная со 2 раунда
                    if self.previous_data and self.current_data:
                        correct_answer = (self.current_data['shape'] == self.previous_data['shape'] and 
                                self.current_data['position'] == self.previous_data['position'])
                    if self.user_answer == correct_answer:
                        self.score += 1
                del self.answer_given  # Удаляем флаг ответа
            # Переход к следующему раунду
            self.timer_canvas.coords(self.timer_bar, 0, 0, 0, self.timer_height)
            self.next_round()

    def check_answer(self, user_answer):
        """Проверка ответа пользователя"""
        if not self.active:
            return
        # Если ответ уже был дан - игнорируем
        if hasattr(self, 'answer_given') and self.answer_given:
            return
        # Блокируем кнопки
        self.yes_button.config(state=tk.DISABLED)
        self.no_button.config(state=tk.DISABLED)
        # Запоминаем ответ пользователя
        self.user_answer = user_answer
        self.answer_given = True
        # Функция для отображения и поддержания сообщения
        def show_and_keep_message():
            if hasattr(self, 'answer_given') and self.answer_given:
                self.shape_canvas.delete("all")
                self.shape_canvas.create_text(
                    150, 300,  # Центр холста
                    text="Ответ сохранен",
                    font=("Arial", 24, "bold"),
                    fill="#4CAF50",  # Зеленый цвет
                    tags="answer_text")
                # Продолжаем обновлять сообщение каждые 100 мс
                self.after(100, show_and_keep_message)
        # Первоначальное отображение сообщения
        show_and_keep_message()

    def next_round(self):
        self.round_number += 1
        self.start_round()
        
    def end_game(self):
        self.active = False
        with open("results.txt", "a", encoding="utf-8") as file:
            file.write(f"8 тест: {self.score} правильных ответов из 10\n")
        self.controller.show_frame(EndPage)
        
    def reset_test(self):
        self.active = True
        self.round_number = 1
        self.score = 0
        self.previous_shape = None
        self.current_shape = None
        if hasattr(self, 'timer_id') and self.timer_id:
            self.after_cancel(self.timer_id)
            self.timer_id = None
        self.yes_button.pack_forget()
        self.no_button.pack_forget()
        self.start_round()

    def reset(self):
        """Метод для сброса прогресса теста"""
        self.active = False
        self.round_number = 1
        self.score = 0
        self.previous_shape = None
        self.current_shape = None
        # Отменяем таймер
        if hasattr(self, 'timer_id') and self.timer_id:
            self.after_cancel(self.timer_id)
            self.timer_id = None
        # Полностью сбрасываем полосу таймера
        self.timer_canvas.delete("all")
        self.timer_bar = self.timer_canvas.create_rectangle(
            0, 0, self.timer_width, self.timer_height, 
            fill="#4CAF50", outline="")
        # Очищаем холст с фигурой
        self.shape_canvas.delete("all")
        # Скрываем кнопки
        self.yes_button.pack_forget()
        self.no_button.pack_forget()

class EndPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#FFFFFF")

        img = cv2.imread("logo.png", cv2.IMREAD_UNCHANGED)
        if img.shape[2] == 4:
            alpha_channel = img[:, :, 3]
            img_rgb = img[:, :, :3]
            white_background = np.ones_like(img_rgb) * 255
            alpha = alpha_channel[:, :, np.newaxis] / 255.0
            img = (img_rgb * alpha + white_background * (1 - alpha)).astype(np.uint8)
        else:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (255, 70))
        self.photo = tk.PhotoImage(data=cv2.imencode('.png', img)[1].tobytes())

        # Верхняя панель
        top_panel = tk.Frame(self, bg="#FFFFFF")
        top_panel.place(x=0, y=0, width=1920, height=100)
        # Логотип слева
        self.image_label = tk.Label(top_panel, image=self.photo, bg="#FFFFFF")
        self.image_label.pack(side="left", padx=10)
        line = tk.Frame(top_panel, bg="black", height=2, width=1920)  # Ширина линии по всей ширине экрана
        line.place(x=0, y=95)  # Размещаем линию под верхней панелью
        label = tk.Label(self, text="Вы прошли все предложенные тесты!", 
                       font=("Arial", 40), bg="#FFFFFF")
        label.place(relx=0.5, rely=0.27, anchor='center')
        instruction_text = (
            "Спасибо за прохождение! Далее вы можете посмотреть свои результаты,\n"
            "а также снова пройти тесты,чтобы улучшить свой результат!")
        instruction_label = tk.Label(self, text=instruction_text, 
                                   font=("Arial", 20), bg="#FFFFFF", justify="center")
        instruction_label.place(relx=0.5, rely=0.45, anchor='center')
        button2 = tk.Button(self, text="Результаты", 
                          bg="#21743F", fg="white", width=20, height=2,
                          font=("Arial", 14),
                          command=lambda: controller.show_frame(ResultsPage))
        button2.place(relx=0.5, rely=0.65, anchor='center')

class ResultsPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#FFFFFF")
        self.controller = controller
        self.no_results_shown = False  # Флаг для отслеживания показа сообщения

        img = cv2.imread("logo.png", cv2.IMREAD_UNCHANGED)
        if img is None:
            raise FileNotFoundError("Не удалось загрузить logo.png - проверьте путь к файлу")
        if img.shape[2] == 4:
            alpha_channel = img[:, :, 3]
            img_rgb = img[:, :, :3]
            white_background = np.ones_like(img_rgb) * 255
            alpha = alpha_channel[:, :, np.newaxis] / 255.0
            img = (img_rgb * alpha + white_background * (1 - alpha)).astype(np.uint8)
        else:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (255, 70))
        self.photo = tk.PhotoImage(data=cv2.imencode('.png', img)[1].tobytes())

        # Верхняя панель
        top_panel = tk.Frame(self, bg="#FFFFFF")
        top_panel.place(x=0, y=0, width=1920, height=100)
        # Логотип слева
        self.image_label = tk.Label(top_panel, image=self.photo, bg="#FFFFFF")
        self.image_label.pack(side="left", padx=10)
        # Горизонтальная линия
        line = tk.Frame(top_panel, bg="black", height=2, width=1920)
        line.place(x=0, y=95)
        # Основной контент
        main_frame = tk.Frame(self, bg="#FFFFFF")
        main_frame.pack(expand=True, fill="both", pady=(100, 0))
        # Заголовок
        title_label = tk.Label(main_frame, text="Результаты тестов", 
                             font=("Arial", 40), bg="#FFFFFF")
        title_label.pack(pady=50) 
        # Фрейм для результатов
        self.results_frame = tk.Frame(main_frame, bg="#FFFFFF")
        self.results_frame.pack(expand=True)
        # Метка с результатами
        self.results_label = tk.Label(self.results_frame, text="", 
                                    font=("Arial", 18), bg="#FFFFFF",
                                    justify="left")
        self.results_label.pack(expand=True)
        # Кнопка "Главное меню"
        main_menu_btn = tk.Button(main_frame, text="Главное меню", width=25, height=2,
                                font=("Arial", 14), bg="#21743F", fg="white", 
                                command=lambda: controller.show_frame(StartPage))
        main_menu_btn.pack(pady=20)
        # Загружаем результаты
        self.update_results()
    
    def update_results(self):
        """Обновление отображения всех результатов без прокрутки"""
        try:
            with open("results.txt", "r", encoding="utf-8") as file:
                results = file.read().strip()
                if results:
                    self.no_results_shown = False  # Сбрасываем флаг при наличии результатов
                    # Очищаем фрейм
                    for widget in self.results_frame.winfo_children():
                        widget.destroy()
                    # Создаем фрейм с вертикальным расположением
                    content_frame = tk.Frame(self.results_frame, bg="#FFFFFF")
                    content_frame.pack(fill="both", expand=True)
                    # Разбиваем на строки
                    lines = [line.strip() for line in results.split("\n") if line.strip()]
                    # Группируем по модулям
                    modules = {
                        "1 модуль": [],
                        "2 модуль": [],
                        "3 модуль": []}
                    for line in lines:
                        if line.startswith(("1 тест", "2 тест", "3 тест")):
                            modules["1 модуль"].append(line)
                        elif line.startswith("4 тест"):
                            modules["2 модуль"].append(line)
                        elif line.startswith(("5 тест", "6 тест", "7 тест", "8 тест")):
                            modules["3 модуль"].append(line)
                    # Отображаем все результаты
                    row = 0
                    for module_name, tests in modules.items():
                        if tests:
                            # Заголовок модуля
                            module_label = tk.Label(content_frame, 
                                                  text=module_name,
                                                  font=("Arial", 19, "bold"),
                                                  bg="#FFFFFF")
                            module_label.grid(row=row, column=0, sticky="w", pady=(0, 2), padx=20)
                            row += 1
                            for test in tests:
                                parts = test.split(":")
                                if len(parts) >= 2:
                                    test_name = parts[0].strip()
                                    test_result = parts[1].strip()
                                    numbers = [int(s) for s in test_result.split() if s.isdigit()]
                                    if len(numbers) >= 2:
                                        correct = numbers[0]
                                        text_color = "#FF0000" if correct <= 5 else "#000000"
                                        result_text = f"{test_name}: {test_result}"
                                        
                                        result_label = tk.Label(content_frame,
                                                              text=result_text,
                                                              font=("Arial", 17),
                                                              fg=text_color,
                                                              bg="#FFFFFF",
                                                              anchor="w")
                                        result_label.grid(row=row, column=0, sticky="w", padx=40, pady=0)
                                        row += 1
                    # Настраиваем пропорциональное распределение строк
                    content_frame.grid_rowconfigure(row, weight=1)
                elif not self.no_results_shown:  # Показываем сообщение только если его еще не показывали
                    for widget in self.results_frame.winfo_children():
                        widget.destroy()
                    no_results_label = tk.Label(self.results_frame, 
                                              text="Результатов пока нет",
                                              font=("Arial", 18),
                                              bg="#FFFFFF")
                    no_results_label.pack(expand=True)
                    self.no_results_shown = True
        except FileNotFoundError:
            if not self.no_results_shown:  # Показываем сообщение только если его еще не показывали
                for widget in self.results_frame.winfo_children():
                    widget.destroy()
                no_results_label = tk.Label(self.results_frame, 
                                          text="Результатов пока нет",
                                          font=("Arial", 18),
                                          bg="#FFFFFF")
                no_results_label.pack(expand=True)
                self.no_results_shown = True

class TkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(bg="#FFFFFF")
        self.title("CogniUp")
        # Запрещаем изменение размера окна
        self.resizable(False, False)
        # Получаем размеры экрана
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        # Устанавливаем окно на весь экран
        self.geometry(f"{screen_width}x{screen_height}+0+0")
        self.attributes('-fullscreen', True)  # Включаем полноэкранный режим
        # Привязываем Escape для проверки полноэкранного режима
        self.bind('<Escape>', self.handle_escape)
        container = tk.Frame(self, bg="#FFFFFF")
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (LoadingScreen, StartPage, Manual1, Test1, Manual2, 
                 Test2, Manual3, Test3, Manual4, Test4, 
                 Manual5, Test5, Manual6, Test6, Manual7, Test7, Manual8, 
                 Test8, ResultsPage, EndPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        # Показываем сначала загрузочный экран
        self.show_frame(LoadingScreen)

    def handle_escape(self, event=None):
        current_state = self.attributes('-fullscreen')
        if current_state:
            self.attributes('-fullscreen', False)  # Выход из полноэкранного режима
        else:
            self.attributes('-fullscreen', True)   # Возврат в полноэкранный режим

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        # Сброс всех тестов при переходе на главную страницу
        if cont == StartPage:
            self.reset_test()
        # Активация тестовых страниц при переходе на них
        if cont in (Test1, Test2, Test3, Test4, Test5, Test6, Test7, Test8):
            # Деактивируем предыдущий тест
            if hasattr(self, 'current_frame') and self.current_frame in (Test1, Test2, Test3, Test4, Test5, Test6, Test7, Test8):
                prev_frame = self.frames[self.current_frame]
                prev_frame.active = False
                if hasattr(prev_frame, 'timer_id') and prev_frame.timer_id:
                    prev_frame.after_cancel(prev_frame.timer_id)
                    prev_frame.timer_id = None
                prev_frame.timer_canvas.delete("all")
            # Активируем новый тест
            frame.active = True
            frame.reset_test()
            frame.start_round()
        self.current_frame = cont
        if cont == ResultsPage:
            frame.update_results()

    def reset_test(self):
        """Метод для сброса всех состояний теста"""
        for page in [Test1, Test2, Test3, Test4, Test5, Test6, Test7, Test8]:
            if page in self.frames:
                self.frames[page].reset()

if __name__ == "__main__":
    app = TkinterApp()
    app.mainloop()