//Дан файл вещественных чисел. Поменять в нем местами минимальный и максимальный элементы.
var
  input, temp: file of real;
  numbers: array of Real;
  min_n, max_n, num: Real;
  min_index, max_index: Integer;
  i, n, count: Integer;
  
begin
  assign(input, 'C:\2курс\осн алг и пр\LR_13\input6.txt');
  rewrite(input);
  
  setlength(numbers, 1000);

  n := 0;
  count := 10;

  writeln('Все заданные числа:');

  for n := 1 to count do
  begin
    num := random * 100;  // Генерация случайного вещественного числа от 0 до 100
    write(input, num);
    writeln(num);
    numbers[n - 1] := num;
  end;
  
  close(input);
  setlength(numbers, n);  // Уменьшаем массив до нужного размера

  min_n := numbers[0];
  max_n := numbers[0];
  min_index := 0;
  max_index := 0;

  for i := 1 to n - 1 do
  begin
    if numbers[i] < min_n then
    begin
      min_n := numbers[i];
      min_index := i;
    end;
    if numbers[i] > max_n then
    begin
      max_n := numbers[i];
      max_index := i;
    end;
  end;

  // Записываем результат в временный файл
  assign(temp, 'C:\2курс\осн алг и пр\LR_13\vrem6.txt');
  rewrite(temp);

  for i := 0 to n - 1 do
  begin
    if i = min_index then
      write(temp, max_n)
    else if i = max_index then
      write(temp, min_n)
    else
      write(temp, numbers[i]);
  end;

  close(temp);
  
  // Перемещаем временный файл на место исходного
  erase(input);
  rename(temp, 'input6.txt');
  
  assign(input, 'C:\2курс\осн алг и пр\LR_13\input6.txt');
  reset(input);

  writeln('Минимальный и максимальный элементы заменены местами. Результат в файле input6.txt');
  
  writeln('Данные из файла input6.txt:');
  
  while not eof(input) do
  begin
    read(input, num);
    writeln(num);  // Выводим число на экран
  end;

  close(input);
end.
