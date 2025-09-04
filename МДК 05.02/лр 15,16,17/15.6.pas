//Запросить у пользователя ввести строку. Проверить ее на наличие недопустимых символов. 
//В качестве первого символа можно использовать только буквы и знак подчеркивания. 
//Остальные символы могут быть буквами, цифрами и знаком подчеркивания
type
  t_chs = set of char;

const
  lett: t_chs = ['a'..'z', 'A'..'Z', '_'];
  num: t_chs = ['0'..'9'];

var
  str: string;
  i: byte;
  flag: boolean;

begin
  flag := true; // Изначально предполагаем, что строка корректна
  writeln('Введите строку:');
  readln(str);
  
  // Проверяем первый символ
  if not (str[1] in lett) then
    flag := false;
  
  // Проверяем остальные символы
  for i := 2 to Length(str) do
  begin
    if not (str[i] in lett + num) then
    begin
      flag := false;
      break; // Прерываем цикл, если найден недопустимый символ
    end;
  end;
  
  // Вывод результата
  if flag then
    writeln('Строка корректна: true')
  else
    writeln('Строка некорректна: false');
end.