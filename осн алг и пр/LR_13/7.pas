//В файле заменить символы с четной позицией на восклицательные знаки (‘!’). Использовать процедуру seek
var
  input: file of char;
  output: file of char;
  ch: char;
  i: integer;

begin
  assign(input, 'C:\2курс\осн алг и пр\LR_13\input7.txt');
  reset(input);
  
  assign(output, 'C:\2курс\осн алг и пр\LR_13\output7.txt');
  rewrite(output);

  i := 0;
  
  // Считываем файл и используем seek для управления позициями
  while not eof(input) do
  begin
    seek(input, i);
    read(input, ch);

    if (i mod 2 = 1) then
      ch := '!';

    write(output, ch);
    i += 1;
  end;

  close(input);
  close(output);

  writeln('Результат записан в файл output7.txt');
end.
