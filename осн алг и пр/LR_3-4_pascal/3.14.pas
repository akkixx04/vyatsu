var
  orel, reshka: integer;
  flip: char;

begin
  orel := 0;
  reshka := 0;
  repeat
    writeln('Н - орел, Т - решка. Для завершения напишите "К":');
    readln(flip);
    
    if flip = 'Н' then
      orel += 1
    else if flip = 'Т' then
      reshka += 1;
    
  until flip = 'К';
  writeln('Итого');
  writeln('Количество орлов: ', orel);
  writeln('Количество решек: ', reshka);
end.