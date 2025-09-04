//В файле записан список чисел. Необходимо переписать его в другой файл в обратном порядке.
const
  MAXSIZE = 50;

type
  Stack = record
    tags: array[1..MAXSIZE] of integer;
    size: integer; 
  end;

var
  input, output: text;
  num: integer;
  S: Stack;

function isEmptyStack(S: Stack): boolean;
begin
  Result := (S.size = 0);
end;

procedure Push(var S: Stack; x: integer);
begin
  if S.size = MAXSIZE then Exit; // выход, если произошло переполнение стека
  S.size := S.size + 1;
  S.tags[S.size] := x; // добавляем элемент
end;

function Pop(var S: Stack): integer;
begin
  if S.size = 0 then 
  begin
    Result := -1; // возвращаем -1, если стек пуст, можно изменить на другое значение
    Exit;
  end;
  Result := S.tags[S.size];
  S.size := S.size - 1;
end;

begin
  S.size := 0;

  assign(input, 'spisok.txt');
  reset(input);
  
  while not eof(input) do
  begin
    readln(input, num);
    Push(S, num);
  end;
  
  close(input);

  assign(output, 'naoborot.txt');
  rewrite(output);
  
  while not isEmptyStack(S) do
  begin
    writeln(output, Pop(S));
  end;

  close(output);
  
  writeln('Числа записаны в файл naoborot.txt в обратном порядке.');
end.
