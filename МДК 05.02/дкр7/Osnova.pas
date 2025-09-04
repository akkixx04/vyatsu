program Osnova;

uses
    LeviCurve_m, Crt, GraphABC;

const
  max_depth = 10; //Максимальная глубина рекурсии

type
  point = record // Определяем новый тип, который представляет точку на плоскости с координатами x, y
    x, y: integer;
  end;
var
  start_p, end_p: point;  //Начальная и конечная точки
  actual_depth: integer;  //Текущая глубина
  scale: real;  //Коэффициент масштабирования
  set_x, set_y: integer; // Смещения по осям X и Y
  need_redraw: boolean; // Необходимость перерисовки

//Обработчик нажатия клавиши
procedure OnKeyPress(Key: char);
begin
  case Key of
    #37: //Стрелка влево
    set_x := set_x - 100; //Перемещение влево
    #39: //Стрелка вправо
    set_x := set_x + 100; //Перемещение вправо
    #38: // Стрелка вверх
    set_y := set_y - 100; //Перемещение вверх
    #40: // Стрелка вниз
    set_y := set_y + 100; //Перемещение вниз
    '+':
    scale := scale * 1.1; //Масштабирование вверх
    '-':
    scale := scale / 1.1; //Масштабирование вниз
    '0'..'9': //Изменение глубины
    actual_depth := ord(Key) - ord('0'); //Преобразование символа цифры в число
  end;
  need_redraw := true; //Установить необходимость перерисовки
end;

//Основная программа
begin
  setwindowsize(800, 600);
  
  start_p.x := 250;
  start_p.y := 300;
  end_p.x := 550;
  end_p.y := 300;
  
  actual_depth := 10; //Начальная глубина
  scale := 1.0;
  set_x := 0;
  set_y := 0;
  need_redraw := true; //Изначально требуется перерисовка
  
  repeat
    if need_redraw then
    begin
      clearwindow(clwhite);
      
      // Отрисовка кривой Леви с учетом текущих параметров
      LeviCurve(round(start_p.x * scale) + set_x, round(start_p.y * scale) + set_y, 
      round(end_p.x * scale) + set_x, round(end_p.y * scale) + set_y, actual_depth);
      
      redraw;
      need_redraw := false;
    end;
    
    if KeyPressed then  //Обрабатывает нажатие клавиши 
      OnKeyPress(ReadKey);
      
    sleep(50);
    
    
  until false;
end.