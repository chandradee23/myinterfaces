import QtQuick 2.8
import QtQuick.Window 2.2
import QtQuick.Controls 2.2

/*Window {
    id:mainWindow
    visible: true
    width: 640
    height: 480
    title: qsTr("Random GUI...")

    QML_Tab{}
}*/

import QtQuick 2.7
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.3

ApplicationWindow {
    visible: true
    width: 640
    height: 480
    title: qsTr("Hello World")

    header: TabBar {
        id: tabBar
        currentIndex: swipeView.currentIndex
        TabButton {
            text: qsTr("First")
        }
        TabButton {
            text: qsTr("Second")
        }
        TabButton {
            text: qsTr("Third")
        }
    }
    SwipeView {
        id: swipeView
        anchors.fill: parent
        currentIndex: tabBar.currentIndex

        //Page1 {
        //}

        Page {
            Label {
                text: qsTr("First page")
                anchors.centerIn: parent
            }
        }
        Page {
            Label {
                text: qsTr("Second page")
                anchors.centerIn: parent
            }
        }
        Page {
            Label {
                 text: qsTr("Third page")
                anchors.centerIn: parent
            }
        }

    }
}
