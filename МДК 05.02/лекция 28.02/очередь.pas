type
  PNode = ^Node;
  Node = record
    value: integer;
    next: PNode;
  end;

  Queue = record
    head, tail: PNode;
  end;

procedure InitQueue(var q: Queue);
begin
  q.head := nil;
  q.tail := nil;
end;

procedure Enqueue(var q: Queue; value: integer);
var
  newNode: PNode;
begin
  New(newNode);
  newNode^.value := value;
  newNode^.next := nil;

  if q.tail = nil then
  begin
    q.head := newNode; // Если очередь пуста, новый элемент становится головой
    q.tail := newNode; // И хвостом
  end
  else
  begin
    q.tail^.next := newNode; // Добавление нового элемента в конец очереди
    q.tail := newNode; // Обновляем хвост
  end;
end;

function Dequeue(var q: Queue): integer;
var
  tempNode: PNode;
begin
  if q.head <> nil then
  begin
    Dequeue := q.head^.value; // Получаем значение из головы очереди
    tempNode := q.head; // Сохраняем текущую голову
    q.head := q.head^.next; // Передвигаем голову на следующий элемент
    
    if q.head = nil then
      q.tail := nil; // Если очередь пуста, обнуляем хвост

    Dispose(tempNode); // Освобождаем память
  end
  else
    Dequeue := 0; // Если очередь пуста
end;

function IsEmpty(q: Queue): boolean;
begin
  IsEmpty := q.head = nil;
end;

procedure SubtractFromQueue(var q: Queue; value: integer);
var
  current: PNode;
begin
  current := q.head;

  while current <> nil do
  begin
    current^.value := current^.value - value; // Вычитаем значение из каждого элемента
    current := current^.next; // Переходим к следующему элементу
  end;
end;

var
  q: Queue;
  inputValue, i: integer;
begin
  InitQueue(q); // Инициализация очереди

  // Пример заполнения очереди
  for i := 1 to 5 do
  begin
    Enqueue(q, i); // Заполняем очередь значениями 1, 2, 3, 4, 5
  end;

  // Вывод начальных значений очереди
  Write('Начальные значения очереди: ');
  while not IsEmpty(q) do
  begin
    Write(Dequeue(q), ' '); // Ожидаем вывод значений в зависимости от введенного числа
  end;
  WriteLn;

  // Возвращаемся для повторного заполнения
  InitQueue(q); // Снова инициализируем очередь
  for i := 1 to 5 do
  begin
    Enqueue(q, i); // Заполняем очередь значениями 1, 2, 3, 4, 5
  end;

  Write('Введите число для вычитания: ');
  ReadLn(inputValue);

  // Вычисление
  SubtractFromQueue(q, inputValue);

  // Вывод результата
  WriteLn('Результат после вычитания:');
  while not IsEmpty(q) do
  begin
    WriteLn(Dequeue(q)); // Ожидаем вывод значений в зависимости от введенного числа
  end;
end.
