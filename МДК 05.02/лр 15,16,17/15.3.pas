//Создать запись toy с информацией об имеющихся в продаже игрушках (название товара (name), 
//цена товара (price) и возрастной диапазон (age), для которого игрушка предназначена). Заполнить несколько товаров.
type
  toy = record
    name: string;
    price: string;
    age: string;
  end;

var
  toys: array[1..100] of toy;
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
  
  
  writeln('Доступные игрушки:');
  writeln('___________________');
  writeln();
  
  for i := 1 to 3 do
  begin
    with toys[i] do
    begin
      writeln('Название: ', name);
      writeln('Цена: ', price, ' руб.');
      writeln('Возрастной диапазон: ', age);
      writeln('--------------------');
    end;
  end;
end.