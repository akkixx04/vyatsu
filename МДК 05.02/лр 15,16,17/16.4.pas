//Дан односвязный (линейный) список. Найти максимальный и минимальный элементы в списке.

type
  PNode = ^TNode;
  TNode = record
    data: integer;
    next: PNode;
  end;
  
var
  head: PNode;

function CreateNode(var head: PNode; value: integer): PNode;
var NewNode: PNode;
begin
  New(NewNode);
  NewNode^.data := value;
  NewNode^.next := head;
  head := NewNode;
end;

procedure FindMinMax(head: PNode; var min, max: Integer);
var
  current: PNode;
begin
  if head = nil then
  begin
    writeln('Список пуст.');
    exit;
  end;

  min := head^.data;
  max := head^.data;
  current := head^.next;

  while current <> nil do
  begin
    if current^.data < min then
      min := current^.data;
    if current^.data > max then
      max := current^.data;
    current := current^.next;
  end;
end;

var
  value, i, min, max: integer;

begin
  head := nil;

  writeln('Введите 5 целых чисел для списка:');
  for i := 1 to 5 do
  begin
    readln(value);
    CreateNode(head, value);
  end;

  FindMinMax(head, min, max);

  writeln('Минимальный элемент в списке: ', min);
  writeln('Максимальный элемент в списке: ', max);

end.
