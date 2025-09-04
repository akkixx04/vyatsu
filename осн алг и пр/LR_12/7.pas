//Найти сумму всех чисел от 1 до n, имеющих ровно 5 делителей.
//Единица и само число входят в число его делителей.
//Входные данные: в единственной строке входного файла z3.in записано одно натуральное число n(1 <= n <= 1012).
//Выходные данные: в единственную строку выходного файла z3.out нужно вывести одно натуральное число — найденную сумму.
var 
  filetext, output: textfile;
  c, n, s, k, i: integer;
begin
  assignfile(filetext, 'C:\2курс\осн алг и пр\LR_12\z3.in.txt');
  reset(filetext);
  assignfile(output, 'C:\2курс\осн алг и пр\LR_12\z3.out.txt');
  rewrite(output);
  c := 0;
  s := 0;
  readln(filetext, n);
  for i := 2 to n do
  begin
    c := 0; 
    for k := 1 to i do 
    begin 
      if i mod k = 0 then
        c := c + 1;
    end;
    if c = 5 then 
      s := s + i;
  end;
  writeln(output, s);
  closefile(filetext);
  closefile(output);
  writeln('Результат записан в файл z3.out')
end.