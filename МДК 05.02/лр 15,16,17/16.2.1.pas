// используя двухсвязные списки
type
  PNode = ^Node;
  Node = record
    word: string[40];
    count: integer;
    next: PNode;
    prev: PNode;  // новый указатель на предыдущий узел
  end;

var
  f: text;
  head: PNode;

function CreateNode(NewWord: string): PNode;
var
  NewNode: PNode;
begin
  New(NewNode);
  NewNode^.word := NewWord;
  NewNode^.count := 1;
  NewNode^.next := nil;
  NewNode^.prev := nil;  // инициализируем указатель на предыдущий узел
  Result := NewNode;
end;

procedure AddFirst(var Head: PNode; NewNode: PNode);
begin
  if Head <> nil then
    Head^.prev := NewNode; // связываем новый узел с первым узлом
  NewNode^.next := Head;
  Head := NewNode;
end;

function TakeWord(var F: Text): string;
var
  c: char;
begin
  Result := '';
  c := ' ';
  while not eof(F) and (c <= ' ') do 
    read(F, c);
    
  while not eof(F) and (c > ' ') do 
  begin
    Result := Result + c;
    read(F, c);
  end;
end;

procedure Print_r(head: PNode);
var
  current: PNode;
  uniqueCount: integer;
begin
  uniqueCount := 0;
  current := head;

  while current <> nil do
  begin
    uniqueCount += 1;
    current := current^.next;
  end;

  writeLn('Количество различных слов: ', uniqueCount);
end;

var
  word: string;
  current: PNode;
  found: boolean;
begin
  assign(f, 'data.txt');
  reset(f);
  
  head := nil;

  repeat
    word := TakeWord(f);
    if word <> '' then
    begin
      current := head;
      found := false;

      // Поиск слова в списке
      while (current <> nil) do
      begin
        if current^.word = word then
        begin
          current^.count += 1;
          found := True;
          break;
        end;
        current := current^.next;
      end;

      // Если слово не найдено, создаем новый узел
      if not found then
      begin
        AddFirst(head, CreateNode(word));
      end;
    end;
  until eof(f);
  
  close(f);
  Print_r(head);
end.
