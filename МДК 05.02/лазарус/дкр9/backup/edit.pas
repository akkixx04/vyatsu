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
    Bir: TComboBox;
    Date1: TDateTimePicker;
    eCountry: TEdit;
    Sostav: TEdit;
    eSrok: TEdit;
    eName: TEdit;
    Label1: TLabel;
    Label2: TLabel;
    Label3: TLabel;
    Label4: TLabel;
    Label5: TLabel;
    Label6: TLabel;
    Label7: TLabel;
    procedure FormShow(Sender: TObject);
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

end.

