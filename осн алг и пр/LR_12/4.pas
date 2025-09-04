//Дано целое число K и текстовый файл. В данном файле вставить пустую строку перед строкой с номером K. Если строки с таким номером нет, то оставить файл без изменений.
//Для решения задачи можно использовать дополнительный временный файл.
var
  filetext, vrem_file: text;
  line: string;
  K, current_line: integer;
  line_K: boolean;

begin
  writeln('Введите номер строки K: ');
  readln(K);

  assign(filetext, 'C:\2курс\осн алг и пр\LR_12\text4.txt');
  reset(filetext);

  assign(vrem_file, 'C:\2курс\осн алг и пр\LR_12\text4vr.txt');
  rewrite(vrem_file);

  current_line := 1;
  line_K := false;

  while not eof(filetext) do
  begin
    readln(filetext, line);

    if current_line = K then
    begin
      writeln(vrem_file);
      line_K := true;
    end;

    writeln(vrem_file, line);
    current_line += 1;
  end;

  close(filetext);
  close(vrem_file);

  if line_K then
  begin
    erase(filetext);
    rename(vrem_file, 'C:\2курс\осн алг и пр\LR_12\text4.txt');
    writeln('Пустая строка была добавлена перед строкой с номером ', K);
  end
  else
  begin
    erase(vrem_file);
    writeln('Строки с номером ', K, ' нет в файле. Файл остался без изменений.');
  end;
end.
