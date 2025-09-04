// Дан текстовый файл. Удалить из него все пустые строки.
var
  filetext, output_file: text;
  line: string;

begin
  assign(filetext, 'C:\2курс\осн алг и пр\LR_12\text6.txt');
  assign(output_file, 'C:\2курс\осн алг и пр\LR_12\output6.txt');

  reset(filetext);
  rewrite(output_file);

  while not eof(filetext) do
  begin
    readln(filetext, line);

    // Проверяем, не пустая ли строка
    if Trim(line) <> '' then
      writeln(output_file, line);
  end;

  close(filetext);
  close(output_file);

  writeln('Пустые строки удалены, результат записан в output6.txt');
end.
