//Дан символьный файл, содержащий, по крайней мере, один символ пробела. Удалить все его элементы, 
//расположенные после последнего символа пробела, включая и этот пробел.
var
  input: file of char;
  output: text;
  content: string;
  last_space: integer;
  ch: char;

begin
  assign(input, 'C:\2курс\осн алг и пр\LR_13\string1.txt');
  reset(input);
  
  content := '';
  while not eof(input) do
  begin
    read(input, ch);
    content := content + ch;
  end;
  close(input);

  last_space := length(content);
  while (last_space > 0) and (content[last_space] <> ' ') do
    dec(last_space);

  if last_space > 0 then
    setlength(content, last_space);

  assign(output, 'C:\2курс\осн алг и пр\LR_13\output1.txt');
  rewrite(output);
  writeLn(output, content);
  close(output);
  writeln('Результат записан в файл output1.txt');
end.
