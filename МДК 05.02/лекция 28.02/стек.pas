
type
  PStack = ^TStack;
  TStack = record
    data: array[1..10] of integer;
    Top: Integer;
  end;

procedure Push(stack: PStack; value: integer);
begin
  if stack^.Top >= 10 then
    WriteLn('Стек переполнен!')
  else begin
    stack^.Top := stack^.Top + 1;
    stack^.Data[stack^.Top] := value;
  end;
end;

function Pop(stack: PStack): integer;
begin
  if stack^.Top <= 0 then
  begin
    WriteLn('Стек пуст!');
    Pop := 0; // Возврат 0 при пустом стеке
  end
  else begin
    Pop := stack^.Data[stack^.Top];
    stack^.Top := stack^.Top - 1;
  end;
end;

procedure RemoveNegatives(stack: PStack);
var
  tempStack: PStack;
  item: integer;
begin
  New(tempStack);
  tempStack^.Top := 0;
  
  while stack^.Top > 0 do
  begin
    item := Pop(stack);
    if item >= 0 then
      Push(tempStack, item);
  end;

  while tempStack^.Top > 0 do
  begin
    item := Pop(tempStack);
    Push(stack, item);
  end;

  Dispose(tempStack);
end;

var
  stack: PStack;
  i: Integer;
  inputValue: Integer;

begin
  New(stack);
  stack^.Top := 0;
  
  WriteLn('Введите 10 целых чисел для заполнения стека:');
  for i := 1 to 10 do
  begin
   Readln(inputValue);
    Push(stack, inputValue);
  end;

  WriteLn('Начальный стек:');
  for i := stack^.Top downto 1 do
    Write(stack^.Data[i], ' ');
  WriteLn;
  
  RemoveNegatives(stack);
  
  WriteLn('Обработанный стек:');
  for i := stack^.Top downto 1 do
    Write(stack^.Data[i], ' ');
  WriteLn;

  Dispose(stack);
end.
