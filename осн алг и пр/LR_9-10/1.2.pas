//Написать процедуру, которая находит максимальный элемент массива и его номер. Исправить процедуру так, чтобы она находила минимальный по модулю элемент, 
//максимальный отрицательный элемент. (в задаче подписать глобальные/локальные переменные, формальные/фактические параметры, передачу параметров по ссылке/по значению)
var // глобальные переменные
  a:array of integer;
  N, j, max_el, max_n, min_el, max_negative:integer;
  negative: boolean;

procedure wwod;
var j: integer; //локальная переменная
begin
  write('Введите количество элементов массива: ');
  readln(N);
  
  setlength(a, N);
  
  if N > 0 then
  begin
    writeln('Введите элементы массива:');
    for j := 0 to N - 1 do
    begin
      read(a[j]);
    end;
  end;
end;
    
procedure poisk1(var m: array of integer; var n: integer); // формальные параметры // передача параметра по ссылке
var  i: integer; //локальная переменная
begin
  max_el := m[0];
  for i := 0 to n - 1 do
    begin
      if m[i] > max_el then
      begin
        max_el := m[i];
        max_n := i + 1;
      end;
    end;
end;

procedure poisk2(m: array of integer; n: integer); // формальные параметры // передача параметра по значению
  var i, j, n2: integer; m2:array of integer; //локальные переменные
  begin
  min_el := abs(m[0]);
    for i := 0 to n - 1 do
    begin
      if abs(m[i]) < min_el then
      begin
        min_el := m[i];
      end;
    end;

  negative := False;   
  max_negative := -289745713485;
  for i := 0 to n - 1 do
  begin
    if m[i] < 0 then
    begin
      negative := True;
      if m[i] > max_negative then
      begin
        max_negative := m[i];
      end;
    end;
  end;
end;

procedure wiwod;
begin
  writeln('Максимальный элемент: ', max_el);
  writeln('Его номер: ', max_n);
  writeln('Минимальный по модулю элемент: ', min_el);
  if negative then
    writeln('Максимальный отрицательный элемент: ', max_negative)
  else 
    writeln('В массиве нет отрицательных чисел');
end;
begin
  wwod;
  poisk1(a,N); // фактические параметры 
  poisk2(a,N); // фактические параметры 
  wiwod;
end.