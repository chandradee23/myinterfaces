import QtQuick 2.0
import QtQuick.Controls 2.2

Item {
    id: tabWidget

    SwipeView {
        id: swipeView
        anchors.fill: parent
        currentIndex: tabBar.currentIndex

        Page {
            Label {
                text: qsTr("Second page")
                anchors.centerIn: parent
            }
        }
    }
}
