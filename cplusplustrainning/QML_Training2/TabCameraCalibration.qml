import QtQuick 2.7

TabCameraCalibrationForm {
    button1.onClicked: {
        console.log("Button Pressed. Entered text: " + textField1.text);
    }
}