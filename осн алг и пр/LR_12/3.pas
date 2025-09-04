// Дана строка S и текстовый файл. Добавить строку S в конец файла.
var
  filetext: text;
  s: string;

begin
  writeln('Введите строку для добавления в файл: ');
  readln(s);

  assign(filetext, 'C:\2курс\осн алг и пр\LR_12\text3.txt');
  append(filetext);

  writeln(filetext, s);

  close(filetext);
  
  writeln('Строка добавлена в конец файла.');
end.
