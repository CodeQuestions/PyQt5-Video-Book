combobox_list_style_str = """
    QListView {
        padding-top:5px;
        font-size: 11px;
        background-color: #2a2b32;
        outline: 0px;  /*去虚线*/
        border-radius: 0px;
        color: #fff;
    }

    QListView::item{
        padding-left:5px;
        background: transparent;
        padding:5px;
        color: #fff;
    }
    QListView::item:hover{
       background-color:#1e90ff;
    }

    QListView::item:selected{
       background-color:#1e90ff;
    }

"""

self.robot_combo_box.findChild(QListView).setStyleSheet(combobox_list_style_str)
self.robot_combo_box.setDisabled(True)