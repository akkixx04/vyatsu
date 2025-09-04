unit LeviCurve_m;

uses
  GraphABC;

type
  point = record
    x, y: integer;
  end;

//Процедура для вычисления координат новой точки при повороте на 45 градусов
function RotatePoint(x1, y1, x2, y2: integer): point;
var
  delta_x, delta_y: integer;
begin
  delta_x := x2 - x1;
  delta_y := y2 - y1;
  result.x := x1 + (delta_x - delta_y) div 2;
  result.y := y1 + (delta_y + delta_x) div 2;
end;

//Рекурсивная процедура для отрисовки кривой Леви
procedure LeviCurve(start_x, start_y, end_x, end_y: integer; depth: integer);//Параметризация
var
  mid_p: point;
begin
  if depth = 0 then //База рекурсии 
  begin
    Line(start_x, start_y, end_x, end_y);  //Базовый случай - рисуем прямую линию
  end
  else
  begin
    mid_p := RotatePoint(start_x, start_y, end_x, end_y); //Вычисление средней точки
    //Декомпозиция
    LeviCurve(start_x, start_y, mid_p.x, mid_p.y, depth - 1); //Рекурсивный вызов для первой половины
    LeviCurve(mid_p.x, mid_p.y, end_x, end_y, depth - 1); //Рекурсивный вызов для второй половины
  end;
end;

end.