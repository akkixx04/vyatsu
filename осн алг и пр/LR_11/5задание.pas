uses GraphABC;
var
  x,y,r:integer;
begin
  setwindowsize(500,500);
  x := 50;
  y := 50;
  r := 10;
  
  repeat
    circle(x,y,r);
    floodfill(x,y,rgb(random(256), random(256), random(256)));
    x += 40;
    y += 40;
    r += 10;
  until r=100;
  
end.