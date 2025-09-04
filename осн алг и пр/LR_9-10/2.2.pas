//Сформировать двумерный массив (8*6). Получить одномерный массив [1..8], элементы которого равны 1, если в соответствующей строке 
//исходного массива нет отрицательных чисел, и  -1  в противном случае. (необходимо использовать подпрограммы)
var
  m: array [,] of integer;
  i, j: integer;
procedure procedure_negative(arr: array [,] of integer);
var
  a, b: integer;
  s: array of integer;
  negative: boolean;
  
begin
  setlength(s, 8);
  for a := 0 to 7 do
  begin
    negative := False;
    for b := 0 to 5 do
    begin
      if arr[a, b] < 0 then
      begin
        negative:=True;
        break
      end
    end;
    if negative then s[a] := -1
    else s[a] := 1
  end;
  for a := 0 to 7 do write(s[a], '; ')
end;
begin
  setlength(m, 8, 6);
  for i := 0 to 7 do
  begin
    writeln('Введите ', i + 1, ' массив.');
   for j := 0 to 5 do readln(m[i, j])
  end;
  writeln('Новый массив:');
  procedure_negative(m)
end.