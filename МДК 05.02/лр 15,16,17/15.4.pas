//Выполнить предыдущее задание с игрушками (запись toy), записывать данные в файл, а затем считывать их из файла и выводить на экран.
type
  toy = record
    name: string;
    price: string;
    age: string;
  end;

var
  toys: array[1..100] of toy;
  f: file;
  i: integer;

begin
  toys[1].name := 'Плюшевый мишка';
  toys[2].name := 'Конструктор магнитный';
  toys[3].name := 'Пазл 100 деталей';
  
  toys[1].price := '500 руб.';
  toys[2].price := '1000 руб.';
  toys[3].price := '300 руб.';
  
  toys[1].age := '0+';
  toys[2].age := '5+';
  toys[3].age := '10+';
  
  assign(f, 'toys.txt');
  rewrite(f);
  
  for i := 1 to 3 do
  begin
    write(f, toys[i]);
  end;
  
  close(f);
  
  assign(f, 'toys.txt');
  reset(f);
  
  for i := 1 to 3 do
  begin
    read(f, toys[i]);
    with toys[i] do
    begin
      writeln('Название: ', name);
      writeln('Цена: ', price, ' руб.');
      writeln('Возрастной диапазон: ', age);
      writeln('--------------------');
    end;
  end;
  
  close(f)
end.
