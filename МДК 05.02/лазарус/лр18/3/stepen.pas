unit stepen;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls, Buttons;

type

  { TForm1 }

  TForm1 = class(TForm)
    BitBtnExit: TBitBtn;
    BitBtnCalcul: TBitBtn;
    EditNum: TEdit;
    EditStep: TEdit;
    LabelNum: TLabel;
    LabelStep: TLabel;
    MemoRes: TMemo;
    procedure BitBtnExitClick(Sender: TObject);
    procedure BitBtnCalculClick(Sender: TObject);
    procedure EditNumChange(Sender: TObject);
    procedure EditStepChange(Sender: TObject);
    procedure MemoResChange(Sender: TObject);
  private

  public

  end;

var
  Form1: TForm1;
  k1,k2:double  ;
  t:longint;

implementation

{$R *.lfm}

{ TForm1 }

procedure TForm1.BitBtnExitClick(Sender: TObject);
begin
     Close
end;

procedure TForm1.BitBtnCalculClick(Sender: TObject);
    var i,t,k,k1:integer;
  begin
    k:=strtoint(EditNum.Text); // число
    k1:=strtoint(EditStep.Text); // степень
    i:=1; t:=1;
    while i<=k1 do
      begin
        t:=t*k;
        i:=i+1;
      end;
    MemoRes.Lines.add('число '+EditNum.Text+' в степени '+EditStep.Text+' равно: '+IntToStr(t));
end;

procedure TForm1.EditNumChange(Sender: TObject);
begin

end;

procedure TForm1.EditStepChange(Sender: TObject);
begin

end;

procedure TForm1.MemoResChange(Sender: TObject);
begin

end;




end.

