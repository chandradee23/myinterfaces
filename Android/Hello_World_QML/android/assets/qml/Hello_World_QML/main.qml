import QtQuick 1.1

CheckableGroup { id: group }
Row {
    id: row
    spacing: platformStyle.paddingMedium
    RadioButton {
        id: button1
        text: "1"
        platformExclusiveGroup: group
    }
    RadioButton {
        id: button2
        text: "2"
        platformExclusiveGroup: group
    }
    RadioButton {
        id: button3
        text: "3"
        platformExclusiveGroup: group
        checked: true
    }
}
