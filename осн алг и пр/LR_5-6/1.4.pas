//4.	Заполнить массив А из 30 элементов случайными числами из диапазона
//[-99, 67]. Сформировать массив В, в который записать только четные элементы массива А.

var
  A, B: array[1..30] of integer;
  i, j: integer;

begin
  randomize;
  for i := 1 to 30 do
  begin
    A[i] := random(-99, 67);
  end;
  j := 1;
  for i := 1 to 30 do
  begin
    if A[i] mod 2 = 0 then
    begin
      B[j] := A[i];
      j := j + 1; 
    end;
  end;
  for i := 1 to 30 do
  begin
    write(A[i], ' ');
  end;
  writeln();
  for i := 1 to j - 1 do
  begin
    write(B[i], ' ');
  end;
end.