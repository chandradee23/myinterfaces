import QtQuick 2.7

TabShowAllCamerasForm {
    button1.onClicked: {
        console.log("Button Pressed. Entered text: " + textField1.text);
    }
}
