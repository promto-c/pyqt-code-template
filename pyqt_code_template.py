# Standard Library Imports
# ------------------------
import sys

# Third Party Imports
# -------------------
from PyQt5 import QtCore, QtGui, QtWidgets


class MyWidget(QtWidgets.QWidget):
    """A PyQt5 widget that performs some task.

    Attributes:
        some_arg (Any): An argument that will be used in the widget.
        some_value (int): A value used in the widget.
    """
    # Initialization and Setup
    # ------------------------
    def __init__(self, parent=None, some_arg=None):
        """Initialize the widget and set up the UI, signal connections, and icon.

        Args:
            parent (QtWidgets.QWidget): The parent widget.
            some_arg (Any): An argument that will be used in the widget.
        """
        # Initialize the super class
        super().__init__(parent)

        # Store the arguments
        self.some_arg = some_arg

        # Initialize setup
        self._setup_attributes()
        self._setup_ui()
        self._setup_icons()
        self._setup_signal_connections()

    def _setup_attributes(self):
        """Set up the initial values for the widget.
        """
        # Attributes
        # ------------------
        self.some_value = 0

        # Private Attributes
        # ------------------
        self._some_private = 0

    def _setup_ui(self):
        """Set up the UI for the widget, including creating widgets and layouts.
        """
        # Create widgets and layouts here
        pass
        # Set the layout for the widget
        # self.setLayout(layout)

    def _setup_signal_connections(self):
        """Set up signal connections between widgets and slots.
        """
        # Connect signals to slots here
        pass

    def _setup_icons(self):
        """Set the icons for the widgets.
        """
        # Set the icons for the widgets here
        pass

    # Private Methods
    # ---------------

    # Extended Methods
    # ----------------
    def some_function(self):
        """Slot for a signal connection.
        """
        pass

    # Special Methods
    # ---------------

    # Event Handling or Override Methods
    # ----------------------------------
    def keyPressEvent(self, event: QtGui.QKeyEvent):
        """Handle key press events.
        """
        # Handle key press events here
        super().keyPressEvent(event)

def main():
    """Create the application, and show the widget.
    """
    # Create the application and the main window
    app = QtWidgets.QApplication(sys.argv)

    # Create an instance of the widget
    widget = MyWidget()

    # Show the window and run the application
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
