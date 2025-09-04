uses GraphABC;
begin
  setwindowsize(1000,500);
  
  circle(100,150,50);
  floodfill(100,150,clred);

  moveto(150,150);
  lineto(450,150);
  lineto(300,70);
  lineto(150,150);
  floodfill(300,123,clBlue);
  
  lineto(300,230);
  lineto(450,150);
  floodfill(300,177,cllime);
  
  circle(500,150,50);
  floodfill(500,150,clyellow);
end.