# Type Checking Imports
# ---------------------
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Any

# Standard Library Imports
# ------------------------
import sys

# Third Party Imports
# -------------------
from qtpy import QtCore, QtGui, QtWidgets


# Class Definitions
# -----------------
class MyWidget(QtWidgets.QWidget):
    """A PyQt5 widget that performs some task.

    Attributes:
        some_arg (Any): An argument that will be used in the widget.
        some_value (int): A value used in the widget.
    """
    # Initialization and Setup
    # ------------------------
    def __init__(self, parent: QtWidgets.QWidget = None, some_arg: 'Any' = None):
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
        self.__setup_attributes()
        self.__setup_ui()
        self.__setup_signal_connections()

    def __setup_attributes(self):
        """Set up the initial values for the widget.
        """
        # Attributes
        # ----------
        self.some_value = 0

        # Private Attributes
        # ------------------
        self._some_private = 0

    def __setup_ui(self):
        """Set up the UI for the widget, including creating widgets, layouts, and setting the icons for the widgets.
        """
        # Create widgets and layouts
        pass
        # Set the layout for the widget
        ...

    def __setup_signal_connections(self):
        """Set up signal connections between widgets and slots.
        """
        # Connect signals to slots
        pass

    # Private Methods
    # ---------------

    # Extended Methods
    # ----------------

    # Special Methods
    # ---------------

    # Event Handling or Override Methods
    # ----------------------------------
    def keyPressEvent(self, event: QtGui.QKeyEvent):
        """Handle key press events.
        """
        # Handle key press events here
        super().keyPressEvent(event)


# Main Function
# -------------
def main():
    """Create the application, and show the widget.
    """
    # Argument Parsing
    # ----------------
    ...

    # Application Setup and Execution
    # -------------------------------
    # Create the application and the main window
    app = QtWidgets.QApplication(sys.argv)

    # Create an instance of the widget
    widget = MyWidget()

    # Show the window and run the application
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
