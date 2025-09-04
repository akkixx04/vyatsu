// В цикле записать в файл числа от 1 до 10 (каждое — в своей строке), а затем их считать и отобразить на экране.
var
  filetext: text;
  a: string;
  i: integer;

begin
  assign(filetext, 'C:\2курс\осн алг и пр\LR_12\text.txt');
  rewrite(filetext);
  for i := 1 to 10 do
  begin
    writeln(filetext, i);
  end;
  close(filetext);
  reset(filetext);
  for i := 1 to 10 do 
  begin
    readln(filetext, a);
    writeln(a);
  end;
  close(filetext);
end.