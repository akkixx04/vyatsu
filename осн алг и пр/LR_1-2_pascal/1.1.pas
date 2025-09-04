var
  r: integer;
  S: real;

begin
  writeln('Введите радиус круга: ');
  readln(r);
  
  S := pi * sqr(r);
  
  writeln('Площадь круга равна: ', S);
end.