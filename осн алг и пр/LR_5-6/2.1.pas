//Составить программу, проверяющую упорядочены ли элементы массива по возрастанию.

const
  N = 2;
var
  A: array[1..N] of integer;
  i: integer;
  isSorted: boolean;
 
begin
randomize;
  for i := 1 to N do
  begin
    A[i] := random(100);
  end;

writeln(A);

isSorted := true;
  
for i := 1 to N - 1 do
  begin
    if A[i] > A[i + 1] then
    begin
      isSorted := false; 
      break;
    end;
  end;
 if isSorted then
    writeln('Массив упорядочен по возрастанию.')
  else
    writeln('Массив не упорядочен по возрастанию.');
end.