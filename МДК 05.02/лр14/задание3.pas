// Написать рекурсивную функцию определения степени числа.
var x,y: integer;
function stepen (a,b: integer):integer; //Параметризация
begin
// База рекурсии
  if b = 0 then
    stepen := 1
  else
// Декомпозиция
    stepen := a * stepen(a, b - 1);
end;
begin
  writeln('Введите число: ');
  readln(x);
  writeln('Введите степень числа: ');
  readln(y);
  writeln(stepen(x,y));
end.