// вывести список слов с убыванием частоты
type
  PNode = ^Node;
  Node = record
    word: string[40];
    count: integer;
    next: PNode;
    prev: PNode;
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
  NewNode^.prev := nil;
  Result := NewNode;
end;

procedure AddFirst(var Head: PNode; NewNode: PNode);
begin
  if Head <> nil then
    Head^.prev := NewNode;
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

procedure Print(head: PNode);
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
  writeln('Количество различных слов: ', uniqueCount);
end;

procedure Sort(var arr: array of PNode);
var
  i, j: integer;
  temp: PNode;
begin
  for i := 0 to High(arr) - 1 do
    for j := 0 to High(arr) - i - 1 do
      if arr[j]^.count < arr[j + 1]^.count then
      begin
        temp := arr[j];
        arr[j] := arr[j + 1];
        arr[j + 1] := temp;
      end;
end;

procedure WriteToF(filename: string; nodesArray: array of PNode);
var
  outputFile: text;
  i: integer;
begin
  assign(outputFile, filename);
  rewrite(outputFile);
  for i := 0 to High(nodesArray) do
    writeln(outputFile, nodesArray[i]^.word, ' - ', nodesArray[i]^.count);
  close(outputFile);
end;

var
  word: string;
  current: PNode;
  found: boolean;
  a: array of PNode;
  i, count_nodes: integer;
begin
  assign(f, 'data.txt');
  reset(f);
  head := nil;

  // Чтение и обработка слов
  repeat
    word := TakeWord(f);
    if word <> '' then
    begin
      current := head;
      found := false;
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
      if not found then
        AddFirst(head, CreateNode(word));
    end;
  until eof(f);
  close(f);

  // Вывод количества уникальных слов
  Print(head);

  // Создание массива узлов
  current := head;
  count_nodes := 0;
  while current <> nil do
  begin
    count_nodes += 1;
    current := current^.next;
  end;

  setlength(a, count_nodes);
  current := head;
  i := 0;
  while (current <> nil) and (i < count_nodes) do
  begin
    a[i] := current;
    current := current^.next;
    i += 1;
  end;

  // Сортировка массива
  Sort(a);

  // Запись результатов в файл
  WriteToF('output.txt', a);
  writeln('Результаты записаны в файл output.txt');
end.