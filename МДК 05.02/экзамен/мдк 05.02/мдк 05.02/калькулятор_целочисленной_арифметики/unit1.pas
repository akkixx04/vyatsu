unit Unit1;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls, ExtCtrls;

type

  { TForm1 }

  TForm1 = class(TForm)
    ButtonMod: TButton;
    OFF: TButton;
    Zero: TButton;
    One: TButton;
    Two: TButton;
    Three: TButton;
    Four: TButton;
    Five: TButton;
    Six: TButton;
    Seven: TButton;
    Eight: TButton;
    Nine: TButton;
    Plus: TButton;
    Ravno: TButton;
    Clear: TButton;
    ButtonDiv: TButton;
    Umnoshenie: TButton;
    Minus: TButton;
    Vvod: TEdit;
    procedure OFFClick(Sender: TObject);
    procedure NumberClick(Sender: TObject);
    procedure OperationClick(Sender: TObject);
    procedure ClearClick(Sender: TObject);
    procedure RavnoClick(Sender: TObject);
    procedure FormCreate(Sender: TObject);
    procedure Edit1KeyPress(Sender: TObject; var Key: char);
  private
    FFirstNumber: Int64;
    FOperation: Char;
    FNewInput: Boolean;
    procedure CalculateResult;
    procedure ShowErrorMessage(const Msg: string);
  public
  end;

var
  Form1: TForm1;

implementation

{$R *.lfm}

{ TForm1 }

procedure TForm1.FormCreate(Sender: TObject);
begin
  FNewInput := True;
  FOperation := #0;
  Vvod.Text := '';
end;

procedure TForm1.Edit1KeyPress(Sender: TObject; var Key: char);
begin
  Key := #0;
end;

procedure TForm1.NumberClick(Sender: TObject);
var
  Number: string;
begin
  Number := (Sender as TButton).Caption;

  if FNewInput then
  begin
    Vvod.Text := '';
    FNewInput := False;
  end;

  if Length(Vvod.Text) >= 15 then
  begin
    ShowErrorMessage('Это максимум!!!');
    Exit;
  end;

  if (Number = '0') and (Vvod.Text = '0') then
    Exit
  else if (Vvod.Text = '0') then
    Vvod.Text := Number
  else
    Vvod.Text := Vvod.Text + Number;
end;

procedure TForm1.OFFClick(Sender: TObject);
begin
   close;
end;

procedure TForm1.OperationClick(Sender: TObject);
var
  Op: string;
begin
  if Vvod.Text = '' then Exit;

  try
    FFirstNumber := StrToInt64(Vvod.Text);
    Op := (Sender as TButton).Caption;

    if Op = 'Div' then
      FOperation := '/'
    else if Op = 'Mod' then
      FOperation := '%'
    else
      FOperation := Op[1];

    FNewInput := True;
  except
    on E: Exception do
    begin
      ShowErrorMessage('Ошибка: ' + E.Message);
      ClearClick(nil);
    end;
  end;
end;

procedure TForm1.ClearClick(Sender: TObject);
begin
  Vvod.Text := '';
  FFirstNumber := 0;
  FOperation := #0;
  FNewInput := True;
end;

procedure TForm1.RavnoClick(Sender: TObject);
begin
  if FOperation = #0 then Exit;
  if Vvod.Text = '' then Exit;

  CalculateResult;
end;

procedure TForm1.CalculateResult;
var
  SecondNumber, Result: Int64;
begin
  try
    SecondNumber := StrToInt64(Vvod.Text);

    case FOperation of
      '+': Result := FFirstNumber + SecondNumber;
      '-': Result := FFirstNumber - SecondNumber;
      '*': Result := FFirstNumber * SecondNumber;
      '/':
        if SecondNumber = 0 then
        begin
          ShowErrorMessage('Деление на ноль!');
          Exit;
        end
        else
          Result := FFirstNumber div SecondNumber;
      '%':
        if SecondNumber = 0 then
        begin
          ShowErrorMessage('Деление на ноль!');
          Exit;
        end
        else
          Result := FFirstNumber mod SecondNumber;
    end;

    Vvod.Text := IntToStr(Result);
    FNewInput := True;
    FOperation := #0;
  except
    on E: EConvertError do
      ShowErrorMessage('Некорректное число');
    on E: ERangeError do
      ShowErrorMessage('Число слишком большое');
  end;
end;

procedure TForm1.ShowErrorMessage(const Msg: string);
begin
  Vvod.Text := Msg;
end;

end.
