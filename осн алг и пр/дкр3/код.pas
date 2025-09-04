function func(x: real): real;
begin
  result := 2 * power(x, 3) + (-1) * power(x, 2) + (-2) * x + (3);
end;

function traps(a, b: real; n: integer): real;
var
  h, sum: real;
  i: integer;
begin
  h := (b - a) / n;
  sum := (func(a) + func(b)) / 2;

  for i := 1 to n - 1 do
    sum := sum + func(a + i * h);

  result := sum * h;
end;

function pervoobraz(x:real):real;
begin
  result := (power(x,4) / 2 ) - (power(x,3) / 3) - power(x,2) + 3*x;
end;

function integral(a, b: real): real;
begin
  result := pervoobraz(b) - pervoobraz(a);
end;

function pogresh(a, b: real; n: integer): real;
begin
  result := abs(traps(a,b,n) - integral(a,b));
end;

procedure menu;
begin
  writeln('Выберите действие:');
  writeln('1 - Вычислить площадь под кривой');
  writeln('2 - Оценка погрешности');
  writeln('0 - Выход');
end;

var
  a, b, S, P, I: real;
  choice, n: integer;

begin
  repeat
    menu;
    readln(choice);
    
    case choice of
      1: begin
           write('Введите нижний предел интегрирования (a): ');
           readln(a);
           write('Введите  верхний предел интегрирования (b): ');
           readln(b);
           write('Введите количество трапеций для интегрирования (n): ');
           readln(n);
           // Проверка на положительность
           if (a < 0) or (b < 0) then
           begin
             writeln('Пределы интегрирования должны быть положительными.');
             continue;
           end;

           S := traps(a, b, n);
           
           writeln('Площадь фигуры: ', S:0:4);
         end;
      2: begin
           write('Введите нижний предел интегрирования (a): ');
           readln(a);
           write('Введите  верхний предел интегрирования (b): ');
           readln(b);
           write('Введите количество трапеций для интегрирования (n): ');
           readln(n);
           // Проверка на положительность
           if (a < 0) or (b < 0) then
           begin
             writeln('Пределы интегрирования должны быть положительными.');
             continue;
           end;

           S := traps(a, b, n);
           I := integral(a, b);
           P := pogresh(a, b, n);
           
           writeln('Приближенное значение интеграла(вычисление по методу трапеции): ', S:0:4);
           writeln('Точное значение интеграла: ', I:0:4);
           writeln('Погрешность: ', P:0:4);
         end;
      0: writeln('Выход из программы...');
    else
      writeln('Некорректный выбор. Попробуйте еще раз.');
    end;

    writeln;
  until choice = 0;
end.
