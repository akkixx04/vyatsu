//Сформировать массив из 20 чисел. Удалить первый положительный элемент. Удалить наименьший элемент массива.
var
  A: array[1..20] of integer;
  i, j, N: integer;
  first_positive_index, min_index: integer;
  min_num: integer;

begin
N := 20;

  randomize;

  for i := 1 to N do
  begin
    A[i] := random(-100,100);
  end;
  writeln('Изначальный массив:');
  write(A);
  writeln();

  first_positive_index := -1;
  for j := 1 to N do
  begin
    if A[j] > 0 then
    begin
      first_positive_index := j;
      break;
    end;
  end;

  if first_positive_index <> -1 then
  begin
    for j := first_positive_index to N - 1 do
    begin
      A[j] := A[j + 1];
    end;
    N := N - 1;
  end;

  writeln('Массив после удаления первого положительного элемента:');
  write(A);
  writeln();

  if N > 0 then
  begin
    min_index := 1;
    min_num := A[1];
    
    for i := 2 to N do
    begin
      if A[i] < min_num then
      begin
        min_num := A[i];
        min_index := i;
      end;
    end;

    for i := min_index to N - 1 do
    begin
      A[i] := A[i + 1];
    end;
    N := N - 1;

    writeln('Массив после удаления наименьшего элемента:');
    write(A);
    writeln();
  end
end.