var
  B, A, X: integer;

begin
  writeln('Введите количество проданных газет: ');
  readln(B);
  writeln('Введите цену продажи каждой из первых 75 газет: ');
  readln(A);
  writeln('Введите цену продажи на каждую из остальных проданных газет: ');
  readln(X);

  if B <= 75 then
    writeln('Заработок равен: ', B * A)
  else
    writeln('Заработок равен: ', 75 * A + (B - 75) * X);
end.
