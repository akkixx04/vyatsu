unit Edit;

{$mode ObjFPC}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls, Buttons,
  DateTimePicker;

type

  { TfEdit }

  TfEdit = class(TForm)
    BitBtn1: TBitBtn;
    BitBtn2: TBitBtn;
    CBNote: TComboBox;
    Dob: TComboBox;
    Date1: TDateTimePicker;
    eCountry: TEdit;
    eSrok: TEdit;
    eName: TEdit;
    Label1: TLabel;
    Label2: TLabel;
    Label3: TLabel;
    Label4: TLabel;
    Label5: TLabel;
    Label6: TLabel;
    procedure FormShow(Sender: TObject);
    procedure Label2Click(Sender: TObject);
  private

  public

  end;

var
  fEdit: TfEdit;

implementation

{$R *.lfm}

{ TfEdit }

procedure TfEdit.FormShow(Sender: TObject);
begin
    eName.SetFocus;
end;

procedure TfEdit.Label2Click(Sender: TObject);
begin

end;

end.

