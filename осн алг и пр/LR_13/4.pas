// Дан файл вещественных чисел. Найти сумму его элементов с четными номерами.
var
  input: file of real;
  output: file of real;
  num, S: real;
  i, count: integer;

begin
  assign(input, 'C:\2курс\осн алг и пр\LR_13\input4.txt');
  rewrite(input);
  
  randomize;
  count := 10;
  S := 0;
  writeln('Все заданные числа');
  for i := 1 to count do
  begin
    num := random * 100; // Генерация случайного вещественного числа от 0 до 100
    write(input, num);
    writeln(num);
  end;
  close(input);
  
  assign(input, 'C:\2курс\осн алг и пр\LR_13\input4.txt');
  reset(input);

  assign(output, 'C:\2курс\осн алг и пр\LR_13\output4.txt');
  rewrite(output);

  i := 0;

  while not eof(input) do
  begin
    read(input, num);
    i += 1;

    if not odd(i) then
      S += num;
  end;
  
  write(output,S);
  
  close(input);
  close(output);
  
  writeln('Сумма элементов на четных позициях: ', S, ' Результат записан в файл output4.txt');

end.