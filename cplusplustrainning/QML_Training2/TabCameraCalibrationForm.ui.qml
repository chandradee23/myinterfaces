import QtQuick 2.7
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.3

Item {
    property alias textField1: textField1
    property alias button1: button1
    property alias switch1: switch1

    RowLayout {
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.topMargin: 20
        anchors.top: parent.top

        TextField {
            id: textField1
            placeholderText: qsTr("Text Field")
        }

        Button {
            id: button1
            text: qsTr("Press Me")
        }
    }

    Column {
        id: column
        x: 220
        y: 99
        width: 200
        height: 271

        Switch {
            id: switch1
            text: qsTr("Switch")
            opacity: 0.5
            spacing: 5
        }

        SwitchDelegate {
            id: switchDelegate
            text: qsTr("Switch Delegate")
        }

        SwipeDelegate {
            id: swipeDelegate
            text: qsTr("Swipe Delegate")
        }

        Slider {
            id: slider
            value: 0.5
        }
    }
}
