// Дан строковый файл. Создать новый строковый файл, содержащий все строки исходного файла наибольшей длины (в обратном порядке).
var
  input, output: file of char;
  line: array of char;
  longest: array of array of char;
  max_len, count, i, j: integer;
  ch: char;

begin
  assign(input, 'C:\2курс\осн алг и пр\LR_13\string2.txt');
  reset(input);

  max_len := 0;
  count := 0;

  while not eof(input) do
  begin
    setlength(line, 0);

    while not eof(input) do
    begin
      read(input, ch);
      if ch = #10 then // Символ новой строки
        break;

      setlength(line, length(line) + 1);
      line[High(line)] := ch;
    end;

    if length(line) > max_len then
    begin
      max_len := length(line);
      count := 1;
      setlength(longest, count);
      longest[0] := line;
    end
    else if length(line) = max_len then
    begin
      setlength(longest, count + 1);
      longest[count] := line;
      count += 1;
    end;
  end;

  close(input);

  // Запись результатов в выходной файл
  assign(output, 'C:\2курс\осн алг и пр\LR_13\output2.txt');
  rewrite(output);

  for i := count - 1 downto 0 do
  begin
    for j := 0 to High(longest[i]) do
      write(output, longest[i][j]);  // Запись символов строки

    write(output, #10);  // Записываем символ новой строки
  end;

  close(output);

  writeln('Строки максимальной длины записаны в файл output2.txt в обратном порядке.');
end.