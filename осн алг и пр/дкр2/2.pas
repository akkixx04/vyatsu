// Написать программу, удаляющую из строки первое и последнее вхождение заданной подстроки.
var
  s, pod_s, res_s: string;
  i, j, first, last, len_s, len_pod_s: integer;
  presence: boolean;

begin
  write('Введите строку: ');
  readln(s);
  write('Введите подстроку для удаления: ');
  readln(pod_s);

  first := -1;
  last := -1;
  
  len_s := length(s);
  len_pod_s := length(pod_s);

  // Находим первое вхождение подстроки
  for i := 1 to len_s - len_pod_s + 1 do
  begin
    presence := true;
    for j := 0 to len_pod_s - 1 do
      if s[i + j] <> pod_s[j + 1] then
      begin
        presence := false;
        break;
      end;
    if presence then
    begin
      first := i;
      break;
    end;
  end;

  // Находим последнее вхождение подстроки
  for i := len_s - len_pod_s + 1 downto 1 do
  begin
    presence := true;
    for j := 0 to len_pod_s - 1 do
      if s[i + j] <> pod_s[j + 1] then
      begin
        presence := false;
        break;
      end;
    if presence then
    begin
      last := i;
      break;
    end;
  end;

    // Формируем результат, удаляя первое и последнее вхождение
  res_s := '';
  
  // Проходим по исходной строке
  for i := 1 to len_s do
  begin
    // Если это первое вхождение подстроки, пропускаем его
    if (first > 0) and (i >= first) and (i < first + len_pod_s) then
      continue;

    // Если это последнее вхождение подстроки, пропускаем его
    if (last > 0) and (i >= last) and (i < last + len_pod_s) then
      continue;

    // Добавляем символ в результирующую строку
    res_s := res_s + s[i];
  end;

  writeln('Результат: ', res_s);
end.