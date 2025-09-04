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
    procedure a1KeyPress(Sender: TObject; var Key: char);
    procedure a2KeyPress(Sender: TObject; var Key: char);
    procedure a3KeyPress(Sender: TObject; var Key: char);
    procedure a4KeyPress(Sender: TObject; var Key: char);
    procedure a5KeyPress(Sender: TObject; var Key: char);
    procedure a6KeyPress(Sender: TObject; var Key: char);
    procedure a7KeyPress(Sender: TObject; var Key: char);
    procedure a8KeyPress(Sender: TObject; var Key: char);
    procedure a9KeyPress(Sender: TObject; var Key: char);
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

procedure TMatrix.a1KeyPress(Sender: TObject; var Key: char);
begin
  a1.ReadOnly:= not ((Key in ['0'..'9', #8]) or ((Key in [',','.']) and
  ((pos(',', a1.Text) = 0) and (pos('.', a1.Text) = 0)) and (a1.Text <> '')))
end;

procedure TMatrix.a2KeyPress(Sender: TObject; var Key: char);
begin
  a2.ReadOnly:= not ((Key in ['0'..'9', #8]) or ((Key in [',','.']) and
  ((pos(',', a2.Text) = 0) and (pos('.', a2.Text) = 0)) and (a2.Text <> '')))
end;

procedure TMatrix.a3KeyPress(Sender: TObject; var Key: char);
begin
  a3.ReadOnly:= not ((Key in ['0'..'9', #8]) or ((Key in [',','.']) and
  ((pos(',', a3.Text) = 0) and (pos('.', a3.Text) = 0)) and (a3.Text <> '')))
end;

procedure TMatrix.a4KeyPress(Sender: TObject; var Key: char);
begin
  a4.ReadOnly:= not ((Key in ['0'..'9', #8]) or ((Key in [',','.']) and
  ((pos(',', a4.Text) = 0) and (pos('.', a4.Text) = 0)) and (a4.Text <> '')))
end;

procedure TMatrix.a5KeyPress(Sender: TObject; var Key: char);
begin
  a5.ReadOnly:= not ((Key in ['0'..'9', #8]) or ((Key in [',','.']) and
  ((pos(',', a5.Text) = 0) and (pos('.', a5.Text) = 0)) and (a5.Text <> '')))
end;


procedure TMatrix.a6KeyPress(Sender: TObject; var Key: char);
begin
  a6.ReadOnly:= not ((Key in ['0'..'9', #8]) or ((Key in [',','.']) and
  ((pos(',', a6.Text) = 0) and (pos('.', a6.Text) = 0)) and (a6.Text <> '')))
end;

procedure TMatrix.a7KeyPress(Sender: TObject; var Key: char);
begin
  a7.ReadOnly:= not ((Key in ['0'..'9', #8]) or ((Key in [',','.']) and
  ((pos(',', a7.Text) = 0) and (pos('.', a7.Text) = 0)) and (a7.Text <> '')))
end;

procedure TMatrix.a8KeyPress(Sender: TObject; var Key: char);
begin
  a8.ReadOnly:= not ((Key in ['0'..'9', #8]) or ((Key in [',','.']) and
  ((pos(',', a8.Text) = 0) and (pos('.', a8.Text) = 0)) and (a8.Text <> '')))
end;

procedure TMatrix.a9KeyPress(Sender: TObject; var Key: char);
begin
  a9.ReadOnly:= not ((Key in ['0'..'9', #8]) or ((Key in [',','.']) and
  ((pos(',', a9.Text) = 0) and (pos('.', a9.Text) = 0)) and (a9.Text <> '')))
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

