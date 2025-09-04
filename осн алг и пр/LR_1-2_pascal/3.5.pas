var
  year: integer;

begin
  writeln('Введите год: ');
  readln(year);

  if (year > 400) and (year mod 100 = 0) and (year mod 400 <> 0) then
    writeln('Год не високосный')
  else if (year mod 4 = 0) then
    writeln('Год високосный')
  else
    writeln('Год не високосный');
end.

