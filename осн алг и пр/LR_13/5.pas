//Дан файл вещественных чисел. Найти его последний локальный максимум 
//(локальным максимумом называется элемент, который больше своих соседей).
var
  input: file of real;
  numbers: array of Real;
  last_loc_max, num: Real;
  last_loc_max_index: Integer;
  n, i, count: Integer;

begin
  assign(input, 'C:\2курс\осн алг и пр\LR_13\input5.txt');
  reset(input);
  
  setlength(numbers, 1);
  
  n := 0;
  randomize;
  count := 10;
  
  writeln('Все заданные числа');
  
  for n := 1 to count do
  begin
    num := random * 100; // Генерация случайного вещественного числа от 0 до 100
    write(input, num);
    writeln(num);
    numbers[High(numbers)] := num;
    setlength(numbers, n + 1);
  end; 
  
  close(input);
  
  setlength(numbers, count);
  
  
  
  last_loc_max := -MaxInt; 
  last_loc_max_index := -1; 

  for i := 1 to n - 2 do
  begin
    if (numbers[i] > numbers[i - 1]) and (numbers[i] > numbers[i + 1]) then
    begin
      last_loc_max := numbers[i];
      last_loc_max_index := i;
    end;
  end;

  if last_loc_max_index <> -1 then
    writeln('Последний локальный максимум: ', last_loc_max)
  else
    writeln('Локальные максимумы не найдены.');

end.
