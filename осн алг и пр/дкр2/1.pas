// Написать программу, выполняющую поиск двух элементов заданного массива, таких, что их разность по модулю максимальна.
var
  A: array of integer;
  i, j, min_el, max_el, R, N: integer;

begin
  write('Введите количество элементов массива: ');
  readln(N);
  
  setlength(A, N);
  
  if N > 0 then
  begin
    writeln('Введите элементы массива:');
    for i := 0 to N - 1 do
    begin
      read(A[i]);
    end;
    
    min_el := A[0];  
    max_el := A[0];
    
    for j := 0 to N - 1 do
    begin
      if A[j] < min_el then
      begin
        min_el := A[j];
      end;
    end;
    
    for j := 0 to N - 1 do
    begin
      if A[j] > max_el then
      begin
        max_el := A[j];
      end;
    end;
    
    R := abs(max_el - min_el);
    
    writeln('Массив: ', A);
    writeln('Элементы: ', max_el, ' и ', min_el);
    writeln('Максимальная разность по модулю: ', R);
  end
  else
  begin
    writeln('Ошибка. Длина массива должна быть больше 0.');
  end;
end.