unit Unit1;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls;

type

  { TMatrix }

  TMatrix = class(TForm)
    a1: TEdit;
    a2: TEdit;
    a3: TEdit;
    a4: TEdit;
    a5: TEdit;
    a6: TEdit;
    a7: TEdit;
    a8: TEdit;
    a9: TEdit;
    btn_answer: TButton;
    Label_answer: TLabel;
    Label_type: TLabel;
    Memo_answer: TMemo;
    type_matrix: TComboBox;
    procedure btn_answerClick(Sender: TObject);
    procedure type_matrixChange(Sender: TObject);
  private
      num1, num2, num3, num4, num5, num6, num7, num8, num9: string;
  public

  end;

var
  Matrix: TMatrix;

implementation

{$R *.lfm}

{ TMatrix }

procedure TMatrix.type_matrixChange(Sender: TObject);
begin
  Memo_answer.Lines.Clear;
  case type_matrix.Text of
  '2 на 2':
    begin
      a1.Visible := False;
      a2.Visible := False;
      a3.Visible := False;
      a4.Visible := False;
      a5.Visible := True;
      a6.Visible := True;
      a7.Visible := False;
      a8.Visible := True;
      a9.Visible := True;
      a1.Text := chr(0);
      a2.Text := chr(0);
      a3.Text := chr(0);
      a4.Text := chr(0);
      a5.Text := chr(0);
      a6.Text := chr(0);
      a7.Text := chr(0);
      a8.Text := chr(0);
      a9.Text := chr(0);
    end;
  '3 на 3':
    begin
      a1.Visible := True;
      a2.Visible := True;
      a3.Visible := True;
      a4.Visible := True;
      a5.Visible := True;
      a6.Visible := True;
      a7.Visible := True;
      a8.Visible := True;
      a9.Visible := True;
      a1.Text := chr(0);
      a2.Text := chr(0);
      a3.Text := chr(0);
      a4.Text := chr(0);
      a5.Text := chr(0);
      a6.Text := chr(0);
      a7.Text := chr(0);
      a8.Text := chr(0);
      a9.Text := chr(0);
    end;
  end;
end;

procedure TMatrix.btn_answerClick(Sender: TObject);
var
  num_answer, num_a1, num_a2, num_a3, num_a4, num_a5, num_a6, num_a7, num_a8, num_a9: real;
  t: boolean;
begin
  Memo_answer.Lines.Clear;
  t := False;
  case type_matrix.Text of
  '2 на 2':
    begin
       num1 := a5.Text;
       num2 := a6.Text;
       num3 := a8.Text;
       num4 := a9.Text;
        if (num1 = '') or (num2 = '') or (num3 = '') or (num4 = '') then Memo_answer.Lines.Add
         ('Ошибка! Строка ввода не должна быть пустой.')
         else
           begin
             t := True;
             num_a5:=StrToFloat(num1);
             num_a6:=StrToFloat(num2);
             num_a8:=StrToFloat(num3);
             num_a9:=StrToFloat(num4);
             num_answer:= (num_a5 * num_a9) - (num_a6 * num_a8);
           end;
    end;
  '3 на 3':
    begin
       num1 := a1.Text;
       num2 := a2.Text;
       num3 := a3.Text;
       num4 := a4.Text;
       num5 := a5.Text;
       num6 := a6.Text;
       num7 := a7.Text;
       num8 := a8.Text;
       num9 := a9.Text;
        if (num1 = '') or (num2 = '') or (num3 = '') or (num4 = '') or (num5 = '') or (num6 = '') or (num7 = '')
         or (num8 = '') or (num9 = '') then Memo_answer.Lines.Add
         ('Ошибка! Строка ввода не должна быть пустой.')
         else
           begin
             t := True;
             num_a1:=StrToFloat(num1);
             num_a2:=StrToFloat(num2);
             num_a3:=StrToFloat(num3);
             num_a4:=StrToFloat(num4);
             num_a5:=StrToFloat(num5);
             num_a6:=StrToFloat(num6);
             num_a7:=StrToFloat(num7);
             num_a8:=StrToFloat(num8);
             num_a9:=StrToFloat(num9);
             num_answer:= (num_a1 * num_a5 * num_a9) + (num_a2 * num_a6 * num_a7) + (num_a3 * num_a4 * num_a8) -
             (num_a3 * num_a5 * num_a7) - (num_a2 * num_a4 * num_a9) - (num_a1 * num_a6 * num_a8);
           end;
    end;
  end;
  if t then
  begin
    Memo_answer.Font.Size := 20;
    Memo_answer.Lines.Add(FloatToStr(num_answer))
  end;
end;

end.

