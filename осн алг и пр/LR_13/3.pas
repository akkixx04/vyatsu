//Дан файл вещественных чисел. Создать два новых файла, первый из которых содержит элементы исходного файла 
//с нечетными номерами (1,3,…), а второй — с четными (2,4,…).
var
  input, chet, nechet: file of real;
  num, num1, num2 : real;
  i, count: integer;

begin
  assign(input, 'C:\2курс\осн алг и пр\LR_13\input3.txt');
  rewrite(input);
  
  count := 10;
  
  writeln('Все заданные числа');
  
  for i := 1 to count do
  begin
    num := random * 100; // Генерация случайного вещественного числа от 0 до 100
    write(input, num);
    writeln(num);
  end;
  close(input);

  assign(input, 'C:\2курс\осн алг и пр\LR_13\input3.txt');
  reset(input);

  assign(nechet, 'C:\2курс\осн алг и пр\LR_13\nechet.txt');
  rewrite(nechet);
  assign(chet, 'C:\2курс\осн алг и пр\LR_13\chet.txt');
  rewrite(chet);

  i := 0;

  while not eof(input) do
  begin
    read(input, num);
    i += 1;
    
    
    if odd(i) then
      write(nechet, num)
    else
      write(chet, num)
  end;
  
  close(input);
  close(nechet);
  close(chet);
  
  writeln('На нечетных позициях:');
  
  assign(nechet, 'C:\2курс\осн алг и пр\LR_13\nechet.txt');
  reset(nechet);
  
  while not eof(nechet) do
  begin
    read(nechet, num1);
    writeln(num1);
  end;

  close(nechet);

  writeln('На четных позициях:');

  assign(chet, 'C:\2курс\осн алг и пр\LR_13\chet.txt');
  reset(chet);
  
  while not eof(chet) do
  begin
    read(chet, num2);
    writeln(num2);
  end;

  close(chet);  
  
  writeln('Готово.Числа на нечетных позициях записаны в файл nechet.txt, а на четных - в chet.txt');
end.
