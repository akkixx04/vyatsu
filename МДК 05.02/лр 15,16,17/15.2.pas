// Для предыдущего задания (record 1) задать таблицу значений с данными о нескольких студентах, и, 
// использовав массив, вывести все данные о студентах в удобочитаемом виде.
type
  anketa = record
    fio: string;
    birth: string;
    kurs: 1..5
  end;

var
  students:  array[1..100] of anketa;
  i: integer;

begin
  students[1].fio := 'Широнина Анна Андреевна';
  students[2].fio := 'Шепрут Виталий Дмитриевич';
  students[3].fio := 'Орлова Александра Дмитриевна';
  
  students[1].birth := '24.07.2007';
  students[2].birth := '03.08.2005';
  students[3].birth := '04.08.2008';
  
  students[1].kurs := 2;
  students[2].kurs := 4;
  students[3].kurs := 1;
  
  for i := 1 to 3 do begin
    writeln('ФИО: ', students[i].fio);
    writeln('Дата рождения: ', students[i].birth);
    writeln('Курс: ', students[i].kurs);
  end;
end.