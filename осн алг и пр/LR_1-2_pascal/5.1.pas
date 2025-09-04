var
  X, Y, K: integer;

begin
  writeln('Введите количество собранных банок с медом: ');
  readln(X);
  writeln('Введите сколько должно быть литров меда в банке, чтобы ее выбрали: ');
  readln(Y);
  writeln('Введите сколько литров меда нужно для пропитания: ');
  readln(K);

  if X * Y >= K then
    writeln('YES')
  else
    writeln('NO');
end.