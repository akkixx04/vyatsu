//Найти наибольший общий делитель методом Евклида (алгоритм Евклида).
var x,y: integer;
function NOD(a,b: integer): integer; // Параметризация
begin
  if b = 0 then // База рекурсии
    begin
    NOD:= a;
    exit;
    end
  else
    begin
    NOD:= NOD(b, a mod b); // Декомпозиция
    exit;
    end
end;
begin
  writeln('Первое число: ');
  readln(x);
  writeln('Второе число: ');
  readln(y);
  writeln(NOD(x,y));
end.
// 36 и 24