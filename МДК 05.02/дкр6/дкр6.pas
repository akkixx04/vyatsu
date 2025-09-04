const
  max_nodes = 100;

type
  Node = record
    data: string;
    next: integer;
  end;

var
  nodes: array[0..max_nodes-1] of Node;
  head: integer;    // Индекс головы списка
  current_index: integer; // Текущий индекс для добавления новых элементов

procedure Initialize();
begin
  head := -1; // Пустой список
  current_index := 0; // Начинаем с первого элемента массива
end;

procedure Append(data: string);
var
  new_index, last_index: integer;
begin
  new_index := current_index;
  current_index := current_index + 1;
  //Получение нового индекса для узла

  nodes[new_index].data := data;
  nodes[new_index].next := -1;
  //Инициализация нового узла

  if head = -1 then
  begin
    head := new_index;
    exit;
  end;

  // Находим последний узел
  last_index := head;
  while nodes[last_index].next <> -1 do
    last_index := nodes[last_index].next;

  nodes[last_index].next := new_index;
  //Добавление нового узла в конец списка
end;

procedure Visual();
var
  curr_index: integer;
begin
  curr_index := head;
  if curr_index = -1 then
  begin
    writeln('Список пуст.');
    exit;
  end;

  write('Содержимое списка: ');
  while curr_index <> -1 do
  begin
    write(nodes[curr_index].data, ' -> ');
    curr_index := nodes[curr_index].next;
  end;
  writeln('nil');
end;

procedure Delete(key: string);
var
  curr_index, prev_index: integer;
begin
  curr_index := head;
  prev_index := -1;

  // Поиск узла с указанным ключом
  while (curr_index <> -1) and (nodes[curr_index].data <> key) do
  begin
    prev_index := curr_index;
    curr_index := nodes[curr_index].next;
  end;

  if curr_index = -1 then
  begin
    writeln('Элемент ', key, ' не найден.');
    exit;
  end;

  if prev_index = -1 then
    head := nodes[curr_index].next  // Удаляем голову
  else
    nodes[prev_index].next := nodes[curr_index].next; 
    //заменяет ссылку на текущий узел ссылкой на узел, идущий сразу после текущего.

end;

procedure Menu();
var
  choice: integer;
  data, key: string;
begin
  Initialize();

  repeat
    writeln('Меню:');
    writeln('1 Добавить элемент');
    writeln('2 Показать список');
    writeln('3 Удалить элемент');
    writeln('4 Выход');
    
    write('Выберите действие: ');
    readln(choice);

    case choice of
      1: 
      begin
        write('Введите элемент для добавления: ');
        readln(data);
        Append(data);
      end;
      2: Visual();
      3: 
      begin
        write('Введите элемент для удаления: ');
        readln(key);
        Delete(key);
      end;
      4: writeln('Выход из программы...');
      else writeln('Неверный выбор. Попробуйте снова.');
    end;
  until choice = 4;
end;

begin
  Menu();
end.