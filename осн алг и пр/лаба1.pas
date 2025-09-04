program z1;

var
  a, b, c: integer;
  x1, x2, d: real;

begin
  writeln('Введите переменные a,b и с');
  readln(a, b, c);
  d := sqr(b) - 4 * a * c;
  if d = 0 then
  begin
    x1 := -b / (2 * a);
    writeln('1 корень: ', x1);
  end;
  if d > 0 then
  begin
    x1 := (-b + sqrt(d)) / (2 * a);
    x2 := (-b - sqrt(d)) / (2 * a);
    writeln('2 корня');
    writeln('первый: ', x1);
    writeln('второй: ', x2);
  end;
  if d < 0 then
  begin
    writeln('Нет корней');
  end;
end.