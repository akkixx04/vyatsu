//В файле input.txt записаны числа (каждое — с новой строки), их количество не превышает 100. 
//Необходимо найти максимальное и минимальное число и записать их в файл output.txt.
var
  filetext, output_file: text;
  num, max_num, min_num: integer;
  first_read: boolean;

begin
  assign(filetext, 'C:\2курс\осн алг и пр\LR_12\text5.txt');
  reset(filetext);

  assign(output_file, 'C:\2курс\осн алг и пр\LR_12\output5.txt');
  rewrite(output_file);

  first_read := true;

  while not eof(filetext) do
  begin
    readln(filetext, num);

    if first_read then
    begin
      max_num := num;
      min_num := num;
      first_read := false;
    end
    else
    begin
      if num > max_num then
        max_num := num;

      if num < min_num then
        min_num := num;
    end;
  end;

  if not first_read then // Если файл не пустой
  begin
    writeln(output_file, 'Максимальное число: ', max_num);
    writeln(output_file, 'Минимальное число: ', min_num);
  end
  else
  begin
    writeln(output_file, 'Файл text5.txt пуст.');
  end;
  
  close(filetext);
  close(output_file);
  
  writeln('Результаты записаны в output5.txt.');
end.
