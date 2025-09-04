uses GraphABC;

const
  size = 50;
  
procedure chessboard;
var
  x, y: integer;
begin

  for y := 0 to 7 do
  begin

    for x := 0 to 7 do
    begin

      if (x + y) mod 2 = 0 then
        setbrushcolor(clwhite)
      else
        setbrushcolor(clblack);

      fillrectangle(x * size, y * size, (x + 1) * size, (y + 1) * size);
    end;
  end;
end;

begin
  setwindowsize(400, 400);
  chessboard;
end.
