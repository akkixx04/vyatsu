var
  N, balls: integer;

begin
  balls := 0;
  N := 5;
  repeat
    balls += N * N;
    N -= 1;
  until N = 0;
  print(balls)
end.