//Создать список из десяти элементов и вывести его на экран. Затем вывести только четные элементы списка.
type
  PNode = ^TNode;
  tnode = record
    data: integer;
    next: PNode;
  end;

var
  head: PNode;
  curr: PNode;
  temp: PNode;
  i: integer;
  value: integer;

procedure addtoend(value: integer);
var
  newnode: PNode;
begin
  New(Newnode);
  Newnode^.data := value;
  Newnode^.next := nil;
  
  if head = nil then
    head := Newnode
  else
  begin
    curr := head;
    while curr^.next <> nil do
      curr := curr^.next;
    curr^.next := Newnode;
  end;
end;

procedure printlist;
begin
  curr := head;
  while curr <> nil do
  begin
    write(curr^.data, ' ');
    curr := curr^.next;
  end;
  writeln;
end;

procedure printevenelements;
begin
  curr := head;
  while curr <> nil do
  begin
    if curr^.data mod 2 = 0 then
      write(curr^.data, ' ');
    curr := curr^.next;
  end;
  writeln;
end;

begin
  head := nil;

  writeln('введите десять элементов списка:');
  for i := 1 to 10 do
  begin
    readln(value);
    addtoend(value);
  end;

  writeln('все элементы списка:');
  printlist;

  writeln('четные элементы списка:');
  printevenelements;
end.