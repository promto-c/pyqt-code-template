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

# Local Imports
# -------------


# Class Definitions
# -----------------
class MyWidget(QtWidgets.QWidget):
    """A Qt widget that performs some task.

    Attributes:
        ...
    """
    # Initialization and Setup
    # ------------------------
    def __init__(self, parent: QtWidgets.QWidget = None):
        """Initialize the widget and set up the UI, signal connections, and icon.

        Args:
            ...
        """
        # Initialize the super class
        super().__init__(parent)

        # Store the arguments
        ...

        # Initialize setup
        self.__setup_attributes()
        self.__setup_ui()
        self.__setup_signal_connections()

    def __setup_attributes(self):
        """Set up the initial values for the widget.
        """
        # Attributes
        # ----------
        ...

        # Private Attributes
        # ------------------
        ...

    def __setup_ui(self):
        """Set up the UI for the widget, including creating widgets, layouts, and setting the icons for the widgets.
        """
        # Create Layouts
        # --------------
        ...

        # Create Widgets
        # --------------
        ...

        # Add Widgets to Layouts
        # ----------------------
        ...

    def __setup_signal_connections(self):
        """Set up signal connections between widgets and slots.
        """
        # Connect signals to slots
        ...

    # Public Methods
    # --------------

    # Utility Methods
    # ---------------

    # Private Methods
    # ---------------

    # Special Methods
    # ---------------

    # Overridden Methods
    # --------------------


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

    # Create and show the widget
    widget = MyWidget()
    widget.show()

    # Run the application
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
