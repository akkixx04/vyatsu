unit FunctionCalculator;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls, Buttons;

type

  { TForm1 }

  TForm1 = class(TForm)
    BitBtn1: TBitBtn;
    ButtonCalculate: TButton;
    EditA: TEdit;
    EditB: TEdit;
    EditH: TEdit;
    Label1: TLabel;
    Label2: TLabel;
    Label3: TLabel;
    procedure BitBtn1Click(Sender: TObject);
    procedure ButtonCalculateClick(Sender: TObject);
    procedure EditHChange(Sender: TObject);
  private
    procedure CalculateFunction;
  public
  end;

var
  Form1: TForm1;

implementation

{$R *.lfm}

{ TForm1 }

procedure TForm1.ButtonCalculateClick(Sender: TObject);
begin
  CalculateFunction;
end;

procedure TForm1.BitBtn1Click(Sender: TObject);
begin
  CLose
end;

procedure TForm1.EditHChange(Sender: TObject);
begin

end;

procedure TForm1.CalculateFunction;
var
  a, b, h, x, y: Double;
  results: String;
begin
  // Проверка ввода
  if not TryStrToFloat(EditA.Text, a) then
  begin
    ShowMessage('Неверное значение a');
    Exit;
  end;

  if not TryStrToFloat(EditB.Text, b) then
  begin
    ShowMessage('Неверное значение b');
    Exit;
  end;

  if not TryStrToFloat(EditH.Text, h) or (h <= 0) then
  begin
    ShowMessage('Шаг h должен быть положительным числом');
    Exit;
  end;

  if a > b then
  begin
    ShowMessage('Начало отрезка a должно быть меньше конца b');
    Exit;
  end;

  // Вычисление значений функции
    results := 'Результаты вычисления y = x²:' + #13#10 + #13#10;
    results := results + Format('%-10s %10s', ['x', 'y']) + #13#10;
    results := results + '--------------------' + #13#10;

    x := a;
    while x <= b + 1E-9 do
    begin
      y := x * x;
      results := results + Format('%-10.2f %10.2f', [x, y]) + #13#10;
      x := x + h;
    end;

    ShowMessage(results);
  end;

end.
