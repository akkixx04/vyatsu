// Даны целые положительные числа N и K. Создать текстовый файл и записать в него N строк, каждая из которых состоит из K символов «*» (звездочка).
var
  filetext: text;
  N, K, i: integer;
  stars: string;

begin
  writeln('Введите значение N (количество строк): ');
  readln(N);
  writeln('Введите значение K (количество символов * в каждой строке): ');
  readln(K);

  stars := '';
  for i := 1 to K do
    stars += '*';

  assign(filetext, 'C:\2курс\осн алг и пр\LR_12\text2.txt');
  rewrite(filetext);

  for i := 1 to N do
  begin
    writeln(filetext, stars);
  end;

  close(filetext);
  
  writeln('Файл успешно создан');
end.
